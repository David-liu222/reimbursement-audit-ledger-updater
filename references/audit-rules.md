# 报销审核规则

These are the current baseline rules distilled from the user's workflow. A newer user-provided rule, valid signed approval, or company policy overrides this file. Record the conflict and the selected basis.

本版包含用户 2026-09-21 明确确认的业务口径。下列已被接受的情形属于正常规则，不是待审批例外；不得被通用核对要求或其他旧版专项 Skill 再次变成缺件。仅更新规则不代表已对某个具体报销包作出通过结论。

## 所有费用的通用控制

先适用该费用类别的范围。2026-10-12用户确认：电话费不执行以下通用控制中的公司抬头/发票有效性审核、OA报销申请依据审核、与其他台账的发票号/月/金额查重；这些事项交财务或不属本技能范围，不作为电话费挂起、拒报或登记的前置条件。其他类别仍执行各自适用控制。

For the controls applicable to the selected category, check:

- The governing policy/standard is identified by document/version and was effective for the expense date. A later one-off approval applies only to its stated scope.
- The request/OA basis covers the claimant, purpose, category, dates, route/location, and expected amount. A retrospective request or changed purpose requires the explanation/approval required by current policy.
- Required invoices/tickets are legible and complete. Check buyer/company title where required, seller, tax identifiers when present, invoice code/number, amount, date, and item description. If authoritative verification is available, check that an invoice is not voided, red-flushed, or otherwise invalid.
- Where actual transaction evidence is supplied or required by the applicable expense rule, match payer, payee/vendor, amount, date, and the claimed transaction. A third-party payment or split/combined payment needs a documented mapping and explanation. Do not confuse transaction evidence with a post-audit 支付证明单; apply the training stage rule below rather than making that form a universal audit prerequisite.
- Identity matches across the request, invoice/ticket, payment, appointment/HR data, and ledger. Real-name tickets must belong to the claimant or documented eligible traveler.
- Refunds, cancellations, credit notes, reimbursements, and returned amounts are deducted.
- Search all relevant ledgers and linked categories for the same OA/request number, invoice code/number, ticket/order number, payment serial, and other primary document identifiers before using secondary date/route/amount similarity.
- If a required policy parameter or primary fact is absent, use `PENDING_EVIDENCE`; do not guess. If facts are complete but a permitted policy exception is requested, use `PENDING_EXCEPTION_APPROVAL`.

## 油价统一口径（2026-09-21 用户确认）

- 探亲、培训及其他按里程油耗公式审核的油费，油价统一使用加油发票对应的**含税单价**。不得将未税单价直接代入后与含税申报金额比较。
- 发票明确列出含税单价时直接使用；单价栏为未税价时，按同一油品行的实际税率换算：`含税单价 = 未税单价 ×（1 + 该行税率）`。不得把示例13%当作固定税率；已含税的单价不重复加税。票据明确免税或零税率时按其实际口径计算。
- 保留原始单价、税率和换算值的精度，先完成里程油耗计算，再将金额四舍五入到分，不先把单价截成两位小数。有折扣时采用票据明确对应的折后含税单价，折扣、退款亦须从有效票据金额中扣除；无法明确归属的折扣或税价信息冲突才转人工确认，不擅自分摊或猜税率，也不以总金额倒推出缺失的单价。
- `计算油费 = 有效公里数 ÷ 100 × 百公里油耗 × 含税单价`；油费可认可金额仍不超过申报金额、扣除折扣退款后的有效含税票据金额、计算油费三者的最小值。再按对应类别、行程方向和制度限额审核；含税口径明确不免除审批、行程、参数来源和查重要求。

## 培训费

