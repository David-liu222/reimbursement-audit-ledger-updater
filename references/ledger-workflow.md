# 审核到台账的工作流

## 电话费的范围与金额路径（2026-10-12）

电话费使用最新版人事表核身份手机号、任职调动及起报月，最新版2026电话费/燃油费人员统计表核月标准，服务账期和金额按人月核算。无需OA报销申请依据、公司抬头/发票有效性审核、其他台账发票号/月/金额查重；下面通用字段、方程、示例和确认后的复核不得把这些重新设为门槛。

- `case_id` 用人员稳定标识＋服务月份；OA及发票号可不适用，不为了补齐字段索要这些资料。
- `requested_amount` 可取本次报销明细单列的人月申报金额，金额输入取可对应到人月的票据/账单；不校验OA申请依据或要求与OA审批额核对。不自动将票据额当作较低申报额的补足金额。
- `duplicate_amount` 在本话费范围为“不适用”，不记录“已查无重复”，也不为使通用方程成立而要求查其他台账。已明确申报时，`final_amount = min(申报金额, 人月票据/账单金额, 最新统计表月标准)`；仅编制票据报销明细而未单列申报时，按票据额与标准两者取低。前提是该服务月具备HR核定的资格；本次核减按申报减核定计算，票据未申报余额单列，不记作扣减。金额、账期等事实未清时不先填最终金额或0。
- 所报人月资格已经确定时，不额外索要全部任职历史；资格明确不符的月份直接不予报销，只有无法判断资格的月份才挂起。分月状态分别判定，其他已核清月份继续处理。
- 本次明细、账单与发票对同笔费用仅计一次，不把多种证据相加。目标月格表示完整月度核定总额：完整重算时按核定值设置，相同值不再累加，不同值记录修订依据；收到部分/追加材料时保留原格，先厘清完整月构成及本次写入关系，不能自动覆盖或相加。仅登记操作关系不清可保留审核通过、登记待处理；金额/月限额本身未清则该人月PENDING_EVIDENCE。这些都是本次金额与写入处理，不是跨台账发票合规查重。
- 审核结果及是否可登记只取本类别适用项。后续OA审批和工资转发状态仍据实际发生记录，不因不核OA申请依据就推断已完成。

## 1. Build the audit table

培训/考试先逐页读取本次PDF及扫描页，按人员/事项和材料类型建立“文件＋页码＋关键数据＋核对结论”的证据索引，再列真实缺件。审批、协议、发票、结业或考试证明可能同处一个PDF，不因文件名未命中而判缺。所需数据已可读取时继续完成公式与票据核对，对外给结果及确实未解决的问题，不只复述审核清单。

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
| unrequested_evidenced_amount | eligible evidenced balance outside the current requested scope, determined after refund/duplicate/ineligible exclusions per item; not a current-request deduction |
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
| category_controls | category-specific facts such as current grade, filed place, trip cycle/count, child age, transport modes, lodging cap, or fuel-calculation basis |

## 2. Reconciliation controls

Before entry, independently calculate and retain in the audit working record (show the concise decision first, not the full checklist):

- each person-event itemization;
- each person's category total;
- category total;
- requested/OA total;
- evidenced gross and refund totals;
- eligible-before-cap total;
- unsupported-requested, duplicate, personal/ineligible, and cap-deduction totals;
- proposed ledger total.

The following equations must balance to `0.00` for the categories to which they apply; phone fees use the person-month path above and do not require an OA comparison or cross-ledger duplicate term:

1. `net_evidenced_amount = evidenced_gross_amount - refund_amount`
2. For each item, first determine `available_evidenced_amount = net_evidenced_amount - duplicate_amount - personal_or_ineligible_amount`, then `unrequested_evidenced_amount = max(0, available_evidenced_amount - requested_amount)` and `eligible_before_cap = available_evidenced_amount - unrequested_evidenced_amount`. Calculate and sum by item; do not offset one item's excess against another item's shortfall. An unknown requested amount is not zero.
3. `final_amount = eligible_before_cap - cap_deduction`, never below `0.00`.
4. `requested_amount - final_amount = documented variance`; identify any `unsupported_requested_amount` within that variance instead of treating it as evidenced expenditure.
5. `proposed ledger total = sum(final_amount)` for the included cases.
6. After OA/payment approval, `approved payable total = final ledger total`; before approval, do not claim those totals have reconciled.

A nonzero requested-to-final difference is valid only when every component is classified and explained. Refund, duplicate, personal/ineligible, and cap classifications must be mutually exclusive so the same amount is not deducted twice. A missing item or unexplained difference cannot be converted to zero by assumption.

本次核减以 `requested_amount - final_amount` 为准，未申报票据余额单列，不写成核减；同一支出在说明、发票和计算表中重复出现只计一次。自驾按每项申报额、有效票据额和公式额取低，再合并独立核定的过路费；不得用更高的油票额补足本次较低申报，也不得由小计倒推出过路费充作已核结果。公式额度造成的限制按制度扣减归类并保留逐项依据，不重复扣两遍。

