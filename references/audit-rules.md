# 报销审核规则

These are the current baseline rules distilled from the user's workflow. A newer user-provided rule, valid signed approval, or company policy overrides this file. Record the conflict and the selected basis.

本版包含用户 2026-09-21 明确确认的业务口径。下列已被接受的情形属于正常规则，不是待审批例外；不得被通用核对要求或其他旧版专项 Skill 再次变成缺件。仅更新规则不代表已对某个具体报销包作出通过结论。

2026-10-21 补充培训/考试PDF取证、住宿数量、无早餐餐补及自驾分项核算口径。以下规则应用于具体材料后才能形成审核结论，不预设某一报销包已通过。

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
- **自行取数复算**：先从本次PDF中的路线/里程、车辆及油耗说明、发票行和适用油耗规则取数，记录来源页码。材料已写明且无冲突的有效往返里程、百公里油耗、单价和税率直接用于复算，不把可自行完成的计算列为“待确认油耗”；核对里程方向、是否重复翻倍、油耗单位和适用车辆/标准。只有必要参数确实缺失、不可读或相互矛盾才挂起油费，不猜油耗，也不倒推参数使申报额成立。
- **分开金额和费用种类**：原说明金额、有效油票额、本次申报油费、公式计算油费、核定油费分别记录；低于票据面额的申报按较低申报额审核，不自动补报差额，也不把未申报余额算作本次核减。过路费另按有效票据逐笔核对，`交通核定小计 = 核定油费 + 核定过路费 + 其他已核准交通费`，再适用该类别限额。不得从交通合计减油费倒推过路费代替核票。
- 原说明的往返油费高于本次申报额，而用户或当前明细已明确本次仅申报较低金额时，按该申报额复算，不再把原说明金额另加一次或继续询问是否全额申报。原说明数不自动等于有效发票金额；保留说明与本次申报的对应记录，真正影响票据、公式或小计的未解释差异才列待确认。

## 培训费

