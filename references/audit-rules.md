# 报销审核规则

These are the current baseline rules distilled from the user's workflow. A newer user-provided rule, valid signed approval, or company policy overrides this file. Record the conflict and the selected basis.

本版包含用户 2026-09-21 明确确认的业务口径。下列已被接受的情形属于正常规则，不是待审批例外；不得被通用核对要求或其他旧版专项 Skill 再次变成缺件。仅更新规则不代表已对某个具体报销包作出通过结论。

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
- 有可识别且与培训人员、课程对应的电子版合格证，即满足合格证明要求；不得仅因不是纸质原件继续挂起，也不额外要求纸质证书或电子证书再盖章。培训审批仍独立核对，证书通过不等于整个报销包已通过。
- If neither an electronic nor paper certificate/completion evidence is supplied, mark the case `PENDING_EVIDENCE`. A statement that training occurred does not replace a valid certificate. If it cannot be supplied, mark it `REJECT`; only a newer explicit company policy can authorize a different rule.
- 仅在发生并申报住宿费时，核对当期差旅标准对应的级别、地点、天数和房间数；不超标即可通过该项。未产生住宿的记为“不适用”，不要求住宿发票、不因缺住宿材料挂起；这不免除培训申请中已有食宿安排的重复报销核对。
- Calculate fuel only with the supplied effective fuel-consumption/mileage formula and vehicle/route evidence. Do not substitute the face value of fuel receipts for the calculated eligible amount. If the formula or required mileage inputs are absent, keep the fuel component `PENDING_EVIDENCE`.
- Toll occurrence dates and invoice issue dates must not precede the covered training journey. They may fall within the training period or after it when they correspond to the return journey or later invoicing. Dates, toll stations, route, and mileage must still agree with the approved training location and journey; an unexplained later date is `PENDING_EVIDENCE`.
- 加油费、过路费票据齐全，费用产生日期及开票日期均在培训期间，且与培训行程对应时，交通票据日期项直接通过，不追加延迟开票证明。培训后的票据按上一条判断，不把探亲油费的宽限口径套用于培训，也不将“培训期间即可通过”误写成一律禁止培训后票据。
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
- 探亲备案地一般登记到市；目的地为该市下属区、县的，按同一备案地核对，工作地点至该区县的有效路线截图及公里数可采用，不强求到市中心或与市级文字逐字相同。无法确定行政归属或跨备案市时再确认，不虚构具体地址。
- Verify the employee's current effective grade against the newest HR/appointment record and use that grade for the applicable home-leave standard. If the filing/ledger grade is stale or the effective grade is unclear, resolve it before calculating.
- 有假条且按适用考勤制度完成签批，即满足请假审批材料要求；也可使用有效家属探亲审批。核对人员、批准期间和探亲行程，不强制要求两种流程同时提供。考勤签批层级依据缺失、签批未完成或存在真实矛盾时再转人工确认。
- 探亲行程原则上在批准期间内；实际出发或返回可比批准边界提前或推后一天，但必须在报销材料中写明具体原因（如上夜班、中班或其他实际原因）。已有具体原因且无矛盾时按规则直接认可，不另设“独立确认”门槛。未写明具体原因的，结论写“不符合标准，待补充具体原因”，状态 `PENDING_EVIDENCE`，不登记；超一天不自动放行。机票、火车票、过路费按该实际行程窗口核对。
- 探亲加油费用产生于探亲期间或探亲后，即通过该项日期审核；相应开票日期在探亲期间或探亲后亦可，不因行程结束后发生或开票而要求补实际加油小票、支付记录、交易明细来证明只是延迟开票。不设置用户未给出的“探亲后最多几天”限制。仍核对票据有效、金额、路线/里程计算及重复报销等其他条件；本条不放宽机票、火车票、过路费的实际行程日期。
- Match the approved leave, filing effective date, filed place, annual eligibility, permitted trip count, used trips, and remaining trips before calculating. Use the ledger as the authoritative count record after checking that prior event blocks are not duplicated or omitted.
- Air and rail tickets must be real-name tickets.
- Reconcile every detail-sheet line to its attachment and require the pre-cap itemized total to equal the matched attachment total. Then apply the effective policy limit; enter only the final capped amount.
- Apply transport limits per one-way journey. When one direction uses two or more eligible transport modes, use the highest applicable one-way mode limit once; do not add mode limits together. Example: self-driving limit `700` RMB and rail/air limit `1,000` RMB means that direction is capped at `1,000` RMB, with reimbursement still limited to actual eligible cost.
- 自驾即可适用自驾规则，无需核实车辆与申请人的产权、借用或使用关系，不要求借车证明或车主授权。车辆型号、排量、百公里油耗用于计算，不用于增加车辆关系门槛。
- 按用户图片1计算：`计算油费（元）= 总公里数 ÷ 100 × 百公里油耗（升/100公里）× 加油发票单价（元/升）`。总公里数按实际有效行程汇总；不得将单程重复翻倍，不得自行猜测油耗或以总金额倒推出缺失的单价。记录路线截图、单/往返里程、车辆型号/排量、百公里油耗和发票单价的依据。多张不同单价票据需有对应计算分段或已确认的分摊口径，不擅自取最高价。
- 本次申报且未重复使用的加油发票合计金额不高于计算油费，即通过油费金额项，不要求发票金额恰好等于计算值。超过时仅按明确公式核减；参数或票据分摊不清则转人工，不猜数。油费可认可金额不高于申报金额、有效发票金额及计算油费三者的最小值；与有效过路费等合计后，再按方向和制度探亲限额计算最终可报金额，不能将计算油费作为额外补贴。
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
