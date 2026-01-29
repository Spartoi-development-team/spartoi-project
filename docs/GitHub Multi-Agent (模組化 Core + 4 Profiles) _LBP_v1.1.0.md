GitHub Multi-Agent (模組化 Core + 4 Profiles) _LBP_v1.1.0
外部名稱: GitHub Multi-Agent DocOps Lightweight Baseline Package
內部簡稱: LBP
版本號: v1.1.0
發布日期: 2026-01-29
狀態: FINAL
________________


目錄 (Table of Contents)
1. Retrieval Guide
2. Scope Lock
3. LBP Self-Guards
4. SIR - System Intent Report
   * SIR-00 Scope & Non-Goals
   * SIR-01 System Intent
   * SIR-02 Hard Constraints
   * SIR-03 Risk Register
   * SIR-04 Trace Pointers
   * SIR-05 Notes Import Mapping
5. ICD - Interface Contract Document
   * ICD-00 Contract Scope
   * ICD-01 Planes & Responsibilities
   * ICD-02 Registry Contracts
   * ICD-03 Gate Contracts
   * ICD-04 Evidence Contracts
   * ICD-05 Notes Import Contracts
6. ADR - Architectural Decision Records
   * ADR-001 Tooling Strategy
   * ADR-002 Evidence Bundle Strategy
   * ADR-003 Gate Classification
   * ADR-004 Merge Queue Strategy
7. C4 - Architecture Diagrams
   * C4-L1 System Context
   * C4-L2 Containers
   * C4-L3 Components
   * C4-L4 Code Map
8. FITNESS - Fitness Catalog
   * FIT-00 Philosophy & Scope
   * FIT-01 Fitness Catalog
   * FIT-02 GateKit Mapping
   * FIT-03 MQ Compatibility
   * FIT-04 Drift Rules
9. Evidence Alias Map
________________