- Required process evidence: the reimbursement/work-request flow plus at least one approved training-application flow or travel flow that covers the participant, purpose, and training dates.
- Required pre-audit attachment evidence: expense explanation, relevant invoices, stamped training agreement, training certificate/completion evidence, and any claimed toll and fuel receipts. A draft or unstamped agreement does not satisfy the stamped-agreement requirement.
- **流程顺序：培训费用审核 → 审核通过 → 办理支付证明单 → 后续支付手续。** 用户确认支付证明单在审核通过后才会有，它不是审核前置材料。其他审核条件全部满足时，判为 `PASS` 或符合条件的 `PASS_WITH_DEDUCTION`，按核定金额及查重规则登记台账；不得仅因无支付证明单转 `PENDING_EVIDENCE`、拒报、要求人工豁免或阻止登记。
- 支付证明单与银行/微信等实际付款凭证是不同材料。不因支付证明单未生成就一律改要付款截图或银行流水；仅对适用制度明确要求、或解决实际金额/日期/交易对应矛盾所必需的付款证据核验。已有付款截图与发票不匹配等真实问题仍需确认；本条不免除培训申请审批、发票、协议、合格证及行程核对。
- 审核通过后，将支付证明单标为后续办理事项；取得后核对人员、事项和金额与最终审核结论及台账一致。审核通过、台账已登记、支付证明单已办理、实际已付款分别记录，不能互相替代；生成或提交单据、支付等外部操作仍需用户授权。
- Match each participant and the training start/end dates in the expense explanation to the approved training application or travel flow. An unexplained participant or date difference is `PENDING_EVIDENCE`.
- The application must state whether meals and lodging are included. If included arrangements exceed the approved travel standard, the excess is personal unless separately approved; outside lodging or meal allowance requires the corresponding explanation/approval.
- Match training provider, agreement, invoice, application, attendee, course, dates, and certificate/completion evidence.
- 有可识别且与培训人员、课程对应的电子版合格证，即满足合格证明要求；不得仅因不是纸质原件继续挂起，也不额外要求纸质证书或电子证书再盖章。培训审批仍独立核对，证书通过不等于整个报销包已通过。
- If neither an electronic nor paper certificate/completion evidence is supplied, mark the case `PENDING_EVIDENCE`. A statement that training occurred does not replace a valid certificate. If it cannot be supplied, mark it `REJECT`; only a newer explicit company policy can authorize a different rule.
- 仅在发生并申报住宿费时，核对当期差旅标准对应的级别、地点、天数和房间数；不超标即可通过该项。未产生住宿的记为“不适用”，不要求住宿发票、不因缺住宿材料挂起；这不免除培训申请中已有食宿安排的重复报销核对。
- Calculate fuel only with the supplied effective fuel-consumption/mileage formula and vehicle/route evidence. Apply the tax-inclusive unit-price basis in “油价统一口径” above. Do not substitute the face value of fuel receipts for the calculated eligible amount. If the formula or required mileage inputs are absent, keep the fuel component `PENDING_EVIDENCE`.
- Toll occurrence dates and invoice issue dates must not precede the covered training journey. They may fall within the training period or after it when they correspond to the return journey or later invoicing. Dates, toll stations, route, and mileage must still agree with the approved training location and journey; an unexplained later date is `PENDING_EVIDENCE`.
- 加油费、过路费票据齐全，费用产生日期及开票日期均在培训期间，且与培训行程对应时，交通票据日期项直接通过，不追加延迟开票证明。培训后的票据按上一条判断，不把探亲油费的宽限口径套用于培训，也不将“培训期间即可通过”误写成一律禁止培训后票据。
- Check that meals, lodging, transport, fuel, tolls, and allowances included in the training package are not also claimed through travel or another category.
- Reconcile every person's itemized total using the workflow equations. An unexplained mismatch remains `PENDING_EVIDENCE` until corrected or supported.
- After the event is `PASS` or eligible `PASS_WITH_DEDUCTION`, update the training ledger with the verified start date, end date, and final reimbursable amount. Do not update a pending or rejected event.

## 电话费（2026-10-12用户更新）

- **分工范围**：无需核对发票公司抬头、购买方税号/地址/银行信息及发票真伪、作废/红冲等有效性，这些由财务审核；本技能的结论写“话费范围审核通过”，不得声称已完成财务发票有效性审核。
- **不核OA申请依据及跨台账查重**：不要求OA报销申请或其审批依据，不与其他台账按发票号、月份、金额查重；缺OA或其他台账不挂起。此调整仅适用于话费，后续台账OA流转及审批后的工资转发仍保留。
- **手机号→人事报表**：参照最新版人事报表中姓名对应的本人手机号/联系电话，结合工号、工作单位及部门处理重名，再核对票据手机号。不得采用紧急联系人电话，也不以旧通讯录覆盖人事表。本人手机号缺失、姓名无法唯一匹配或确实不一致时才列人工确认，不自行以发票号码填回人员资料。
- **月标准→最新统计表**：全部话费人员按最新版《2026年：电话费、燃油费报销人员统计》所载标准审核，不以固定制度金额、旧台账、岗位推断金额覆盖。任命人员取“话费报销标准”；无任命人员有有效数值的“已执行标准”时采用该值，该字段空时采用同一最新版表“话费申请标准”。用户指定的最新版表即为标准依据，不额外索要OA证明；“建议调整标准”不自动作为已执行标准。明确标注未执行、数值缺失或真实冲突时再确认。
- **任职生效与起报月→人事任职/调动记录**：使用最新版人事报表“任职汇总表”“调动人员明细表”及任职履历，按所报服务月份对应的有效记录核定；不能把入职、发文、合同或统计表审批日期当任职生效日。人事记录明确起报月份时按其执行；新任班组长仍从任职次月起报。相关任职日期缺失或调动时间冲突影响所报月份时才确认，不再索要OA申请依据替代。
- **按人按月核算**：核对服务账期、票据/明细金额及手机号与人事身份；多月账单仅在有可追溯月度分摊时拆分。金额或账期不可读/不明仍需确认，这是金额核算，不是财务发票有效性审核。
- 每个有资格月份：`实报金额 = min(该人该月票据/账单金额, 最新统计表月标准)`；不符合起报月份的金额不予纳入。使用最终核定月金额登记，不把季度合计写进一个月，不将未报销的超额部分写入台账。
- 不做跨台账查重不改变登记目标格的写入方式：同一人同一月再次运行，核定值相同则不重复累加，值不同时说明修订依据。目标写入冲突可待处理，但不标为“发票重复报销”或新增电话费合规缺件。

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
- 按用户图片1及最新含税口径计算：`计算油费（元）= 总公里数 ÷ 100 × 百公里油耗（升/100公里）× 加油发票含税单价（元/升）`，单价取值和换算遵循上文“油价统一口径”。总公里数按实际有效行程汇总；不得将单程重复翻倍，不得自行猜测油耗或以总金额倒推出缺失的单价。记录路线截图、单/往返里程、车辆型号/排量、百公里油耗和发票单价、税率及含税换算的依据。多张不同单价票据需有对应计算分段或已确认的分摊口径，不擅自取最高价。
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
