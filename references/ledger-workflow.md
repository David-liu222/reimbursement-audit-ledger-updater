# 审核到台账的工作流

## 1. Build the audit table

Use one row per person-event or person-month with these fields:

| Field | Meaning |
| --- | --- |
| category | training, phone, home leave, or travel |
| person_id | stable employee/person identifier |
| person_name | employee name |
| department | current department |
| event_period | month or start/end dates |
| source_amount | total supported by source tickets/invoices |
| policy_cap | applicable cap, if any |
| excluded_amount | unsupported, duplicated, or over-cap amount |
| final_amount | source amount minus exclusions, capped as required |
| decision | PASS, PASS_WITH_DEDUCTION, HOLD, or REJECT |
| evidence | filename plus page/sheet/cell |
| issue | exact missing/conflicting item |

## 2. Reconciliation controls

Before entry, independently calculate:

- each person-event itemization;
- each person's category total;
- category total;
- OA/request total;
- proposed ledger total.

All differences must be `0.00` before a record becomes `PASS`. A cap deduction is not a reconciliation error when it is explicitly shown as `excluded_amount`.

## 3. Entry gate

- `PASS`: write `final_amount`.
- `PASS_WITH_DEDUCTION`: write `final_amount`; report source, cap, and deduction.
- `HOLD` or `REJECT`: do not write a new final amount. Preserve any pre-existing entry and list the corrective action needed.

For an already-entered amount that is demonstrably arithmetically wrong, create a revision copy and correct only after the source itemization and OA/request amount agree. Report the old value, new value, and reason.

## 4. Duplicate and period checks

- Do not add a record if the same person, category, period/event dates, and amount already exist.
- For repeated event blocks, match exact start/end dates before using the next blank block.
- For monthly columns, verify the header month rather than assuming a column letter.
- A blank cell and a zero have different meanings. Never turn missing evidence into zero expense.

## 5. OA status

Maintain these states outside the financial amount cells unless the template already provides a status field:

1. `审核中`
2. `可进入OA`
3. `OA审批中`
4. `OA已通过`
5. `已转工资核算`

Workbook editing alone does not advance the external OA or forwarding state.

## 6. Final verification

- Reopen the saved workbook and read every changed cell.
- Recalculate the entered totals independently.
- Compare source and output workbook structure.
- Confirm that only authorized cells/parts changed.
- Render each changed area and inspect alignment, borders, number/date formats, clipping, and nearby headers.
- Keep unrelated pre-existing formula or external-link errors unchanged and report them separately.