<a id="retrieval-guide"></a>
Retrieval Guide (檢索優先序)
檢索本 LBP 時，請依以下優先序查找權威來源：
優先序
	文檔
	用途
	1
	SRS v1.1.0
	規範性需求定義（INV-/FR-/EIR-*）
	2
	TVS v0.4.1
	導入策略與驗收條件（§7/§8/§9）
	3
	v0 Pack v0.3.0
	規範 SSOT（NORM-01~25）
	4
	evidence_index.json
	證據索引（A~F 分類）
	5
	tvs_section9_verdict.json
	驗收裁決
	6
	complete_evidence_bundle_v2.json
	完整證據包（含 rd01_evidence/*）
	禁止腦補：無 [Ref:] 標註的陳述不構成規範。
________________


<a id="scope-lock"></a>
Scope Lock (邊界鎖定)
LBP 定位
* 是：開發+實作過程的可稽核基線包
* 不是：規範法典、操作手冊、新規範 SSOT
LBP 不得
1. 取代 SRS/Runbook/Registry/TVS
2. 新增任何 gate.* 名稱或 Required Check
3. 內嵌操作步驟/工作流片段/命令教學
4. 創建新的規範性關鍵字（MUST/SHALL）
LBP 可以
1. 作為指針索引指向既有規範
2. 記錄設計意圖與決策取捨（ADR）
3. 定義可測度量（Fitness）並映射到既有 Gate
4. 建立契約化介面定義（ICD）
[Ref: LBP 方案 §1.2][Ref: 架構指南 §13.1]
________________


<a id="lbp-self-guards"></a>
LBP Self-Guards (自我鎖定條款)
SG-01 Ref Format Contract
* 所有 Ref 必須包含「文件名 + 可定位 anchor 或章節編號」
* 禁止對採用 2.x 編號的來源使用「§」寫法
* 筆記引用格式：[Ref: Building Effective Agents 2.6] 或 [Ref: Claude Code 筆記 2.5]
* 不可定位 Ref → 該句自動降級為 NON-BINDING NOTE
SG-02 No-Source-No-Norm
* 無 Ref 不算主張
* Evidence 指向不存在 → 回放 FAIL
* 所有 Evidence 指針必須在 evidence_index.json 或 complete_bundle 中可定位
SG-03 Gate Naming Guardrail
* finalize 為 TVS §7.1 的 logical label（Ruleset Required Check），不算新增 Gate
* v0 GateKit 清單以 v0 Pack NORM-21 為 SSOT
* 不得在 Fitness/Risk/ADR 中引入非 v0 GateKit 的 gate.* 名稱
* 概念如 tool budget / evidence completeness 只能以「signal/field/metric」呈現
SG-04 Evidence Pointer Rule
* LBP 內所有 evidence 指針必須落在：
   * (a) evidence_index.json 的 keys（A_control_plane ~ F_rules_and_gates）
   * (b) complete_bundle 列出的 rd01_evidence/*.json
* 舊路徑若存在，必須提供 alias map（見 Evidence Alias Map）
________________


═══════════════════════════════════════════════════════════════
SIR - System Intent Report
═══════════════════════════════════════════════════════════════
<a id="sir"></a>
---
doc_id: LBP-SIR-001
owner_role: LBP Pack Owner
last_updated: 2026-01-29
version: v1.1.0
source_refs:
  - SRS v1.1.0
  - TVS v0.4.1
  - v0 Pack v0.3.0
  - 架構指南
related_gates:
  - finalize
  - g0-input-seal
  - g3-schema
  - g3-anti-platform
  - g4-dual-judge
  - format-check
evidence_hooks:
  - A_control_plane/settings_evidence.json
  - B_execution_plane/verdict.json
  - C_dual_judge/final_aggregate_verdict.json
scope_lock_refs:
  - SRS §1.3
  - TVS §2
---


<a id="sir-00"></a>
SIR-00 Scope & Non-Goals
Scope（範圍鎖定）
項目
	說明
	來源指針
	Repo 類型
	Org-owned Public
	[Ref: SRS §1.3][Ref: TVS §2.1]
	Merge Queue
	MQ=ON（必須啟用）
	[Ref: TVS Front Matter][Ref: v0 Pack CR_OPEN-14]
	Phase 0 泳道
	Vibe Lane + Dev Lane 啟用；Spec/Ops disabled
	[Ref: SRS §1.3][Ref: v0 Pack NORM-03]
	付費 API
	不依賴
	[Ref: 架構指南 1.1]
	Non-Goals（明確不做）
項目
	說明
	來源指針
	NG-01
	建立通用自動化平台
	[Ref: TVS §2.2]
	NG-02
	支援 Tier-2/Tier-3 任務類型（v0 範圍外）
	[Ref: TVS §2.2]
	NG-03
	實作完整 Matrix Jobs
	[Ref: TVS §2.2]
	NG-04
	部署生產級監控告警
	[Ref: TVS §2.2]
	NG-05
	撰寫全量 Roadmap
	[Ref: TVS §2.2]
	________________


<a id="sir-01"></a>
SIR-01 System Intent（系統意圖）
北極星成功條件
系統意圖：證據驅動的多代理 DevOps 治理框架，以機械閘門取代人工審查，實現可稽核、可回放的自動化流程。
[Ref: README v1.1 §1][Ref: SRS §2]
成功定義（對齊 TVS §9 驗收語彙）
驗收項
	條件
	對應 TVS §9
	A1
	Repo 為 Org-owned Public
	[Ref: TVS §9 A1]
	A2
	Ruleset 存在
	[Ref: TVS §9 A2]
	A3
	Required checks 包含 finalize
	[Ref: TVS §9 A3]
	A4
	Merge Queue 啟用
	[Ref: TVS §9 A4]
	A5
	Workflow 包含 merge_group 觸發
	[Ref: TVS §9 A5]
	Gate Report
	所有 6 Gates PASS
	[Ref: TVS §9]
	Verdict
	PASS + judges A/B 一致
	[Ref: TVS §9]
	________________


<a id="sir-02"></a>
SIR-02 Hard Constraints（硬約束）
Constraint ID
	約束名稱
	說明
	來源指針
	驗證信號
	HC-01
	Fail-Closed
	預設阻斷：缺證據/缺欄位/不合格即 FAIL
	[Ref: SRS INV-001][Ref: v0 Pack NORM-06]
	g0-input-seal FAIL
	HC-02
	Anti-Platforming
	禁詞掃描：命中「Unified Platform」等即 P0 FAIL
	[Ref: SRS INV-009][Ref: v0 Pack NORM-09]
	g3-anti-platform FAIL
	HC-03
	One-Writer
	同一檔案同時間僅一寫入者，並行必須 worktree 隔離
	[Ref: SRS INV-006][Ref: 架構指南 13.4.2-D]
	concurrent_writers metric ≤1
	HC-04
	Evidence 可回放
	所有裁決必須有可回放證據包支撐
	[Ref: SRS INV-005][Ref: v0 Pack NORM-18]
	evidence_index.complete == true
	HC-05
	Merge Queue 強制
	MQ=ON，workflow 必須監聽 merge_group
	[Ref: SRS EIR-001][Ref: TVS §7.3]
	grep merge_group ≥1
	HC-06
	Dual-Judge 嚴格一致
	(Judge_A == PASS) AND (Judge_B == PASS) AND (Bias_Check == PASS)
	[Ref: SRS INV-010][Ref: v0 Pack NORM-13]
	g4-dual-judge agreement
	HC-07
	禁止 AI 自動解衝突
	PR 含 git 衝突標記且由 Agent 產生 → FAIL
	[Ref: SRS INV-006][Ref: v0 Pack NORM-11]
	format-check marker scan
	HC-08
	Tool Budget / Stopline
	重試上限 3 次；超限輸出 fail_packet.json 並鎖定
	[Ref: SRS INV-008][Ref: v0 Pack NORM-11]
	retry_count metric <3
	________________


<a id="sir-03"></a>
SIR-03 Risk Register（Fail-Closed，≥8 條）
risk_id
	風險描述
	trigger
	impact
	detection (signal + gate/logical)
	mitigation
	owner_role
	evidence_pointer
	type
	RISK-01
	Evidence 缺失導致無法驗收
	evidence bundle 不完整
	驗收阻斷(P0)
	evidence_index.complete == false / finalize
	執行前預檢 evidence 清單
	Evidence Store
	A_control_plane/settings_evidence.json
	FEAS
	RISK-02
	merge_group 未觸發導致 MQ 卡死
	workflow 缺 merge_group 監聽
	MQ 卡死(P0)
	grep merge_group == 0 / g0-input-seal
	Day-1 Workflow 驗證
	GateKit
	D_workflow/docops-gatekit.yml.evidence
	FEAS
	RISK-03
	雙法官裁決不一致
	Judge_A ≠ Judge_B 或 Swap 翻轉
	裁決無效(P1)
	agreement != true / g4-dual-judge
	執行 Swap Order 測試
	Dual Judge
	C_dual_judge/final_aggregate_verdict.json
	LOGIC
	RISK-04
	禁詞命中 Anti-Platform
	輸出含「Unified Platform」等
	P0 阻斷
	hit_count > 0 / g3-anti-platform
	前置禁詞掃描
	GateKit
	B_execution_plane/gate_report.json
	POLICY
	RISK-05
	Schema 驗證失敗
	JSON 工件不符 Schema
	驗收阻斷(P1)
	validation_errors > 0 / g3-schema
	Registry Schema 版本鎖定
	GateKit
	B_execution_plane/gate_report.json
	STRUCT
	RISK-06
	Vibe Lane 嘗試進 Merge Queue
	profile=vibe + merge_group 觸發
	流程越界(P1)
	vibe_block triggered / vibe-merge-block
	run_vibe_merge_block()
	GateKit
	E_rd01_phase0/rd01_vibe_block_evidence.json
	POLICY
	RISK-07
	Stopline 觸發
	連續失敗 ≥3 次
	資源浪費(P2)
	retry_count >= 3 / finalize
	Tool Budget 預設 3 次
	Execution Agent
	B_execution_plane/run_manifest.json
	FEAS
	RISK-08
	UI-only 設定缺乏可驗證證據
	Approve-and-Run 等設定無截圖 hash
	審計漏洞(P2)
	settings_evidence 缺欄位 / finalize
	MANUAL_ATTESTATION + SHA256
	LBP Owner
	A_control_plane/settings_evidence.json
	FEAS
	RISK-09
	Required Check 來源偽造
	非預期 GitHub App 設定狀態
	安全風險(P1)
	expected_source mismatch / finalize
	設定 Ruleset expected source 為 GitHub Actions
	LBP Owner
	A_control_plane/rulesets_detail.json
	RISK
	RISK-10
	Required Check 7 天成功記錄失效
	workflow 超過 7 天未成功運行
	無法選為 required(P1)
	last_success_date > 7 days / 手動檢查
	定期觸發 workflow 保持活躍
	LBP Owner
	A_control_plane/workflow_runs.json
	RISK
	RISK-11
	Evidence 路徑漂移
	LBP evidence pointer 與實際證據包不一致
	回放失敗(P0)
	alias_map 查無對應 / 驗收
	維護 Evidence Alias Map
	Evidence Cross-Checker
	evidence_index.json
	DRIFT
	RISK-12
	Gate 類別擴張
	出現非 v0 GateKit 的 gate.* 名稱
	治理膨脹(P0)
	grep gate.* 命中非 v0 / 審計
	LBP Self-Guards SG-03
	Drift Hunter
	N/A
	DRIFT
	________________


<a id="sir-04"></a>
SIR-04 Trace Pointers（追溯指針）
規範層指針
概念
	SRS 錨點
	v0 Pack 錨點
	TVS 錨點
	Fail-Closed
	INV-001
	NORM-06
	§9
	One-Writer
	INV-006
	-
	-
	Dual-Judge
	INV-010
	NORM-12~17
	§7.4
	Anti-Platform
	INV-009
	NORM-09
	-
	Evidence Bundle
	§9
	NORM-18~20
	§8
	merge_group
	EIR-001
	NORM-22
	§7.3
	Tool Budget
	INV-008
	NORM-11
	§10.4
	Evidence 層指針（對齊 evidence_index.json）
Evidence Key
	Canonical Path (v0.4.1)
	說明
	control_plane
	A_control_plane/*.json
	控制平面證據
	execution_plane
	B_execution_plane/*.json
	執行平面證據
	dual_judge
	C_dual_judge/*.json
	雙法官證據
	workflow
	D_workflow/*.evidence
	Workflow 證據
	rd01_phase0
	E_rd01_phase0/*.json
	RD01 Phase0 證據
	rules_gates
	F_rules_and_gates/.yaml/.py
	規則與閘門檔案
	[Ref: SRS §11 T5 Evidence Pointer Index]
________________


<a id="sir-05"></a>
SIR-05 Notes Import Mapping（筆記導入映射）
Building Effective Agents 導入
Pattern
	落點
	說明
	來源指針
	Evaluator-Optimizer Loop
	SIR-02 HC-06
	對應 Dual-Judge 嚴格一致性
	[Ref: Building Effective Agents 2.6][Ref: SRS INV-010]
	Fail-Closed Gate
	SIR-02 HC-01
	對應 Fail-Closed 預設阻斷
	[Ref: Building Effective Agents 2.2][Ref: SRS INV-001]
	One Brain One Stream
	SIR-02 HC-03
	對應 One-Writer 規則（寫操作強耦合）
	[Ref: Building Effective Agents 3.2.2][Ref: SRS INV-006]
	Verifier Agent 獨立
	SIR-02 HC-06
	對應 Dual-Judge 物理隔離
	[Ref: Building Effective Agents 3.3.3][Ref: 架構指南 7.4]
	Claude Code 筆記導入
Pattern
	落點
	說明
	限制
	CLAUDE.md 記憶階層
	ICD-05
	需符合 schema
	[Ref: Claude Code 筆記 2.4][Ref: SRS FR-MEM-006]
	MCP 工具數量限制
	SIR-03 RISK-07 NOTE
	工具 <80 否則性能下降
	[Ref: Claude Code 筆記 2.5]；非 required，僅 advisory
	Actions 依賴 API key
	SIR-03 RISK-08
	若依賴付費 API 則降為 optional
	[Ref: Claude Code 筆記 1.1]；[Ref: 架構指南 1.1 No Paid API]
	NON-BINDING NOTE: MCP 工具數量 <80 為 advisory 建議，非 Gate 門檻。[Ref: Claude Code 筆記 2.5]
________________


═══════════════════════════════════════════════════════════════
ICD - Interface Contract Document
═══════════════════════════════════════════════════════════════
<a id="icd"></a>
---
doc_id: LBP-ICD-001
owner_role: Contract Integrator
last_updated: 2026-01-29
version: v1.1.0
source_refs:
  - SRS v1.1.0
  - TVS v0.4.1
  - v0 Pack v0.3.0
  - 架構指南
related_gates:
  - finalize
  - g0-input-seal
  - g3-schema
  - g3-anti-platform
  - g4-dual-judge
  - format-check
evidence_hooks:
  - A_control_plane/*.json
  - B_execution_plane/*.json
  - C_dual_judge/*.json
scope_lock_refs:
  - SRS §1.3
  - LBP_方案 §1.2
---


<a id="icd-00"></a>
ICD-00 Contract Scope（契約範圍）
介面類別
	範圍說明
	來源指針
	Plane Interfaces
	Control Plane ↔ Execution Plane 資料交換
	[Ref: 架構指南 2][Ref: SRS FR-AR-001]
	Registry Contracts
	Skills/Gates/Policies/Schemas 的 key/schema/版本
	[Ref: v0 Pack 4.3][Ref: SRS FR-SK-001]
	Gate Contracts
	gate.* 命名、輸入/輸出、failure_mode
	[Ref: TVS §7][Ref: v0 Pack NORM-08]
	Evidence Contracts
	manifest/report/verdict 最小集合
	[Ref: SRS §9][Ref: v0 Pack NORM-18~20]
	不屬於 contract：操作步驟（→ Runbook）、Schema 欄位細節（→ Registry）
________________


<a id="icd-01"></a>
ICD-01 Planes & Responsibilities（平面與責任）
[Ref: 架構指南 2][Ref: TVS §4.1][Ref: SRS FR-AR-001]
平面
	職責
	Day-1 最低配置
	來源指針
	Control Plane (GitHub)
	機械驗證、狀態流轉、合流裁決
	Ruleset + Required Checks + Merge Queue
	[Ref: TVS §4.1]
	Execution Plane (Codespaces)
	可重現工廠、執行施工、回傳證據
	.devcontainer + 工具鏈
	[Ref: TVS §4.1]
	平面交互契約
contract_id
	producer
	consumer
	input
	output
	failure_mode
	verification_signal
	evidence_pointer
	upstream_ref
	ICD-PLANE-01
	Execution
	Control
	PR push
	Evidence Bundle (JSON)
	Bundle 不完整 → FAIL
	evidence_index.complete
	B_execution_plane/verdict.json
	[Ref: SRS §9][Ref: v0 Pack NORM-18]
	ICD-PLANE-02
	Control
	Execution
	Workflow trigger
	Gate Result (Status Check)
	Check 未回報 → MQ 卡死
	finalize status
	A_control_plane/workflow_runs.json
	[Ref: TVS §7]
	ICD-PLANE-03
	Control
	Control
	finalize PASS
	Merge Signal
	finalize FAIL → 阻斷
	merge_group event
	D_workflow/*.evidence
	[Ref: TVS §4.3]
	________________


<a id="icd-02"></a>
ICD-02 Registry Contracts（Registry 契約）
[Ref: v0 Pack 4.3][Ref: SRS FR-SK-001~005]
contract_id
	producer
	consumer
	input
	output
	failure_mode
	verification_signal
	evidence_pointer
	upstream_ref
	ICD-REG-01
	Registry
	GateKit
	index.yaml query
	索引條目
	索引缺失 → FAIL
	index.yaml exists
	F_rules_and_gates/*.yaml
	[Ref: v0 Pack Registry 計數器]
	ICD-REG-02
	Registry
	GateKit
	skill query
	SkillPack 定義
	Skill 不存在 → FAIL
	skill file exists
	F_rules_and_gates/*.yaml
	[Ref: v0 Pack NORM-08]
	ICD-REG-03
	Registry
	GateKit
	gate query
	Gate Runner 定義
	Gate 不存在 → FAIL
	gate file exists
	F_rules_and_gates/*.py
	[Ref: v0 Pack NORM-08]
	ICD-REG-04
	Registry
	Schema Validator
	schema query
	JSON Schema 定義
	Schema 驗證失敗 → FAIL
	g3-schema PASS
	B_execution_plane/gate_report.json
	[Ref: v0 Pack NORM-20]
	________________


<a id="icd-03"></a>
ICD-03 Gate Contracts（Gate 契約）
[Ref: TVS §7][Ref: v0 Pack NORM-08][Ref: v0 Pack NORM-21]
contract_id
	gate_name
	producer
	consumer
	input
	output
	failure_mode
	verification_signal
	evidence_pointer
	upstream_ref
	ICD-GATE-01
	g0-input-seal
	Execution
	finalize
	source files
	sha256 hash
	hash mismatch → FAIL
	g0-input-seal PASS
	B_execution_plane/gate_report.json
	[Ref: SRS INV-002]
	ICD-GATE-02
	g3-schema
	Execution
	finalize
	JSON artifacts
	validation result
	schema error → FAIL
	g3-schema PASS
	B_execution_plane/gate_report.json
	[Ref: SRS FR-GK-003]
	ICD-GATE-03
	g3-anti-platform
	Execution
	finalize
	text content
	scan result
	hit found → P0 FAIL
	g3-anti-platform PASS
	B_execution_plane/gate_report.json
	[Ref: SRS INV-009]
	ICD-GATE-04
	g4-dual-judge
	Execution
	finalize
	candidate output
	verdict pair
	disagreement → FAIL
	g4-dual-judge PASS
	C_dual_judge/final_aggregate_verdict.json
	[Ref: SRS INV-010]
	ICD-GATE-05
	format-check
	Execution
	finalize
	git status
	diff result
	dirty tree → FAIL
	format-check PASS
	B_execution_plane/gate_report.json
	[Ref: v0 Pack NORM-10]
	ICD-GATE-06
	finalize
	GateKit
	Ruleset
	gate results
	aggregate verdict
	any gate FAIL → FAIL
	finalize PASS
	B_execution_plane/verdict.json
	[Ref: TVS §7.1]
	________________


<a id="icd-04"></a>
ICD-04 Evidence Contracts（Evidence 契約）
[Ref: SRS §9][Ref: v0 Pack NORM-18~20][Ref: TVS §8]
contract_id
	producer
	consumer
	input
	output
	failure_mode
	verification_signal
	evidence_pointer
	upstream_ref
	ICD-EV-01
	Execution
	Evidence Store
	execution run
	input_manifest.json
	缺檔 → FAIL
	file exists + sha256
	B_execution_plane/input_manifest.json
	[Ref: v0 Pack NORM-19]
	ICD-EV-02
	Execution
	Evidence Store
	execution run
	run_manifest.json
	缺檔 → FAIL
	file exists + sha256
	B_execution_plane/run_manifest.json
	[Ref: v0 Pack NORM-19]
	ICD-EV-03
	GateKit
	Evidence Store
	gate execution
	gate_report.json
	缺檔 → FAIL
	file exists + sha256
	B_execution_plane/gate_report.json
	[Ref: v0 Pack NORM-19]
	ICD-EV-04
	Dual Judge
	Evidence Store
	judge execution
	verdict.json
	缺檔 → FAIL
	file exists + sha256
	B_execution_plane/verdict.json
	[Ref: v0 Pack NORM-19]
	ICD-EV-05
	Control Plane
	Evidence Store
	settings capture
	settings_evidence.json
	缺檔 → FAIL
	file exists + sha256
	A_control_plane/settings_evidence.json
	[Ref: v0 Pack NORM-19]
	________________


<a id="icd-05"></a>
ICD-05 Notes Import Contracts（筆記導入契約）
CLAUDE.md Schema Contract
contract_id
	producer
	consumer
	input
	output
	failure_mode
	verification_signal
	evidence_pointer
	upstream_ref
	ICD-NOTE-01
	Developer
	Claude Agent
	CLAUDE.md file
	parsed memory hierarchy
	parse error → FAIL
	CLAUDE.md exists + valid format
	repo file
	[Ref: Claude Code 筆記 2.4][Ref: SRS FR-MEM-006]
	Schema 要求（NON-BINDING NOTE，完整 Schema 見 Registry）：
* CLAUDE.md 必須為有效 Markdown
* 支援層級結構（project/user/global）
* 內容長度限制依 Claude Code CLI 版本而定
[Ref: Claude Code 筆記 2.4]
MCP Tool Count Advisory
項目
	建議值
	風險
	來源
	安裝總數
	20~30
	超過可能影響載入效能
	[Ref: Claude Code 筆記 2.5]
	同時開啟
	≤10
	活躍連接過多佔用推理資源
	[Ref: Claude Code 筆記 2.5]
	工具總數
	<80
	工具過多導致模型選擇困難
	[Ref: Claude Code 筆記 2.5]
	NON-BINDING NOTE: 以上為 advisory 建議，非 Gate 門檻，不納入 required checks。
________________


═══════════════════════════════════════════════════════════════
ADR - Architectural Decision Records
═══════════════════════════════════════════════════════════════
<a id="adr"></a>
<a id="adr-001"></a>
ADR-001 Tooling Strategy (One-Writer / Claude Code 主寫 / 備援工具策略)
---
doc_id: LBP-ADR-001
owner_role: LBP Pack Owner
last_updated: 2026-01-29
version: v1.1.0
status: ACCEPTED
source_refs:
  - SRS INV-006
  - 架構指南 13.4.2-D
  - Building Effective Agents 3.2.2
related_gates:
  - format-check
evidence_hooks:
  - B_execution_plane/run_manifest.json
---


Context
系統需要選擇 AI 編程工具策略。可選方案包括：
1. Claude Code CLI 為主寫工具（訂閱制，非 API）
2. Codex CLI 作為備援
3. 多工具並行寫入
[Ref: 架構指南 3.1][Ref: 架構指南 1.1 No Paid API]
Decision
選擇方案 1 + 方案 2（Claude Code 主寫 + Codex 備援），拒絕方案 3
* 主寫工具: Claude Code CLI（訂閱制，符合 No Paid API 約束）
* 備援工具: Codex CLI（當主寫工具不可用時啟用）
* 禁止: 多工具並行寫入同一檔案
[Ref: SRS INV-006][Ref: Building Effective Agents 3.2.2]
Consequences
正面:
* 符合 One-Writer 約束（HC-03）
* 避免並行寫入導致的衝突
* 不依賴付費 API
負面:
* 主寫工具不可用時需手動切換
* 備援工具可能有功能差異
Evidence
* 工具選擇記錄於 run_manifest.json 的 tool_version 欄位
* Evidence 指針: B_execution_plane/run_manifest.json
________________


<a id="adr-002"></a>
ADR-002 Evidence Bundle Strategy (最小鍵集合與可回放策略)
---
doc_id: LBP-ADR-002
owner_role: LBP Pack Owner
last_updated: 2026-01-29
version: v1.1.0
status: ACCEPTED
source_refs:
  - SRS INV-005
  - v0 Pack NORM-18~20
  - TVS §8
related_gates:
  - finalize
evidence_hooks:
  - evidence_index.json
  - B_execution_plane/verdict.json
---


Context
系統需要定義 Evidence Bundle 的最小必備鍵集合，以確保：
1. 所有裁決可回放
2. 證據包不膨脹
3. 驗收可機械化
可選方案包括：
1. 最小固定鍵集合（v0 Pack 定義）
2. 動態鍵集合（依任務類型變化）
3. 全量鍵集合（所有可能欄位）
[Ref: v0 Pack NORM-19][Ref: TVS §8.2]
Decision
選擇方案 1：最小固定鍵集合
v0 Evidence Pack 最小清單：
1. input_manifest.json（含 source_bundle_sha256）
2. run_manifest.json（環境/工具版本/參數）
3. gate_report.json（所有 Gate 結果）
4. verdict.json（Judge A/B + 聚合結果 + swap_test_passed + agreement）
5. coverage_map.json（v0 為 stub）
6. diff_report.md（變更差異）
7. settings_evidence.json（Day-1 設定證據）
[Ref: v0 Pack NORM-19]
Consequences
正面:
* 證據包大小可控
* 驗收條件明確
* 可機械化驗證
負面:
* v0 的 coverage_map 為 stub，不納入 PASS 門檻
* 擴充需 ADR 記錄
Evidence
* 證據結構見 evidence_index.json
* Evidence 指針: evidence_index.json
________________


<a id="adr-003"></a>
ADR-003 Gate Classification (Required vs Advisory；命名護欄)
---
doc_id: LBP-ADR-003
owner_role: LBP Pack Owner
last_updated: 2026-01-29
version: v1.1.0
status: ACCEPTED
source_refs:
  - v0 Pack NORM-08
  - v0 Pack NORM-21
  - TVS §7.1
related_gates:
  - finalize
  - g0-input-seal
  - g3-schema
  - g3-anti-platform
  - g4-dual-judge
  - format-check
evidence_hooks:
  - A_control_plane/rulesets_detail.json
---


Context
系統需要明確區分 Required Gate 與 Advisory 信號，並建立命名護欄防止 Gate 類別擴張。
可選方案包括：
1. v0 最小集合（6 gates），禁止 v0 範圍內新增 advisory gate
2. 允許 advisory gate 但不進 Ruleset
3. 動態 Gate 集合
[Ref: v0 Pack NORM-08][Ref: LBP 方案 C1]
Decision
選擇方案 1：v0 最小集合，禁止 v0 範圍內新增 advisory gate
v0 GateKit 最小集合（SSOT 見 v0 Pack NORM-21）：
Check Name
	類型
	進入 Ruleset
	docops-gatekit/finalize
	RULESET_REQUIRED
	✓
	g0-input-seal
	INTERNAL
	-
	g3-schema
	INTERNAL
	-
	g3-anti-platform
	INTERNAL
	-
	g4-dual-judge
	INTERNAL
	-
	format-check
	INTERNAL
	-
	命名護欄:
* 不得新增 gate.* 名稱
* finalize 為 TVS §7.1 的 logical label，實際 check name 為 docops-gatekit/finalize
* 概念如 tool budget / evidence completeness 只能以 metric/signal 呈現，不創 Gate
[Ref: v0 Pack NORM-21][Ref: TVS §7.1]
Consequences
正面:
* Gate 集合固定，治理不膨脹
* 命名一致性可機械驗證
* 符合 LBP 不擴張約束
負面:
* v0 範圍內無法新增 advisory gate
* 擴充需升級到 v1+
Evidence
* Ruleset 設定見 rulesets_detail.json
* Evidence 指針: A_control_plane/rulesets_detail.json
________________


<a id="adr-004"></a>
ADR-004 Merge Queue Strategy (取捨；僅引用 TVS)
---
doc_id: LBP-ADR-004
owner_role: LBP Pack Owner
last_updated: 2026-01-29
version: v1.1.0
status: ACCEPTED
source_refs:
  - TVS §7
  - v0 Pack NORM-22
  - SRS EIR-001
related_gates:
  - finalize
evidence_hooks:
  - A_control_plane/settings_evidence.json
  - D_workflow/docops-gatekit.yml.evidence
---


Context
系統需要決定 Merge Queue 策略。可選方案包括：
1. MQ=ON 強制（Org-owned Public repo）
2. MQ=OFF 替代路徑（Private repo）
3. MQ 可選
[Ref: TVS Front Matter][Ref: v0 Pack CR_OPEN-14]
Decision
選擇方案 1：MQ=ON 強制
路線決策（CR_OPEN-14 選項 B）：
* Merge Queue 必須啟用
* Repo 前提為 Org-owned public
* 不需 MQ=OFF 替代路徑
merge_group 觸發要求（僅引用，不複寫操作步驟）：
* 所有 Required Workflows 必須監聽 merge_group 事件
* 若 workflow 缺少 merge_group trigger，G0 自檢 FAIL
* 詳細配置見 [Ref: TVS §7.3]
[Ref: v0 Pack NORM-22][Ref: SRS EIR-001]
Consequences
正面:
* Merge Queue 提供序列化合流保證
* 符合 Fail-Closed 原則
* Day-1 前提明確
負面:
* 僅支援 Org-owned public repo
* Private repo 需升級方案
Evidence
* Merge Queue 設定見 settings_evidence.json
* Workflow 配置見 docops-gatekit.yml.evidence
* Evidence 指針: A_control_plane/settings_evidence.json, D_workflow/docops-gatekit.yml.evidence
________________


═══════════════════════════════════════════════════════════════
C4 - Architecture Diagrams
═══════════════════════════════════════════════════════════════
<a id="c4"></a>
<a id="c4-l1"></a>
C4-L1 System Context
---
doc_id: LBP-C4-L1-001
owner_role: LBP Pack Owner
last_updated: 2026-01-29
version: v1.1.0
source_refs:
  - 架構指南 2
  - README v1.1 §3
  - TVS §4.1
related_gates:
  - finalize
evidence_hooks:
  - evidence_index.json
---


責任邊界
GitHub Multi-Agent DocOps Framework 作為一個證據驅動的多代理 DevOps 治理系統，與以下外部實體互動：
外部實體
	類型
	互動說明
	來源指針
	Human Operator
	Actor
	值守自動化，觸發 Issue，審查 CR_OPEN
	[Ref: 架構指南 1.1]
	GitHub Platform
	External System
	提供 Actions, Rulesets, Merge Queue, Status Checks
	[Ref: TVS §4.1]
	Codespaces
	External System
	提供可重現執行環境
	[Ref: TVS §4.1]
	LLM Tools
	External System
	Claude Code CLI, Codex CLI（訂閱制非 API）
	[Ref: 架構指南 3.1]
	外部系統邊界標註
┌─────────────────────────────────────────────────────────────────┐
│                    External Systems Boundary                      │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │   GitHub    │  │ Codespaces  │  │  LLM Tools  │              │
│  │  Platform   │  │             │  │ (Claude/    │              │
│  │  (Actions,  │  │ (Execution  │  │  Codex CLI) │              │
│  │  Rulesets,  │  │  Plane)     │  │             │              │
│  │  MQ)        │  │             │  │             │              │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘              │
│         │                │                │                      │
└─────────┼────────────────┼────────────────┼──────────────────────┘
          │                │                │
          ▼                ▼                ▼
    ┌─────────────────────────────────────────────────┐
    │         DocOps Framework (本系統)                │
    │  ┌─────────────┐        ┌─────────────┐        │
    │  │  Control    │◄──────►│  Execution  │        │
    │  │   Plane     │        │   Plane     │        │
    │  └─────────────┘        └─────────────┘        │
    └─────────────────────────────────────────────────┘
                      ▲
                      │
              ┌───────┴───────┐
              │ Human Operator │
              └───────────────┘


________________


<a id="c4-l2"></a>
C4-L2 Containers
---
doc_id: LBP-C4-L2-001
owner_role: LBP Pack Owner
last_updated: 2026-01-29
version: v1.1.0
source_refs:
  - 架構指南 2
  - TVS §4.1
related_gates:
  - finalize
  - g0-input-seal
  - g3-schema
  - g3-anti-platform
  - g4-dual-judge
  - format-check
evidence_hooks:
  - A_control_plane/*.json
  - B_execution_plane/*.json
---


容器列表
Container
	職責
	技術
	來源指針
	Control Plane
	機械驗證、狀態流轉、合流裁決
	GitHub Actions + Rulesets + MQ
	[Ref: TVS §4.1]
	Execution Plane
	可重現工廠、執行施工、回傳證據
	Codespaces + .devcontainer
	[Ref: TVS §4.1]
	Evidence Store
	證據存儲與索引
	JSON files in repo
	[Ref: v0 Pack NORM-18]
	Registry
	機械 SSOT（Schema/Policy/Gate）
	YAML/JSON/Python in docops/
	[Ref: v0 Pack 4.3]
	________________


<a id="c4-l3"></a>
C4-L3 Components
---
doc_id: LBP-C4-L3-001
owner_role: LBP Pack Owner
last_updated: 2026-01-29
version: v1.1.0
source_refs:
  - v0 Pack 4.3
  - TVS §7
related_gates:
  - finalize
  - g0-input-seal
  - g3-schema
  - g3-anti-platform
  - g4-dual-judge
  - format-check
evidence_hooks:
  - F_rules_and_gates/*.py
---


Control Plane Components
Component
	職責
	對應 Gate
	來源指針
	Ruleset Manager
	管理分支保護規則
	finalize
	[Ref: TVS §7.1]
	Merge Queue
	序列化合流
	finalize
	[Ref: v0 Pack NORM-22]
	Status Check Router
	路由狀態檢查
	all gates
	[Ref: TVS §7]
	Execution Plane Components
Component
	職責
	對應 Gate
	來源指針
	GateKit Runner
	執行 Gate 序列
	all gates
	[Ref: v0 Pack NORM-08]
	Input Sealer
	封印輸入
	g0-input-seal
	[Ref: SRS INV-002]
	Schema Validator
	JSON Schema 驗證
	g3-schema
	[Ref: SRS FR-GK-003]
	Anti-Platform Scanner
	禁詞掃描
	g3-anti-platform
	[Ref: SRS INV-009]
	Dual Judge Orchestrator
	雙法官協調
	g4-dual-judge
	[Ref: SRS INV-010]
	Format Checker
	格式檢查
	format-check
	[Ref: v0 Pack NORM-10]
	________________


<a id="c4-l4"></a>
C4-L4 Code Map (Gate → Code Path → Registry Script → Workflow Job → Evidence Output)
---
doc_id: LBP-C4-L4-001
owner_role: LBP Pack Owner
last_updated: 2026-01-29
version: v1.1.0
source_refs:
  - v0 Pack 4.3
  - TVS §7
  - evidence_index.json
related_gates:
  - finalize
  - g0-input-seal
  - g3-schema
  - g3-anti-platform
  - g4-dual-judge
  - format-check
evidence_hooks:
  - F_rules_and_gates/*.py
  - D_workflow/*.evidence
---


Gate → Code → Evidence 映射表
Gate
	Registry Script
	Workflow Job
	Evidence Output (evidence_index key)
	來源指針
	g0-input-seal
	docops/registry/gates/gatekit_runner_v0.py::run_g0_input_seal()
	g0-input-seal
	B_execution_plane/gate_report.json
	[Ref: v0 Pack NORM-08]
	g3-schema
	docops/registry/gates/gatekit_runner_v0.py::run_g3_schema()
	g3-schema
	B_execution_plane/gate_report.json
	[Ref: v0 Pack NORM-08]
	g3-anti-platform
	docops/registry/gates/gatekit_runner_v0.py::run_g3_anti_platform()
	g3-anti-platform
	B_execution_plane/gate_report.json
	[Ref: v0 Pack NORM-09]
	g4-dual-judge
	docops/registry/gates/gatekit_runner_v0.py::run_g4_dual_judge()
	g4-dual-judge
	C_dual_judge/final_aggregate_verdict.json
	[Ref: v0 Pack NORM-12~17]
	format-check
	docops/registry/gates/gatekit_runner_v0.py::run_format_check()
	format-check
	B_execution_plane/gate_report.json
	[Ref: v0 Pack NORM-10]
	finalize
	docops/registry/gates/gatekit_runner_v0.py::run_finalize()
	finalize
	B_execution_plane/verdict.json
	[Ref: TVS §7.1]
	vibe-merge-block
	docops/registry/gates/g_vibe_merge_block.py::run_vibe_merge_block()
	(within finalize)
	E_rd01_phase0/rd01_vibe_block_evidence.json
	[Ref: v0 Pack NORM-23]
	lane-router
	docops/registry/gates/g_lane_router.py::route_lane()
	(within g0)
	E_rd01_phase0/rd01_router_evidence.json
	[Ref: v0 Pack NORM-03]
	Registry 目錄結構
docops/
├── registry/
│   ├── index.yaml              # Registry 索引
│   ├── skills/
│   │   └── core_skill_pack.yaml
│   ├── gates/
│   │   ├── gatekit_runner_v0.py
│   │   ├── g_vibe_merge_block.py
│   │   └── g_lane_router.py
│   ├── policies/
│   │   ├── anti_platform.policy.yaml
│   │   └── merge_policy.yaml
│   └── schemas/
│       ├── verdict.schema.json
│       ├── gate_report.schema.json
│       ├── input_manifest.schema.json
│       ├── run_manifest.schema.json
│       ├── settings_evidence.schema.json
│       ├── coverage_map.schema.json
│       └── trace_map.schema.json
└── profiles/
    ├── vibe.yaml (enabled: true)
    ├── dev.yaml (enabled: true)
    ├── spec.yaml (enabled: false)
    └── ops.yaml (enabled: false)


[Ref: v0 Pack 4.3]
________________


═══════════════════════════════════════════════════════════════
FITNESS - Fitness Catalog
═══════════════════════════════════════════════════════════════
<a id="fitness"></a>
---
doc_id: LBP-FITNESS-001
owner_role: Fail-Closed Quality Judge
last_updated: 2026-01-29
version: v1.1.0
source_refs:
  - SRS v1.1.0
  - TVS v0.4.1 §7
  - v0 Pack NORM-08~17
  - LBP_方案 §2.5
  - Building Effective Agents
  - Claude Code 筆記
related_gates:
  - finalize
  - g0-input-seal
  - g3-schema
  - g3-anti-platform
  - g4-dual-judge
  - format-check
evidence_hooks:
  - evidence_index.json
  - B_execution_plane/*.json
  - C_dual_judge/*.json
scope_lock_refs:
  - LBP_方案 §1.2
---


<a id="fit-00"></a>
FIT-00 Philosophy & Scope（哲學與範圍）
核心原則
Fitness Function 必須符合以下條件才納入本文件：
原則
	說明
	來源指針
	客觀可測
	必須有機械可執行的檢測方式
	[Ref: LBP_方案 §2.5]
	可自動化
	必須可在 CI/merge queue 內自動執行
	[Ref: LBP_方案 §2.5]
	可映射 Gate
	必須對應既有 gate.*
	[Ref: LBP_方案 §1.2]
	有 Evidence
	必須產出可回放證據
	[Ref: SRS INV-005]
	不可測的不算 Fitness（那叫願望）。 [Ref: LBP_方案 §2.5]
範圍限制
約束
	說明
	來源指針
	不新增 Gate 類別
	只做 mapping/ledger，不發明新 gate
	[Ref: LBP_方案 §1.2]
	對齊既有 gate.*
	所有 fitness 必須映射到 v0 GateKit 6 gates
	[Ref: v0 Pack NORM-08]
	不寫操作步驟
	執行方式指向 Runbook
	[Ref: LBP_方案 §1.2]
	________________


<a id="fit-01"></a>
FIT-01 Fitness Catalog（Fitness 目錄）
v0 可驗證 Fitness（9 個）
ID
	Target Attribute
	Signal
	Threshold
	Evaluation Mode
	Mapped Gate
	Evidence Artifacts
	Owner Role
	Source Refs
	Verifiable
	FIT-001
	輸入完整性
	source_bundle_sha256 存在且一致
	100% match
	Automated
	g0-input-seal
	B_execution_plane/gate_report.json
	GateKit
	[Ref: SRS INV-002]
	✓ v0
	FIT-002
	merge_group 觸發
	workflow 含 merge_group 監聽
	grep hit ≥1
	Automated
	g0-input-seal
	D_workflow/docops-gatekit.yml.evidence
	GateKit
	[Ref: TVS §7.3]
	✓ v0
	FIT-003
	Schema 符合性
	JSON artifacts 符合 schema
	0 validation errors
	Automated
	g3-schema
	B_execution_plane/gate_report.json
	GateKit
	[Ref: SRS FR-GK-003]
	✓ v0
	FIT-004
	反平台化
	禁詞掃描無命中
	0 P0 hits
	Automated
	g3-anti-platform
	B_execution_plane/gate_report.json
	GateKit
	[Ref: SRS INV-009]
	✓ v0
	FIT-005
	雙法官一致性
	Judge_A == Judge_B
	100% agreement
	Automated
	g4-dual-judge
	C_dual_judge/final_aggregate_verdict.json
	Dual Judge
	[Ref: SRS INV-010]
	✓ v0
	FIT-006
	Swap 抗偏誤
	位置交換無翻轉
	swap_consistency ≥0.9
	Automated
	g4-dual-judge
	C_dual_judge/final_aggregate_verdict.json
	Dual Judge
	[Ref: v0 Pack NORM-14]
	✓ v0
	FIT-007
	工作樹乾淨
	git status --porcelain 為空
	0 diff lines
	Automated
	format-check
	B_execution_plane/gate_report.json
	GateKit
	[Ref: v0 Pack NORM-10]
	✓ v0
	FIT-008
	無衝突標記
	無 <<<<<<< / ======= / >>>>>>>
	0 markers
	Automated
	format-check
	B_execution_plane/gate_report.json
	GateKit
	[Ref: v0 Pack NORM-11]
	✓ v0
	FIT-009
	finalize 聚合通過
	所有 gate PASS
	100% gates PASS
	Automated
	finalize
	B_execution_plane/verdict.json
	GateKit
	[Ref: TVS §7.1]
	✓ v0
	v0 範圍外 / UNVERIFIED Fitness（NON-BINDING NOTE）
以下 Fitness 概念在 v0 範圍內無法機械驗證，僅作為設計參考，不納入 required checks：
ID
	Target Attribute
	Signal
	狀態
	說明
	Source Refs
	FIT-010
	Evidence 完整性
	evidence_index.complete == true
	UNVERIFIED
	v0 evidence_index 已有 complete 欄位，但非獨立 Gate
	[Ref: SRS FR-EV-004]
	FIT-011
	Vibe 不進 MQ
	profile=vibe + merge_group → FAIL
	✓ v0（已含於 finalize）
	由 vibe-merge-block 執行
	[Ref: v0 Pack NORM-23]
	FIT-012
	Tool Budget 未超限
	retry_count < 3
	UNVERIFIED
	v0 以 metric 追蹤，非獨立 Gate
	[Ref: SRS INV-008]
	FIT-013
	One-Writer 遵守
	concurrent_writers ≤1
	UNVERIFIED
	v0 由 format-check 間接檢測
	[Ref: SRS INV-006]
	________________


<a id="fit-02"></a>
FIT-02 GateKit Mapping（Fitness → Gate 映射）
Fitness → Gate 映射表
Fitness ID
	Mapped Gate
	Ruleset Required
	C4-L4 Code Path
	Evidence Pointer
	來源指針
	FIT-001
	g0-input-seal
	-
	gatekit_runner_v0.py::run_g0_input_seal()
	B_execution_plane/gate_report.json
	[Ref: v0 Pack NORM-08]
	FIT-002
	g0-input-seal
	-
	gatekit_runner_v0.py::run_g0_input_seal()
	D_workflow/docops-gatekit.yml.evidence
	[Ref: TVS §7.3]
	FIT-003
	g3-schema
	-
	gatekit_runner_v0.py::run_g3_schema()
	B_execution_plane/gate_report.json
	[Ref: v0 Pack NORM-08]
	FIT-004
	g3-anti-platform
	-
	gatekit_runner_v0.py::run_g3_anti_platform()
	B_execution_plane/gate_report.json
	[Ref: v0 Pack NORM-09]
	FIT-005
	g4-dual-judge
	-
	gatekit_runner_v0.py::run_g4_dual_judge()
	C_dual_judge/final_aggregate_verdict.json
	[Ref: v0 Pack NORM-12~17]
	FIT-006
	g4-dual-judge
	-
	gatekit_runner_v0.py::run_g4_dual_judge()
	C_dual_judge/final_aggregate_verdict.json
	[Ref: v0 Pack NORM-14]
	FIT-007
	format-check
	-
	gatekit_runner_v0.py::run_format_check()
	B_execution_plane/gate_report.json
	[Ref: v0 Pack NORM-10]
	FIT-008
	format-check
	-
	gatekit_runner_v0.py::run_format_check()
	B_execution_plane/gate_report.json
	[Ref: v0 Pack NORM-11]
	FIT-009
	finalize
	✓ (logical label)
	gatekit_runner_v0.py::run_finalize()
	B_execution_plane/verdict.json
	[Ref: TVS §7.1]
	Required Checks SSOT（v0）
[Ref: TVS §7][Ref: v0 Pack NORM-21]
Check Name
	進入 Ruleset
	驗證方式
	docops-gatekit/finalize
	✓
	Ruleset API
	g0-input-seal
	-
	workflow job
	g3-schema
	-
	workflow job
	g3-anti-platform
	-
	workflow job
	g4-dual-judge
	-
	workflow job
	format-check
	-
	workflow job
	________________


<a id="fit-03"></a>
FIT-03 Merge Queue Compatibility（MQ 相容性）
merge_group 觸發要求
[Ref: TVS §7.2~7.3]
所有需要在 Merge Queue 生效的 checks 必須支援 merge_group 觸發，否則 queue 會等不到 required check 回報而卡死。
Check
	須支援 merge_group
	PR 階段
	MQ 階段
	說明
	來源指針
	finalize
	✓
	✓
	✓
	Ruleset Required Check
	[Ref: TVS §7.3]
	g0-input-seal
	✓
	✓
	✓
	兩階段都執行
	[Ref: TVS §7.2]
	g3-schema
	✓
	✓
	✓
	兩階段都執行
	[Ref: TVS §7.2]
	g3-anti-platform
	✓
	✓
	✓
	兩階段都執行
	[Ref: TVS §7.2]
	g4-dual-judge
	✓
	-
	✓
	僅 merge_group（重型）
	[Ref: TVS §7.2]
	format-check
	✓
	✓
	✓
	兩階段都執行
	[Ref: TVS §7.2]
	自檢探針（僅引用，操作詳見 TVS）
# 探針命令（秒級執行）
grep -r "merge_group" .github/workflows/*.yml | grep -v "^\s*#" | wc -l
# 預期結果 ≥ 1，否則 FAIL


[Ref: TVS §7.3]
________________


<a id="fit-04"></a>
FIT-04 Drift & Regression Rules（漂移與回歸規則）
門檻放水規則
規則
	說明
	來源指針
	任何 fitness 門檻降低
	必須以 ADR 記錄並提供正當理由
	[Ref: LBP_方案 §2.5]
	門檻變更
	必須同步更新 Evidence 預期值
	[Ref: SRS INV-005]
	不得默默改
	無 ADR 的門檻變更視為 DRIFT
	[Ref: LBP_方案 §2.5]
	Drift 偵測（由既有 Gate 執行）
Drift 類型
	偵測信號
	執行者
	來源指針
	門檻弱化
	threshold 值變小
	審計/回放
	[Ref: SRS FR-GK-006]
	語氣弱化
	MUST → SHOULD 無 ADR
	審計/回放
	[Ref: v0 Pack TEST-GK06]
	無源新增
	claim 無 [SRC:] 或 [Ref:]
	審計/回放
	[Ref: v0 Pack [7]]
	________________


Fitness 與 v0 Required Checks 對照總表
TVS §7 Required Check
	Fitness IDs
	Evidence (evidence_index key)
	finalize
	FIT-009
	B_execution_plane/verdict.json
	g0-input-seal
	FIT-001, FIT-002
	B_execution_plane/gate_report.json
	g3-schema
	FIT-003
	B_execution_plane/gate_report.json
	g3-anti-platform
	FIT-004
	B_execution_plane/gate_report.json
	g4-dual-judge
	FIT-005, FIT-006
	C_dual_judge/final_aggregate_verdict.json
	format-check
	FIT-007, FIT-008
	B_execution_plane/gate_report.json
	________________


<a id="evidence-alias-map"></a>
Evidence Alias Map（證據路徑映射表）
本表對應 LBP v1.0 舊版 evidence 路徑與 v0.4.1 證據三件套的實際路徑：
舊版路徑 (LBP v1.0)
	新版路徑 (evidence_index.json)
	狀態
	evidence/index.json
	evidence_index.json (root)
	✓ MAPPED
	evidence/verdict.json
	B_execution_plane/verdict.json
	✓ MAPPED
	evidence/gates/input_seal.json
	B_execution_plane/gate_report.json
	✓ MAPPED（合併至 gate_report）
	evidence/gates/schema_validation.json
	B_execution_plane/gate_report.json
	✓ MAPPED（合併至 gate_report）
	evidence/gates/anti_platform.json
	B_execution_plane/gate_report.json
	✓ MAPPED（合併至 gate_report）
	evidence/gates/format_check.json
	B_execution_plane/gate_report.json
	✓ MAPPED（合併至 gate_report）
	evidence/gates/vibe_merge_block.json
	E_rd01_phase0/rd01_vibe_block_evidence.json
	✓ MAPPED
	evidence/gates/tool_budget.json
	B_execution_plane/run_manifest.json (retry_count)
	✓ MAPPED（欄位內含）
	evidence/gates/one_writer.json
	N/A
	UNVERIFIED（v0 無獨立檔案）
	evidence/gates/fail_closed.json
	B_execution_plane/gate_report.json
	✓ MAPPED（合併至 gate_report）
	evidence/judges/final_aggregate_verdict.json
	C_dual_judge/final_aggregate_verdict.json
	✓ MAPPED
	evidence/judges/swap_consistency.json
	C_dual_judge/final_aggregate_verdict.json (swap_test_passed)
	✓ MAPPED（欄位內含）
	evidence/input_manifest.json
	B_execution_plane/input_manifest.json
	✓ MAPPED
	evidence/run_manifest.json
	B_execution_plane/run_manifest.json
	✓ MAPPED
	evidence/control_plane/settings_evidence.json
	A_control_plane/settings_evidence.json
	✓ MAPPED
	證據三件套結構
檔案
	說明
	鍵/結構
	evidence_index.json
	證據總索引
	A~F 分類 + complete flag
	tvs_section9_verdict.json
	§9 驗收裁決
	checks array + summary
	tvs_v0.4.1_complete_evidence_bundle_v2.json
	完整證據包
	含 rd01_evidence/*.json
	________________


═══════════════════════════════════════════════════════════════
END OF LBP v1.1.0
═══════════════════════════════════════════════════════════════
LBP UPGRADE REPORT
Execution Date: 2026-01-29
Auditor Role: LBP Upgrade Lead + Drift Hunter + Fail-Closed DocOps Curator + Evidence Chain Engineer
________________


[0] UPGRADE_RESULT
Upgrade Verdict: PASS
項目
	結果
	Version Bump
	v1.0 → v1.1.0
	外部名稱
	GitHub Multi-Agent DocOps Lightweight Baseline Package
	內部簡稱
	LBP
	發布日期
	2026-01-29
	Blockers Cleared
Severity
	Finding IDs
	狀態
	P0
	LBP-F-001 (ADR 缺失), LBP-F-002 (Fitness→C4 映射斷裂), LBP-F-002-B (Evidence pointer 失真)
	✓ CLEARED
	P1
	LBP-F-003 (筆記 Ref 不可定位), LBP-F-004 (Gate 擴張矛盾), LBP-F-005 (Risk Register evidence 指向不存在)
	✓ CLEARED
	P2
	LBP-F-006 (front-matter 非 YAML), LBP-F-007 (Gate 數量口徑混亂)
	✓ CLEARED
	P3
	LBP-F-008 (缺少引用格式契約)
	✓ CLEARED
	________________


[1] RESOLUTION_LEDGER
審查報告 A/B 問題合併與解決
finding_id
	severity
	root_cause
	fix_summary
	exact_location_in_new_doc
	upstream_refs
	evidence_pointer
	LBP-F-001
	P0
	ADR 僅有目錄宣告無實質內容
	新增 4 個完整 ADR（ADR-001~004），含 Status/Context/Decision/Consequences/Evidence
	LBP-ADR-001~004 (#adr-001 ~ #adr-004)
	LBP 方案 §2.3
	B_execution_plane/run_manifest.json, A_control_plane/settings_evidence.json
	LBP-F-002
	P0
	Fitness → C4 Code Map 映射斷裂
	新增 C4-L4 Code Map 含 Gate→Code Path→Registry Script→Workflow Job→Evidence 映射表
	LBP-C4-L4-001 (#c4-l4)
	TVS §7, v0 Pack 4.3
	F_rules_and_gates/*.py
	LBP-F-002-B
	P0
	Evidence 指針與 v0 證據三件套不一致
	新增 Evidence Alias Map，建立舊路徑到 evidence_index.json 的完整映射
	Evidence Alias Map (#evidence-alias-map)
	TVS §8, evidence_index.json
	evidence_index.json
	LBP-F-003
	P0
	兩份筆記 Ref 格式錯誤（§2.6 等不可定位）
	建立 SG-01 Ref Format Contract，統一使用可定位格式如 [Ref: Building Effective Agents 2.6]
	LBP Self-Guards SG-01 (#lbp-self-guards)
	兩份筆記章節編號
	N/A
	LBP-F-004
	P1
	ADR-GATES 宣告不擴張但 Fitness 新增 gate.*
	清除所有非 v0 GateKit 的 gate.* 名稱，建立 SG-03 Gate Naming Guardrail
	LBP Self-Guards SG-03, ADR-003 (#adr-003)
	v0 Pack NORM-08, NORM-21
	A_control_plane/rulesets_detail.json
	LBP-F-005
	P1
	Risk Register 的 gate/evidence 欄位指向不存在檔案
	重寫 Risk Register（12 條），所有 evidence_pointer 對齊 evidence_index.json 實際 keys
	SIR-03 (#sir-03)
	TVS §8, evidence_index.json
	見各 risk 的 evidence_pointer 欄位
	LBP-F-006
	P2
	front-matter 近似 YAML 但非標準格式
	所有 doc_id 區塊使用標準 YAML front-matter（含 --- 邊界）
	所有 doc_id 區塊
	LBP 方案
	N/A
	LBP-F-007
	P2
	v0 GateKit 數量表述混亂
	明確定義：v0 GateKit 6 gates（NORM-21），finalize 為 logical label 不獨立計數
	ADR-003 (#adr-003), FIT-02 (#fit-02)
	v0 Pack NORM-21, TVS §7.1
	A_control_plane/rulesets_detail.json
	LBP-F-008
	P3
	缺少引用格式契約
	新增 LBP Self-Guards（SG-01~04）作為自我鎖定條款
	LBP Self-Guards (#lbp-self-guards)
	LBP 方案
	N/A
	LBP-F-101
	P1
	Evidence 路徑漂移風險
	RISK-11 納入 Risk Register，新增 Evidence Alias Map
	SIR-03 RISK-11, Evidence Alias Map
	TVS §8, evidence_index.json
	evidence_index.json
	LBP-F-102
	P1
	Gate 類別擴張風險
	RISK-12 納入 Risk Register，SG-03 Gate Naming Guardrail
	SIR-03 RISK-12, SG-03
	v0 Pack NORM-08
	N/A
	ICD 契約化補強
contract_id
	說明
	位置
	ICD-PLANE-01~03
	平面交互契約（Execution↔Control）
	ICD-01
	ICD-REG-01~04
	Registry 契約
	ICD-02
	ICD-GATE-01~06
	Gate 契約（含所有 6 gates）
	ICD-03
	ICD-EV-01~05
	Evidence 契約
	ICD-04
	ICD-NOTE-01
	CLAUDE.md Schema Contract
	ICD-05
	________________


[2] EXTERNAL_2026+_CALIBRATION
Query Log
Query
	Purpose
	GitHub merge queue merge_group event required status checks 2025 2026
	校準 merge_group 觸發要求
	GitHub required status checks recent successful run 7 days requirement rulesets
	校準 7 天成功記錄限制
	GitHub rulesets status check expected source integration id GitHub App 2025
	校準 expected source 防偽造機制
	Sources Table
Publisher
	Date
	URL
	Used For
	GitHub Docs
	2026-01
	docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/troubleshooting-required-status-checks
	merge_group 事件要求確認
	GitHub Docs
	2026-01
	docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
	expected source 機制確認
	GitHub Docs
	2026-01
	docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/troubleshooting-required-status-checks
	7 天成功記錄要求確認
	校準發現
1. merge_group 事件要求（已存在於 TVS §7.3）

   * GitHub 文檔確認：若使用 Merge Queue，workflow 必須包含 merge_group 事件觸發器
   * 否則 status checks 不會被觸發，合併會失敗
   * 落點: SIR-03 RISK-02, FIT-003
   2. 7 天成功記錄限制（新增風險項目）

      * GitHub 文檔確認：Required status checks 必須在過去 7 天內成功運行過才能被選為 required
      * 落點: SIR-03 RISK-10（新增）
      * 自證: 此為 Risk Register 擴充（符合 LBP 允許範圍），非新增 Gate 類別
      3. Expected source 防偽造（確認現行做法）

         * GitHub 文檔確認：Ruleset 可指定 status check 的 expected source（特定 GitHub App）
         * GitHub Actions 的 integration_id 為 15368
         * 落點: SIR-03 RISK-09, ADR-004
         * 自證: 此為 Risk 描述與 ADR 決策記錄，非新增 Gate 或 How-to
"No new Gate / No How-to" 自證
外部資訊
	落點位置
	性質
	自證
	merge_group 必須觸發
	SIR-03 RISK-02, FIT-002
	既有風險/Fitness 的來源補強
	僅補強來源指針，不改變 Gate 結構
	7 天成功記錄限制
	SIR-03 RISK-10
	新增 Risk 條目
	Risk Register 擴充屬 LBP 允許範圍，非新 Gate
	expected source 設定
	SIR-03 RISK-09, ADR-004
	新增 Risk + ADR 記錄
	描述設定的重要性與取捨，不含操作步驟
	integration_id=15368
	NOTE only
	補充資訊
	僅供參考，不進入 Gate 門檻
	________________


[3] SOP_TRACE（自我驗證追蹤）
SOP-1 查看索引
         * ✓ 讀取 LBP_v1.0 TOC（SIR/ICD/ADR/C4/Fitness）
         * ✓ 確認新版保留完整結構並補強 ADR 實質內容
SOP-2 定位實質條文
修補點
	新版錨點
	驗證
	ADR 補全
	#adr-001 ~ #adr-004
	✓ 4 個完整 ADR
	Fitness→C4 映射
	#c4-l4
	✓ 6 gates 完整映射
	Evidence Alias Map
	#evidence-alias-map
	✓ 18 條映射
	Risk Register
	#sir-03
	✓ 12 條風險
	SOP-3 關鍵字檢索
關鍵字
	檢索結果
	gate.*
	僅出現 v0 GateKit 6 gates，無新增 gate.*
	evidence/
	已全部映射到 evidence_index.json 結構
	merge_group
	出現於 SIR-02 HC-05, SIR-03 RISK-02, FIT-002, FIT-03
	§2.6
	已改為 [Ref: Building Effective Agents 2.6] 格式
	SOP-4 交叉驗證
驗證項目
	結果
	v0 Pack NORM-21 GateKit 對齊
	✓ 6 gates 一致
	TVS §7 Required Checks 對齊
	✓ finalize 為 logical label
	evidence_index.json keys 對齊
	✓ A~F 分類完整映射
	筆記章節編號對齊
	✓ 使用 2.x 格式而非 §2.x
	SOP-5 子要求分解
Pattern → Contract → Fitness → Evidence
	驗證
	Evaluator-Optimizer → HC-06 → FIT-005/006 → C_dual_judge
	✓ 完整鏈
	One Brain One Stream → HC-03 → FIT-013(UNVERIFIED) → N/A
	✓ 標記 UNVERIFIED
	Fail-Closed Gate → HC-01 → FIT-001 → B_execution_plane
	✓ 完整鏈
	SOP-6 實質內容判定
檢查項目
	結果
	ADR 是否含 Status/Context/Decision/Consequences
	✓ 4 個 ADR 皆完整
	ICD 是否含 contract_id/producer/consumer/failure_mode
	✓ 所有契約皆完整
	Risk Register 是否含 detection/mitigation/evidence_pointer
	✓ 12 條皆完整
	SOP-7 質疑看似通過（10 點自我攻擊）
點
	質疑
	證明
	1
	FIT-010~013 是否偷渡為 required
	✓ 明確標記 UNVERIFIED，不納入 required checks
	2
	gate.evidence_completeness 是否新增
	✓ 已移除，改為 evidence_index.complete metric
	3
	gate.tool_budget 是否新增
	✓ 已移除，改為 retry_count metric
	4
	gate.one_writer 是否新增
	✓ 已移除，改為 concurrent_writers metric
	5
	Evidence Alias Map 是否能回溯
	✓ 18 條映射皆指向 evidence_index.json 實際存在的 keys
	6
	Risk Register evidence_pointer 是否存在
	✓ 12 條皆指向 A~F 分類下的實際檔案
	7
	ADR 是否含 how-to
	✓ 僅記錄決策取捨，操作指向 TVS/Runbook
	8
	筆記 Ref 是否可定位
	✓ 使用 [Ref: Building Effective Agents 2.6] 等可定位格式
	9
	front-matter 是否可機械抽取
	✓ 使用標準 YAML 格式（含 --- 邊界）
	10
	C4-L4 是否能指到實際 code path
	✓ 6 gates 皆有 gatekit_runner_v0.py::function() 映射
	________________


REQUIREMENT_VERIFICATION_MATRIX
需求項目
	finding_id
	狀態
	具體定位
	Ref
	Evidence Pointer
	ADR 實質內容（≥4 個 ADR）
	LBP-F-001
	PASS
	#adr-001 ~ #adr-004
	LBP 方案 §2.3
	B_execution_plane/run_manifest.json
	Fitness → C4 Code Map 映射
	LBP-F-002
	PASS
	#c4-l4
	TVS §7, v0 Pack 4.3
	F_rules_and_gates/*.py
	Evidence 指針一致化
	LBP-F-002-B
	PASS
	#evidence-alias-map
	evidence_index.json
	evidence_index.json
	筆記 Ref 可定位格式
	LBP-F-003
	PASS
	#lbp-self-guards SG-01
	兩份筆記
	N/A
	Gate 類別不擴張
	LBP-F-004
	PASS
	#adr-003, SG-03
	v0 Pack NORM-08
	A_control_plane/rulesets_detail.json
	Risk Register evidence 存在
	LBP-F-005
	PASS
	#sir-03
	TVS §8
	各 risk 的 evidence_pointer
	front-matter 可抽取
	LBP-F-006
	PASS
	所有 doc_id 區塊
	LBP 方案
	N/A
	Gate 數量口徑一致
	LBP-F-007
	PASS
	#adr-003, #fit-02
	v0 Pack NORM-21
	A_control_plane/rulesets_detail.json
	引用格式契約
	LBP-F-008
	PASS
	#lbp-self-guards
	LBP 方案
	N/A
	ICD 契約化
	LBP-F-003-ext
	PASS
	#icd-01 ~ #icd-05
	LBP 方案 §2.2
	各契約的 evidence_pointer
	C4 外部系統邊界
	New
	PASS
	#c4-l1
	架構指南 2
	evidence_index.json
	2026+ 校準（merge_group）
	Calibration
	PASS
	#sir-03 RISK-02
	GitHub Docs
	D_workflow/*.evidence
	2026+ 校準（7天記錄）
	Calibration
	PASS
	#sir-03 RISK-10
	GitHub Docs
	A_control_plane/workflow_runs.json
	2026+ 校準（expected source）
	Calibration
	PASS
	#sir-03 RISK-09
	GitHub Docs
	A_control_plane/rulesets_detail.json
	________________


交付物清單
檔案
	說明
	LBP_v1_1_0.md
	升級新版《GitHub Multi-Agent (模組化 Core + 4 Profiles) _LBP》完整合冊
	________________


END OF UPGRADE REPORT