## 3. Entry gate

- `PASS`: write `final_amount` once the target write is resolved. 电话费仅登记关系不明时，保留通过及原目标格，列登记待处理；不是把通过状态改成缺件。
- `PASS_WITH_DEDUCTION`: write `final_amount` only when the deduction follows a supplied rule without judgment and no required claimant acknowledgement remains; report source, eligibility amount, each deduction, and final amount.
- `PENDING_EVIDENCE`: do not write a new final amount. State the exact missing material or disputed fact and the evidence or authorized fact confirmation required.
- `PENDING_EXCEPTION_APPROVAL`: do not write a new final amount. State the policy deviation, amount affected, and required approval level/source.
- After resolution, record who resolved it, their role, time, exact scope, and basis; recalculate and change the decision to `PASS`, `PASS_WITH_DEDUCTION`, or `REJECT`. Only a pass state opens the entry gate.
- `REJECT`: do not write a new final amount. Preserve any pre-existing entry and list the corrective action needed.

The user's standing instruction that manually confirmed cases may later be registered defines the workflow; it is not itself confirmation of any future individual case.

培训费的支付证明单在费用审核通过后办理，不属于此处的审核前置材料或登记门槛。其他条件完整且查重通过时，即使支付证明单尚未生成，也可按PASS或符合条件的PASS_WITH_DEDUCTION登记；把“待办理支付证明单”列为后续事项，不列入缺件清单。只有真正未解决的审批、票据、行程或必要交易证据问题才继续挂起。

## 4. Decision examples

- Complete evidence required at the current audit stage, valid invoices and any applicable transaction evidence, matching dates/route/identity, no duplicate, known standards, and balanced equations: `PASS`, then register. For training, a not-yet-issued post-audit 支付证明单 does not change this result.
- Complete evidence with a purely formula-based cap reduction and no required acknowledgement: `PASS_WITH_DEDUCTION`, then register the reduced amount.
- Missing invoice, certificate, appointment record, filed-place proof, mileage rule, or unexplained date/route difference: `PENDING_EVIDENCE`; do not register until cleared.
- Complete facts but an over-standard room, route deviation, or other permitted exception: `PENDING_EXCEPTION_APPROVAL`; do not register until the authorized scoped approval is recorded.
- Mandatory completion/examination proof confirmed unavailable and unable to be supplied, with no policy-authorized alternative; duplicate already reimbursed; invalid/voided evidence with no replacement; or denied exception: `REJECT`; do not register. A document merely absent from the current package remains on the evidence-supply path first.

For home leave, a six-trip cycle, an under-12 zero-count event, and a post-Spring-Festival reset affect `category_controls` and the ledger count, not the amount reconciliation equations. For mixed transport, record modes by direction and apply only the highest applicable one-way cap for that direction.

For training/examinations, retain the approved event/travel period and the PDF page index in `category_controls` or the audit report. Lodging records need invoice quantity/unit, service period, rooms/occupants, matched eligible nights and applicable cap. Meal records need the breakfast/other-meal evidence, eligible days, applicable meal rates and deductions. Fuel records need the original explanation amount, actual valid invoice amount, current requested fuel amount, effective mileage, consumption, raw price/tax rate/tax-inclusive price, calculated fuel amount and allowed fuel amount; retain source pages for each input. Itemize toll evidence and allowed toll amount separately, then reconcile the transport subtotal. These are audit results to calculate from existing material, not an automatic missing-evidence checklist.

For an already-entered amount that is demonstrably arithmetically wrong, create a revision copy and correct only after the source itemization and OA/request amount agree. Report the old value, new value, and reason.

## 5. Duplicate and period checks

以下跨台账/原始凭证查重要求不适用于电话费。电话费仅核本人账期、月标准、HR起报月，以及登记目标格不重复累加；不得因其他台账缺失或未完成发票号/月/金额查重而阻止话费通过。其他类别继续执行以下规则。

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

For training, separately track 支付证明单 as “审核通过后待办理 / 已办理” only from actual evidence. Missing a post-audit form does not reverse an otherwise valid audit pass, and an issued form is not proof of actual payment. Do not infer payment or complete downstream actions automatically.

Record the OA flow/reference and the exact approved workbook/version before changing a state to `OA已通过`. A later revision must return to the appropriate review state unless the approval explicitly covers it.

## 7. Final verification

- Reopen the saved workbook and read every changed cell.
- Recalculate the entered totals independently.
- Compare source and output workbook structure.
- Confirm that only authorized cells/parts changed.
- Render each changed area and inspect alignment, borders, number/date formats, clipping, and nearby headers.
- Keep unrelated pre-existing formula or external-link errors unchanged and report them separately.
