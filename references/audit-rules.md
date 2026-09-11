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

- Required evidence: work-request/OA flow, payment proof, training application, invoice, training agreement, and completion/certificate evidence.
- The application must state whether meals and lodging are included. If included arrangements exceed the approved travel standard, the excess is personal unless separately approved; outside lodging or meal allowance requires the corresponding explanation/approval.
- Match training provider, agreement, invoice, application, attendee, course, dates, and certificate/completion evidence.
- If the certificate or completion evidence is missing from the packet, mark the case `PENDING_EVIDENCE` and request supplementary evidence. Under the user's current no-certificate-no-reimbursement rule, a statement that training occurred does not replace a valid certificate. If it cannot be supplied, mark it `REJECT`; only a newer explicit company policy can authorize a different rule.
- Fuel and toll dates, route, and mileage must agree with the approved training time and location.
- Check that meals, lodging, transport, fuel, tolls, and allowances included in the training package are not also claimed through travel or another category. Use the approved mileage/fuel rule; if none is supplied, keep that component `PENDING_EVIDENCE`.
- Reconcile every person's itemized total using the workflow equations. An unexplained mismatch remains `PENDING_EVIDENCE` until corrected or supported.

## 电话费

- Confirm that the person and monthly standard are supported by the current ledger/policy.
- A newly appointed team leader starts reimbursement from the following month.
- The invoice buyer must be the company. Match the billed phone number to the person using the newest address book or approved personnel record.
- Match the billing/service period to the ledger month; allocate a multi-month bill only when the bill or operator statement supports the monthly split.
- Verify the appointment effective date and the first eligible month. For transfer, suspension, resignation, dual-role, or other eligibility changes, apply a supplied effective-period rule; otherwise keep the affected month `PENDING_EVIDENCE`.
- Calculate monthly reimbursable amount as the lesser of invoice amount and monthly standard. Enter the final monthly amount, not the uncapped invoice total. If claimant acknowledgement of a reduction is required by current policy, record it before entry.

## 探亲费

- Focus on authenticity: valid filed place, eligibility, annual scheme, used trip count, and remaining count.
- Match the approved leave, filing effective date, filed place, annual eligibility, permitted trip count, used trips, and remaining trips before calculating.
- Air and rail tickets must be real-name tickets.
- Fuel and toll dates must fall within or be explained against the approved leave period; route must match the filed place.
- When an expense precedes the leave date, require a specific explanation such as a night-shift departure. Do not accept a generic unexplained mismatch.
- Apply the applicable level/transport cap. Enter only the capped final amount.
- For self-driving fuel/tolls, require the applicable mileage/fuel calculation rule and reconcile dates, route, kilometers, fuel quantity/amount, and toll stations. If the rule is missing, keep the affected component `PENDING_EVIDENCE`.
- Check duplicate ticket/invoice/route fingerprints against linked travel reimbursements.

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
