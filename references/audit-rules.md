# 报销审核规则

These are the current baseline rules distilled from the user's workflow. A newer user-provided rule, valid signed approval, or company policy overrides this file. Record the conflict and the selected basis.

## 所有费用的通用控制

Before applying category rules, check:

- The governing policy/standard is identified by document/version and was effective for the expense date. A later one-off approval applies only to its stated scope.
- The request/OA basis covers the claimant, purpose, category, dates, route/location, and expected amount. A retrospective request or changed purpose requires the explanation/approval required by current policy.
- Required invoices/tickets are legible and complete. Check buyer/company title where required, seller, tax identifiers when present, invoice code/number, amount, date, and item description. If authoritative verification is available, check that an invoice is not voided, red-flushed, or otherwise invalid.
- Payment proof agrees with payer, payee/vendor, amount, date, and the claimed transaction. A third-party payment or split/combined payment needs a documented mapping and explanation.
- Identity matches across the request, invoice/ticket, payment, appointment/HR data, and ledger. Real-name tickets must belong to the claimant or documented eligible traveler.
- Refunds, cancellations, credit notes, reimbursements, and returned amounts are deducted.
- Search all relevant ledgers and linked categories for the same OA/request number, invoice code/number, ticket/order number, payment serial, and other primary document identifiers before using secondary date/route/amount similarity.
- If a required policy parameter or primary fact is absent, use `PENDING_EVIDENCE`; do not guess. If facts are complete but a permitted policy exception is requested, use `PENDING_EXCEPTION_APPROVAL`.

## 培训费

- Required process evidence: the reimbursement/work-request flow plus at least one approved training-application flow or travel flow that covers the participant, purpose, and training dates.
- Required attachment evidence: expense explanation, payment proof, relevant invoices, stamped training agreement, training certificate/completion evidence, and any claimed toll and fuel receipts. A draft or unstamped agreement does not satisfy the stamped-agreement requirement.
- Match each participant and the training start/end dates in the expense explanation to the approved training application or travel flow. An unexplained participant or date difference is `PENDING_EVIDENCE`.
- The application must state whether meals and lodging are included. If included arrangements exceed the approved travel standard, the excess is personal unless separately approved; outside lodging or meal allowance requires the corresponding explanation/approval.
- Match training provider, agreement, invoice, application, attendee, course, dates, and certificate/completion evidence.
- If the certificate or completion evidence is missing from the packet, mark the case `PENDING_EVIDENCE` and request supplementary evidence. Under the user's current no-certificate-no-reimbursement rule, a statement that training occurred does not replace a valid certificate. If it cannot be supplied, mark it `REJECT`; only a newer explicit company policy can authorize a different rule.
- Check lodging against the effective travel lodging standard for the participant's current grade, destination, eligible nights, room count, and occupants. A missing grade/destination standard is `PENDING_EVIDENCE`; an over-standard stay follows the documented exception-approval path when allowed.
- Calculate fuel only with the supplied effective fuel-consumption/mileage formula and vehicle/route evidence. Do not substitute the face value of fuel receipts for the calculated eligible amount. If the formula or required mileage inputs are absent, keep the fuel component `PENDING_EVIDENCE`.
- Toll occurrence dates and invoice issue dates must not precede the covered training journey. They may fall within the training period or after it when they correspond to the return journey or later invoicing. Dates, toll stations, route, and mileage must still agree with the approved training location and journey; an unexplained later date is `PENDING_EVIDENCE`.
- Check that meals, lodging, transport, fuel, tolls, and allowances included in the training package are not also claimed through travel or another category.
- Reconcile every person's itemized total using the workflow equations. An unexplained mismatch remains `PENDING_EVIDENCE` until corrected or supported.
- After the event is `PASS` or eligible `PASS_WITH_DEDUCTION`, update the training ledger with the verified start date, end date, and final reimbursable amount. Do not update a pending or rejected event.

## 电话费

- Confirm that the person and monthly standard are supported by the current ledger/policy.
- A newly appointed team leader starts reimbursement from the following month.
- The invoice buyer must be the company. Match the billed phone number to the person using the newest address book or approved personnel record.
- Match the billing/service period to the ledger month; allocate a multi-month bill only when the bill or operator statement supports the monthly split.
- Verify the appointment effective date and the first eligible month. For transfer, suspension, resignation, dual-role, or other eligibility changes, apply a supplied effective-period rule; otherwise keep the affected month `PENDING_EVIDENCE`.
- Calculate monthly reimbursable amount as the lesser of invoice amount and monthly standard. Enter the final monthly amount, not the uncapped invoice total. If claimant acknowledgement of a reduction is required by current policy, record it before entry.

