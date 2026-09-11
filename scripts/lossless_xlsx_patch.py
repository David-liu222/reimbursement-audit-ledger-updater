#!/usr/bin/env python3
"""Patch explicit XLSX cell values while preserving unrelated package parts.

Usage:
  python lossless_xlsx_patch.py --input source.xlsx --output revised.xlsx --updates updates.json

updates.json:
[
  {"sheet": "Sheet1", "cell": "B2", "value": 123.45},
  {"sheet": "Sheet1", "cell": "C2", "value": "已核对"},
  {"sheet": "Sheet1", "cell": "D2", "value": null},
  {"sheet": "Sheet1", "cell": "E2", "type": "date", "value": "2026-09-11"}
]
"""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import os
import re
import tempfile
import zipfile
from collections import defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET

MAIN_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"m": MAIN_NS, "r": REL_NS, "p": PKG_REL_NS}
ET.register_namespace("", MAIN_NS)
ET.register_namespace("r", REL_NS)


def col_index(ref: str) -> int:
    match = re.fullmatch(r"([A-Z]+)([1-9][0-9]*)", ref.upper())
    if not match:
        raise ValueError(f"Invalid A1 cell reference: {ref}")
    value = 0
    for char in match.group(1):
        value = value * 26 + ord(char) - 64
    return value


def row_index(ref: str) -> int:
    match = re.fullmatch(r"([A-Z]+)([1-9][0-9]*)", ref.upper())
    if not match:
        raise ValueError(f"Invalid A1 cell reference: {ref}")
    return int(match.group(2))


def sheet_parts(archive: zipfile.ZipFile) -> dict[str, str]:
    workbook = ET.fromstring(archive.read("xl/workbook.xml"))
    rels = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
    targets = {
        rel.attrib["Id"]: rel.attrib["Target"].lstrip("/")
        for rel in rels.findall("p:Relationship", NS)
    }
    result = {}
    for sheet in workbook.findall("m:sheets/m:sheet", NS):
        rel_id = sheet.attrib[f"{{{REL_NS}}}id"]
        target = targets[rel_id]
        result[sheet.attrib["name"]] = target if target.startswith("xl/") else f"xl/{target}"
    return result


def workbook_epoch(archive: zipfile.ZipFile) -> dt.datetime:
    root = ET.fromstring(archive.read("xl/workbook.xml"))
    props = root.find("m:workbookPr", NS)
    use_1904 = props is not None and props.attrib.get("date1904") in {"1", "true", "TRUE"}
    return dt.datetime(1904, 1, 1) if use_1904 else dt.datetime(1899, 12, 30)


def excel_serial(value: str, epoch: dt.datetime) -> float:
    parsed = dt.datetime.fromisoformat(value)
    delta = parsed - epoch
    return delta.days + (delta.seconds + delta.microseconds / 1_000_000) / 86400


def find_or_create_cell(root: ET.Element, ref: str) -> ET.Element:
    ref = ref.upper()
    row_no = row_index(ref)
    sheet_data = root.find("m:sheetData", NS)
    if sheet_data is None:
        raise ValueError("Worksheet has no sheetData")
    rows = list(sheet_data.findall("m:row", NS))
    row = next((item for item in rows if int(item.attrib["r"]) == row_no), None)
    if row is None:
        row = ET.Element(f"{{{MAIN_NS}}}row", {"r": str(row_no)})
        position = next((i for i, item in enumerate(rows) if int(item.attrib["r"]) > row_no), len(rows))
        sheet_data.insert(position, row)
    cells = list(row.findall("m:c", NS))
    cell = next((item for item in cells if item.attrib.get("r") == ref), None)
    if cell is not None:
        return cell
    target_col = col_index(ref)
    position = next((i for i, item in enumerate(cells) if col_index(item.attrib["r"]) > target_col), len(cells))
    cell = ET.Element(f"{{{MAIN_NS}}}c", {"r": ref})
    neighbors = list(reversed(cells[:position])) + cells[position:]
    styled = next((item for item in neighbors if item.attrib.get("s") is not None), None)
    if styled is not None:
        cell.attrib["s"] = styled.attrib["s"]
    row.insert(position, cell)
    return cell


def clear_payload(cell: ET.Element) -> None:
    cell.attrib.pop("t", None)
    for child in list(cell):
        if child.tag in {f"{{{MAIN_NS}}}f", f"{{{MAIN_NS}}}v", f"{{{MAIN_NS}}}is"}:
            cell.remove(child)


def write_value(cell: ET.Element, update: dict, epoch: dt.datetime) -> None:
    clear_payload(cell)
    value = update.get("value")
    kind = update.get("type")
    if value is None:
        return
    if kind == "date":
        value = excel_serial(str(value), epoch)
    if isinstance(value, bool):
        cell.attrib["t"] = "b"
        ET.SubElement(cell, f"{{{MAIN_NS}}}v").text = "1" if value else "0"
    elif isinstance(value, (int, float)):
        ET.SubElement(cell, f"{{{MAIN_NS}}}v").text = format(value, ".15g")
    elif kind == "date":
        ET.SubElement(cell, f"{{{MAIN_NS}}}v").text = format(value, ".15g")
    else:
        cell.attrib["t"] = "inlineStr"
        inline = ET.SubElement(cell, f"{{{MAIN_NS}}}is")
        text = ET.SubElement(inline, f"{{{MAIN_NS}}}t")
        text.text = str(value)


def patch(input_path: Path, output_path: Path, updates: list[dict]) -> list[str]:
    by_sheet = defaultdict(list)
    for update in updates:
        if not {"sheet", "cell", "value"}.issubset(update):
            raise ValueError(f"Each update requires sheet, cell, and value: {update}")
        by_sheet[update["sheet"]].append(update)

    with zipfile.ZipFile(input_path, "r") as source:
        parts = sheet_parts(source)
        epoch = workbook_epoch(source)
        missing = sorted(set(by_sheet) - set(parts))
        if missing:
            raise ValueError(f"Unknown worksheet(s): {missing}")
        replacements = {}
        changed = []
        for sheet_name, sheet_updates in by_sheet.items():
            part = parts[sheet_name]
            root = ET.fromstring(source.read(part))
            for update in sheet_updates:
                ref = update["cell"].upper()
                write_value(find_or_create_cell(root, ref), update, epoch)
                changed.append(f"{sheet_name}!{ref}")
            replacements[part] = ET.tostring(root, encoding="utf-8", xml_declaration=True)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        handle, temp_name = tempfile.mkstemp(suffix=".xlsx", dir=output_path.parent)
        os.close(handle)
        try:
            with zipfile.ZipFile(temp_name, "w") as destination:
                for item in source.infolist():
                    destination.writestr(copy.copy(item), replacements.get(item.filename, source.read(item.filename)))
            os.replace(temp_name, output_path)
        finally:
            if os.path.exists(temp_name):
                os.unlink(temp_name)
    return changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--updates", required=True, type=Path)
    args = parser.parse_args()
    if args.input.suffix.lower() != ".xlsx" or args.output.suffix.lower() != ".xlsx":
        raise SystemExit("This script supports .xlsx input and output only")
    updates = json.loads(args.updates.read_text(encoding="utf-8"))
    if not isinstance(updates, list):
        raise SystemExit("Updates JSON must be a list")
    changed = patch(args.input, args.output, updates)
    print(json.dumps({"output": str(args.output), "changed_cells": changed}, ensure_ascii=False))


if __name__ == "__main__":
    main()