- **先核对完整PDF**：按本次文件清单核查合并PDF全部有关页面；扫描页或提取不到的页需渲染阅读，不能只查文件名、首页或可搜索文字。按“人员/事项—审批—协议—发票—结业或考试证明—住宿—交通—重复报销”建立文件及页码索引，记录已找到、已核对、不可读/冲突、确认缺失或不适用。某项材料藏在合并PDF内，不要求再次单独提供；找到材料仍须核对签批、盖章、人员、日期及金额，不能仅因存在就通过。
- PDF尚未检查完时，状态应为“材料待读取/核对中”，先继续读取；不据此宣称缺件。全部有关材料核对后，只有确实缺失、不可读或影响结论的冲突才列 `PENDING_EVIDENCE`，注明缺哪一项及查阅范围。审核底稿记录查重范围与结果，未取得相应历史资料时不得声称已完成跨报销查重。
- Required process evidence: the reimbursement/work-request flow plus at least one approved training/examination-application flow or travel flow that covers the participant, purpose, and event dates.
- Required pre-audit attachment evidence: expense explanation, relevant invoices, stamped training agreement, completion/certificate or examination evidence appropriate to the approved event, and any claimed lodging, toll and fuel receipts. A draft or unstamped agreement does not satisfy the stamped-agreement requirement. Read these inside the supplied PDFs before requesting replacements.
- **流程顺序：培训费用审核 → 审核通过 → 办理支付证明单 → 后续支付手续。** 用户确认支付证明单在审核通过后才会有，它不是审核前置材料。其他审核条件全部满足时，判为 `PASS` 或符合条件的 `PASS_WITH_DEDUCTION`，按核定金额及查重规则登记台账；不得仅因无支付证明单转 `PENDING_EVIDENCE`、拒报、要求人工豁免或阻止登记。
- 支付证明单与银行/微信等实际付款凭证是不同材料。不因支付证明单未生成就一律改要付款截图或银行流水；仅对适用制度明确要求、或解决实际金额/日期/交易对应矛盾所必需的付款证据核验。已有付款截图与发票不匹配等真实问题仍需确认；本条不免除培训申请审批、发票、协议、合格证及行程核对。
- 审核通过后，将支付证明单标为后续办理事项；取得后核对人员、事项和金额与最终审核结论及台账一致。审核通过、台账已登记、支付证明单已办理、实际已付款分别记录，不能互相替代；生成或提交单据、支付等外部操作仍需用户授权。
- Match each participant and the training start/end dates in the expense explanation to the approved training application or travel flow. An unexplained participant or date difference is `PENDING_EVIDENCE`.
- The application must state whether meals and lodging are included. If included arrangements exceed the approved travel standard, the excess is personal unless separately approved; outside lodging or meal allowance requires the corresponding explanation/approval.
- Match training/examination provider, agreement, invoice, application, attendee, course/exam, dates, and completion/examination evidence. Use evidence appropriate to the approved event; do not demand a second training-completion document when the applicable examination proof already meets that event's requirement.
- 有可识别且与培训人员、课程对应的电子版合格证，即满足合格证明要求；不得仅因不是纸质原件继续挂起，也不额外要求纸质证书或电子证书再盖章。培训审批仍独立核对，证书通过不等于整个报销包已通过。
- If no valid electronic or paper completion/certificate/examination evidence appropriate to the event is supplied, mark the case `PENDING_EVIDENCE`. A statement or attendance record alone does not replace the mandatory proof. Mark it `REJECT` only when the required proof is confirmed unavailable and cannot be supplied, with no policy-authorized alternative; a newer explicit company policy may authorize a different rule.
- 仅在发生并申报住宿费时，核对当期差旅标准对应的级别、地点、住宿数量和房间数。**以住宿发票载明的计费天数/晚数/房晚及单位为依据**，结合发票服务期间、入住人员、房间数和同包住宿明细核对；发票明确写10天时按10个计费天数审核，不另设“必须再证明10晚”的材料门槛，也不把7月21日至7月30日的日期差直接当9晚核减。发票写9晚则按9晚核，再核单价、金额及标准。“间夜”须识别房间数，共住房费只计一次。起止日期只作交叉核对，只有数量、人员、计费范围或金额出现真实矛盾才列具体疑点；发票只列总额时先查同包住宿明细取得数量。未产生住宿的记为“不适用”，不要求住宿发票、不因缺住宿材料挂起；这不免除食宿已包含的重复报销核对。
- 适用国内差旅全天餐补、酒店证明不含早餐且无其他供餐证据时，按早30元、午60元、晚60元，合计150元/人/有效全天核算，不再因“不含早餐标准未明确”挂起。同包可识别并对应入住的酒店订单或截图写明不含早餐，即可作为早餐依据，不重复索要另一份证明。仍核对已提供的机构/接待供餐安排，确已供餐才扣对应餐次；出发返回日及培训超过一个月、特定地域等已有专项标准按适用规则执行。酒店住宿限额仍按人员级别、地点和发票数量单独核对。
- Calculate fuel from the supplied effective mileage, fuel-consumption basis and vehicle/route evidence using the formula in “油价统一口径” above. When the inputs are already written in the PDFs, independently calculate the result and compare the requested amount, valid invoice amount and calculated amount; do not merely return “需核对油耗”. Do not substitute the face value of fuel receipts for the calculated eligible amount. Only genuinely absent or conflicting required inputs keep the fuel component `PENDING_EVIDENCE`; tolls are checked separately.
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
- **按人按月核算**：核对服务账期、票据/明细金额及手机号与人事身份；多月账单仅在有可追溯月度分摊时拆分。同一笔话费的报销明细、账单、发票或付款说明是相互对应的证据，只计一次费用；只有确定不同支出才合并金额，不为此扫描其他台账。金额或账期不可读/不明仍需确认，这是金额核算，不是财务发票有效性审核。
- **执行顺序**：先匹配员工及本人手机号，再定位服务月份、判断该月资格，随后取适用标准、核对票据与申报金额，最后逐人逐月给结论并登记。金额按服务月而非开票月归属；只影响个别月份的问题不阻塞其他已核清月份。
- 任职/调动记录只在确实影响所报月份资格时成为必核事实。最新HR及现有记录已能确定该月有资格、无影响该月的岗位变动时，不因未找到全部任职履历而挂起；现有记录确实不能判断该月是否已到起报月时才待确认。已明确早于起报月的，直接判该人月不予报销，不列“待补OA”。
- 每个有资格月份先算 `金额上限 = min(该人该月票据/账单金额, 最新统计表月标准)`。本次明细单列了该人月申报金额时，`最终实报金额 = min(申报金额, 金额上限)`，不得自动补高申报额；仅要求从票据编制报销明细且没有另列申报额时，按金额上限核算。票据面额高于申报不自动构成问题，未申报余额不等于本次核减。
- 已明确申报的，申报与核定相同为 `PASS`；按标准或票据金额确定性核减为 `PASS_WITH_DEDUCTION`，注明 `本次核减 = 申报金额 - 最终实报金额`；本人手机号、该月资格、标准、金额或分摊事实未清才 `PENDING_EVIDENCE`。身份/起报月份已明确不符则该人月不予报销，不登记。使用最终核定月金额登记，不把季度合计写进一个月，不将超额或未申报余额写入台账。
- 数值0与空值分别处理：执行标准明确为0时按0核算，不改取申请标准；执行字段有非数值或明确待执行标记时确认该实际问题，不绕过它取更高值。任何缺失事实只影响相应人月。
- 对外只给姓名、月份、话费范围结论、核定金额、登记动作和关键待办；金额底稿保留来源版本、实际表头/单元格、票据额、申报额、标准和差额。公司抬头/有效性由财务核的说明在整批结果中说明一次，不对每人重复列为“待确认”。
- 不做跨台账查重不改变登记目标格的写入方式：目标月格表示该人该月完整核定总额。完整重算才以核定月总额设置目标格，相同值不再累加，修改值记录依据；只收到追加/部分材料时，不能把本次金额当完整月总额覆盖，也不能盲目相加。仅写入关系不清时保留原格、列“登记待处理”，不改成发票重复报销或费用不合规；若月总额/标准余额本身未核清，受影响金额仍待确认。不额外要求其他台账来完成本次范围外查重。