## 探亲费

- Focus on authenticity: valid filed place, eligibility, annual scheme, used trip count, and remaining count.
- Compare the claimed filed place with the year-start filing and any later approved change history. Use the filed place effective for the journey date. A mismatch without an approved effective change is `PENDING_EVIDENCE` and is not cured by the reimbursement form alone.
- Verify the employee's current effective grade against the newest HR/appointment record and use that grade for the applicable home-leave standard. If the filing/ledger grade is stale or the effective grade is unclear, resolve it before calculating.
- Match the family-visit flow or leave flow to the claimant/traveler, approved start/end dates, filed place, purpose, and route. The detail-sheet start/end dates and every flight, rail, fuel, and toll occurrence date must fall within that approved period, except a specifically explained and independently confirmed work-schedule departure such as the documented night-shift case.
- Match the approved leave, filing effective date, filed place, annual eligibility, permitted trip count, used trips, and remaining trips before calculating. Use the ledger as the authoritative count record after checking that prior event blocks are not duplicated or omitted.
- Air and rail tickets must be real-name tickets.
- Reconcile every detail-sheet line to its attachment and require the pre-cap itemized total to equal the matched attachment total. Then apply the effective policy limit; enter only the final capped amount.
- Apply transport limits per one-way journey. When one direction uses two or more eligible transport modes, use the highest applicable one-way mode limit once; do not add mode limits together. Example: self-driving limit `700` RMB and rail/air limit `1,000` RMB means that direction is capped at `1,000` RMB, with reimbursement still limited to actual eligible cost.
- For self-driving fuel/tolls, require the applicable mileage/fuel calculation rule and reconcile dates, route, kilometers, fuel quantity/amount, and toll stations. If the rule is missing, keep the affected component `PENDING_EVIDENCE`.
- For a family visitor under age 12 on the journey start date, eligible home-leave expense may be reimbursed but consumes `0` of the employee's six-trip allowance. A visitor age 12 or older consumes the applicable trip count from the employee's six-trip allowance. Verify identity, relationship, and date of birth; if multiple age-12-or-older visitors share one flow and the ledger counting unit is unclear, use `PENDING_EVIDENCE` rather than inventing a count.
- Reject the event when the applicable ledger cycle already contains six consumed trips and the new event would exceed six. Do not use the calendar-year boundary alone: keep counting in the current cycle until the company-recognized next-year Spring Festival reset point, then start a new cycle. If the exact annual reset date is not supplied, use `PENDING_EVIDENCE` and request the annual notice/policy date.
- Check duplicate ticket/invoice/route fingerprints against linked travel reimbursements.
- After the event is `PASS` or eligible `PASS_WITH_DEDUCTION`, update the home-leave ledger with approved journey dates, final reimbursable amount, trip count consumed, remaining count, applicable cycle, and any under-12 no-count notation. Do not update a pending or rejected event.

## 差旅费

- Lodging must comply with the applicable standard.
- For employees below manager/deputy-manager level, two people on the same trip may use only one standard room under the user's stated rule.
- Determine meal allowance from whether the hotel includes breakfast. Under the user's current stated rule, breakfast included corresponds to 150 RMB/day unless a newer policy overrides it.
- Determine destination/rank lodging cap, eligible nights, transport class, allowance days, and departure/return-day treatment from the supplied effective standard. The known breakfast-included amount does not establish the amount for hotels without breakfast; do not infer it.
- If two eligible travelers should share one room, reconcile room occupants, dates, room count, and invoice. A separate room or over-standard stay requires the applicable scoped exception approval before reimbursement.
- Reconcile dates, routes, travelers, lodging nights, tickets, and any linked training/home-leave segments.

## 台账与后续流程

- Every reimbursement type requires a ledger maintained by the finance reviewer.
- Training, phone, home-leave, and related ledgers must circulate through OA.
- After approval, forward the approved ledger to 邓姐 and 小蔺 for payroll calculation.
- At month end, collect and update department home-leave filed places and evidence.
