# 人工确认与例外审批权限

Use this matrix whenever a case cannot pass directly. Prefer an explicit company authority matrix or OA routing rule when supplied; this file defines the safe fallback.

| Role/source | May establish | May not establish alone |
| --- | --- | --- |
| Claimant or preparer | Supply missing documents; explain dates, route, purpose, payment, or participants | Approve their own reimbursement; waive a mandatory document; authorize an over-standard exception |
| Department/business confirmer | Confirm business purpose, attendance, itinerary, participants, work schedule, or why an event date differs | Validate invoice status, alter finance calculations, or waive company reimbursement policy unless separately authorized |
| Finance reviewer | Verify document completeness, invoice/payment mapping, duplicates, calculations, caps, ledger entry, and whether evidence clears a fact issue | Invent missing standards or approve a policy exception unless a supplied authority rule grants that power |
| Authorized OA/management approver | Approve the specific exception types and amounts within the supplied authority/routing rule | Turn a non-waivable condition into a payable item or approve beyond the scope/limit of their authority |
| Authoritative system/document | Verify invoice status, appointment date, ticket identity, payment transaction, OA status, or policy version | Supply business judgment not represented in the source |

## Resolution rules

- `PENDING_EVIDENCE` requires the missing document, authoritative system record, or a permitted fact confirmation from an independent role. A claimant's explanation is evidence to review, not self-approval.
- A mandatory material such as the training certificate under the current rule must actually be supplied and matched. It cannot be replaced by an informal confirmation.
- `PENDING_EXCEPTION_APPROVAL` requires an OA approval or other recorded approval that identifies the claimant/event, exception, affected period, and amount. Confirm that the approver is authorized for that exception.
- Never infer authority from job title alone when the company has not supplied an approval matrix. Keep the item pending and state which authority rule is missing.
- Record resolver name, role, timestamp, conclusion, scope, and source reference. Preserve the underlying message/document with the case record when permitted.
- After resolution, rerun duplicate, amount, cap, date, route, and total checks. Resolution of one issue does not clear unrelated issues.