## 探亲费

- **2026-10-21最新范围优先**：以下“无需在PDF另附”不等于取消事实核对；不得以通用材料、旧专项或人工确认规则恢复已取消的上传/说明门槛。
- Focus on authenticity: valid filed place, eligibility, annual scheme, used trip count, and remaining count.
- **核对来源而非重复附件**：PDF附件不要求另附探亲审批、备案地备案资料或年度已用/剩余次数截图。有效请假/探亲审批可从关联流程、OA或已有审批记录核验；备案地及变更、年度方案和已用/剩余次数从现有备案表、报销台账及可核记录核验，并在底稿记来源。已能核实的，不因PDF没有这些附件挂起或要求重复上传；确实无法取得必要记录或存在实质冲突时才列具体待办，不把“未随PDF上传”写成“未审批/未备案/次数未核”。仅有流程链接而未读取内容不等于已核。
- **个人与家属探亲分开**：员工本人探亲无需附亲属证明、亲属关系证明或探亲地证明，不因缺这些证明挂起。仍把申报目的地与现有有效备案记录核对；不另要求户口簿、居住证明等来再次证明已备案地点。家属探亲涉及报销资格及年龄计次，仍核对实际探亲人的身份、与员工关系及出生日期，可用已有可核记录，不将本人探亲的简化扩大为家属资料一律免核。本次不改变新建/变更备案的既有管理流程。
- Compare the claimed filed place with the year-start filing and any later approved change history. Use the filed place effective for the journey date. A mismatch without an approved effective change is `PENDING_EVIDENCE` and is not cured by the reimbursement form alone.
- 探亲备案地一般登记到市；目的地为该市下属区、县的，按同一备案地核对，工作地点至该区县的有效路线截图及公里数可采用，不强求到市中心或与市级文字逐字相同。无法确定行政归属或跨备案市时再确认，不虚构具体地址。
- Verify the employee's current effective grade against the newest HR/appointment record and use that grade for the applicable home-leave standard. If the filing/ledger grade is stale or the effective grade is unclear, resolve it before calculating.
- 有假条且按适用考勤制度完成签批，即满足请假审批要求；也可使用有效家属探亲审批。可读取关联流程核对，不强制审批截图在PDF内，也不要求两种流程同时提供。核对人员、批准期间和探亲行程；签批未完成、必要签批权限无法判断或存在真实矛盾时才转人工确认。
- **自驾过路费路线**：过路票据的起点、终点与本次申报探亲路线对应即可，按去程/返程方向分别核对，返程的起终点按反方向对应。地名及收费站可按能够确定的实际地区对应，不强求文字逐字相同；沿用备案市内区县有效规则。不要求中间高速、收费站序列、导航推荐路线完全一致，不因这些差别追加绕行说明或挂起。分段收费票可合并识别对应方向的整体起终点；明显无关路段或真正不能确定起终点时才列具体问题。油费仍独立按有效公里数、油耗及含税单价复算，起终点项通过不代表油费或整案自动通过。
- **自驾过路票一天容差**：通行时间在申报/批准期间内，或比对应出发/返回日、批准边界提前或推后一个自然日，且能对应本次探亲往返行程时，日期项直接符合标准。不得再以未写夜班、中班或晚下班等原因为缺件，不索要排班证明、额外说明或单独人工确认；不把通行时间直接改写为原批准日期。该规则只认可一天差异，不自动放行超过一天或无关行程的票据，也不叠加成两天。核对实际通行日期，单纯开票日期不冒充实际行程日期。
- **其他交通日期保持原口径**：机票、火车票等原则上在有效批准期间；提前或推后一天仍须材料中写明具体原因，有原因且无矛盾直接认可，无原因才待补。不得把自驾过路票的无说明一天容差推广到这些票据。探亲加油费用产生于探亲期间或探亲后，即通过该项日期审核；相应开票日期在探亲期间或探亲后亦可，不因行程结束后发生或开票而要求补实际加油小票、支付记录、交易明细来证明只是延迟开票。不设置用户未给出的“探亲后最多几天”限制。仍核对票据有效、金额、里程油耗及重复报销等其他条件；三类日期口径分别记录。
- Match the approved leave, filing effective date, filed place, annual eligibility, permitted trip count, used trips, and remaining trips before calculating. Use the ledger as the authoritative count record after checking that prior event blocks are not duplicated or omitted.
- Air and rail tickets must be real-name tickets.
- Reconcile every detail-sheet line to the usable attachment amount within the current requested scope. Record any eligible invoice balance outside that scope separately; the full invoice face value need not equal a lower current request. Apply the effective policy limit to the reconciled eligible amount; enter only the final capped amount.
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
- 国内适用全天餐补为150元/人/天，分早30元、午60元、晚60元。酒店不含早餐且无其他供餐证据时保留早餐补助；含早餐则扣30元，全天仅剩午晚餐时为120元。其他已供餐餐次按对应标准扣除，不得沿用“含早餐仍按150、不含早餐待确认”的旧口径。较新的有效制度或适用专项标准优先。
- Determine destination/rank lodging cap, eligible nights, transport class, allowance days, and departure/return-day treatment from the supplied effective standard. Verify lodging quantity from the invoice and associated stay details, not solely the inclusive calendar-day count.
- If two eligible travelers should share one room, reconcile room occupants, dates, room count, and invoice. A separate room or over-standard stay requires the applicable scoped exception approval before reimbursement.
- Reconcile dates, routes, travelers, lodging nights, tickets, and any linked training/home-leave segments.

## 台账与后续流程

- Every reimbursement type requires a ledger maintained by the finance reviewer.
- Training, phone, home-leave, and related ledgers must circulate through OA.
- After approval, forward the approved ledger to 邓姐 and 小蔺 for payroll calculation.
- At month end, collect and update department home-leave filed places and evidence.
