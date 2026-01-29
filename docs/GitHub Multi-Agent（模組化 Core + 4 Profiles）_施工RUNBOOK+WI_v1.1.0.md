GitHub Multi-Agent（模組化 Core + 4 Profiles）_施工RUNBOOK+WI
________________


文件元資料 (Document Metadata)
項目
	內容
	doc_id
	GMA-RUNBOOK-WI-001
	version
	v1.1.0
	last_updated
	2026-01-29
	scope
	v0 (Vibe + Dev Lane)
	lanes
	vibe + dev
	authority
	Implementation SSOT（施工手冊）
	diátaxis_type
	How-to（操作導向）
	source_docs
	SRS v1.1.0, TVS v0.4.1, LBP v1.1.0, v0 Pack v0.3.0, 架構指南, README v1.1
	evidence_set
	evidence_index.json, tvs_section9_verdict.json, tvs_v0.4.1_complete_evidence_bundle_v2.json
	upgrade_from
	v1.0.0
	________________


SSOT / Evidence / Gate 定位聲明
本文件為 Implementation SSOT（施工手冊），只描述「怎麼做」，不「立法」。
SSOT 類型
	權威文件
	本文件角色
	規範 SSOT
	SRS v1.1.0
	引用 [Ref: SRS ...]
	操作 SSOT
	本 RUNBOOK+WI
	施工指引
	機械 SSOT
	Registry (v0 Pack)
	引用 [Ref: v0 Pack ...]
	導入策略
	TVS v0.4.1
	引用 [Ref: TVS ...]
	Evidence 定位：所有 evidence 路徑以 evidence_index.json 的 A~F 分類為準。
Gate 定位：v0 GateKit 固定 6 gates（[Ref: LBP Success Definition]；[Ref: v0 Pack NORM-21] 約束不得新增），不得新增。
________________


導讀（≤12 行，AI/LLM 易檢索）
1. 如何用：依 R0~R7 主流程執行施工；遇到具體操作，跳轉 WI-ENV/WI-CP/WI-DEV/WI-FAIL。
2. 如何檢索：使用 TOC 錨點或搜尋關鍵字；術語映射見"索引與映射"章節。
3. 如何避免遺漏：
   * 每個硬約束必須有：(a) Runbook 章節落點，(b) WI 編號，(c) 驗證信號，(d) Evidence 落點。
   * Coverage Ledger (R5) 提供完整映射；Appendix B 提供 20+ 條抽核。
4. RAG-Triad 提示：
   * Context：所有引用必須指向具體上游條款（SRS/TVS/LBP/v0 Pack）。
   * Grounding：所有驗證信號必須有 evidence 落點。
   * Utility：所有步驟必須可照做（含命令/範例）。
5. 防幻覺：無 [Ref:] 標註的陳述不構成規範；AI 嚴禁腦補需求。
________________


目錄 (Table of Contents)
RUNBOOK 區塊
* R0. 總則（原則/定位/邊界/職責/RACI）
* R1. 施工前置：v0 施工準備
* R2. 施工主流程（Phase-0 ~ Phase-5）
   * R2.1 Phase-0：Input Seal
   * R2.2 Phase-1：Plan Freeze
   * R2.3 Phase-2：Implementation
   * R2.4 Phase-3：Local GateKit 預檢
   * R2.5 Phase-4：Dual-Judge
   * R2.6 Phase-5：PR & Merge Queue
   * R2.7 ID 規約與命名一致性
* R3. Evidence 與可回放
* R4. 驗收清單（Acceptance Checklist）
* R5. 覆蓋台帳（Coverage Ledger）
* R6. Failure Handling（失敗處理）
* R7. 變更控制（Change Control）
WORK INSTRUCTIONS 區塊
* WI-ENV：環境指令
   * WI-ENV-01：建立/重建 Codespace
   * WI-ENV-02：Secrets/權限收斂
   * WI-ENV-03：Codespaces 成本與停用策略
* WI-CP：控制平面指令
   * WI-CP-01：Ruleset 變更與 settings_evidence
   * WI-CP-02：Workflow permissions 最小化
   * WI-CP-03：MQ + merge_group 合規自檢
* WI-DEV：v0 施工主線指令
   * WI-DEV-01：Input Seal & Plan Freeze
   * WI-DEV-02：One-Writer 實作與 worktree 並行
   * WI-DEV-03：Local GateKit 預檢 + Stopline
   * WI-DEV-04：Dual-Judge 與 Negative Test
   * WI-DEV-05：PR → MQ 合流
* WI-FAIL：失敗處理指令
   * WI-FAIL-01：重試上限/fail_packet/鎖定
   * WI-FAIL-02：MQ 卡死診斷與復原
   * WI-FAIL-03：Expected Source 防偽造閉環
附錄
* Appendix A：Issue Resolution Matrix
* Appendix B：Coverage Ledger（20+ 條抽核）
* Appendix C：Change Log（v1.0.0 → v1.1.0）
________________


索引與映射（必備，AI/LLM 強制力高）
Glossary（術語表）
術語
	別名
	定義位置
	說明
	GateKit
	gates, Gate Runner
	R2.4, WI-DEV-03
	機械閘門套件
	Evidence Bundle
	evidence, 證據包
	R3
	可回放證據集合
	Control Plane
	GitHub Actions, Ruleset, MQ
	R0.4
	控制平面（驗證/合流）
	Execution Plane
	Codespaces
	R0.4, WI-ENV-01
	執行平面（施工環境）
	Fail-Closed
	fail-closed, 預設阻斷
	R0.1(1), R6
	缺證據即 FAIL
	One-Writer
	one_writer, 單寫入者
	R0.1(3), R2.3
	同檔同時只允許一個 AI 寫
	Stopline
	stop_line, 停止線
	R0.1(8), R6
	重試上限觸發停手
	Dual-Judge
	雙法官
	R2.5, WI-DEV-04
	Judge A + Judge B 一致
	Merge Queue
	MQ, 合流佇列
	R2.6
	GitHub 序列化合流機制
	merge_group
	merge_group 事件
	R2.6, WI-CP-03
	MQ 觸發的 workflow 事件
	Vibe Lane
	vibe, 探索原型泳道
	R2.6
	不得進入 MQ
	Negative Test
	負向測試
	WI-DEV-04
	刻意破壞驗證 FAIL
	ID/Name Mapping（命名對照表，Canonical 優先）
規則：以 evidence/gate_report.json 的 id 為 Canonical（使用 underscore）。
類型
	Canonical ID
	Workflow Job Name
	備註
	Gate
	g0_input_seal
	g0-input-seal
	Runbook 敘述可用 hyphen，機械必對齊 Canonical
	Gate
	g3_schema
	g3-schema
	

	Gate
	g3_anti_platform
	g3-anti-platform
	

	Gate
	g4_dual_judge
	g4-dual-judge
	

	Gate
	format_check
	format-check
	

	Required Check
	docops-gatekit/finalize
	finalize
	唯一進入 Ruleset 的 check
	機械驗證：check_name_consistency.py 比對 RULESET_REQUIRED；gate_report.json 比對 Canonical ID。
