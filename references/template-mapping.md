# 2026 台账模板结构

Use this reference only for the known 2026 templates or a workbook confirmed to have the same structure. Always inspect actual headers first.

## 电话费、燃油费报销人员统计.xlsx

### 2026-10-12话费取数更新

标准来源为用户提供的最新版2026统计表；手机号、任职及起报月份来自最新版人事报表。2026-09-30人事表当前字段定位如下，仅供查找，执行时仍按表头发现：

- `在职人员信息表`：F姓名、E工号、C工作单位、G工作部门、AD联系电话；AE为紧急联系人电话，不得用于本人手机号。
- `任职汇总表`：D姓名、C工号、I任职日期、K任职履历。
- `调动人员明细表`：D姓名、C工号、F调动时间，E/G原部门岗位，H/I调动部门岗位。读取与服务月份对应的生效记录，不以表的生成日期替代。
- 2026统计表 `任命人员话费福利`：C姓名、I话费报销标准。
- 2026统计表 `无任命人员话费福利`：C姓名、J话费申请标准、K已执行标准、L建议调整标准。有有效K则用K，K空则按用户指定最新版J；L不是自动生效值。H开始报销月份/I报销依据/P审批时间不替代人事任职调动依据，也不触发OA校验。
- 旧通讯录、旧版内置人事简表及历史2023页仅供历史对照；不得在最新字段缺失时静默代用。用户以后提供更新版本时重识别字段和来源，不固定本次行号。

Primary current-year sheet: `无任命人员话费福利`.

- Match employees by name plus identity/personnel data; the known current sheet stores the name in column C.
- Monthly phone columns are grouped under `电话费`, normally January through December in columns T:AE.
- Enter monthly final reimbursable amounts. Do not place quarterly totals in one month.
- Home-leave filed place and trip blocks normally begin at column AF. Read the two header rows to resolve exact start/end/amount triplets.
- Before appending a home-leave event, reconcile the effective filed place, current grade, approved leave/family-visit period, transport cap, and current cycle's consumed-trip count. Do not infer the count only from nonblank amounts when an under-12 event is marked as non-counting.
- Write the verified start/end dates and final reimbursable amount only after a pass decision. Preserve or add an audit/remarks record for trip count consumed (`0` for a verified under-12 family visitor), remaining count, cycle/reset basis, and mixed-transport one-way cap when the template permits; otherwise keep these in the linked audit report.
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
- Use the verified training dates matched to the expense explanation and approved training/travel flow. Enter the audited final amount after accommodation, calculated fuel, toll, duplicate, and cap checks.
- Append only to the first completely blank triplet after the event is `PASS` or `PASS_WITH_DEDUCTION`.

## 探亲备案地备案统计表.xls

Known fields normally include department, name, ID number, position, grade, filed place, work-location housing status, proof status, and remarks.

- Match by ID first.
- Add or change a filed place only from the department's month-end update and supporting evidence.
- For a change, retain a revision copy and record the effective year/date and approval basis in the existing remarks field when the template permits.
- `.xls` is a binary format. Prefer native Excel editing. If native editing is unavailable, save a separately named `.xlsx` revision and disclose the conversion.

## Do Not Hard-Code

Rows change as employees are added or moved. Find rows by stable identity and columns by visible headers. Treat the coordinates above as a verified starting point, not a universal schema.
