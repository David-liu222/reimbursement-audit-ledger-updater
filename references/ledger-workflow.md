# 审核到台账的工作流

## 1. Build the audit table

Use one row per person-event or person-month with these fields:

| Field | Meaning |
| --- | --- |
| category | training, phone, home leave, or travel |
| case_id | OA/request ID + person ID + category + event/month, or another stable equivalent |
| person_id | stable employee/person identifier |
| person_name | employee name |
| department | current department |
| event_period | month or start/end dates |
| requested_amount | amount submitted in the request/OA form |
| evidenced_gross_amount | face value of case-matched invoices/tickets before refunds and eligibility exclusions |
| refund_amount | refunds, cancellations, credit notes, or returned amounts tied to those documents |
| eligible_before_cap | net evidenced amount that passes identity, date, route, purpose, and category rules before caps |
| policy_cap | applicable cap, if any |
| unsupported_requested_amount | part of the requested amount without sufficient evidence |
| duplicate_amount | amount already claimed or reimbursed elsewhere |
| personal_or_ineligible_amount | personal, out-of-scope, or otherwise ineligible amount |
| cap_deduction | eligible amount excluded only because of a reimbursement cap |
| final_amount | amount allowed for ledger entry after all deductions |
| variance_reason | explanation of requested amount minus final amount |
| decision | PASS, PASS_WITH_DEDUCTION, PENDING_EVIDENCE, PENDING_EXCEPTION_APPROVAL, or REJECT |
| evidence | filename plus page/sheet/cell |
| issue | exact missing/conflicting item |
| resolution_path | none, supply_evidence, fact_confirmation, claimant_acknowledgement, or exception_approval |
| resolved_by_and_role | case-specific resolver and role, when required |
| resolved_at | resolution date/time, when required |
| resolution_scope | person, event, period, amount, and issue covered |
| resolution_basis | supplied evidence, OA item, message, or policy/approval reference |
| policy_version | rule document and effective date used for the case |
| primary_document_ids | OA/request, invoice, ticket/order, and payment identifiers used for traceability and deduplication |

## 2. Reconciliation controls

Before entry, independently calculate and show:

- each person-event itemization;
- each person's category total;
- category total;
- requested/OA total;
- evidenced gross and refund totals;
- eligible-before-cap total;
- unsupported-requested, duplicate, personal/ineligible, and cap-deduction totals;
- proposed ledger total.

The following equations must balance to `0.00` before a record can pass:

1. `net_evidenced_amount = evidenced_gross_amount - refund_amount`
2. `eligible_before_cap = net_evidenced_amount - duplicate_amount - personal_or_ineligible_amount`
3. `final_amount = eligible_before_cap - cap_deduction`, never below `0.00`.
4. `requested_amount - final_amount = documented variance`; identify any `unsupported_requested_amount` within that variance instead of treating it as evidenced expenditure.
5. `proposed ledger total = sum(final_amount)` for the included cases.
6. After OA/payment approval, `approved payable total = final ledger total`; before approval, do not claim those totals have reconciled.

A nonzero requested-to-final difference is valid only when every component is classified and explained. Refund, duplicate, personal/ineligible, and cap classifications must be mutually exclusive so the same amount is not deducted twice. A missing item or unexplained difference cannot be converted to zero by assumption.

## 3. Entry gate

- `PASS`: write `final_amount`.
- `PASS_WITH_DEDUCTION`: write `final_amount` only when the deduction follows a supplied rule without judgment and no required claimant acknowledgement remains; report source, eligibility amount, each deduction, and final amount.
- `PENDING_EVIDENCE`: do not write a new final amount. State the exact missing material or disputed fact and the evidence or authorized fact confirmation required.
- `PENDING_EXCEPTION_APPROVAL`: do not write a new final amount. State the policy deviation, amount affected, and required approval level/source.
- After resolution, record who resolved it, their role, time, exact scope, and basis; recalculate and change the decision to `PASS`, `PASS_WITH_DEDUCTION`, or `REJECT`. Only a pass state opens the entry gate.
- `REJECT`: do not write a new final amount. Preserve any pre-existing entry and list the corrective action needed.

The user's standing instruction that manually confirmed cases may later be registered defines the workflow; it is not itself confirmation of any future individual case.

## 4. Decision examples

- Complete evidence, valid invoice/payment, matching dates/route/identity, no duplicate, known standards, and balanced equations: `PASS`, then register.
- Complete evidence with a purely formula-based cap reduction and no required acknowledgement: `PASS_WITH_DEDUCTION`, then register the reduced amount.
- Missing invoice, certificate, appointment record, filed-place proof, mileage rule, or unexplained date/route difference: `PENDING_EVIDENCE`; do not register until cleared.
- Complete facts but an over-standard room, route deviation, or other permitted exception: `PENDING_EXCEPTION_APPROVAL`; do not register until the authorized scoped approval is recorded.
- Mandatory certificate confirmed absent, duplicate already reimbursed, invalid/voided evidence with no replacement, or denied exception: `REJECT`; do not register.

For an already-entered amount that is demonstrably arithmetically wrong, create a revision copy and correct only after the source itemization and OA/request amount agree. Report the old value, new value, and reason.

## 5. Duplicate and period checks

- Deduplicate first by invoice code/number, ticket/order number, payment serial, OA/request number, and existing ledger reference. Use person, category, period, route, vendor, and amount only as secondary signals.
- Treat a matching primary document identifier as a likely duplicate even if the submitted amount changed. Treat matching person/date/amount without a matching primary identifier as a review signal, not conclusive duplication.
- Do not add a record if the same `case_id` or verified primary document has already been entered.
- For repeated event blocks, match exact start/end dates before using the next blank block.
- For monthly columns, verify the header month rather than assuming a column letter.
- A blank cell and a zero have different meanings. Never turn missing evidence into zero expense.

## 6. OA status

Maintain these states outside the financial amount cells unless the template already provides a status field:

1. `审核中`
2. `可进入OA`
3. `OA审批中`
4. `OA已通过`
5. `已转工资核算`

Workbook editing alone does not advance the external OA or forwarding state.

Record the OA flow/reference and the exact approved workbook/version before changing a state to `OA已通过`. A later revision must return to the appropriate review state unless the approval explicitly covers it.

## 7. Final verification

- Reopen the saved workbook and read every changed cell.
- Recalculate the entered totals independently.
- Compare source and output workbook structure.
- Confirm that only authorized cells/parts changed.
- Render each changed area and inspect alignment, borders, number/date formats, clipping, and nearby headers.
- Keep unrelated pre-existing formula or external-link errors unchanged and report them separately.