[Ref: v0 Pack NORM-21][Ref: LBP ADR-003]
Evidence Path Canon（一句話釘死）
規則：本文件內所有 evidence 路徑皆以 repo root 為基準，必含 evidence/ 前綴（不得省略）。
* 正確：evidence/A_control_plane/settings_evidence.json
* 錯誤：A_control_plane/settings_evidence.json（禁止省略前綴）
Evidence Path Alias Map（A~F 六分類全覆蓋）
分類
	Canonical Path (v0.4.1)
	舊版 Alias
	說明
	A
	evidence/A_control_plane/repo_info.json
	-
	Repo 資訊
	A
	evidence/A_control_plane/settings_evidence.json
	evidence/control_plane/settings_evidence.json
	控制平面設定
	A
	evidence/A_control_plane/rulesets_detail.json
	-
	Ruleset 詳情
	A
	evidence/A_control_plane/workflow_runs.json
	-
	Workflow 執行記錄
	B
	evidence/B_execution_plane/input_manifest.json
	evidence/input_manifest.json
	輸入封印
	B
	evidence/B_execution_plane/run_manifest.json
	evidence/run_manifest.json
	運行清單
	B
	evidence/B_execution_plane/gate_report.json
	evidence/gates/fail_closed.json
	閘門報告（合併）
	B
	evidence/B_execution_plane/verdict.json
	evidence/verdict.json
	最終裁決
	C
	evidence/C_dual_judge/judge_a_verdict.json
	-
	Judge A 裁決
	C
	evidence/C_dual_judge/judge_b_verdict.json
	-
	Judge B 裁決
	C
	evidence/C_dual_judge/final_aggregate_verdict.json
	evidence/judges/final_aggregate_verdict.json
	聚合裁決
	D
	evidence/D_workflow/docops-gatekit.yml.evidence
	-
	Workflow 證據
	E
	evidence/E_rd01_phase0/rd01_profiles_evidence.json
	-
	Phase 0 Profile 設定
	E
	evidence/E_rd01_phase0/rd01_vibe_block_evidence.json
	-
	Vibe Block 測試
	E
	evidence/E_rd01_phase0/rd01_router_evidence.json
	-
	Lane Router 測試
	F
	evidence/F_rules_and_gates/*.py
	-
	Gate 腳本
	F
	evidence/F_rules_and_gates/*.yaml
	-
	規則定義
	[Ref: evidence_index.json][Ref: LBP Evidence Alias Map]
Upstream-to-Runbook Map（上游 → 章節錨點）
上游文件
	條款/章節
	本文件落點
	WI 編號
	SRS v1.1.0
	INV-001 (Fail-Closed)
	R0.1(1), R2.4, R6
	WI-FAIL-01
	SRS v1.1.0
	INV-002 (Input Seal)
	R2.1
	WI-DEV-01
	SRS v1.1.0
	INV-003 (ID Addressability)
	R1.2
	-
	SRS v1.1.0
	INV-004 (Trace Map)
	R3, R5
	-
	SRS v1.1.0
	INV-006 (One-Writer)
	R2.3
	WI-DEV-02
	SRS v1.1.0
	INV-007 (Negative Test)
	R2.5
	WI-DEV-04
	SRS v1.1.0
	INV-008 (Stopline)
	R2.4, R6
	WI-FAIL-01
	SRS v1.1.0
	INV-009 (Anti-Platform)
	R2.4
	WI-DEV-03
	SRS v1.1.0
	INV-010 (Dual-Judge)
	R2.5
	WI-DEV-04
	SRS v1.1.0
	EIR-001 (merge_group)
	R2.6
	WI-CP-03
	v0 Pack
	NORM-21 (Required Checks)
	R2.6
	WI-CP-01
	v0 Pack
	NORM-22 (MQ + merge_group)
	R2.6
	WI-CP-03
	v0 Pack
	NORM-23 (Vibe 限制)
	R2.6
	WI-DEV-05
	TVS v0.4.1
	§9 (驗收條件)
	R4
	-
	LBP v1.1.0
	Success Definition (6 Gates)
	R0.1(5), R2.7
	-
	架構指南
	§13.4.2 (Day-1 設定)
	R1.3
	WI-ENV-01
	________________


════════════════════════════════════════════════════════════════════════════════
[R U N B O O K]
主流程：從 Issue 到 Merge 的最小閉環
════════════════════════════════════════════════════════════════════════════════
________________


<a id="r0-總則"></a>
R0. 總則（原則/定位/邊界/職責/RACI）
R0.1 施工十大原則（不可違反）
#
	原則
	說明
	來源
	1
	Fail-Closed
	缺檔/缺欄位/缺 check/缺 evidence → 一律 FAIL
	[Ref: SRS INV-001]
	2
	Evidence-First
	先定 evidence 形狀與落點，再動手改檔
	[Ref: v0 Pack NORM-18]
	3
	One-Writer
	同檔同時只允許一個 AI 寫；並行要 worktree/分支隔離
	[Ref: SRS INV-006]
	4
	No Paid API
	只用訂閱工具（Claude Code/Codex）+ GitHub 原生能力
	[Ref: 架構指南 1.1]
	5
	Gate Set 固定
	v0 固定 6 gates（[Ref: LBP Success Definition]），不得新增
	[Ref: v0 Pack NORM-21]
	6
	Merge Queue=ON
	workflow 必須監聽 merge_group
	[Ref: TVS §7.3]
	7
	最小權限
	GITHUB_TOKEN/Secrets 最小化；expected source 鎖定
	[Ref: SRS NFR-SEC-001]
	8
	Stopline
	同類失敗重試 ≥3 次 → 輸出 fail_packet 並停手
	[Ref: SRS INV-008]
	9
	不自動解衝突
	AI 禁止自動解 Git conflict
	[Ref: 架構指南 3.1]
	10
	Doc Boundaries
	Runbook/WI 只寫「怎麼做」；Spec/Registry 才寫「是什麼」
	[Ref: 架構指南 §13.1]
	R0.2 文件定位
類型
	權威來源
	本文件角色
	Implementation SSOT
	本 RUNBOOK+WI
	施工手冊（僅描述操作）
	Normative SSOT
	SRS v1.1.0
	只引用，不改寫
	Mechanical SSOT
	Registry/v0 Pack
	只引用，不新增
	R0.3 邊界（禁止事項）
#
	禁止
	後果
	1
	新增規範性關鍵字（MUST/SHALL/REQUIRED）
	視為越權，須改為引用
	2
	新增 gate 名稱 / required check 名稱
	v0 gate set 固定，違反即 FAIL
	3
	平台化（把施工流程抽象成通用平台）
	違反 anti-platforming
	4
	改寫 Spec/Registry 定義
	只能引用，不得改寫
	R0.4 職責矩陣（RACI）
項目
	Claude Code
	Codex
	GitHub (Actions/Ruleset/MQ)
	Human Operator
	施工主寫（改檔）
	R
	C（提 patch skeleton）
	-
	A（Stopline/授權）
	機械 gate 執行
	R
	C（獨立驗證）
	R（required checks）
	A（只看 PASS/FAIL）
	雙法官審查
	Judge-A
	Judge-B
	C（驗 JSON）
	A（看聚合 verdict）
	合流
	-
	-
	R（Merge Queue）
	A（enable auto-merge）
	Evidence 產出
	R
	C（回放驗證）
	-
	A（稽核）
	目標：人工只做授權與例外處理，平常不做判斷題。
________________


<a id="r1-施工前置"></a>
R1. 施工前置：v0 施工準備
R1.1 環境確認
前提：
* Repo 為 Org-owned Public（MQ 免費使用前提）
* devcontainer 配置存在
* Ruleset 已設定 docops-gatekit/finalize 為 required check
執行：見 WI-ENV-01
R1.2 Issue 到 Task ID 映射
Task ID 命名規則：
場景
	格式
	範例
	一般施工任務
	TASK-{issue_number}
	TASK-42
	TVS 驗收任務
	tvs-YYYYMMDD-seq
	tvs-20260128-001
	需求原子 ID 規則（引用）：
[Ref: SRS INV-003] 所有需求原子（REQ/DEC/ASM）具唯一 ID，由 SRS 定義。
施工期間：只引用既有 ID，不得新增/修改需求原子 ID。
操作指引：
1. 從 Issue 獲取 issue_number
2. 建立 Task ID：TASK_ID="TASK-${issue_number}"
3. 建立 evidence 目錄：mkdir -p docops/evidence/${TASK_ID}
4. 若需引用需求原子，查閱 SRS 獲取已定義的 ID
5. Coverage Ledger 映射：INV-003 → 本節（R1.2）
R1.3 Day-1 設定確認
依 WI-ENV-01 與 WI-CP-01 完成環境與控制平面設定。
________________


<a id="r2-施工主流程"></a>
R2. 施工主流程（Phase-0 ~ Phase-5）
Phase-0: Input Seal → Phase-1: Plan Freeze → Phase-2: Implementation 
    → Phase-3: Local GateKit → Phase-4: Dual-Judge → Phase-5: PR & MQ


________________


<a id="r21-phase-0input-seal"></a>
R2.1 Phase-0：Input Seal
目的：封印輸入，確保來源可追溯。
步驟：
1. 識別所有 required sources（上游文件）
2. 計算每個輸入檔案的 SHA256
3. 產出 input_manifest.json
執行：見 WI-DEV-01
PASS 信號：
* input_manifest.json 存在
* 所有 SHA256 正確
* g0-input-seal PASS
[Ref: SRS INV-002]
________________


<a id="r22-phase-1plan-freeze"></a>
R2.2 Phase-1：Plan Freeze
目的：凍結變更計畫，限制 patch 範圍。
步驟：
1. 產出 patch skeleton（≤7 行/檔案）
2. Codex 審查 patch skeleton（確認無越權）
3. 固化 patch skeleton 到 evidence 或 PR 描述
執行：見 WI-DEV-01
PASS 信號：
* patch skeleton 存在
* 每檔案變更 ≤7 行
* Codex 審查無異議
[Ref: v0 Pack NORM-19]
________________


<a id="r23-phase-2implementation"></a>
R2.3 Phase-2：Implementation
目的：執行變更，遵守 One-Writer 原則。
One-Writer 規則：
* 同檔同時只允許一個 AI 寫入
* 並行需使用 worktree 或分支隔離
* 工具切換需記錄於 run_manifest
執行：見 WI-DEV-02
PASS 信號：
* run_manifest.tool_version 記錄主寫工具
* 無並行寫入同檔
[Ref: SRS INV-006][Ref: LBP ADR-001]
________________


<a id="r24-phase-3local-gatekit-預檢"></a>
R2.4 Phase-3：Local GateKit 預檢
目的：本地執行 Gate 驗證，減少 CI 失敗。
Gate 執行序列與 Stopline（v0 固定 6 gates [Ref: LBP Success Definition]）：
Gate (Canonical ID)
	Workflow Job
	重試上限
	FAIL 後行為
	g0_input_seal
	g0-input-seal
	3
	fail_packet + 停手
	g3_schema
	g3-schema
	3
	fail_packet + 停手
	g3_anti_platform
	g3-anti-platform
	3
	P0 FAIL + 停手
	g4_dual_judge
	g4-dual-judge
	3
	fail_packet + 停手
	format_check
	format-check
	3
	fail_packet + 停手
	(finalize)
	docops-gatekit/finalize
	-
	聚合結果
	執行：見 WI-DEV-03
fail_packet 範例（一致性強制）：
{
  "task_id": "TASK-XXX",
  "failed_gate": "g3_schema",
  "retry_count": 3,
  "last_error": "schema validation failed: missing field 'created_at'",
  "stopline_triggered": true,
  "generated_at": "2026-01-29T10:30:00Z"
}


[Ref: SRS INV-008][Ref: v0 Pack NORM-06]
________________


<a id="r25-phase-4dual-judge"></a>
R2.5 Phase-4：Dual-Judge
目的：雙法官裁決，防止單一 LLM 偏誤。
裁決規則：
* Judge A（Claude Code）+ Judge B（Codex）必須一致
* Swap Test：交換位置後結論不可翻轉
* 任一法官 FAIL → 聚合結果 FAIL
Negative Test 執行指引（[Ref: SRS INV-007]）：
定義：刻意破壞約束、邊界條件、或衝突場景，預期 FAIL/偵測。
執行方法：
1. 選取一個 gate 或驗證邏輯
2. 刻意修改輸入使其違反約束（如移除必要欄位、插入禁詞）
3. 執行 gate，確認結果為 FAIL
4. 恢復輸入，確認結果為 PASS
5. 記錄於 evidence：negative_test_type、expected_result、actual_result
執行：見 WI-DEV-04
Evidence 記錄欄位：
{
  "negative_tests": [
    {
      "test_id": "NT-001",
      "target_gate": "g3_anti_platform",
      "negative_test_type": "inject_forbidden_keyword",
      "expected_result": "FAIL",
      "actual_result": "FAIL",
      "notes": "Injected 'Unified Platform' keyword, gate correctly blocked"
    }
  ]
}


[Ref: SRS INV-010][Ref: v0 Pack NORM-12~17]
________________


<a id="r26-phase-5pr--merge-queue"></a>
R2.6 Phase-5：PR & Merge Queue
目的：建立 PR，進入 Merge Queue 自動合流。
PR 必備元素：
元素
	要求
	Title
	[{LANE}] {簡述} 或 [TASK-XXX] {簡述}
	Description
	evidence 指針與 patch skeleton
	Labels
	vibe 或 dev（依泳道）
	Workflow 必要條件：
on:
  pull_request:
    branches: [main]
  merge_group:          # ← 必須存在！
    branches: [main]


[Ref: TVS §7.3][Ref: v0 Pack NORM-22]
Required Checks SSOT（v0）：
類型
	Check Name
	說明
	RULESET_REQUIRED
	docops-gatekit/finalize
	唯一進入 Ruleset 的 check
	INTERNAL
	g0-input-seal
	workflow job name
	INTERNAL
	g3-schema
	workflow job name
	INTERNAL
	g3-anti-platform
	workflow job name
	INTERNAL
	g4-dual-judge
	workflow job name
	INTERNAL
	format-check
	workflow job name
	[Ref: v0 Pack NORM-21]
Vibe Lane 合流限制：
* 帶 [VIBE] 標記的 PR 不得進入 Merge Queue
* Lane 判定優先序：以 profile=... 旗標為準；標題只作輔助提示；缺 profile 視為 FAIL
* 偵測到 profile=vibe + merge_group → FAIL
[Ref: SRS FR-GV-004][Ref: v0 Pack NORM-23]
合流路徑：
PR 建立 → Required Checks 執行 → 全 PASS → 進入 Merge Queue
                                          ↓
                               merge_group 觸發重跑
                                          ↓
                               全 PASS → 自動合流


執行：見 WI-DEV-05
________________


<a id="r27-id-規約與命名一致性"></a>
R2.7 ID 規約與命名一致性
Canonical 規則：
類型
	Canonical 格式
	範例
	說明
	Gate ID
	underscore
	g0_input_seal
	以 gate_report.json 為準
	Workflow Job Name
	hyphen
	g0-input-seal
	允許不同，需有映射
	Required Check
	slash 分隔
	docops-gatekit/finalize
	Ruleset 唯一
	Evidence Path
	forward slash
	evidence/A_control_plane/...
	必含 evidence/ 前綴
	機械驗證：
* check_name_consistency.py 驗證 RULESET_REQUIRED
* gate_report.json 的 id 欄位為 Gate ID 的 Canonical
"6 Gates" 引用依據：
* 數量定義：[Ref: LBP Success Definition]
* 不得新增約束：[Ref: v0 Pack NORM-21]
________________


<a id="r3-evidence-與可回放"></a>
R3. Evidence 與可回放
路徑規約（強制）：本文件內所有 evidence 路徑皆以 repo root 為基準，必含 evidence/ 前綴（不得省略）。
R3.1 Evidence Bundle 結構（v0.4.1 對齊）
evidence/
├── A_control_plane/
│   ├── repo_info.json
│   ├── settings_evidence.json
│   ├── rulesets_detail.json
│   └── workflow_runs.json
├── B_execution_plane/
│   ├── input_manifest.json      ← MUST
│   ├── run_manifest.json        ← MUST
│   ├── gate_report.json         ← MUST
│   └── verdict.json             ← MUST
├── C_dual_judge/
│   ├── judge_a_verdict.json
│   ├── judge_b_verdict.json
│   └── final_aggregate_verdict.json
├── D_workflow/
│   └── docops-gatekit.yml.evidence
├── E_rd01_phase0/
│   ├── rd01_profiles_evidence.json
│   ├── rd01_vibe_block_evidence.json
│   └── rd01_router_evidence.json
└── F_rules_and_gates/
    └── *.py, *.yaml


[Ref: evidence_index.json][Ref: TVS §8]
R3.2 必備 Evidence 清單
Evidence
	路徑
	必要性
	說明
	Input Manifest
	evidence/B_execution_plane/input_manifest.json
	MUST
	輸入封印
	Run Manifest
	evidence/B_execution_plane/run_manifest.json
	MUST
	運行清單
	Gate Report
	evidence/B_execution_plane/gate_report.json
	MUST
	閘門報告
	Verdict
	evidence/B_execution_plane/verdict.json
	MUST
	最終裁決
	Settings Evidence
	evidence/A_control_plane/settings_evidence.json
	MUST
	控制平面設定
	Dual Judge (if Dev)
	evidence/C_dual_judge/*.json
	CONDITIONAL
	雙法官裁決
	[Ref: SRS §9][Ref: v0 Pack NORM-18~20]
R3.3 SHA256 / Manifest 規範
項目
	規範
	Hash 格式
	sha256:{64-char-hex-digest}
	檔案完整性
	所有 MUST 檔案缺失即 FAIL
	時間戳記
	ISO8601 格式，單調遞增
	R3.4 Evidence Path Alias Map（完整 A~F 分類）
見 索引與映射 > Evidence Path Alias Map
________________


<a id="r4-驗收清單"></a>
R4. 驗收清單（Acceptance Checklist）
R4.1 控制平面驗收（A 級）
#
	項目
	驗證方式
	PASS 條件
	Evidence
	A1
	Repo Org-owned Public
	gh api
	owner.type = "Organization"
	evidence/A_control_plane/repo_info.json
	A2
	Ruleset 存在
	Ruleset API
	回傳非空陣列
	evidence/A_control_plane/settings_evidence.json
	A3
	Required Check 含 finalize
	Ruleset API
	docops-gatekit/finalize 存在
	evidence/A_control_plane/settings_evidence.json
	A4
	Merge Queue 啟用
	Ruleset API
	merge_queue.enabled = true
	evidence/A_control_plane/settings_evidence.json
	A5
	Workflow 含 merge_group
	grep
	merge_group 存在
	evidence/D_workflow/*.evidence
	[Ref: TVS §9.1.1][Ref: tvs_section9_verdict.json]
R4.2 執行平面驗收（B 級）
#
	項目
	驗證方式
	PASS 條件
	Evidence
	B1
	Gate Report 全 PASS
	Schema 驗證
	所有 gate status=PASS
	evidence/B_execution_plane/gate_report.json
	B2
	Verdict PASS
	verdict.json
	status = "PASS"
	evidence/B_execution_plane/verdict.json
	B3
	Manual Attestations
	SHA256
	所有 attestation 有 hash
	evidence/A_control_plane/settings_evidence.json
	R4.3 RD01 驗收（Phase 0 專屬）
#
	項目
	驗證方式
	PASS 條件
	Evidence
	RD01-1
	Profiles Phase 0 Config
	JSON 檢查
	vibe=true, dev=true, spec=false, ops=false
	evidence/E_rd01_phase0/rd01_profiles_evidence.json
	RD01-2
	Vibe Lane Merge Block
	測試案例
	2/2 passed
	evidence/E_rd01_phase0/rd01_vibe_block_evidence.json
	RD01-3
	Lane Router
	測試案例
	5/5 passed
	evidence/E_rd01_phase0/rd01_router_evidence.json
	[Ref: tvs_section9_verdict.json]
R4.4 驗收結果對齊（tvs_section9_verdict）
Check
	Status
	說明
	A1~A5
	PASS
	控制平面全通過
	B: Manual attestations
	PASS
	All 3 attestations have SHA256
	Gate Report (v2)
	PASS
	All 6 gates PASS
	Verdict
	PASS
	judges: [(judge_a, PASS), (judge_b, PASS)]
	RD01-1~3
	PASS
	Phase 0 全通過
	Final Verdict
	PASS
	11/11 passed
	[Ref: tvs_section9_verdict.json]
________________


<a id="r5-覆蓋台帳"></a>
R5. 覆蓋台帳（Coverage Ledger）
R5.1 上游硬約束 → Runbook/WI 落點映射
#
	上游來源
	硬約束/需求
	Runbook 章節
	WI 編號
	驗證信號
	Evidence 落點
	FAIL 行為
	1
	SRS INV-001
	Fail-Closed
	R0.1(1), R2.4
	WI-FAIL-01
	gate.fail_closed
	evidence/B_execution_plane/gate_report.json
	立即 FAIL
	2
	SRS INV-002
	Input Seal SHA256
	R2.1
	WI-DEV-01
	g0-input-seal
	evidence/B_execution_plane/input_manifest.json
	立即 FAIL
	3
	SRS INV-003
	ID Addressability
	R1.2
	-
	只引用不新增 ID
	無獨立 evidence（靠 SRS 定義）
	N/A
	4
	SRS INV-004
	Trace Map
	R3, R5
	-
	source pointer 存在
	evidence/E_rd01_phase0/rd01_router_evidence.json
	立即 FAIL
	5
	SRS INV-005
	Evidence Replay
	R3
	-
	gate.evidence_replay
	evidence/B_execution_plane/verdict.json
	立即 FAIL
	6
	SRS INV-006
	One-Writer
	R2.3
	WI-DEV-02
	concurrent_writers ≤1
	evidence/B_execution_plane/run_manifest.json
	立即 FAIL
	7
	SRS INV-007
	Negative Test
	R2.5
	WI-DEV-04
	negative_test_type 存在
	evidence/C_dual_judge/judge_b_verdict.json
	立即 FAIL
	8
	SRS INV-008
	Tool Budget/Stopline
	R2.4, R6
	WI-FAIL-01
	retry_count < 3
	evidence/B_execution_plane/run_manifest.json
	觸發 Stopline
	9
	SRS INV-009
	Anti-Platforming
	R2.4
	WI-DEV-03
	g3-anti-platform
	evidence/B_execution_plane/gate_report.json
	P0 FAIL
	10
	SRS INV-010
	Dual-Judge Agreement
	R2.5
	WI-DEV-04
	g4-dual-judge
	evidence/C_dual_judge/final_aggregate_verdict.json
	立即 FAIL
	11
	SRS EIR-001
	merge_group 事件
	R2.6
	WI-CP-03
	merge_group trigger
	evidence/D_workflow/*.evidence
	MQ 卡死
	12
	v0 Pack NORM-21
	Required Checks SSOT
	R2.6, R2.7
	WI-CP-01
	finalize 存在
	evidence/A_control_plane/settings_evidence.json
	立即 FAIL
	13
	v0 Pack NORM-22
	MQ + merge_group
	R2.6
	WI-CP-03
	workflow 含 merge_group
	evidence/D_workflow/*.evidence
	MQ 卡死
	14
	v0 Pack NORM-23
	Vibe Lane 合流限制
	R2.6
	WI-DEV-05
	vibe_merge_block
	evidence/E_rd01_phase0/rd01_vibe_block_evidence.json
	立即 FAIL
	15
	TVS §9
	驗收條件 A1~RD01-3
	R4
	-
	tvs_section9_verdict
	tvs_section9_verdict.json
	立即 FAIL
	16
	LBP ADR-001
	Claude Code 主寫
	R2.3
	WI-DEV-02
	run_manifest.tool_version
	evidence/B_execution_plane/run_manifest.json
	記錄
	17
	架構指南 §13.4.2
	Day-1 設定
	R1.3
	WI-ENV-01
	Codespace 建立成功
	evidence/A_control_plane/settings_evidence.json
	阻斷
	18
	LBP Success Def
	6 Gates 固定
	R0.1(5), R2.7
	-
	無新增 gate
	evidence/B_execution_plane/gate_report.json
	違反即 FAIL
	R5.2 SRS Invariants 覆蓋對照
INV-ID
	名稱
	Runbook 落點
	WI 落點
	狀態
	INV-001
	Fail-Closed
	R0.1(1), R2.4
	WI-FAIL-01
	✓ COVERED
	INV-002
	Input Seal
	R2.1
	WI-DEV-01
	✓ COVERED
	INV-003
	ID Addressability
	R1.2
	-
	✓ COVERED
	INV-004
	Trace Map
	R3, R5
	-
	✓ COVERED
	INV-005
	Evidence Replay
	R3
	-
	✓ COVERED
	INV-006
	One-Writer
	R2.3
	WI-DEV-02
	✓ COVERED
	INV-007
	Verifier Report
	R2.5
	WI-DEV-04
	✓ COVERED
	INV-008
	Tool Budget
	R2.4, R6
	WI-FAIL-01
	✓ COVERED
	INV-009
	Anti-Platforming
	R2.4
	WI-DEV-03
	✓ COVERED
	INV-010
	Dual-Judge
	R2.5
	WI-DEV-04
	✓ COVERED
	Coverage Rate: 100% (10/10 INV)
________________


<a id="r6-failure-handling"></a>
R6. Failure Handling（失敗處理）
R6.1 Stopline 觸發條件
條件
	閾值
	行為
	同類 Gate 重試
	≥3 次
	輸出 fail_packet + 停手
	Dual-Judge 分歧
	任一法官 FAIL
	立即 FAIL
	MQ 卡死
	Expected 狀態 >30 分鐘
	診斷 + 修復（見 WI-FAIL-02）
	R6.2 fail_packet Schema
{
  "task_id": "string (required)",
  "failed_gate": "string (required)",
  "retry_count": "integer (required)",
  "last_error": "string (required)",
  "stopline_triggered": "boolean (required)",
  "generated_at": "ISO8601 (required)"
}


R6.3 人類介入時機
1. Stopline 觸發（連續失敗 ≥3 次）
2. 權限授權（Ruleset 變更）
3. 例外處置（fail_packet 產出後）
4. MQ 長時間卡死
執行：見 WI-FAIL-01、WI-FAIL-02
________________


<a id="r7-變更控制"></a>
R7. 變更控制（Change Control）
R7.1 變更原則
原則
	說明
	Runbook 不得改寫 Spec/Registry
	若需要規範變更，走 SRS 升級流程
	Gate 擴充需版本升級 + ADR
	v0 gate set 固定；新 gate 需 v1+ 並記錄 ADR
	變更需有 Evidence 足跡
	任何施工變更需產出 evidence
	R7.2 版本升級路徑
v0 (Vibe + Dev) → v1 (+ Spec Lane) → v2 (+ Ops Lane)
                         ↑
                 需要 ADR + SRS 修訂


R7.3 ADR 觸發條件
條件
	是否需要 ADR
	新增 Gate 類別
	YES
	新增 Required Check
	YES
	變更 Evidence 結構
	YES
	修改 Runbook 流程
	NO（但需 changelog）
	修復錯字
	NO
	________________


════════════════════════════════════════════════════════════════════════════════
[W O R K I N S T R U C T I O N S]
WI：可照做的操作說明
════════════════════════════════════════════════════════════════════════════════
________________


<a id="wi-env-環境指令"></a>
WI-ENV：環境指令
________________


<a id="wi-env-01"></a>
WI-ENV-01：建立/重建 Codespace（含 prebuild）
項目
	內容
	Purpose
	確保每次施工都在可重現沙盒，且不靠本機算力
	Scope
	v0 施工環境建立
	Preconditions
	Repo 為 Org-owned Public；devcontainer 配置存在
	Responsible
	R: Human Operator / A: -
	Steps：
#
	動作
	命令/操作
	預期結果
	1
	進入 Repo
	GitHub UI 或 gh repo view
	顯示 repo 資訊
	2
	點擊 Code → Codespaces → Create
	GitHub UI
	Codespace 建立中
	3
	等待 devcontainer 建置
	自動
	終端機可用
	4
	驗證工具鏈
	python --version && gh --version
	版本顯示
	5
	確認 git 狀態
	git status
	clean working tree
	Outputs：
* Codespace 實例 ID
* 記錄於 run_manifest.json 的 runner.env
PASS Signals：
* devcontainer 建置成功
* 工具鏈版本可顯示
* git status clean
FAIL / Stopline：
* devcontainer 建置失敗 → 檢查 .devcontainer/devcontainer.json
* 工具鏈缺失 → 重建 Codespace
Evidence：
* evidence/B_execution_plane/run_manifest.json（runner.env 欄位）
References：
* [Ref: README §5 Quickstart]
* [Ref: TVS §4.4]
* Ref: GitHub Docs: Codespaces
________________


<a id="wi-env-02"></a>
WI-ENV-02：Secrets/權限收斂（Codespaces Security Baseline）
項目
	內容
	Purpose
	確保 Codespaces 環境安全基線
	Scope
	Secrets 管理、權限最小化
	Preconditions
	Codespace 已建立
	Responsible
	R: Human Operator / A: Repo Admin
	Steps：
#
	動作
	說明
	預期結果
	1
	確認 Codespaces secrets 設定
	Settings → Secrets and variables → Codespaces
	僅必要 secrets
	2
	禁止硬編碼敏感資訊
	程式碼審查
	無 hardcode
	3
	Settings Sync 僅允許信任清單
	手動確認
	已收斂
	4
	Extensions 僅允許信任清單
	手動確認
	已收斂
	5
	記錄信任清單到 evidence
	填寫 settings_evidence
	JSON 欄位完整
	Evidence 記錄格式：
{
  "trust": {
    "allowlist_extensions": ["ms-python.python", "GitHub.copilot"],
    "allowlist_settings_sync": ["editor.fontSize", "editor.tabSize"],
    "collected_at": "2026-01-29T10:00:00Z",
    "collected_by": "@username"
  }
}


Outputs：
* evidence/A_control_plane/settings_evidence.json 含 trust 欄位
PASS Signals：
* secrets 僅含必要項目
* 無 hardcode 敏感資訊
* trust 欄位非空（或明示空=PASS）
FAIL / Stopline：
* 發現硬編碼 secrets → 立即移除
* 未記錄信任清單 → 補記錄
Evidence：
* evidence/A_control_plane/settings_evidence.json
References：
* [Ref: SRS NFR-SEC-001]
* Ref: GitHub Docs: Codespaces secrets
________________


<a id="wi-env-03"></a>
WI-ENV-03：Codespaces 成本與停用策略
項目
	內容
	Purpose
	控制 Codespaces 成本，避免帳單爆炸
	Scope
	Stop/Idle timeout/Delete/Storage
	Preconditions
	有 Codespaces 使用權限
	Responsible
	R: Human Operator / A: Billing Manager
	Steps：
#
	動作
	命令/操作
	預期結果
	1
	設定 Idle Timeout
	Settings → Codespaces → Default idle timeout
	建議：30 分鐘（預設）或 15 分鐘（積極節省）
	2
	設定 Retention Period
	Settings → Codespaces → Default retention period
	建議：7-14 天
	3
	選擇適當 Machine Type
	建立時選擇
	建議：2-core（足夠大多數工作）
	4
	施工完成後停止 Codespace
	gh codespace stop 或 UI
	Codespace 狀態=Stopped
	5
	不再使用時刪除 Codespace
	gh codespace delete 或 UI
	Codespace 已刪除
	6
	記錄成本策略到 evidence
	截圖或 JSON
	可回放
	CLI 命令範例：
# 列出所有 Codespaces
gh codespace list


# 停止 Codespace
gh codespace stop -c <codespace-name>


# 刪除 Codespace
gh codespace delete -c <codespace-name>


# 查看 Codespace 狀態
gh codespace view -c <codespace-name>


Evidence 記錄格式（擇一）：
選項 A：JSON 封包
{
  "codespaces_cost_policy": {
    "idle_timeout_minutes": 30,
    "retention_period_days": 14,
    "default_machine_type": "2-core",
    "policy_adopted_at": "2026-01-29T10:00:00Z",
    "adopted_by": "@username"
  }
}


選項 B：截圖 + hash
{
  "codespaces_cost_policy": {
    "screenshot_path": "evidence/A_control_plane/codespaces_settings.png",
    "screenshot_sha256": "abc123...",
    "captured_at": "2026-01-29T10:00:00Z"
  }
}


Outputs：
* 成本策略配置完成
* evidence/A_control_plane/settings_evidence.json 含 codespaces_cost_policy 欄位
PASS Signals：
* idle timeout ≤30 分鐘
* retention period ≤14 天
* evidence 記錄完整
FAIL / Stopline：
* idle timeout 未設定 → 設定
* Codespace 長期未使用未刪除 → 刪除
Evidence：
* evidence/A_control_plane/settings_evidence.json
References：
* Ref: GitHub Docs: Managing the cost of GitHub Codespaces
* Ref: GitHub Docs: Configuring automatic deletion of your codespaces
【OPT】可選強化：
* 組織層級可設定 Maximum idle timeout constraint
* 組織層級可設定 Retention period constraint
* 定期審查 Codespaces 使用報告
________________


<a id="wi-cp-控制平面指令"></a>
WI-CP：控制平面指令
________________


<a id="wi-cp-01"></a>
WI-CP-01：Ruleset 變更與 settings_evidence 封包
項目
	內容
	Purpose
	確保 Ruleset 配置正確並留下可回放證據
	Scope
	Ruleset 設定、Required Check 配置
	Preconditions
	Repo Admin 權限
	Responsible
	R: Repo Admin / A: Human Operator
	Steps：
#
	動作
	命令/操作
	預期結果
	1
	進入 Ruleset 設定
	Settings → Rules → Rulesets
	顯示現有 rulesets
	2
	確認/建立主幹保護規則
	見下方配置
	Ruleset 存在
	3
	確認 Required Check
	docops-gatekit/finalize
	Check 已加入
	4
	確認 Expected Source
	GitHub Actions
	防偽造設定完成
	5
	確認 Merge Queue 啟用
	merge_queue.enabled = true
	MQ 已啟用
	6
	產出 settings_evidence
	執行收集腳本或手動
	JSON 檔案產出
	Ruleset 設定範本：
Ruleset 設定:
  - Name: main-protection
  - Target: main branch
  - Require merge queue: ✓
  - Require status checks to pass: ✓
  - Required Check: docops-gatekit/finalize
  - Expected source: GitHub Actions    # ← 防偽造
  - Block force pushes: ✓


settings_evidence Schema：
{
  "collected_at": "2026-01-29T10:00:00Z",
  "collector": "@username",
  "ruleset": {
    "name": "main-protection",
    "required_checks": ["docops-gatekit/finalize"],
    "expected_source": "GitHub Actions",
    "merge_queue_enabled": true,
    "enforcement": "active"
  },
  "fork_approval": {
    "setting": "Require approval for all external contributors",
    "screenshot_sha256": "abc123..."
  },
  "token_permissions": {
    "default": "read",
    "screenshot_sha256": "def456..."
  }
}


Outputs：
* evidence/A_control_plane/settings_evidence.json
* evidence/A_control_plane/rulesets_detail.json
PASS Signals：
* Ruleset 存在且 enforcement=active
* Required check 含 docops-gatekit/finalize
* Merge Queue 已啟用
* Expected source 已設定
FAIL / Stopline：
* Ruleset 不存在 → 建立
* Required check 缺失 → 新增
* Expected source 未設定 → 設定（見 WI-FAIL-03）
Evidence：
* evidence/A_control_plane/settings_evidence.json
* evidence/A_control_plane/rulesets_detail.json
References：
* [Ref: v0 Pack NORM-21]
* [Ref: SRS EIR-002]
________________


<a id="wi-cp-02"></a>
WI-CP-02：Workflow permissions 最小化
項目
	內容
	Purpose
	確保 GITHUB_TOKEN 權限最小化
	Scope
	Workflow permissions 配置
	Preconditions
	Workflow 檔案存在
	Responsible
	R: Developer / A: Repo Admin
	Steps：
#
	動作
	命令/操作
	預期結果
	1
	打開 workflow 檔案
	.github/workflows/docops-gatekit.yml
	檔案可編輯
	2
	設定頂層 permissions
	見下方範例
	permissions block 存在
	3
	驗證權限最小化
	檢查 scope
	僅必要權限
	4
	提交變更
	git commit
	變更已提交
	Permissions YAML 範例（可直接複製貼上）：
name: docops-gatekit


on:
  pull_request:
    branches: [main]
  merge_group:
    branches: [main]


# ===== 最小權限設定（強制） =====
permissions:
  contents: read        # 讀取 repo 內容
  statuses: write       # 回報 status check（若需要）
  # 不需要的權限保持預設 none


jobs:
  finalize:
    name: docops-gatekit/finalize
    runs-on: ubuntu-latest
    steps:
      # ... 步驟 ...


權限說明：
權限
	設定
	說明
	contents
	read
	讀取 repo 內容（必要）
	statuses
	write
	回報 status check（必要時）
	pull-requests
	read
	讀取 PR 資訊（若需要）
	其他
	none
	預設不授權
	與現有 workflow 相容性：
* 若 workflow 需要寫入 contents（如自動 commit），需提升為 contents: write
* 若使用第三方 action，需確認其所需權限並最小化授權
Outputs：
* workflow 檔案已更新
* evidence/D_workflow/docops-gatekit.yml.evidence
PASS Signals：
* permissions block 存在
* 僅必要權限被授予
* workflow 執行成功
FAIL / Stopline：
* permissions block 缺失 → 新增
* 權限過大 → 收斂
* workflow 因權限不足失敗 → 最小化提升必要權限
Evidence：
* evidence/D_workflow/docops-gatekit.yml.evidence
References：
* [Ref: SRS NFR-SEC-001]
* [Ref: v0 Pack NORM-24]
* Ref: GitHub Docs: Automatic token authentication
【OPT】可選強化：
* 組織層級設定 Default permissions 為 read-only
* 使用 permissions: {} 強制每個 job 明確指定權限
* Pin 第三方 actions 到 commit SHA
________________


<a id="wi-cp-03"></a>
WI-CP-03：MQ + merge_group 合規自檢
項目
	內容
	Purpose
	確保 Merge Queue 啟用且 workflow 監聽 merge_group
	Scope
	MQ 配置、workflow trigger
	Preconditions
	Ruleset 已配置
	Responsible
	R: Developer / A: Repo Admin
	Steps：
#
	動作
	命令
	預期結果
	1
	檢查 MQ 啟用
	gh api /repos/{o}/{r}/rulesets
	merge_queue.enabled = true
	2
	檢查 workflow trigger
	grep -r "merge_group" .github/workflows/
	命中
	3
	驗證 trigger 格式
	檢查 YAML
	見下方範例
	正確的 workflow trigger：
on:
  pull_request:
    branches: [main]
  merge_group:          # ← 必須存在
    branches: [main]


自檢命令：
# 檢查 workflow 是否包含 merge_group
grep -l "merge_group" .github/workflows/*.yml


# 若無結果，需要修復 workflow


Outputs：
* evidence/D_workflow/docops-gatekit.yml.evidence
PASS Signals：
* merge_group 關鍵字存在
* MQ 已啟用
FAIL / Stopline：
* merge_group 缺失 → MQ 會卡死，立即修復
* MQ 未啟用 → 啟用
Evidence：
* evidence/D_workflow/docops-gatekit.yml.evidence
* evidence/A_control_plane/settings_evidence.json
References：
* [Ref: v0 Pack NORM-22]
* [Ref: TVS §7.3]
* Ref: GitHub Docs: Managing a merge queue
________________


<a id="wi-dev-v0-施工主線指令"></a>
WI-DEV：v0 施工主線指令
________________


<a id="wi-dev-01"></a>
WI-DEV-01：Input Seal & Plan Freeze（patch skeleton 流程）
項目
	內容
	Purpose
	封印輸入並凍結變更計畫
	Scope
	Phase-0 + Phase-1
	Preconditions
	Issue 已建立；Codespace 可用
	Responsible
	R: Claude Code / C: Codex / A: Human
	Steps：
#
	動作
	命令/操作
	預期結果
	1
	建立 Task ID
	TASK_ID="TASK-{issue_number}"
	Task ID 設定
	2
	建立 evidence 目錄
	mkdir -p docops/evidence/${TASK_ID}
	目錄存在
	3
	產生 input_manifest
	見下方 Python
	JSON 檔案產出
	4
	產生 run_manifest
	見下方 Python
	JSON 檔案產出
	5
	產出 patch skeleton
	Claude Code 產出
	≤7 行/檔案
	6
	Codex 審查 patch skeleton
	Codex 執行
	無越權
	7
	固化 patch skeleton
	存入 evidence 或 PR 描述
	可回放
	input_manifest 產生範例：
import hashlib
import json
from datetime import datetime, timezone


def generate_input_manifest(task_id, input_files):
    manifest = {
        "task_id": task_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "inputs": []
    }
    for f in input_files:
        with open(f, 'rb') as fp:
            sha = hashlib.sha256(fp.read()).hexdigest()
        manifest["inputs"].append({
            "name": f.split('/')[-1],
            "path": f,
            "sha256": sha
        })
    return manifest


run_manifest Schema（含 retry_count）：
{
  "task_id": "TASK-XXX",
  "runner": {
    "env": "codespaces",
    "python": "Python 3.11.x"
  },
  "git": {
    "branch": "fix/TASK-XXX",
    "commit": "abc123..."
  },
  "tool_version": "claude-code-1.0.x",
  "retry_count": 0,
  "failed_gate": null,
  "created_at": "ISO8601"
}


Outputs：
* evidence/B_execution_plane/input_manifest.json
* evidence/B_execution_plane/run_manifest.json
* patch_skeleton.md（或 PR 描述）
PASS Signals：
* input_manifest 含所有 required sources
* SHA256 正確
* patch skeleton ≤7 行/檔案
FAIL / Stopline：
* required source 缺失 → 阻斷
* SHA256 不符 → 阻斷
* patch skeleton 越權 → 阻斷
Evidence：
* evidence/B_execution_plane/input_manifest.json
* evidence/B_execution_plane/run_manifest.json
References：
* [Ref: SRS INV-002]
* [Ref: v0 Pack NORM-19]
* [Ref: v0 Pack Runbook §2.1, §2.2]
________________


<a id="wi-dev-02"></a>
WI-DEV-02：One-Writer 實作與 worktree 並行守則
項目
	內容
	Purpose
	確保同檔同時只有一個寫入者
	Scope
	Phase-2 Implementation
	Preconditions
	Plan Freeze 完成
	Responsible
	R: Claude Code / C: Codex / A: Human
	Steps：
#
	動作
	命令/操作
	預期結果
	1
	建立工作分支
	git checkout -b fix/${TASK_ID}
	分支存在
	2
	確認主寫工具
	Claude Code
	記錄於 run_manifest
	3
	執行變更
	依 patch skeleton
	檔案更新
	4
	驗證 git status
	git status
	預期變更
	5
	提交變更
	git commit -m "..."
	commit 成功
	並行場景處理（含 worktree 命令範例）：
場景
	處理方式
	命令
	不同檔案需並行
	使用 git worktree
	見下方命令
	同一檔案需協作
	序列化：先 A 完成並 commit，再 B 接手
	N/A
	主寫工具不可用
	切換 Codex 為備援，記錄於 run_manifest
	N/A
	git worktree 命令範例：
# 建立 worktree（在不同目錄處理不同分支）
git worktree add ../worktree-feature-b feature-b


# 列出所有 worktree
git worktree list


# 進入 worktree 工作
cd ../worktree-feature-b
# ... 在此處進行 feature-b 的工作 ...


# 完成後移除 worktree
git worktree remove ../worktree-feature-b


# 或強制移除（若有未提交變更）
git worktree remove --force ../worktree-feature-b


worktree 並行策略：
main
├── worktree-a/  ← Claude Code 處理 feature-a
│   └── (獨立工作樹)
├── worktree-b/  ← Codex 處理 feature-b（不同檔案）
│   └── (獨立工作樹)
└── 原始目錄/    ← 主要工作區


Outputs：
* 更新後的檔案
* git commit
* evidence/B_execution_plane/run_manifest.json（tool_version 欄位）
PASS Signals：
* 同時只有一個寫入者
* run_manifest 記錄 tool_version
FAIL / Stopline：
* 偵測到並行寫入同檔 → 阻斷
* 工具切換未記錄 → 補記錄
Evidence：
* evidence/B_execution_plane/run_manifest.json
References：
* [Ref: SRS INV-006]
* [Ref: LBP ADR-001]
________________


<a id="wi-dev-03"></a>
WI-DEV-03：Local GateKit 預檢 + Stopline
項目
	內容
	Purpose
	本地執行 Gate 驗證，減少 CI 失敗
	Scope
	Phase-3 Local GateKit
	Preconditions
	Implementation 完成
	Responsible
	R: Claude Code / C: Codex / A: Human
	Steps：
#
	動作
	命令
	預期結果
	1
	執行 g0-input-seal
	python docops/registry/gates/gatekit_runner_v0.py g0
	PASS
	2
	執行 g3-schema
	python docops/registry/gates/gatekit_runner_v0.py g3-schema
	PASS
	3
	執行 g3-anti-platform
	python docops/registry/gates/gatekit_runner_v0.py g3-anti-platform
	PASS
	4
	執行 format-check
	git status --porcelain
	空輸出（clean）
	5
	記錄 gate_report
	產出 JSON
	存入 evidence
	Gate 執行序列與 Stopline：
Gate (Canonical)
	重試上限
	FAIL 後行為
	g0_input_seal
	3
	fail_packet + 停手
	g3_schema
	3
	fail_packet + 停手
	g3_anti_platform
	0
	P0 FAIL + 立即停手
	format_check
	3
	fail_packet + 停手
	Stopline 觸發邏輯：
# 偽代碼
retry_count = run_manifest.get("retry_count", 0)
if gate_result == "FAIL":
    retry_count += 1
    run_manifest["retry_count"] = retry_count
    run_manifest["failed_gate"] = gate_id
    
    if retry_count >= 3:
        emit_fail_packet(task_id, gate_id, retry_count, error_msg)
        halt_execution()


Outputs：
* evidence/B_execution_plane/gate_report.json
* 若觸發 Stopline：fail_packet.json
PASS Signals：
* 所有 gate PASS
* gate_report.json 存在
FAIL / Stopline：
* 任一 gate FAIL → 重試或 fail_packet
* retry_count ≥3 → 停手，輸出 fail_packet
Evidence：
* evidence/B_execution_plane/gate_report.json
* evidence/B_execution_plane/run_manifest.json（retry_count 欄位）
References：
* [Ref: SRS INV-008]
* [Ref: v0 Pack NORM-06~11]
________________


<a id="wi-dev-04"></a>
WI-DEV-04：Dual-Judge 與 Negative Test
項目
	內容
	Purpose
	雙法官裁決 + 負向測試驗證
	Scope
	Phase-4 Dual-Judge
	Preconditions
	Local GateKit 全 PASS
	Responsible
	R: Claude Code (Judge-A) / R: Codex (Judge-B) / A: Human
	Steps：
#
	動作
	執行者
	預期結果
	1
	Judge A 審查
	Claude Code
	judge_a_verdict.json
	2
	Judge B 審查
	Codex
	judge_b_verdict.json
	3
	執行 Swap Test
	交換位置重審
	結論不翻轉
	4
	執行 Negative Test
	見下方
	預期 FAIL 確實 FAIL
	5
	聚合裁決
	judge_aggregate.py
	final_aggregate_verdict.json
	Negative Test 執行方法（[Ref: SRS INV-007]）：
#
	動作
	說明
	預期結果
	1
	選取目標 gate
	例如 g3_anti_platform
	-
	2
	刻意破壞輸入
	插入禁詞如 "Unified Platform"
	輸入已破壞
	3
	執行 gate
	python gatekit_runner_v0.py g3-anti-platform
	FAIL
	4
	確認 FAIL
	檢查 gate 輸出
	status=FAIL
	5
	恢復輸入
	移除禁詞
	輸入已恢復
	6
	重新執行 gate
	python gatekit_runner_v0.py g3-anti-platform
	PASS
	7
	記錄結果
	填寫 negative_tests 欄位
	evidence 完整
	Negative Test Evidence 格式：
{
  "negative_tests": [
    {
      "test_id": "NT-001",
      "target_gate": "g3_anti_platform",
      "negative_test_type": "inject_forbidden_keyword",
      "input_modification": "Added 'Unified Platform' to test file",
      "expected_result": "FAIL",
      "actual_result": "FAIL",
      "restored_result": "PASS",
      "executed_at": "2026-01-29T10:30:00Z",
      "executor": "judge_b_codex"
    }
  ]
}


final_aggregate_verdict Schema：
{
  "task_id": "TASK-XXX",
  "aggregator": "judge_aggregate.py (deterministic)",
  "judge_a": {
    "id": "judge_a_claude",
    "verdict": "PASS",
    "timestamp": "ISO8601"
  },
  "judge_b": {
    "id": "judge_b_codex",
    "verdict": "PASS",
    "timestamp": "ISO8601"
  },
  "swap_test_passed": true,
  "negative_tests_passed": true,
  "final_verdict": "PASS",
  "aggregated_at": "ISO8601"
}


Outputs：
* evidence/C_dual_judge/judge_a_verdict.json
* evidence/C_dual_judge/judge_b_verdict.json
* evidence/C_dual_judge/final_aggregate_verdict.json
PASS Signals：
* Judge A == Judge B == PASS
* swap_test_passed == true
* negative_tests_passed == true
FAIL / Stopline：
* 任一法官 FAIL → 聚合 FAIL
* Swap Test 翻轉 → 聚合 FAIL
* Negative Test 未執行預期 FAIL → 需調查
Evidence：
* evidence/C_dual_judge/*.json
References：
* [Ref: SRS INV-007]
* [Ref: SRS INV-010]
* [Ref: v0 Pack NORM-12~17]
________________


<a id="wi-dev-05"></a>
WI-DEV-05：PR → MQ 合流
項目
	內容
	Purpose
	建立 PR 並進入 Merge Queue
	Scope
	Phase-5 PR & Merge Queue
	Preconditions
	Dual-Judge PASS
	Responsible
	R: Developer / A: Repo Admin
	Steps：
#
	動作
	命令/操作
	預期結果
	1
	推送分支
	git push origin fix/${TASK_ID}
	分支已推送
	2
	建立 PR
	gh pr create --title "[DEV] TASK-XXX" --body "..."
	PR 已建立
	3
	設定 Label
	gh pr edit --add-label "dev"
	Label 已設定
	4
	等待 Required Checks
	GitHub UI
	全 PASS
	5
	加入 Merge Queue
	gh pr merge --merge-queue 或 UI
	進入 MQ
	6
	等待 merge_group 執行
	自動
	Workflow 執行
	7
	自動合流
	GitHub MQ
	合流完成
	PR Title 格式：
Lane
	格式
	範例
	Dev
	[DEV] {簡述}
	[DEV] Fix schema validation
	Vibe
	[VIBE] {簡述}
	[VIBE] Prototype new feature
	Vibe Lane 合流阻斷：
IF profile == "vibe" AND event == "merge_group":
    FAIL("Vibe Lane PR cannot enter Merge Queue")


Lane 判定優先序：
1. 以 profile=... 旗標為準（從 profiles/*.yaml 讀取）
2. 標題 [VIBE]/[DEV] 只作輔助提示
3. 缺 profile 視為 FAIL
Outputs：
* PR 已建立
* Merge 完成
* evidence/A_control_plane/workflow_runs.json
PASS Signals：
* Required Checks 全 PASS
* merge_group workflow 執行成功
* PR 已 merge
FAIL / Stopline：
* Required Checks FAIL → 見 WI-FAIL-01
* MQ 卡死 → 見 WI-FAIL-02
* Vibe PR 誤入 MQ → 見 WI-FAIL-03
Evidence：
* evidence/A_control_plane/workflow_runs.json
* evidence/D_workflow/docops-gatekit.yml.evidence
References：
* [Ref: SRS FR-GV-004]
* [Ref: v0 Pack NORM-23]
* Ref: GitHub Docs: Merging a pull request with a merge queue
________________


<a id="wi-fail-失敗處理指令"></a>
WI-FAIL：失敗處理指令
________________


<a id="wi-fail-01"></a>
WI-FAIL-01：重試上限/fail_packet/鎖定
項目
	內容
	Purpose
	處理 Stopline 觸發後的失敗情況
	Scope
	重試超限、fail_packet 產出
	Preconditions
	Gate 執行 FAIL 且 retry_count ≥3
	Responsible
	R: AI (Claude/Codex) / A: Human
	Steps：
#
	動作
	說明
	預期結果
	1
	檢查 retry_count
	從 run_manifest 讀取
	確認 ≥3
	2
	產出 fail_packet
	見下方 Schema
	JSON 檔案產出
	3
	停止執行
	不再重試
	流程暫停
	4
	通知人類
	輸出 fail_packet 路徑
	人類收到通知
	5
	等待人類介入
	人工判斷
	決策下達
	fail_packet Schema（完整且一致）：
{
  "task_id": "TASK-XXX",
  "failed_gate": "g3_schema",
  "retry_count": 3,
  "last_error": "schema validation failed: missing field 'created_at'",
  "stopline_triggered": true,
  "generated_at": "2026-01-29T10:30:00Z",
  "run_manifest_ref": "evidence/B_execution_plane/run_manifest.json",
  "recommended_action": "Check schema definition and input data"
}


人類介入決策：
決策
	行為
	修復後重試
	reset retry_count，重新執行
	放棄任務
	記錄於 evidence，關閉 Issue
	升級處理
	記錄 ADR，走變更流程
	Outputs：
* fail_packet.json
* 人類決策記錄
PASS Signals：
* fail_packet 格式正確
* 人類已介入
FAIL / Stopline：
* fail_packet 格式錯誤 → 修正後重新產出
Evidence：
* evidence/B_execution_plane/fail_packet.json
* evidence/B_execution_plane/run_manifest.json
References：
* [Ref: SRS INV-008]
________________


<a id="wi-fail-02"></a>
WI-FAIL-02：MQ 卡死診斷與復原
項目
	內容
	Purpose
	診斷並復原 Merge Queue 卡死狀況
	Scope
	MQ Expected 狀態、workflow 未觸發
	Preconditions
	PR 進入 MQ 後長時間無進展
	Responsible
	R: Developer / A: Repo Admin
	Steps：
#
	動作
	命令/檢查
	預期結果
	1
	檢查 MQ 狀態
	GitHub UI → Merge Queue
	顯示 PR 狀態
	2
	檢查 workflow 是否觸發
	Actions tab
	是否有 merge_group 執行
	3
	檢查 workflow 是否含 merge_group
	grep "merge_group" .github/workflows/*.yml
	命中
	4
	若缺 merge_group
	修復 workflow
	新增 trigger
	5
	重新觸發
	將 PR 移出再加入 MQ
	重新排隊
	常見原因與修復：
原因
	症狀
	修復
	workflow 缺 merge_group
	Expected 狀態永久 pending
	新增 merge_group: trigger
	Required Check 未在近期成功跑過
	Check 無法選取
	先在 main 跑一次 workflow
	path filter 排除
	workflow 未觸發
	調整 path filter 或移除
	診斷命令：
# 檢查 workflow 是否包含 merge_group
grep -A5 "^on:" .github/workflows/docops-gatekit.yml


# 預期輸出應包含：
# on:
#   pull_request:
#     branches: [main]
#   merge_group:
#     branches: [main]


最短復原路徑：
1. 確認 workflow 含 merge_group: → 若無則新增
2. 推送修復後的 workflow
3. 將 PR 移出 MQ
4. 重新將 PR 加入 MQ
5. 確認 workflow 觸發
Outputs：
* workflow 已修復（若需要）
* MQ 恢復運作
PASS Signals：
* merge_group workflow 觸發成功
* PR 成功合流
FAIL / Stopline：
* 多次嘗試仍無法修復 → 人工介入
Evidence：
* evidence/D_workflow/docops-gatekit.yml.evidence
* evidence/A_control_plane/workflow_runs.json
References：
* [Ref: v0 Pack NORM-22]
* Ref: GitHub Docs: Troubleshooting required status checks
________________


<a id="wi-fail-03"></a>
WI-FAIL-03：Expected Source 防偽造閉環
項目
	內容
	Purpose
	設定並驗證 Required Check 的 Expected Source
	Scope
	防止 status check 偽造
	Preconditions
	Ruleset 已配置
	Responsible
	R: Repo Admin / A: Human
	背景：
* 具有寫入權限的使用者可透過 API 直接報告 status check
* Expected Source 功能可限制只接受來自特定來源（如 GitHub Actions）的 status
Steps：
#
	動作
	命令/操作
	預期結果
	1
	進入 Ruleset 設定
	Settings → Rules → Rulesets
	顯示 rulesets
	2
	編輯 Required Checks
	點擊 Edit
	進入編輯模式
	3
	設定 Expected Source
	選擇 "GitHub Actions"
	來源已設定
	4
	儲存設定
	Save changes
	設定已儲存
	5
	驗證設定生效
	重新檢視 Ruleset JSON
	expected_source 非空
	6
	記錄到 evidence
	更新 settings_evidence
	欄位完整
	設定驗證命令：
# 透過 API 檢查 Ruleset 設定
gh api /repos/{owner}/{repo}/rulesets


# 檢查回傳 JSON 中的 required_status_checks
# 應包含 expected_source 欄位


Evidence 記錄格式：
{
  "ruleset": {
    "name": "main-protection",
    "required_checks": ["docops-gatekit/finalize"],
    "expected_source": "GitHub Actions",
    "expected_source_verified": true,
    "verification_method": "API query + UI screenshot",
    "verified_at": "2026-01-29T10:00:00Z"
  }
}


驗證設定已生效：
檢查項目
	預期結果
	驗證方式
	expected_source 非空
	"GitHub Actions"
	API 查詢
	來自其他來源的 status 被拒絕
	不計入 required checks
	測試
	Outputs：
* Ruleset 設定已更新
* evidence/A_control_plane/settings_evidence.json（expected_source 欄位）
PASS Signals：
* expected_source 已設定且非空
* 驗證截圖/JSON 已記錄
FAIL / Stopline：
* expected_source 未設定 → 設定
* 無法驗證設定 → 人工確認
Evidence：
* evidence/A_control_plane/settings_evidence.json
* evidence/A_control_plane/rulesets_detail.json
References：
* [Ref: SRS NFR-SEC-001]
* Ref: GitHub Docs: Available rules for rulesets
________________


Self-Verification（文件尾端驗證）
不可違反硬約束落地對照
#
	硬約束
	來源
	落地章節
	落地 WI
	Coverage Ledger 行號
	1
	Fail-Closed
	SRS INV-001
	R0.1(1), R2.4
	WI-FAIL-01
	#1
	2
	Input Seal SHA256
	SRS INV-002
	R2.1
	WI-DEV-01
	#2
	3
	ID Addressability
	SRS INV-003
	R1.2
	-
	#3
	4
	Trace Map
	SRS INV-004
	R3, R5
	-
	#4
	5
	One-Writer
	SRS INV-006
	R2.3
	WI-DEV-02
	#6
	6
	Negative Test
	SRS INV-007
	R2.5
	WI-DEV-04
	#7
	7
	Tool Budget/Stopline
	SRS INV-008
	R2.4, R6
	WI-FAIL-01
	#8
	8
	Anti-Platforming
	SRS INV-009
	R2.4
	WI-DEV-03
	#9
	9
	Dual-Judge Agreement
	SRS INV-010
	R2.5
	WI-DEV-04
	#10
	10
	merge_group 事件
	SRS EIR-001
	R2.6
	WI-CP-03
	#11
	11
	Required Checks SSOT
	v0 Pack NORM-21
	R2.6, R2.7
	WI-CP-01
	#12
	12
	MQ + merge_group
	v0 Pack NORM-22
	R2.6
	WI-CP-03
	#13
	13
	Vibe Lane 合流限制
	v0 Pack NORM-23
	R2.6
	WI-DEV-05
	#14
	狀態：13/13 硬約束已落地
最少人工介入設計對照
人工介入點
	機械化替代
	Evidence
	Gate 判定
	GateKit 自動執行
	gate_report.json
	合流批准
	Merge Queue 自動合流
	MQ logs
	雙法官裁決
	Dual-Judge 自動聚合
	final_aggregate_verdict.json
	Stopline 觸發
	retry_count 機械計數
	run_manifest.json
	Vibe 合流阻斷
	vibe_merge_block Gate
	rd01_vibe_block_evidence.json
	人類只在以下情況介入：
1. Stopline 觸發（連續失敗 ≥3 次）
2. 權限授權（Ruleset 變更）
3. 例外處置（fail_packet 產出後）
WI 計數驗證
類別
	WI 編號
	數量
	WI-ENV
	WI-ENV-01, WI-ENV-02, WI-ENV-03
	3
	WI-CP
	WI-CP-01, WI-CP-02, WI-CP-03
	3
	WI-DEV
	WI-DEV-01, WI-DEV-02, WI-DEV-03, WI-DEV-04, WI-DEV-05
	5
	WI-FAIL
	WI-FAIL-01, WI-FAIL-02, WI-FAIL-03
	3
	總計
	

	14
	最終判定
檢查項
	結果
	輸入文件完整性
	✓ PASS (全部可讀)
	版本正確性
	✓ PASS (v1.1.0)
	硬約束落地
	✓ PASS (13/13)
	合約詞對照
	✓ PASS
	最少人工介入
	✓ PASS
	Coverage Ledger
	✓ PASS (18 條映射)
	WI 完整性
	✓ PASS (14 WI)
	Evidence Path 一致性
	✓ PASS (全含 evidence/ 前綴)
	ID 命名一致性
	✓ PASS (有對照表)
	Overall Verdict: ✓ PASS
________________


<a id="appendix-a-issue-resolution-matrix"></a>
Appendix A：Issue Resolution Matrix
審查報告 A 問題解決
Issue ID
	Severity
	問題要點
	修補策略
	目標錨點
	驗證信號
	狀態
	A-F-001
	BLOCKER
	INV-003 覆蓋宣告但無具體操作步驟
	R1.2 補充需求原子 ID 操作指引
	R1.2
	"只引用既有 ID，不得新增/修改" 存在
	✓ RESOLVED
	A-F-002
	BLOCKER
	INV-007 Negative Test 缺 WI 落地
	WI-DEV-04 補充 Negative Test 執行方法
	WI-DEV-04
	negative_test_type 欄位定義存在
	✓ RESOLVED
	A-F-003
	MAJOR
	WI-CP-02 缺 permissions YAML 範例
	WI-CP-02 補充可複製貼上的範例
	WI-CP-02
	permissions YAML 範例存在
	✓ RESOLVED
	A-F-004
	MAJOR
	Evidence Path Alias Map 僅列 3 條
	補齊 A~F 六分類全覆蓋
	索引與映射
	6 分類全覆蓋
	✓ RESOLVED
	A-F-005
	MAJOR
	fail_packet 缺 generated_at
	R2.4 範例補充 generated_at
	R2.4
	generated_at 欄位存在
	✓ RESOLVED
	A-F-006
	MINOR
	WI-DEV-02 缺 worktree 命令範例
	補充 git worktree 命令
	WI-DEV-02
	git worktree 命令存在
	✓ RESOLVED
	A-F-007
	MINOR
	Task ID 命名規則混淆
	R1.2 明確區分場景
	R1.2
	場景表格存在
	✓ RESOLVED
	A-F-008
	MINOR
	缺 Codespaces 成本策略
	新增 WI-ENV-03
	WI-ENV-03
	WI-ENV-03 存在
	✓ RESOLVED
	審查報告 B 問題解決
Issue ID
	Severity
	問題要點
	修補策略
	目標錨點
	驗證信號
	狀態
	B-F-001
	BLOCKER
	Evidence 路徑規約混用（evidence/ 前綴漂移）
	R3 新增路徑規約一句話釘死 + 全表一致化
	R3, R5
	所有路徑含 evidence/ 前綴
	✓ RESOLVED
	B-F-002
	MAJOR
	"6 gates" 引用點可疑
	修正引用為 LBP Success Definition
	R0.1(5), R2.7
	引用正確
	✓ RESOLVED
	B-F-003
	MAJOR
	Gate/Check 命名規約未固化
	新增 R2.7 ID 規約與命名一致性 + 對照表
	R2.7, 索引與映射
	對照表存在
	✓ RESOLVED
	B-F-004
	MINOR
	缺術語/路徑/ID 對照表
	新增索引與映射章節
	索引與映射
	Glossary + Mapping 存在
	✓ RESOLVED
	B-F-005
	BLOCKER
	覆蓋台帳 trace_map 不存在
	INV-004 映射改為 rd01_router_evidence.json
	R5 #4
	映射指向存在的 evidence
	✓ RESOLVED
	B-F-006
	MAJOR
	expected source 只收集未設定/驗證
	新增 WI-FAIL-03 閉環
	WI-FAIL-03
	設定+驗證步驟存在
	✓ RESOLVED
	B-F-007
	MINOR
	GITHUB_TOKEN 缺可貼上片段
	WI-CP-02 補充完整範例
	WI-CP-02
	YAML 範例可直接複製
	✓ RESOLVED
	B-F-008
	MINOR
	Codespaces 信任清單缺 evidence 化
	WI-ENV-02 補充 evidence 格式
	WI-ENV-02
	trust 欄位定義存在
	✓ RESOLVED
	B-F-009
	MAJOR
	run_manifest schema 缺 retry_count
	WI-DEV-01 補充完整 schema
	WI-DEV-01
	retry_count 欄位存在
	✓ RESOLVED
	B-F-010
	MINOR
	Vibe lane 判定規則不清
	R2.6 補充 lane 判定優先序
	R2.6
	優先序說明存在
	✓ RESOLVED
	B-F-011
	MINOR
	Self-Verification WI 計數誤差
	修正為 14 WI
	Self-Verification
	計數正確
	✓ RESOLVED
	B-F-012
	MINOR
	版本書寫粒度不一致
	統一使用完整版本號
	全文
	v0.3.0, v0.4.1, v1.1.0
	✓ RESOLVED
	________________


<a id="appendix-b-coverage-ledger"></a>
Appendix B：Coverage Ledger（20+ 條抽核）
抽核清單
#
	上游要求
	Ref
	新版落點
	驗證信號
	Evidence 落點
	狀態
	1
	Fail-Closed
	SRS INV-001
	R0.1(1), R2.4, R6
	gate.fail_closed
	evidence/B_execution_plane/gate_report.json
	✓ PASS
	2
	Input Seal
	SRS INV-002
	R2.1, WI-DEV-01
	g0-input-seal
	evidence/B_execution_plane/input_manifest.json
	✓ PASS
	3
	ID Addressability
	SRS INV-003
	R1.2
	只引用不新增
	SRS 定義
	✓ PASS
	4
	Trace Map
	SRS INV-004
	R3, R5
	source pointer
	evidence/E_rd01_phase0/rd01_router_evidence.json
	✓ PASS
	5
	Evidence Replay
	SRS INV-005
	R3
	gate.evidence_replay
	evidence/B_execution_plane/verdict.json
	✓ PASS
	6
	One-Writer
	SRS INV-006
	R2.3, WI-DEV-02
	run_manifest.tool_version
	evidence/B_execution_plane/run_manifest.json
	✓ PASS
	7
	Negative Test
	SRS INV-007
	R2.5, WI-DEV-04
	negative_test_type
	evidence/C_dual_judge/judge_b_verdict.json
	✓ PASS
	8
	Tool Budget/Stopline
	SRS INV-008
	R2.4, R6, WI-FAIL-01
	retry_count ≥3
	evidence/B_execution_plane/run_manifest.json
	✓ PASS
	9
	Anti-Platforming
	SRS INV-009
	R2.4, WI-DEV-03
	g3-anti-platform
	evidence/B_execution_plane/gate_report.json
	✓ PASS
	10
	Dual-Judge
	SRS INV-010
	R2.5, WI-DEV-04
	g4-dual-judge
	evidence/C_dual_judge/final_aggregate_verdict.json
	✓ PASS
	11
	merge_group
	SRS EIR-001
	R2.6, WI-CP-03
	trigger 存在
	evidence/D_workflow/*.evidence
	✓ PASS
	12
	Required Checks SSOT
	v0 Pack NORM-21
	R2.6, R2.7, WI-CP-01
	finalize 存在
	evidence/A_control_plane/settings_evidence.json
	✓ PASS
	13
	MQ + merge_group
	v0 Pack NORM-22
	R2.6, WI-CP-03
	workflow 含 merge_group
	evidence/D_workflow/*.evidence
	✓ PASS
	14
	Vibe Lane 限制
	v0 Pack NORM-23
	R2.6, WI-DEV-05
	vibe_merge_block
	evidence/E_rd01_phase0/rd01_vibe_block_evidence.json
	✓ PASS
	15
	TVS A1 Repo Org-owned
	TVS §9
	R4.1
	owner.type
	evidence/A_control_plane/repo_info.json
	✓ PASS
	16
	TVS A2 Ruleset exists
	TVS §9
	R4.1
	非空陣列
	evidence/A_control_plane/settings_evidence.json
	✓ PASS
	17
	TVS A3 finalize
	TVS §9
	R4.1
	check 存在
	evidence/A_control_plane/settings_evidence.json
	✓ PASS
	18
	TVS A4 MQ enabled
	TVS §9
	R4.1
	merge_queue.enabled
	evidence/A_control_plane/settings_evidence.json
	✓ PASS
	19
	TVS A5 merge_group
	TVS §9
	R4.1
	grep 命中
	evidence/D_workflow/*.evidence
	✓ PASS
	20
	RD01-1 Profiles
	TVS §9
	R4.3
	vibe=true, dev=true
	evidence/E_rd01_phase0/rd01_profiles_evidence.json
	✓ PASS
	21
	RD01-2 Vibe Block
	TVS §9
	R4.3
	2/2 passed
	evidence/E_rd01_phase0/rd01_vibe_block_evidence.json
	✓ PASS
	22
	RD01-3 Lane Router
	TVS §9
	R4.3
	5/5 passed
	evidence/E_rd01_phase0/rd01_router_evidence.json
	✓ PASS
	23
	6 Gates 固定
	LBP Success Def
	R0.1(5), R2.7
	無新增 gate
	evidence/B_execution_plane/gate_report.json
	✓ PASS
	24
	Claude Code 主寫
	LBP ADR-001
	R2.3, WI-DEV-02
	tool_version
	evidence/B_execution_plane/run_manifest.json
	✓ PASS
	25
	Expected Source
	GitHub Docs
	WI-CP-01, WI-FAIL-03
	expected_source 非空
	evidence/A_control_plane/settings_evidence.json
	✓ PASS
	抽核結果：25/25 PASS
________________


<a id="appendix-c-change-log"></a>
Appendix C：Change Log（v1.0.0 → v1.1.0）
Patch ID
	意圖級摘要
	目標章節
	P-001
	補充 INV-003 (ID Addressability) 操作指引：明確「只引用既有 ID，不得新增/修改」
	R1.2
	P-002
	補充 INV-007 (Negative Test) WI 執行方法：提供完整執行步驟與 evidence 欄位
	R2.5, WI-DEV-04
	P-003
	新增「索引與映射」章節：Glossary + ID/Name Mapping + Evidence Path Alias Map (A~F 六分類)
	文件開頭
	P-004
	固化 Evidence 路徑規約：一句話釘死「必含 evidence/ 前綴」
	R3
	P-005
	全表一致化 Evidence 路徑：R4/R5 所有路徑補齊 evidence/ 前綴
	R4, R5
	P-006
	修正 INV-004 Evidence 映射：從不存在的 trace_map.json 改為 rd01_router_evidence.json
	R5
	P-007
	新增 R2.7 ID 規約與命名一致性：Canonical 優先 + 對照表
	R2.7
	P-008
	修正「6 Gates」引用：從 NORM-21 改為 LBP Success Definition
	R0.1(5), R2.7
	P-009
	WI-CP-02 補充 permissions YAML 範例：可直接複製貼上
	WI-CP-02
	P-010
	WI-DEV-02 補充 git worktree 命令範例：完整 add/list/remove 命令
	WI-DEV-02
	P-011
	R2.4 fail_packet 範例補充 generated_at timestamp
	R2.4
	P-012
	WI-DEV-01 run_manifest schema 補充 retry_count/failed_gate 欄位
	WI-DEV-01
	P-013
	新增 WI-ENV-03 Codespaces 成本與停用策略
	WI-ENV-03
	P-014
	新增 WI-FAIL-03 Expected Source 防偽造閉環：設定+驗證+evidence
	WI-FAIL-03
	P-015
	WI-ENV-02 補充信任清單 evidence 格式
	WI-ENV-02
	P-016
	R2.6 補充 Vibe Lane 判定優先序：profile 旗標優先
	R2.6
	P-017
	Self-Verification WI 計數修正：11 → 14
	Self-Verification
	P-018
	版本書寫統一：全部使用完整版本號 (v0.3.0, v0.4.1, v1.1.0)
	全文
	P-019
	補充 Upstream-to-Runbook Map 映射表
	索引與映射
	P-020
	新增 WI-FAIL-02 MQ 卡死診斷與復原最短路徑
	WI-FAIL-02
	________________


文件結束
________________


Metadata Footer:
* doc_id: GMA-RUNBOOK-WI-001
* version: v1.1.0
* generated_at: 2026-01-29
* authority: Implementation SSOT
* scope: v0 (Vibe + Dev Lane)
* upgrade_from: v1.0.0
* total_patches: 20
________________


【OPT】2026+ 外部最佳實務參考（Non-binding）
以下為 2026 年以後搜索到的最新可信來源，僅供參考，不構成新規範：
1. Merge Queue + merge_group：GitHub Docs 確認若使用 MQ，workflow 必須包含 merge_group 事件觸發器（已落地於 WI-CP-03）
2. Required status checks 7 天限制：GitHub 文檔確認 Required status checks 必須在過去 7 天內成功運行過才能被選為 required（風險項）
3. GITHUB_TOKEN 最小權限：GitHub 官方建議設定 default permissions 為 read-only，在 workflow 中按需提升（已落地於 WI-CP-02）
4. Codespaces 成本控制：GitHub Docs 建議設定 idle timeout (30 分鐘預設) 和 retention period (7-14 天)（已落地於 WI-ENV-03）
5. Expected Source：GitHub Docs 確認 Rulesets 支援設定 required status check 的 expected source 來防止偽造（已落地於 WI-FAIL-03）
6. Actions Pin SHA：GitHub 安全最佳實務建議 pin 第三方 actions 到完整 commit SHA（標記為 OPT）
來源：
* GitHub Docs: Managing a merge queue (docs.github.com)
* GitHub Docs: Troubleshooting required status checks (docs.github.com)
* GitHub Docs: Automatic token authentication (docs.github.com)
* GitHub Docs: Managing the cost of GitHub Codespaces (docs.github.com)
* GitHub Docs: Available rules for rulesets (docs.github.com)
* GitGuardian Blog: GitHub Actions Security Best Practices (2025)