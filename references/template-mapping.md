# 2026 台账模板结构

Use this reference only for the known 2026 templates or a workbook confirmed to have the same structure. Always inspect actual headers first.

## 电话费、燃油费报销人员统计.xlsx

Primary current-year sheet: `无任命人员话费福利`.

- Match employees by name plus identity/personnel data; the known current sheet stores the name in column C.
- Monthly phone columns are grouped under `电话费`, normally January through December in columns T:AE.
- Enter monthly final reimbursable amounts. Do not place quarterly totals in one month.
- Home-leave filed place and trip blocks normally begin at column AF. Read the two header rows to resolve exact start/end/amount triplets.
- The workbook contains external links and historical sheets. A valid narrow edit must preserve them.

## 培训费报销人员统计.xlsx

Primary current-year sheet: `2026培训费`.

- Identity fields normally use B:F: department, name, position, ID number, phone.
- Training events use repeated triplets:
  - G:I
  - J:L
  - M:O
  - P:R
  - S:U
- Each triplet is start date, end date, amount. Column V is the nearby remarks area.
- Match by ID plus name. If the same start/end dates already exist, reconcile that event rather than appending a duplicate.
- Append only to the first completely blank triplet after the event is `PASS` or `PASS_WITH_DEDUCTION`.

## 探亲备案地备案统计表.xls

Known fields normally include department, name, ID number, position, grade, filed place, work-location housing status, proof status, and remarks.

- Match by ID first.
- Add or change a filed place only from the department's month-end update and supporting evidence.
- For a change, retain a revision copy and record the effective year/date and approval basis in the existing remarks field when the template permits.
- `.xls` is a binary format. Prefer native Excel editing. If native editing is unavailable, save a separately named `.xlsx` revision and disclose the conversion.

## Do Not Hard-Code

Rows change as employees are added or moved. Find rows by stable identity and columns by visible headers. Treat the coordinates above as a verified starting point, not a universal schema.
