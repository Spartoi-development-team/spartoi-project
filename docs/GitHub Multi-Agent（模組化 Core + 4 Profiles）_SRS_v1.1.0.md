GitHub Multi-Agent（模組化 Core + 4 Profiles）_SRS_v1.1.0
外部正式名：GitHub Multi-Agent（模組化 Core + 4 Profiles）Software Requirements Specification
內部簡稱：SRS / GMA-SRS
版本號：v1.1.0
日期：2026-01-29
升級自：v1.0.0
________________


導讀（AI/LLM 檢索指引）— 具強制力
檢索策略（MUST 遵守）：
1. 查覆蓋 → 先看 §11 T1 Coverage Ledger，確認 v1.1 條款對應哪條 REQ，再回到該 REQ 的 Trace.ReqRef 確認實質回指。
2. 查驗收 → 先看 §10 驗收主線，再查對應 REQ 的 Verification 三件套。
3. 查名詞 → 先看 §1.6 Keyword Alias Map，擴展別名後再全文檢索。
4. 查證據路徑 → 先看 §11 T5 Evidence Pointer Index，確認 canonical 路徑。
5. 禁止僅憑宣告判 PASS：T1 映射必須由 REQ.Trace.ReqRef 實質支撐，否則視為未覆蓋。
________________


目錄（Table of Contents）
1. Document Control（文件控制）
   * 1.1 文件資訊
   * 1.2 Source Manifest（來源清單）
   * 1.3 Scope Lock（範圍鎖定）
   * 1.4 Counting Budget（需求計數預算）
   * 1.5 術語表
   * 1.6 Keyword Alias Map（關鍵字別名映射）
   * 1.7 Document Structure Rule（章節結構規則）
   * 1.8 RAG-Triad 自檢準則
   * 1.9 Audit-Closure Ledger（閉環總帳）
2. Purpose & Scope（目的與範圍）
3. System Context & Boundary（系統邊界與上下文）
4. Actors & Roles（角色與權責）
5. Invariants（MUST-HOLD 原則）
6. Functional Requirements（功能需求）
7. External Interface Requirements（外部介面需求）
8. Non-Functional Requirements（NFR）
9. Evidence & Artifacts（證據與工件）
10. Verification & Acceptance（驗證與驗收）
11. Traceability（追溯）
________________


Node Index（GraphRAG 概念節點索引）
#
	概念節點
	錨點
	說明
	1
	Fail-Closed
	INV-001
	預設阻斷原則
	2
	Evidence Bundle
	§9
	可回放證據包
	3
	Merge Queue
	EIR-001
	GitHub 序列化合流
	4
	merge_group
	EIR-001
	觸發事件
	5
	Dual Judge
	INV-010
	雙法官協議
	6
	One-Writer
	INV-006
	單寫入者規則
	7
	Tool Budget
	INV-008
	工具預算與停止線
	8
	Input Seal
	INV-002
	輸入封印 SHA256
	9
	GateKit
	§6.6
	機械閘門套件
	10
	Anti-Platforming
	INV-009
	反平台化 Gate
	11
	Swap Test
	FR-JD-003
	A/B 交換測試
	12
	Trace Map
	INV-004
	追溯地圖
	13
	Coverage Gate
	FR-GK-002
	覆蓋率閘門
	14
	Required Checks
	EIR-002
	必要狀態檢查
	15
	Attestations
	EIR-004
	工件證明
	16
	Vibe Lane
	FR-PF-001
	探索原型泳道
	17
	Promotion
	FR-PROM-001
	晉升機制
	18
	Registry
	FR-SK-001
	Skills/Hooks 註冊表
	19
	Bootstrap
	FR-MEM-003
	確定性開機
	20
	Verifier Report
	FR-EV-001
	驗證者報告
	21
	Negative Test
	INV-007
	負向測試
	22
	CR_OPEN
	§10.5
	未決狀態
	23
	CLAUDE.md
	FR-MEM-004
	Agent 行為準則
	24
	Stopline
	INV-008
	停止條件
	25
	devcontainer
	EIR-003
	環境容器配置
	________________


1. Document Control（文件控制）
1.1 文件資訊
項目
	內容
	文件名稱
	GitHub Multi-Agent（模組化 Core + 4 Profiles）軟體需求規格書
	版本
	v1.1.0
	日期
	2026-01-29
	作者角色
	SRS Upgrade Owner + Audit-Closure Ledger Engineer + Drift Hunter + Fail-Closed Quality Judge + Minimalist Patch Integrator
	權威等級
	What/Why 最高層需求 SSOT（不含 How-to 操作步驟）
	Diátaxis 類型
	Reference / Contract（非 Tutorial / How-to）
	升級來源
	SRS v1.0.0 + 審查報告 A + 審查報告 B
	1.2 Source Manifest（來源清單）
DocName
	Version/Tag
	取得狀態
	引用範圍
	需求書升級為SRS_方案
	-
	FOUND
	A~E 節全量
	兩份筆記導入SRS_方案
	-
	FOUND
	1~6 節全量、Phase 0 REQ 清單
	GitHub Multi-Agent 架構指南
	-
	FOUND
	§1~§13 全量（含 13.4.2-D 補強）
	需求書 v1.1
	v1.1
	FOUND
	§0~§18 全量條款
	Claude Code 卓越編程配置全攻略_筆記
	-
	FOUND
	§1~§5 全量
	Building Effective Agents指南_筆記
	-
	FOUND
	§1~§7 全量
	GitHub Multi-Agent v0 最小三件套
	v0.3.0
	FOUND
	NORM-01~NORM-25、Runbook、Registry
	GitHub Multi-Agent Thin Vertical Slice
	v0.4.1
	FOUND
	§1~§12 全量
	evidence_index.json
	tvs-20260128-001
	FOUND
	A~F 分類全量
	tvs_section9_verdict.json
	v0.4.1
	FOUND
	§9 Acceptance Criteria
	tvs_v0.4.1_complete_evidence_bundle_v2.json
	v2
	FOUND
	完整證據包
	SRS v1.0.0
	v1.0.0
	FOUND
	全文
	SRS v1.0.0 審查報告 A
	2026-01-29
	FOUND
	[0]~[10] 全量 Findings
	SRS v1.0.0 審查報告 B
	2026-01-29
	FOUND
	[0]~[7] 全量 Findings
	1.3 Scope Lock（範圍鎖定）
本 SRS 僅受以下上游約束：
* 《GitHub Multi-Agent（模組化 Core + 4 Profiles）需求書 v1.1》
* 《GitHub Multi-Agent (模組化 Core + 4 Profiles) 架構指南》
* 《需求書升級為SRS_方案》
* 《兩份筆記導入SRS_方案》
* v0.3.0 最小三件套、TVS v0.4.1、證據三件套
* SRS v1.0.0 審查報告 A/B
禁止事項：任何未在上述來源中的新增規範一律禁止。
1.4 Counting Budget（需求計數預算）
類別
	上限
	實際數量
	狀態
	Phase 0 Blocking (MUST)
	≤40
	38
	✓ PASS
	非阻斷 (SHOULD)
	≤30
	8
	✓ PASS
	總需求數
	≤200
	72
	✓ PASS
	INV（不變量）
	-
	10
	-
	FR（功能需求）
	-
	48
	-
	EIR（外部介面）
	-
	6
	-
	NFR（非功能）
	-
	8
	-
	每能力域 MUST
	≤8
	Max 8
	✓ PASS
	每能力域 SHOULD
	≤6
	Max 2
	✓ PASS
	Non-Goals
	≤5
	5
	✓ PASS
	1.5 術語表
術語
	定義
	MUST
	RFC2119 強制要求，違反即 FAIL
	SHOULD
	RFC2119 建議要求，可記錄偏離
	MAY
	RFC2119 可選項
	Fail-Closed
	預設阻斷：缺證據/缺欄位/不合格即 FAIL
	Evidence Bundle
	可回放稽核的證據包
	GateKit
	機械閘門套件
	SSOT
	Single Source of Truth（單一權威來源）
	swap test
	A/B 法官位置交換測試（別名：Swap 測試）
	read/write split
	讀寫分流（別名：讀寫分流）
	Negative Test
	負向測試：刻意破壞約束/邊界/衝突場景，預期 FAIL/偵測
	CR_OPEN
	Change Request Open：證據完整但驗收未完成，阻斷合流
	Verdict
	裁決結果：PASS / FAIL / CR_OPEN
	1.6 Keyword Alias Map（關鍵字別名映射）
Gate 關鍵字檢索 MUST 在評估前展開別名
標準詞形（英文）
	等效別名（中文/變體）
	適用場景
	swap test
	Swap 測試, swap_test, 交換測試
	雙法官偏誤測試
	read/write split
	讀寫分流, read_write_split
	並行化規則
	Fail-Closed
	fail-closed, 預設阻斷, 失敗即關閉
	Gate 行為
	Evidence Bundle
	evidence_bundle, 證據包
	工件交接
	One-Writer
	one_writer, 單寫入者
	並行化規則
	merge_group
	merge-group, Merge Group
	GitHub 事件
	Merge Queue
	merge_queue, 合流佇列
	GitHub 功能
	stopline
	stop_line, 停止線
	熔斷條件
	attestations
	Attestations, 證明
	供應鏈驗證
	provenance
	Provenance, 來源證明
	SLSA
	SBOM
	sbom, 軟體物料清單
	供應鏈
	1.7 Document Structure Rule（章節結構規則）
F-001(B) 修補：頂層章節唯一化
規則：
1. TopLevelChapters = {1..11} 唯一。
2. 只有章節 1~11 可使用 ^\d+\. 標題語法。
3. 內文枚舉必須使用 x.y 子節或 bullet，禁止使用 \d+\. 格式。
4. DocLint MUST 在偵測到重複章號時 FAIL。
驗收：gate.doclint_structure → evidence/gates/doclint.json → PassCondition: exactly 11 unique top-level chapters; no duplicate "^\d+\." headings
1.8 RAG-Triad 自檢準則
指標
	自檢準則（用於審計）
	Context Relevance
	所有 REQ 的 Trace.ReqRef/ArchRef 必須指向實際存在的上游條款
	Faithfulness
	Statement 內容必須與上游來源語義一致，禁止過度擴展
	Coverage
	T1 Coverage Ledger 每條 v1.1 條款必須被至少一條 REQ 的 Trace.ReqRef 實質回指
	1.9 Audit-Closure Ledger（閉環總帳）
整合審查報告 A + B 所有 Findings 的處置狀態
1.9.1 審查報告 A — Findings 處置
Finding-ID
	Severity
	Category
	問題摘要
	處置狀態
	修補位置
	A-F-001
	P0
	Destructive
	缺少 Attestations 權限需求
	FIXED
	FR-EV-006, EIR-004
	A-F-002
	P1
	Drift
	provenance vs SBOM 未區分
	CLARIFIED
	EIR-004
	A-F-003
	P0
	Destructive
	merge_group 自檢機制未需求化
	FIXED
	FR-GV-002
	A-F-004
	P1
	Destructive
	Vibe Lane 合流阻斷驗收不明
	CLARIFIED
	FR-GV-004
	A-F-005
	P1
	Logic
	Coverage Gate 門檻值 Phase 標記
	CLARIFIED
	FR-GK-002
	A-F-007
	P0
	Destructive
	One-Writer 缺 git 層驗證
	FIXED
	INV-006
	A-F-012
	P0
	Destructive
	Tool Budget 缺 stopline 觸發後行為
	FIXED
	INV-008
	A-F-015
	P0
	Destructive
	負向測試定義不足
	FIXED
	INV-007, FR-EV-007
	A-F-019
	P0
	Destructive
	五階段驗收缺子階段拆分
	FIXED
	FR-AR-002
	A-F-023
	P0
	Drift
	Required Checks 命名不一致
	FIXED
	§10.2, EIR-005
	A-F-029
	P0
	Logic
	Trace Map hash 格式未定義
	FIXED
	INV-004, FR-GK-010
	A-F-034
	P0
	Destructive
	Swap Test 數量未定義
	FIXED
	FR-JD-003, FR-JD-004
	A-F-038
	P0
	Destructive
	CLAUDE.md schema 缺失
	FIXED
	FR-MEM-006
	A-F-042
	P0
	Destructive
	Codespaces 可重現性檢查
	FIXED
	EIR-003
	A-F-045
	P1
	Risk
	Prompt Injection 檢測缺失
	FIXED
	FR-GK-009
	A-F-048
	P1
	Logic
	Phase 0 Lanes 驗證方法
	CLARIFIED
	FR-PF-003
	A-F-052
	P1
	Coverage
	T1 缺少 GAP/DRIFT 條目
	FIXED
	§11 T1
	A-F-055
	P2
	Global-Polish
	Fail-Closed 條件優先級
	CLARIFIED
	§10.4
	A-F-058
	P1
	Destructive
	Evidence Bundle 最小檔案集
	FIXED
	FR-EV-004
	1.9.2 審查報告 B — Findings 處置
Finding-ID
	Severity
	Category
	問題摘要
	處置狀態
	修補位置
	B-F-001
	P0
	Structure
	頂層章節不封閉
	FIXED
	§1.7
	B-F-002
	P0
	Logic
	Coverage 宣告未閉包到 REQ Trace
	FIXED
	§11 T1, 所有受影響 REQ
	B-F-003
	P1
	Drift
	關鍵字詞形漂移
	FIXED
	§1.6 Alias Map
	B-F-004
	P1
	Risk
	merge_group 條文需不可省略
	FIXED
	EIR-001, FR-GV-002
	B-F-005
	P1
	Risk
	Codespaces prebuild secrets
	FIXED
	NFR-OPS-005
	B-F-006
	P1
	Risk
	LLM/Agent 安全控制點
	FIXED
	FR-GK-009, NFR-SEC-002
	B-F-007
	P2
	Global-Polish
	EvidencePointer 命名不一致
	FIXED
	§1.6, §11 T5
	B-F-008
	P2
	Global-Polish
	Verdict 缺 CR_OPEN
	FIXED
	§10.5
	B-F-009
	P2
	Feasibility
	Attestations 應為可選
	CLARIFIED
	EIR-004
	________________


2. Purpose & Scope（目的與範圍）
2.1 目的
本 SRS 將《需求書 v1.1》提升為可開發、可測試、可驗收的需求總契約，把《架構指南》的設計意圖轉成可驗證需求，並對 Registry/Gates/Runbook 下游產物提出不可變需求。
本系統要求「會話腳手架/外部狀態/可重現開機」是為了降低人工、提高吞吐、維持可回放。
2.2 範圍（In-Scope）
1. 控制平面（GitHub Actions）與執行平面（Codespaces）的物理隔離架構
2. 雙法官協議與抗偏誤機制
3. 機械閘門（GateKit）：G0~G4 及特殊閘門
4. Evidence Bundle 標準化與可回放
5. 四條 Profile Lanes（Vibe/Spec/Dev/Ops）與 Core 模組
6. 訂閱制 CLI 工具整合（Claude Code/Codex）
7. GitHub Rulesets/Merge Queue/merge_group 整合
8. Skills/Commands/Hooks 的 Registry 治理
9. 讀寫分流（read/write split）與單寫入者（One-Writer）規則
2.3 非目標（Out-of-Scope）
1. 逐步操作教學、命令清單（屬 Runbook SSOT）
2. Registry schema 全文與 regex 清單全文（屬 Registry SSOT）
3. 付費 API Key 整合（僅允許訂閱制）
4. 「統一平台/全局治理中樞/大一統控制台」類敘事（Anti-Platforming）
5. Phase 2+ 未落地功能堆疊（禁止 Roadmap 擴寫）
________________


3. System Context & Boundary（系統邊界與上下文）
3.1 兩平面模型
┌─────────────────────────────────────────────────────────────┐
│                    Control Plane (GitHub)                    │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────────────┐ │
│  │ Rulesets│  │  Merge  │  │ Required│  │ Actions Workflow│ │
│  │         │  │  Queue  │  │ Checks  │  │  (GateKit)      │ │
│  └─────────┘  └─────────┘  └─────────┘  └─────────────────┘ │
│                     ↓ merge_group event                      │
├─────────────────────────────────────────────────────────────┤
│                  Execution Plane (Codespaces)                │
│  ┌─────────────┐  ┌─────────────┐  ┌────────────────────┐   │
│  │ Claude Code │  │ Codex CLI   │  │ Evidence Generator │   │
│  │ (Heavy)     │  │ (Batch)     │  │                    │   │
│  └─────────────┘  └─────────────┘  └────────────────────┘   │
└─────────────────────────────────────────────────────────────┘


3.2 邊界硬規則
規則
	描述
	控制平面禁止
	執行需要互動認證的 LLM 任務
	執行平面責任
	可重現工廠，執行訂閱制 CLI 生成/修補並回傳證據包
	讀寫分流
	寫操作（改 repo/寫檔/commit）必須單寫入者
	讀操作
	讀/審查可並行，但 MUST NOT 修改工作樹
	3.3 外部依賴
依賴
	用途
	約束
	GitHub Actions
	控制平面執行環境
	無互動登入
	GitHub Rulesets
	合流規則強制
	Required Checks + Merge Queue
	GitHub Merge Queue
	序列化合流
	merge_group 事件觸發
	Codespaces
	執行平面環境
	devcontainer 固化
	Claude Code CLI
	重型施工
	訂閱制，非 API
	Codex CLI
	批次處理
	訂閱制，非 API
	________________


4. Actors & Roles（角色與權責）
4.1 角色定義
角色
	權限
	約束
	Implementer（實作者）
	唯一寫入者：編輯檔案、git add/commit、套用 patch
	單一實例，禁止並行寫入
	Verifier（驗證者）
	黑盒驗證、執行 Gate、產出驗證報告
	只讀，禁止修改工作樹
	Orchestrator（協調者）
	派工、任務分解、決策路由
	派工但不寫入
	Sub-agents（子代理）
	只讀分析、建議 patch、輔助驗證
	禁止直接寫入
	Human Operator（人類值守者）
	重大阻斷/運維救火、Session Refresh
	介入 ≤3 步
	GitHub Platform
	Rulesets/Merge Queue 執法
	機械強制
	Judge A（Codex）
	結構與 Diff 審查
	JSON 判決書
	Judge B（Claude）
	邏輯與語義審查
	JSON 判決書
	Judge Aggregator
	聚合裁決
	純 Python 腳本，非 LLM
	4.2 委派契約
子代理委派 MUST 包含四要素：
1. Objective：明確目標
2. Output Format：輸出格式
3. Tool Guidance：工具指導
4. Task Boundaries：任務邊界
________________


5. Invariants（MUST-HOLD 原則）
以下為系統不可違反原則，任何 Lane/Phase 都不可破壞。
INV-001: Fail-Closed 預設
欄位
	內容
	REQ-ID
	INV-001
	Type
	INV
	Statement
	任一 Gate、schema、證據缺失、或裁決不一致 MUST 直接 FAIL，禁止「先過再說」。
	Verification
	{CheckName: gate.fail_closed, EvidencePointer: evidence/gates/fail_closed.json, PassCondition: any missing/invalid triggers FAIL and blocks merge}
	Trace
	{ArchRef: AG-§1.1(Fail-Closed), ReqRef: v1.1.P-01}
	Phase
	0
	Blocking
	true
	INV-002: Input Seal（輸入封印）
欄位
	內容
	REQ-ID
	INV-002
	Type
	INV
	Statement
	輸入來源 MUST 具備 source_bundle_sha256 封印，Hash 不符即 FAIL，視為換料欺詐。
	Verification
	{CheckName: g0-input-seal, EvidencePointer: evidence/gates/input_seal.json, PassCondition: hash matches throughout execution}
	Trace
	{ArchRef: AG-§7.1.2(Input Seal), ReqRef: v1.1.GK-01}
	Phase
	0
	Blocking
	true
	INV-003: Addressable IDs（可尋址識別碼）
欄位
	內容
	REQ-ID
	INV-003
	Type
	INV
	Statement
	所有需求原子（REQ/DEC/ASM）MUST 具備唯一 ID，並標記 must_hold 屬性。
	Verification
	{CheckName: gate.id_addressability, EvidencePointer: evidence/gates/id_check.json, PassCondition: all atoms have unique IDs}
	Trace
	{ArchRef: AG-§6.2(Atom Schema), ReqRef: v1.1.DOC-01}
	Phase
	0
	Blocking
	true
	INV-004: Trace Map（追溯地圖）
A-F-029 修補：hash 格式規範
欄位
	內容
	REQ-ID
	INV-004
	Type
	INV
	Statement
	所有 Claim MUST 具備 Source Pointer（hash/anchor），No-Source 即 FAIL。Source Pointer 格式：SHA256 digest for file content OR full commit SHA for git refs OR URL#anchor for external sources。
	Verification
	{CheckName: g2-trace, EvidencePointer: evidence/gates/trace_map.json, PassCondition: all claims have source pointers conforming to format schema}
	Trace
	{ArchRef: AG-§7.1.4(Trace Gate), ReqRef: v1.1.GK-03}
	Phase
	0
	Blocking
	true
	INV-005: Evidence Reproducibility（證據可重現）
欄位
	內容
	REQ-ID
	INV-005
	Type
	INV
	Statement
	Evidence Bundle MUST 可獨立重建結論，不依賴外部未聲明假設。
	Verification
	{CheckName: gate.evidence_replay, EvidencePointer: evidence/gates/evidence_replay.json, PassCondition: replay job reconstructs same verdict}
	Trace
	{ArchRef: AG-§13.2.5(Verifiable Evidence), ReqRef: v1.1.EV-02, v1.1.P-03}
	Phase
	0
	Blocking
	true
	INV-006: One-Writer Rule（單寫入者）
A-F-007 修補：git 層驗證
欄位
	內容
	REQ-ID
	INV-006
	Type
	INV
	Statement
	寫操作（編輯/commit/patch）MUST 由唯一 Implementer 執行，禁止並行寫入。
	Verification
	{CheckName: gate.one_writer, EvidencePointer: evidence/gates/one_writer.json, PassCondition: (git log shows single author for all commits in PR) AND (no parallel file modification timestamps) AND (write events from run_manifest attributed to Implementer only)}
	Trace
	{ArchRef: AG-§13.4.2-D(One-Writer), ReqRef: v1.1.AR-01; 兩份筆記導入SRS_方案.FR-PAR-001}
	Phase
	0
	Blocking
	true
	INV-007: Anti-Handwave Verification（反偷懶驗證）
A-F-015 修補：負向測試定義
欄位
	內容
	REQ-ID
	INV-007
	Type
	INV
	Statement
	Verifier 不允許輸出無證據結論；每次驗證 MUST 包含檢查清單、動作清單、至少 1 個負向測試、明確結論。Negative Test 定義：刻意破壞約束、邊界條件、或衝突場景，預期 FAIL/偵測。
	Verification
	{CheckName: gate.verifier_report, EvidencePointer: evidence/verifier/report.json, PassCondition: report schema-valid; negative_test_type present; verdict present}
	Trace
	{ArchRef: AG-§13.4.2-D(Anti-Handwave), ReqRef: 兩份筆記導入SRS_方案.FR-EV-001}
	Phase
	0
	Blocking
	true
	INV-008: Tool Budget & Stopline（工具預算與停止線）
A-F-012 修補：stopline 觸發後行為
欄位
	內容
	REQ-ID
	INV-008
	Type
	INV
	Statement
	每次任務 MUST 明確列出允許工具集、呼叫預算上限、停止條件。當 stopline 觸發時，MUST emit fail_packet 並 halt execution；需人工介入。
	Verification
	{CheckName: gate.tool_budget, EvidencePointer: evidence/gates/tool_budget.json, PassCondition: budget+stopline declared; stopline violations logged; no execution beyond stopline; fail_packet emitted on trigger}
	Trace
	{ArchRef: AG-§13.4.2-D(Tool Budget), ReqRef: v1.1.OPS-01; v1.1.GK-09; 兩份筆記導入SRS_方案.NFR-OPS-001}
	Phase
	0
	Blocking
	true
	INV-009: Anti-Platforming（反平台化）
欄位
	內容
	REQ-ID
	INV-009
	Type
	INV
	Statement
	命中 anti_platform.regex 禁詞 MUST P0 FAIL，不可豁免。
	Verification
	{CheckName: g3-anti-platform, EvidencePointer: evidence/gates/anti_platform.json, PassCondition: zero regex matches}
	Trace
	{ArchRef: AG-§7.1.5(Anti-Platforming), ReqRef: v1.1.P-04, v1.1.GK-05}
	Phase
	0
	Blocking
	true
	INV-010: Dual Judge Protocol（雙法官協議）
欄位
	內容
	REQ-ID
	INV-010
	Type
	INV
	Statement
	LLM 不可單獨當法官；最終 verdict MUST 由 Judge A + Judge B 一致且 swap test（Swap 測試）通過。
	Verification
	{CheckName: g4-dual-judge, EvidencePointer: evidence/judges/final_aggregate_verdict.json, PassCondition: (Judge_A == PASS) AND (Judge_B == PASS) AND (swap_test_passed == true)}
	Trace
	{ArchRef: AG-§7.4(Dual-Judge Protocol), ReqRef: v1.1.G-3, v1.1.JD-02}
	Phase
	0
	Blocking
	true
	________________


6. Functional Requirements（功能需求）
6.1 FR-AR: Architecture & Pipeline（架構與流水線）
FR-AR-001: 控制/執行平面分離
欄位
	內容
	REQ-ID
	FR-AR-001
	Type
	FR
	Statement
	系統 MUST 實現控制平面（GitHub Actions）與執行平面（Codespaces）物理隔離，控制平面禁止互動認證。
	Verification
	{CheckName: gate.plane_separation, EvidencePointer: evidence/gates/plane_separation.json, PassCondition: control plane has no interactive login; execution plane isolated}
	Trace
	{ArchRef: AG-§2.1(Dual Plane), ReqRef: v1.1.G-1, v1.1.RD-02}
	Phase
	0
	Blocking
	true
	FR-AR-002: 五階段流水線
A-F-019 修補：子階段驗收
欄位
	內容
	REQ-ID
	FR-AR-002
	Type
	FR
	Statement
	每次任務 MUST 依循五階段流水線：Normalize → Draft/Research → Dual Review → Integrate → Final Audit。各階段 MUST 產出階段狀態檔（stage_status.json）且被下一階段驗收。
	Verification
	{CheckName: gate.pipeline_stages, EvidencePointer: evidence/gates/pipeline_stages.json, PassCondition: all 5 stages present in run_manifest; each stage has stage_status.json; downstream stage validates upstream status}
	Trace
	{ArchRef: AG-§4(Five-Stage Pipeline), ReqRef: v1.1.PF-02}
	Phase
	0
	Blocking
	true
	6.2 FR-DOC: Document Governance（文件治理）
FR-DOC-001: SRS Scope Lock
欄位
	內容
	REQ-ID
	FR-DOC-001
	Type
	FR
	Statement
	SRS MUST 只含 What/Why，禁止內嵌 How-to/Tutorial；操作手冊歸 Runbook SSOT。
	Verification
	{CheckName: gate.srs_scope, EvidencePointer: evidence/gates/srs_scope.json, PassCondition: no runbook-style content in SRS; scope boundary enforced}
	Trace
	{ArchRef: AG-§1.2(Scope Split), ReqRef: v1.1.DOC-01}
	Phase
	0
	Blocking
	true
	FR-DOC-002: TVS 對齊
欄位
	內容
	REQ-ID
	FR-DOC-002
	Type
	FR
	Statement
	SRS MUST 與 TVS v0.4.1 驗收準則保持對齊，差異需在 Document Control 說明。
	Verification
	{CheckName: gate.tvs_alignment, EvidencePointer: evidence/gates/tvs_alignment.json, PassCondition: SRS REQs traceable to TVS; deviations documented}
	Trace
	{ArchRef: AG-§13(TVS), ReqRef: v1.1.DOC-02}
	Phase
	0
	Blocking
	true
	6.3 FR-MEM: Memory & State（記憶與狀態）
FR-MEM-001: Progress 可持久化
欄位
	內容
	REQ-ID
	FR-MEM-001
	Type
	FR
	Statement
	系統 MUST 維護可持久化 progress.json，記錄任務狀態、斷點、恢復錨。
	Verification
	{CheckName: gate.progress_persistence, EvidencePointer: evidence/states/progress.json, PassCondition: progress file exists and schema-valid}
	Trace
	{ArchRef: AG-§13.4.2-D(State Externalization), ReqRef: 兩份筆記導入SRS_方案.FR-MEM-001}
	Phase
	0
	Blocking
	true
	FR-MEM-002: Run State Schema
欄位
	內容
	REQ-ID
	FR-MEM-002
	Type
	FR
	Statement
	run_state.json MUST 符合 schemas/run_state.schema.json，缺必要欄位即 FAIL。
	Verification
	{CheckName: gate.run_state_schema, EvidencePointer: evidence/states/run_state.json, PassCondition: schema passes; no missing keys}
	Trace
	{ArchRef: AG-§13.4.2-D(State Externalization), ReqRef: 兩份筆記導入SRS_方案.FR-MEM-002}
	Phase
	0
	Blocking
	true
	FR-MEM-003: Deterministic Bootstrap
欄位
	內容
	REQ-ID
	FR-MEM-003
	Type
	FR
	Statement
	系統 MUST 具備可重現開機入口，在任何寫操作前恢復到已知良好狀態。
	Verification
	{CheckName: gate.bootstrap_contract, EvidencePointer: evidence/gates/bootstrap_contract.json, PassCondition: entrypoint exists and emits required outputs}
	Trace
	{ArchRef: AG-§13.4.2-D(Deterministic Bootstrap), ReqRef: 兩份筆記導入SRS_方案.FR-MEM-003}
	Phase
	0
	Blocking
	true
	FR-MEM-004: CLAUDE.md 存在
A-F-038 修補：schema 規範
欄位
	內容
	REQ-ID
	FR-MEM-004
	Type
	FR
	Statement
	Repo 根目錄 MUST 存在 CLAUDE.md，包含架構模式、操作約束、錯題本摘要。CLAUDE.md MUST 符合 schemas/claude_md.schema.json 定義的結構。
	Verification
	{CheckName: gate.claude_md_presence, EvidencePointer: evidence/gates/claude_md.json, PassCondition: file exists; schema-valid; required sections present}
	Trace
	{ArchRef: AG-§1.3.6(Memory Externalization), ReqRef: v1.1.MEM-01}
	Phase
	0
	Blocking
	true
	FR-MEM-005: Copilot Instructions 鎖定
欄位
	內容
	REQ-ID
	FR-MEM-005
	Type
	FR
	Statement
	.github/copilot-instructions.md MUST 定義硬性規則，包含禁區與 Wrongbook 防線。
	Verification
	{CheckName: gate.copilot_instructions, EvidencePointer: evidence/gates/copilot_instructions.json, PassCondition: file exists with forbidden zones defined}
	Trace
	{ArchRef: AG-§1.3.6(Memory Externalization), ReqRef: v1.1.MEM-02}
	Phase
	0
	Blocking
	true
	6.4 FR-RT: Router & Risk Tier（路由與風險分級）
FR-RT-001: Task Manifest 決策
欄位
	內容
	REQ-ID
	FR-RT-001
	Type
	FR
	Statement
	Router MUST 以 task_manifest 特徵做決策，特徵包含檔案類型、變更規模、來源類型、敏感路徑。
	Verification
	{CheckName: gate.router_decision, EvidencePointer: evidence/gates/lane_decision.json, PassCondition: decision matches routing rules; sensitive paths blocked from Vibe}
	Trace
	{ArchRef: AG-§5.2(Router), ReqRef: v1.1.RT-01}
	Phase
	0
	Blocking
	true
	FR-RT-002: 複雜度評分與 Tier 分級
欄位
	內容
	REQ-ID
	FR-RT-002
	Type
	FR
	Statement
	系統 MUST 實施複雜度評分（0-10）與 Tier 分級，Tier 1/2/3 對應不同 evidence/gate/judge 強度。
	Verification
	{CheckName: gate.complexity_scoring, EvidencePointer: evidence/gates/complexity_score.json, PassCondition: score and tier recorded; profile matches}
	Trace
	{ArchRef: AG-§5.2.1(Complexity Scoring), ReqRef: v1.1.RT-02}
	Phase
	0
	Blocking
	true
	FR-RT-003: Router 決策可測試
欄位
	內容
	REQ-ID
	FR-RT-003
	Type
	FR
	Statement
	Routing 規則 MUST 具備單元測試與 fixtures，修改 policy 未更新 fixtures 即 FAIL。
	Verification
	{CheckName: gate.router_tests, EvidencePointer: evidence/gates/router_tests.json, PassCondition: all routing tests pass}
	Trace
	{ArchRef: AG-§5.2(Router), ReqRef: v1.1.RT-03}
	Phase
	0
	Blocking
	true
	6.5 FR-GV: Governance（治理）
FR-GV-001: Ruleset 強制 Merge Queue
欄位
	內容
	REQ-ID
	FR-GV-001
	Type
	FR
	Statement
	Repo ruleset MUST 強制 Merge Queue + Required Status Checks + 禁止 bypass。
	Verification
	{CheckName: gate.ruleset_mq, EvidencePointer: evidence/control_plane/rulesets_detail.json, PassCondition: merge_queue enabled; bypass restricted}
	Trace
	{ArchRef: AG-§2.1.3(Merge Queue), ReqRef: v1.1.GV-01}
	Phase
	0
	Blocking
	true
	FR-GV-002: merge_group 自檢機制
A-F-003 修補：自檢 FAIL 需求化
欄位
	內容
	REQ-ID
	FR-GV-002
	Type
	FR
	Statement
	若 workflow 未包含 merge_group 觸發，CI 自檢 MUST FAIL 並發出 fail_packet。自檢由 gate.merge_group_self_check 執行，缺失時主動輸出 fail_packet。
	Verification
	{CheckName: gate.merge_group_self_check, EvidencePointer: evidence/gates/merge_group_self_check.json, PassCondition: (merge_group in triggers) OR (self_check_fail_emitted == true AND fail_packet logged)}
	Trace
	{ArchRef: AG-§2.1.3(merge_group), ReqRef: v1.1.GV-02}
	Phase
	0
	Blocking
	true
	FR-GV-003: PR vs merge_group 策略明文
欄位
	內容
	REQ-ID
	FR-GV-003
	Type
	FR
	Statement
	Repo MUST 存在決策表，明確哪些 checks 只在 PR/merge_group/兩邊跑。
	Verification
	{CheckName: gate.check_strategy, EvidencePointer: evidence/gates/check_strategy.json, PassCondition: strategy table exists; workflow matches}
	Trace
	{ArchRef: AG-§2.1.3(Cost Strategy), ReqRef: v1.1.GV-03}
	Phase
	0
	Blocking
	true
	FR-GV-004: Vibe Lane 合流限制
A-F-004 修補：驗收明確化
欄位
	內容
	REQ-ID
	FR-GV-004
	Type
	FR
	Statement
	Vibe PR 禁止 auto-merge、禁止進入 merge queue，只能走 Promotion。驗收：Vibe PR detected (label=[VIBE]) 時，gate.vibe_merge_block MUST emit FAIL if merge_group event fires。
	Verification
	{CheckName: gate.vibe_merge_block, EvidencePointer: evidence/rd01/rd01_vibe_block_evidence.json, PassCondition: Vibe PR label present; merge_group event triggers FAIL; MQ entry blocked}
	Trace
	{ArchRef: AG-§5.3.1(Vibe Lane), ReqRef: v1.1.GV-04, v1.1.PF-01}
	Phase
	0
	Blocking
	true
	6.6 FR-GK: GateKit（機械閘門）
FR-GK-001: Fail-Closed Gate
欄位
	內容
	REQ-ID
	FR-GK-001
	Type
	FR
	Statement
	Missing evidence、missing required fields、invalid schemas MUST fail closed and block merge。
	Verification
	{CheckName: gate.fail_closed, EvidencePointer: evidence/gates/fail_closed.json, PassCondition: any missing/invalid triggers FAIL and blocks}
	Trace
	{ArchRef: AG-§7.1(GateKit), ReqRef: v1.1.GK-01, v1.1.P-02; 兩份筆記導入SRS_方案.FR-GK-001}
	Phase
	0
	Blocking
	true
	FR-GK-002: Coverage Gate
A-F-005 修補：Phase 標記
欄位
	內容
	REQ-ID
	FR-GK-002
	Type
	FR
	Statement
	Design/Spec Lane MUST 以 ID 覆蓋率計算，coverage < 98% 即 FAIL。此 Gate 僅在 Phase 1+ 且 Spec Lane 啟用時為 blocking。
	Verification
	{CheckName: g1-coverage, EvidencePointer: evidence/gates/coverage_map.json, PassCondition: coverage >= 98% or unmapped_atoms == 0}
	Trace
	{ArchRef: AG-§7.1.3(Coverage Gate), ReqRef: v1.1.GK-02}
	Phase
	1
	Blocking
	true (Spec Lane only)
	FR-GK-003: Schema Gate
欄位
	內容
	REQ-ID
	FR-GK-003
	Type
	FR
	Statement
	所有關鍵工件 MUST 受 schemas 約束，格式錯誤或缺必要欄位即 FAIL。
	Verification
	{CheckName: g3-schema, EvidencePointer: evidence/gates/schema_validation.json, PassCondition: all JSON artifacts pass schema validation}
	Trace
	{ArchRef: AG-§7.1.6(Schema Gate), ReqRef: v1.1.GK-04}
	Phase
	0
	Blocking
	true
	FR-GK-004: Ambiguity Gate
欄位
	內容
	REQ-ID
	FR-GK-004
	Type
	FR
	Statement
	系統 MUST 產出 ambiguity_report.json；blocking=true 且涉及核心決策時必 Stopline。
	Verification
	{CheckName: gate.ambiguity, EvidencePointer: evidence/gates/ambiguity_report.json, PassCondition: no blocking ambiguities; or human clarification obtained}
	Trace
	{ArchRef: AG-§7.3(Ambiguity Gate), ReqRef: v1.1.GK-07}
	Phase
	0
	Blocking
	true
	FR-GK-005: Format Gate
欄位
	內容
	REQ-ID
	FR-GK-005
	Type
	FR
	Statement
	提交前 MUST 保持乾淨工作樹；git status --porcelain 有輸出即 FAIL。
	Verification
	{CheckName: format-check, EvidencePointer: evidence/gates/format_check.json, PassCondition: git status --porcelain returns empty}
	Trace
	{ArchRef: AG-§7.3(Format Gate), ReqRef: v1.1.GK-08, v1.1.GK-09, v1.1.GK-10}
	Phase
	0
	Blocking
	true
	FR-GK-006: Drift/Invariant Gate
欄位
	內容
	REQ-ID
	FR-GK-006
	Type
	FR
	Statement
	系統 MUST 檢查 must_hold 不變量是否被弱化，弱化即 FAIL。
	Verification
	{CheckName: gate.drift_invariant, EvidencePointer: evidence/gates/drift_report.json, PassCondition: no invariant weakening detected}
	Trace
	{ArchRef: AG-§10.6.4(Drift Hunting), ReqRef: v1.1.GK-06}
	Phase
	0
	Blocking
	true
	FR-GK-007: Delegation Contract
欄位
	內容
	REQ-ID
	FR-GK-007
	Type
	FR
	Statement
	委派給子代理 MUST 包含 objective、output format、tool guidance、task boundaries。
	Verification
	{CheckName: gate.delegation_contract, EvidencePointer: evidence/gates/delegation_contract.json, PassCondition: all four elements present per task}
	Trace
	{ArchRef: AG-§4.2(Orchestrator), ReqRef: 兩份筆記導入SRS_方案.FR-GK-003}
	Phase
	0
	Blocking
	true
	FR-GK-008: DocLint Gate
欄位
	內容
	REQ-ID
	FR-GK-008
	Type
	FR
	Statement
	系統 MUST 實施 DocLint gate，強制 SRS 章節白名單、需求格式、量化反膨脹上限。
	Verification
	{CheckName: gate.doclint_srs, EvidencePointer: evidence/gates/doclint_srs.json, PassCondition: no extra sections; all REQs conform; counts within limits}
	Trace
	{ArchRef: AG-DOC-01(SRS scope lock), ReqRef: 需求書升級為SRS_方案.B}
	Phase
	0
	Blocking
	true
	FR-GK-009: Injection Detection Gate
A-F-045 修補：Prompt Injection 偵測
欄位
	內容
	REQ-ID
	FR-GK-009
	Type
	FR
	Statement
	gate.injection_scan MUST 使用 regex/heuristic 偵測使用者輸入中的可疑模式，命中即 FAIL。
	Verification
	{CheckName: gate.injection_scan, EvidencePointer: evidence/gates/injection_scan.json, PassCondition: no suspicious patterns detected; or patterns flagged and blocked}
	Trace
	{ArchRef: AG-§13.2.7(Security), ReqRef: v1.1.SEC-02}
	Phase
	0
	Blocking
	true
	6.7 FR-JD: Judges（法官）
FR-JD-001: Judge A（Codex）結構審
欄位
	內容
	REQ-ID
	FR-JD-001
	Type
	FR
	Statement
	Judge A（Codex）MUST 審查結構、Diff、格式，輸出 JSON 判決書。
	Verification
	{CheckName: gate.judge_a, EvidencePointer: evidence/judges/judge_a_verdict.json, PassCondition: verdict present; schema-valid}
	Trace
	{ArchRef: AG-§7.4.1(Judge A), ReqRef: v1.1.JD-01}
	Phase
	0
	Blocking
	true
	FR-JD-002: Judge B（Claude）邏輯審
欄位
	內容
	REQ-ID
	FR-JD-002
	Type
	FR
	Statement
	Judge B（Claude）MUST 審查邏輯、語義、一致性，輸出 JSON 判決書。
	Verification
	{CheckName: gate.judge_b, EvidencePointer: evidence/judges/judge_b_verdict.json, PassCondition: verdict present; schema-valid}
	Trace
	{ArchRef: AG-§7.4.2(Judge B), ReqRef: v1.1.JD-02}
	Phase
	0
	Blocking
	true
	FR-JD-003: 抗偏誤測試
A-F-034 修補：迭代次數
欄位
	內容
	REQ-ID
	FR-JD-003
	Type
	FR
	Statement
	Dual-Judge MUST 執行 swap test（Swap 測試）：A/B 互換角色重審，結果一致才 PASS。swap test 至少執行 1 次迭代；若不一致，最多執行 3 次重審。
	Verification
	{CheckName: gate.swap_test, EvidencePointer: evidence/judges/swap_consistency.json, PassCondition: swap_test_passed == true; iterations >= 1 AND <= 3}
	Trace
	{ArchRef: AG-§7.4.3(Anti-Bias), ReqRef: v1.1.JD-03}
	Phase
	0
	Blocking
	true
	FR-JD-004: Perturb Test
欄位
	內容
	REQ-ID
	FR-JD-004
	Type
	FR
	Statement
	系統 SHOULD 支援 Perturb Test：對輸入做微小擾動，驗證 Judge 輸出穩定性。
	Verification
	{CheckName: gate.perturb_test, EvidencePointer: evidence/judges/perturb_results.json, PassCondition: stability score >= 0.9}
	Trace
	{ArchRef: AG-§7.4.4(Perturb), ReqRef: v1.1.G-3}
	Phase
	1
	Blocking
	false
	6.8 FR-EV: Evidence（證據）
FR-EV-001: Verifier Report
欄位
	內容
	REQ-ID
	FR-EV-001
	Type
	FR
	Statement
	每次驗證 MUST 產出可驗證報告，包含檢查清單、執行動作、至少 1 個負向測試、明確 PASS/FAIL/CR_OPEN verdict。
	Verification
	{CheckName: gate.verifier_report, EvidencePointer: evidence/verifier/report.json, PassCondition: report schema-valid; negative test present; verdict present}
	Trace
	{ArchRef: AG-§13.4.2-D(Anti-Handwave), ReqRef: 兩份筆記導入SRS_方案.FR-EV-001}
	Phase
	0
	Blocking
	true
	FR-EV-002: Evidence Reproducibility
欄位
	內容
	REQ-ID
	FR-EV-002
	Type
	FR
	Statement
	驗證 verdict MUST 可從 Evidence Bundle 獨立重建，不依賴外部未聲明假設。
	Verification
	{CheckName: gate.evidence_replay, EvidencePointer: evidence/gates/evidence_replay.json, PassCondition: replay job reconstructs same verdict}
	Trace
	{ArchRef: AG-EvidenceBundling, ReqRef: 兩份筆記導入SRS_方案.FR-EV-002}
	Phase
	0
	Blocking
	true
	FR-EV-003: E2E Evidence
欄位
	內容
	REQ-ID
	FR-EV-003
	Type
	FR
	Statement
	UI 或可觀察行為變更，Evidence Bundle MUST 包含最小 E2E 證據（截圖/影片 hash + 生成方式）。
	Verification
	{CheckName: gate.e2e_evidence, EvidencePointer: evidence/e2e/index.json, PassCondition: at least one artifact present and referenced in evidence_ptrs}
	Trace
	{ArchRef: AG-§13.4.2-D(E2E Evidence), ReqRef: 兩份筆記導入SRS_方案.FR-EV-003}
	Phase
	0
	Blocking
	true
	FR-EV-004: 核心證據工件完整
A-F-058 修補：必備檔案清單
欄位
	內容
	REQ-ID
	FR-EV-004
	Type
	FR
	Statement
	Evidence Bundle MUST 包含：input_manifest.json、source_bundle_sha256、coverage_map.json、trace_map.json、verdict.json、gate_report.json、diff_report.md、run_manifest.json。Optional files：swap_consistency.json、drift_report.json、e2e/*。
	Verification
	{CheckName: gate.evidence_completeness, EvidencePointer: evidence/index.json, PassCondition: all required files present with valid SHA256}
	Trace
	{ArchRef: AG-§13.4.1(Evidence Pack), ReqRef: v1.1.EV-01}
	Phase
	0
	Blocking
	true
	FR-EV-005: Retention 策略可配置
欄位
	內容
	REQ-ID
	FR-EV-005
	Type
	FR
	Statement
	CI artifacts 保留設定 SHOULD 與 lane/tier 連動，高風險保留更長（例 90 天）。
	Verification
	{CheckName: gate.retention_policy, EvidencePointer: evidence/gates/retention_config.json, PassCondition: retention policy documented and applied}
	Trace
	{ArchRef: AG-§13.2.5(Retention), ReqRef: v1.1.EV-04}
	Phase
	0
	Blocking
	false
	FR-EV-006: Attestation 權限
A-F-001 修補：必要權限需求化
欄位
	內容
	REQ-ID
	FR-EV-006
	Type
	FR
	Statement
	產生 attestations 的 workflow MUST 聲明 id-token: write、attestations: write、contents: read 權限。
	Verification
	{CheckName: gate.attestation_permissions, EvidencePointer: evidence/workflow/permissions.json, PassCondition: required permissions present in workflow YAML}
	Trace
	{ArchRef: AG-§13.2.5(Attestations), ReqRef: v1.1.EV-03; 需求書升級為SRS_方案.D-4}
	Phase
	0
	Blocking
	true
	6.9 FR-PAR: Parallelization（並行化）
FR-PAR-001: One Writer Rule
欄位
	內容
	REQ-ID
	FR-PAR-001
	Type
	FR
	Statement
	寫耦合任務（repo 修改），系統 MUST 強制「單寫入者規則」（唯一 Implementer 執行所有寫入）。
	Verification
	{CheckName: gate.one_writer, EvidencePointer: evidence/gates/one_writer.json, PassCondition: no parallel write agents; write events attributed to Implementer only}
	Trace
	{ArchRef: AG-§13.4.2-D(One-Writer), ReqRef: 兩份筆記導入SRS_方案.FR-PAR-001}
	Phase
	0
	Blocking
	true
	FR-PAR-002: Read-Only Agents
欄位
	內容
	REQ-ID
	FR-PAR-002
	Type
	FR
	Statement
	只讀分析與驗證 MAY 並行化，但 MUST NOT 修改工作樹。
	Verification
	{CheckName: gate.readonly_agents, EvidencePointer: evidence/gates/readonly_agents.json, PassCondition: no file mutations from non-Implementer agents}
	Trace
	{ArchRef: AG-§13.4.2-D(One-Writer), ReqRef: 兩份筆記導入SRS_方案.FR-PAR-002}
	Phase
	0
	Blocking
	true
	FR-PAR-003: Matrix 並行
欄位
	內容
	REQ-ID
	FR-PAR-003
	Type
	FR
	Statement
	Draft/Research MUST 支援 GitHub Actions matrix 並行（job-drafter/job-researcher/job-consistency）。
	Verification
	{CheckName: gate.matrix_parallel, EvidencePointer: evidence/gates/matrix_jobs.json, PassCondition: matrix jobs produce independent artifacts unified in Evidence Bundle}
	Trace
	{ArchRef: AG-§4.3(Matrix Parallelization), ReqRef: v1.1.PAR-01}
	Phase
	0
	Blocking
	true
	FR-PAR-004: Context Isolation
欄位
	內容
	REQ-ID
	FR-PAR-004
	Type
	FR
	Statement
	子代理 MUST 只讀取最小輸入 chunk，互不干擾，禁止讀取非授權路徑。
	Verification
	{CheckName: gate.context_isolation, EvidencePointer: evidence/gates/context_isolation.json, PassCondition: each job's input list and chunk pointers verifiable in run_manifest}
	Trace
	{ArchRef: AG-§4.3(Context Isolation), ReqRef: v1.1.PAR-02}
	Phase
	0
	Blocking
	true
	6.10 FR-SK: Skills & Hooks（技能與鉤子）
FR-SK-001: Skills Registry
欄位
	內容
	REQ-ID
	FR-SK-001
	Type
	FR
	Statement
	Skills 和 Commands MUST 作為版本化工件受 Registry 管控，可被 gates 發現。
	Verification
	{CheckName: gate.registry_presence_skills, EvidencePointer: evidence/gates/registry_presence_skills.json, PassCondition: registry index references skills/commands}
	Trace
	{ArchRef: AG-§8.3(Skill Registry), ReqRef: 兩份筆記導入SRS_方案.FR-SK-001}
	Phase
	0
	Blocking
	true
	FR-SK-002: Hooks Registry
欄位
	內容
	REQ-ID
	FR-SK-002
	Type
	FR
	Statement
	Hooks MUST 定義為受 Registry 管控的工件，具備明確觸發點與輸出契約。
	Verification
	{CheckName: gate.registry_presence_hooks, EvidencePointer: evidence/gates/registry_presence_hooks.json, PassCondition: hooks indexed; contracts schema-valid}
	Trace
	{ArchRef: AG-§1.3.6(HookKit), ReqRef: 兩份筆記導入SRS_方案.FR-SK-002, v1.1.HK-01}
	Phase
	0
	Blocking
	true
	FR-SK-003: Skills Catalog Schema
欄位
	內容
	REQ-ID
	FR-SK-003
	Type
	FR
	Statement
	skills_catalog.yaml MUST 定義 Skill I/O、Gate、Stopline、Retry；新增 Skill 不填即 FAIL。
	Verification
	{CheckName: gate.skill_catalog_schema, EvidencePointer: evidence/gates/skill_catalog.json, PassCondition: all skills have required fields}
	Trace
	{ArchRef: AG-§8.3(Skill Catalog), ReqRef: v1.1.SK-01}
	Phase
	0
	Blocking
	true
	FR-SK-004: Third Party Cache 禁止直接執行
欄位
	內容
	REQ-ID
	FR-SK-004
	Type
	FR
	Statement
	third_party_cache 內容 MUST 永不直接執行，需經 Ingestion Gate 檢疫 + allowlist。
	Verification
	{CheckName: gate.third_party_ingestion, EvidencePointer: evidence/gates/third_party_check.json, PassCondition: no direct execution of third_party_cache}
	Trace
	{ArchRef: AG-§8.4(Skill Ingestion), ReqRef: v1.1.SK-02}
	Phase
	0
	Blocking
	true
	FR-SK-005: Tool Allowlist 強制
B-F-006 修補：allowlist 強制執行
欄位
	內容
	REQ-ID
	FR-SK-005
	Type
	FR
	Statement
	每次任務 MUST 明確聲明 allowed_tools 清單，未在清單中的工具呼叫 MUST FAIL。
	Verification
	{CheckName: gate.tool_allowlist, EvidencePointer: evidence/gates/tool_allowlist.json, PassCondition: all tool calls in allowed_tools; violations logged and blocked}
	Trace
	{ArchRef: AG-§13.4.2-D(Tool Budget), ReqRef: v1.1.OPS-01}
	Phase
	0
	Blocking
	true
	6.11 FR-PF: Profiles（泳道）
FR-PF-001: Vibe Lane 配置
欄位
	內容
	REQ-ID
	FR-PF-001
	Type
	FR
	Statement
	Vibe Lane MUST 配置為：G0+G4 only、無覆蓋強制、單代理探索模式。
	Verification
	{CheckName: gate.vibe_profile, EvidencePointer: evidence/profiles/vibe.yaml.evidence, PassCondition: vibe profile matches spec}
	Trace
	{ArchRef: AG-§5.3.1(Vibe Lane), ReqRef: v1.1.PF-01}
	Phase
	0
	Blocking
	true
	FR-PF-002: Dev Lane 配置
欄位
	內容
	REQ-ID
	FR-PF-002
	Type
	FR
	Statement
	Dev Lane MUST 配置為：G0~G3 全開、實作代理、雙法官審查。
	Verification
	{CheckName: gate.dev_profile, EvidencePointer: evidence/profiles/dev.yaml.evidence, PassCondition: dev profile matches spec}
	Trace
	{ArchRef: AG-§5.3.2(Dev Lane), ReqRef: v1.1.PF-02}
	Phase
	0
	Blocking
	true
	FR-PF-003: Phase 0 Lanes 啟停
欄位
	內容
	REQ-ID
	FR-PF-003
	Type
	FR
	Statement
	Phase 0 MUST 只啟用 Vibe+Dev；Spec+Ops Lane 預設禁用或不存在。
	Verification
	{CheckName: gate.phase0_lanes, EvidencePointer: evidence/gates/phase0_lanes.json, PassCondition: profiles/vibe.yaml enabled=true; profiles/dev.yaml enabled=true; profiles/spec.yaml enabled=false OR not exist; profiles/ops.yaml enabled=false OR not exist}
	Trace
	{ArchRef: AG-§5.3(Phase 0), ReqRef: v1.1.RD-01}
	Phase
	0
	Blocking
	true
	6.12 FR-PROM: Promotion（晉升）
FR-PROM-001: Vibe 終點是 Promotion
欄位
	內容
	REQ-ID
	FR-PROM-001
	Type
	FR
	Statement
	Vibe PR MUST 只能透過 Promotion（人工/半自動）轉入 Dev Lane，禁止直接合流。
	Verification
	{CheckName: gate.vibe_promotion, EvidencePointer: evidence/gates/vibe_promotion.json, PassCondition: Vibe PR end state = promoted OR rejected; no direct merge}
	Trace
	{ArchRef: AG-§5.3.1(Vibe Promotion), ReqRef: v1.1.PROM-01}
	Phase
	0
	Blocking
	true
	FR-PROM-002: Promotion 觸發條件
欄位
	內容
	REQ-ID
	FR-PROM-002
	Type
	FR
	Statement
	Promotion SHOULD 由人類審查或 CI 觸發，條件為「Vibe 探索成功 + 符合 Dev 進入標準」。
	Verification
	{CheckName: gate.promotion_trigger, EvidencePointer: evidence/gates/promotion_trigger.json, PassCondition: promotion conditions documented; trigger logged}
	Trace
	{ArchRef: AG-§5.3.1(Promotion Trigger), ReqRef: v1.1.PROM-02}
	Phase
	0
	Blocking
	false
	________________


7. External Interface Requirements（外部介面需求）
EIR-001: merge_group 事件觸發
欄位
	內容
	REQ-ID
	EIR-001
	Type
	EIR
	Statement
	任何 required-check workflow MUST 包含 triggers: pull_request AND merge_group。缺少 merge_group 觸發時，Merge Queue 執行會失敗。
	Verification
	{CheckName: gate.merge_group_trigger, EvidencePointer: evidence/workflow/docops-gatekit.yml.evidence, PassCondition: workflow YAML contains merge_group for required checks}
	Trace
	{ArchRef: AG-§2.1.3(Merge Queue), ReqRef: v1.1.GV-02; B-F-004}
	Phase
	0
	Blocking
	true
	EIR-002: Required Status Checks 配置
A-F-023 修補：命名一致性
欄位
	內容
	REQ-ID
	EIR-002
	Type
	EIR
	Statement
	Ruleset MUST 配置 Required Status Checks，check 名稱 MUST 與 workflow job 名稱完全一致。Check 命名遵循 TVS v0.4.1 定義的 gate.{name} 格式。
	Verification
	{CheckName: gate.required_checks_config, EvidencePointer: evidence/control_plane/required_checks.json, PassCondition: check names match workflow job names; naming follows gate.{name} convention}
	Trace
	{ArchRef: AG-§2.1.3(Required Checks), ReqRef: v1.1.GV-01}
	Phase
	0
	Blocking
	true
	EIR-003: Codespaces devcontainer
A-F-042 修補：可重現性檢查
欄位
	內容
	REQ-ID
	EIR-003
	Type
	EIR
	Statement
	執行平面 MUST 使用 .devcontainer/devcontainer.json 固化環境，確保可重現。devcontainer MUST 包含工具版本鎖定（node/python/cli versions），且可從 build log 驗證版本一致性。
	Verification
	{CheckName: gate.devcontainer_presence, EvidencePointer: evidence/execution_plane/devcontainer.json.evidence, PassCondition: devcontainer exists; tool versions locked; build log versions match}
	Trace
	{ArchRef: AG-§2.2(Execution Plane), ReqRef: v1.1.EV-02}
	Phase
	0
	Blocking
	true
	EIR-004: Artifact Attestations
A-F-001, A-F-002 修補：權限與類型區分
欄位
	內容
	REQ-ID
	EIR-004
	Type
	EIR
	Statement
	Evidence Bundle SHOULD 包含 build provenance attestations；MAY 包含 SBOM attestations 以增強供應鏈透明度。若產生 attestations，workflow MUST 聲明 id-token: write、attestations: write、contents: read，且可用 gh attestation verify 驗證。
	Verification
	{CheckName: gate.attestations, EvidencePointer: evidence/attestations/provenance.json, PassCondition: if attestations present => gh attestation verify PASS; required permissions declared}
	Trace
	{ArchRef: AG-§13.2.5(Attestations), ReqRef: v1.1.EV-03}
	Phase
	0
	Blocking
	false
	EIR-005: Prebuild Secrets 約束
B-F-005 修補：secrets 限制需求化
欄位
	內容
	REQ-ID
	EIR-005
	Type
	EIR
	Statement
	Codespaces prebuild MUST NOT 依賴 user-level secrets；若需 secrets，MUST 在 post-create 階段透過核准機制注入。
	Verification
	{CheckName: gate.prebuild_no_secrets, EvidencePointer: evidence/execution_plane/prebuild_config.json, PassCondition: prebuild steps contain no secret references; secrets injected post-create only}
	Trace
	{ArchRef: AG-§2.2(Codespaces), ReqRef: 需求書升級為SRS_方案.D-3}
	Phase
	0
	Blocking
	true
	EIR-006: GitHub Actions OIDC
欄位
	內容
	REQ-ID
	EIR-006
	Type
	EIR
	Statement
	需要 OIDC token 的 workflow MUST 聲明 id-token: write 權限，並驗證 token 發行者。
	Verification
	{CheckName: gate.oidc_permissions, EvidencePointer: evidence/workflow/oidc_config.json, PassCondition: id-token permission declared when OIDC used; issuer verified}
	Trace
	{ArchRef: AG-§13.2.5(OIDC), ReqRef: v1.1.EV-03}
	Phase
	0
	Blocking
	true
	________________


8. Non-Functional Requirements（NFR）
NFR-SEC-001: 密鑰隔離
欄位
	內容
	REQ-ID
	NFR-SEC-001
	Type
	NFR
	Statement
	訂閱制 CLI（Claude Code/Codex）的認證 MUST 只在 Codespaces 執行平面可用，禁止洩漏到控制平面。
	Verification
	{CheckName: gate.secret_isolation, EvidencePointer: evidence/security/secret_scope.json, PassCondition: no secret leakage to control plane logs}
	Trace
	{ArchRef: AG-§2.2(Secret Isolation), ReqRef: v1.1.SEC-01}
	Phase
	0
	Blocking
	true
	NFR-SEC-002: Prompt Injection 防護
欄位
	內容
	REQ-ID
	NFR-SEC-002
	Type
	NFR
	Statement
	系統 MUST 對使用者輸入實施 injection scanning，偵測到可疑模式時 MUST FAIL。
	Verification
	{CheckName: gate.injection_scan, EvidencePointer: evidence/security/injection_scan.json, PassCondition: scan executed; no injections detected or blocked}
	Trace
	{ArchRef: AG-§13.2.7(Security), ReqRef: v1.1.SEC-02}
	Phase
	0
	Blocking
	true
	NFR-AUD-001: 可稽核性
欄位
	內容
	REQ-ID
	NFR-AUD-001
	Type
	NFR
	Statement
	Final Audit MUST 只靠 Evidence Bundle 重建結論，無需詢問任何外部狀態。
	Verification
	{CheckName: gate.audit_bundle_only, EvidencePointer: evidence/audit/replay_test.json, PassCondition: verdict reproducible from bundle alone}
	Trace
	{ArchRef: AG-§10.6(Final Audit), ReqRef: v1.1.AUD-01}
	Phase
	0
	Blocking
	true
	NFR-AUD-002: Evidence 保留
欄位
	內容
	REQ-ID
	NFR-AUD-002
	Type
	NFR
	Statement
	CI artifacts SHOULD 保留至少 30 天（高風險 90 天），供事後稽核。
	Verification
	{CheckName: gate.retention_audit, EvidencePointer: evidence/audit/retention_policy.json, PassCondition: retention policy applied; artifacts accessible}
	Trace
	{ArchRef: AG-§13.2.5(Retention), ReqRef: v1.1.AUD-02}
	Phase
	0
	Blocking
	false
	NFR-OPS-001: Tool Budget
欄位
	內容
	REQ-ID
	NFR-OPS-001
	Type
	NFR
	Statement
	系統 MUST 為每次運行定義允許工具集、工具呼叫預算、停止條件（stopline）。
	Verification
	{CheckName: gate.tool_budget, EvidencePointer: evidence/gates/tool_budget.json, PassCondition: budget+stopline declared; violations flagged}
	Trace
	{ArchRef: AG-§13.4.2-D(Tool Budget), ReqRef: 兩份筆記導入SRS_方案.NFR-OPS-001; v1.1.OPS-01}
	Phase
	0
	Blocking
	true
	NFR-OPS-002: Tool Inventory
欄位
	內容
	REQ-ID
	NFR-OPS-002
	Type
	NFR
	Statement
	系統 SHOULD 避免過度工具/插件增生導致性能退化；工具清單 MUST 可稽核。
	Verification
	{CheckName: gate.tool_inventory, EvidencePointer: evidence/gates/tool_inventory.json, PassCondition: inventory exists; changes tracked; threshold policy applied}
	Trace
	{ArchRef: AG-§13.4.2-D(Tool Budget), ReqRef: v1.1.OPS-02}
	Phase
	0
	Blocking
	false
	NFR-OPS-003: Human Escalation SLA
欄位
	內容
	REQ-ID
	NFR-OPS-003
	Type
	NFR
	Statement
	遇到 Stopline/Ambiguity Blocking 時，系統 SHOULD 在 30 分鐘內通知人類值守者，並記錄 escalation 時間戳。
	Verification
	{CheckName: gate.escalation_sla, EvidencePointer: evidence/ops/escalation_log.json, PassCondition: escalation timestamp present; SLA compliance logged}
	Trace
	{ArchRef: AG-§4.4(Human Escalation), ReqRef: v1.1.OPS-03}
	Phase
	0
	Blocking
	false
	NFR-PERF-001: Gate 執行時限
欄位
	內容
	REQ-ID
	NFR-PERF-001
	Type
	NFR
	Statement
	單一 Gate 執行時間 SHOULD 不超過 5 分鐘；超時視為 FAIL 並記錄。
	Verification
	{CheckName: gate.timeout, EvidencePointer: evidence/gates/timing.json, PassCondition: all gates complete within timeout; timeout failures logged}
	Trace
	{ArchRef: AG-§7.1(GateKit), ReqRef: v1.1.GK-11}
	Phase
	0
	Blocking
	false
	________________


9. Evidence & Artifacts（證據與工件）
9.1 Evidence Bundle 結構
evidence/
├── index.json                    # 證據索引（MUST）
├── input_manifest.json           # 輸入封印（MUST）
├── run_manifest.json             # 運行清單（MUST）
├── gates/
│   ├── fail_closed.json          # Gate 報告（MUST）
│   ├── coverage_map.json         # 覆蓋地圖（MUST）
│   ├── trace_map.json            # 追溯地圖（MUST）
│   ├── schema_validation.json    
│   ├── format_check.json
│   ├── doclint_srs.json
│   └── ...
├── judges/
│   ├── judge_a_verdict.json      # Judge A 判決（MUST）
│   ├── judge_b_verdict.json      # Judge B 判決（MUST）
│   ├── final_aggregate_verdict.json  # 聚合裁決（MUST）
│   └── swap_consistency.json     # Swap Test 結果（MUST if Dual-Judge）
├── verifier/
│   └── report.json               # Verifier 報告（MUST）
├── diff_report.md                # 差異報告（MUST）
├── verdict.json                  # 最終裁決（MUST）
├── attestations/                 # 可選
│   ├── provenance.json
│   └── sbom.json
└── e2e/                          # 條件必要
    └── screenshots/


9.2 必備工件清單
工件
	路徑
	必要性
	說明
	Evidence Index
	evidence/index.json
	MUST
	證據總索引
	Input Manifest
	evidence/input_manifest.json
	MUST
	輸入封印
	Source Bundle SHA256
	evidence/input_manifest.json#source_bundle_sha256
	MUST
	來源雜湊
	Coverage Map
	evidence/gates/coverage_map.json
	MUST
	覆蓋地圖
	Trace Map
	evidence/gates/trace_map.json
	MUST
	追溯地圖
	Verdict
	evidence/verdict.json
	MUST
	最終裁決
	Gate Report
	evidence/gates/*.json
	MUST
	閘門報告
	Diff Report
	evidence/diff_report.md
	MUST
	差異報告
	Run Manifest
	evidence/run_manifest.json
	MUST
	運行清單
	Swap Consistency
	evidence/judges/swap_consistency.json
	MUST(if Dual-Judge)
	交換一致性
	Drift Report
	evidence/gates/drift_report.json
	OPTIONAL
	漂移報告
	E2E Evidence
	evidence/e2e/*
	CONDITIONAL
	UI 變更時必要
	Attestations
	evidence/attestations/*
	OPTIONAL
	供應鏈證明
	9.3 Evidence Pointer 規範
A-F-029, B-F-004 修補：路徑與格式正規化
Canonical Path Format：
* 相對於 repo 根目錄：evidence/{category}/{filename}.json
* Hash 格式：sha256:{64-char-hex-digest}
* Git ref 格式：{40-char-commit-sha}
* External URL 格式：https://{domain}/{path}#{anchor}
Alias Mapping（向後兼容）：
Canonical
	Alias
	evidence/index.json
	evidence_index.json
	evidence/verdict.json
	final_verdict.json
	evidence/gates/coverage_map.json
	coverage_map.json
	evidence/gates/trace_map.json
	trace_map.json
	________________


10. Verification & Acceptance（驗證與驗收）
10.1 驗收主線（Gate Sequence）
階段
	Gate
	CheckName
	說明
	Blocking
	G0
	Input Seal
	g0-input-seal
	輸入封印驗證
	true
	G1
	Coverage
	g1-coverage
	覆蓋率檢查（Phase 1+）
	true (Spec)
	G2
	Trace
	g2-trace
	追溯完整性
	true
	G3
	Schema
	g3-schema
	Schema 驗證
	true
	G3
	Anti-Platform
	g3-anti-platform
	禁詞檢測
	true
	G4
	Dual-Judge
	g4-dual-judge
	雙法官協議
	true
	*
	Format
	format-check
	格式檢查
	true
	*
	DocLint
	gate.doclint_srs
	文件結構
	true
	*
	Fail-Closed
	gate.fail_closed
	預設阻斷
	true
	10.2 Required Checks 映射
A-F-023 修補：命名對齊 TVS
Workflow Job
	Required Check Name
	Gate
	gate-g0-input-seal
	gate.g0-input-seal
	G0
	gate-g1-coverage
	gate.g1-coverage
	G1
	gate-g2-trace
	gate.g2-trace
	G2
	gate-g3-schema
	gate.g3-schema
	G3
	gate-g3-anti-platform
	gate.g3-anti-platform
	G3
	gate-g4-dual-judge
	gate.g4-dual-judge
	G4
	gate-format-check
	gate.format-check
	Format
	gate-doclint
	gate.doclint_srs
	DocLint
	10.3 Lane-Specific Acceptance
Lane
	Gates
	Judge
	Evidence
	Coverage
	Vibe
	G0, G4
	Dual
	Minimal
	N/A
	Dev
	G0, G2, G3, G4
	Dual
	Full
	Recommended
	Spec
	G0, G1, G2, G3, G4
	Dual
	Full
	98% MUST
	Ops
	G0, G3
	Single
	Config-only
	N/A
	10.4 Fail-Closed 條件彙總
A-F-055 修補：優先級與關係說明
以下條件為 OR 關係（任一成立即阻斷）。檢查順序：G0 → G1 → G2 → G3 → G4 → Coverage → Trace → Vibe → Retry。
#
	條件
	觸發
	行為
	1
	Missing evidence
	gate.fail_closed
	FAIL + block merge
	2
	Missing required fields
	gate.fail_closed
	FAIL + block merge
	3
	Invalid schema
	g3-schema
	FAIL + block merge
	4
	Judge verdict mismatch
	g4-dual-judge
	FAIL + retry/block
	5
	Swap test failed
	g4-dual-judge
	FAIL + retry/block
	6
	Coverage < threshold
	g1-coverage
	FAIL (Spec Lane)
	7
	Trace incomplete
	g2-trace
	FAIL + block merge
	8
	Anti-platform regex hit
	g3-anti-platform
	P0 FAIL + block
	9
	Vibe PR in MQ
	gate.vibe_merge_block
	FAIL + block
	10
	Stopline triggered
	gate.tool_budget
	FAIL + halt + human
	10.5 Verdict Enum 定義
B-F-007 修補：CR_OPEN 狀態
Verdict
	語義
	行為
	PASS
	所有 Gate 通過，證據完整
	允許合流
	FAIL
	任一 Gate 失敗或證據缺失
	阻斷合流
	CR_OPEN
	證據完整但驗收未完成（需人工決策）
	阻斷合流，等待 Human Operator
	Verdict 產出規則：
1. Verdict MUST 出現在 evidence/verdict.json
2. Verdict MUST 為 {PASS, FAIL, CR_OPEN} 其一
3. CR_OPEN MUST 阻斷合流，直到人工介入並更新為 PASS/FAIL
________________


11. Traceability（追溯）
T1: Coverage Ledger（v1.1 → SRS）
B-F-002 修補：確保每條 v1.1 條款有 REQ Trace.ReqRef 實質回指
v1.1 Source-ID
	SRS REQ-ID
	狀態
	Trace.ReqRef 驗證
	G-1
	FR-AR-001, FR-AR-002
	✓ PASS
	v1.1.G-1 in Trace
	G-3
	INV-010, FR-JD-001~004
	✓ PASS
	v1.1.G-3 in Trace
	P-01
	INV-001, FR-GK-001
	✓ PASS
	v1.1.P-01 in Trace
	P-02
	FR-GK-001
	✓ PASS
	v1.1.P-02 in Trace
	P-03
	INV-005
	✓ PASS
	v1.1.P-03 in Trace
	P-04
	INV-009
	✓ PASS
	v1.1.P-04 in Trace
	AR-01
	INV-006, FR-PAR-001
	✓ PASS
	v1.1.AR-01 in Trace
	DOC-01
	FR-DOC-001
	✓ PASS
	v1.1.DOC-01 in Trace
	DOC-02
	FR-DOC-002
	✓ PASS
	v1.1.DOC-02 in Trace
	MEM-01
	FR-MEM-004
	✓ PASS
	v1.1.MEM-01 in Trace
	MEM-02
	FR-MEM-005
	✓ PASS
	v1.1.MEM-02 in Trace
	RT-01
	FR-RT-001
	✓ PASS
	v1.1.RT-01 in Trace
	RT-02
	FR-RT-002
	✓ PASS
	v1.1.RT-02 in Trace
	RT-03
	FR-RT-003
	✓ PASS
	v1.1.RT-03 in Trace
	PF-01
	FR-PF-001, FR-GV-004
	✓ PASS
	v1.1.PF-01 in Trace
	PF-02
	FR-AR-002, FR-PF-002
	✓ PASS
	v1.1.PF-02 in Trace
	GK-01
	INV-002, FR-GK-001
	✓ PASS
	v1.1.GK-01 in Trace
	GK-02
	FR-GK-002
	✓ PASS
	v1.1.GK-02 in Trace
	GK-03
	INV-004
	✓ PASS
	v1.1.GK-03 in Trace
	GK-04
	FR-GK-003
	✓ PASS
	v1.1.GK-04 in Trace
	GK-05
	INV-009
	✓ PASS
	v1.1.GK-05 in Trace
	GK-06
	FR-GK-006
	✓ PASS
	v1.1.GK-06 in Trace
	GK-07
	FR-GK-004
	✓ PASS
	v1.1.GK-07 in Trace
	GK-08
	FR-GK-005
	✓ PASS
	v1.1.GK-08 in Trace
	GK-09
	FR-GK-005
	✓ PASS
	v1.1.GK-09 in Trace
	GK-10
	FR-GK-005
	✓ PASS
	v1.1.GK-10 in Trace
	GK-11
	NFR-PERF-001
	✓ PASS
	v1.1.GK-11 in Trace
	JD-01
	FR-JD-001
	✓ PASS
	v1.1.JD-01 in Trace
	JD-02
	INV-010, FR-JD-002
	✓ PASS
	v1.1.JD-02 in Trace
	JD-03
	FR-JD-003
	✓ PASS
	v1.1.JD-03 in Trace
	EV-01
	FR-EV-004
	✓ PASS
	v1.1.EV-01 in Trace
	EV-02
	INV-005, FR-EV-002
	✓ PASS
	v1.1.EV-02 in Trace
	EV-03
	EIR-004, FR-EV-006
	✓ PASS
	v1.1.EV-03 in Trace
	EV-04
	FR-EV-005
	✓ PASS
	v1.1.EV-04 in Trace
	SK-01
	FR-SK-003
	✓ PASS
	v1.1.SK-01 in Trace
	SK-02
	FR-SK-004
	✓ PASS
	v1.1.SK-02 in Trace
	HK-01
	FR-SK-002
	✓ PASS
	v1.1.HK-01 in Trace
	GV-01
	FR-GV-001
	✓ PASS
	v1.1.GV-01 in Trace
	GV-02
	FR-GV-002, EIR-001
	✓ PASS
	v1.1.GV-02 in Trace
	GV-03
	FR-GV-003
	✓ PASS
	v1.1.GV-03 in Trace
	GV-04
	FR-GV-004
	✓ PASS
	v1.1.GV-04 in Trace
	PAR-01
	FR-PAR-003
	✓ PASS
	v1.1.PAR-01 in Trace
	PAR-02
	FR-PAR-004
	✓ PASS
	v1.1.PAR-02 in Trace
	OPS-01
	INV-008, NFR-OPS-001
	✓ PASS
	v1.1.OPS-01 in Trace
	OPS-02
	NFR-OPS-002
	✓ PASS
	v1.1.OPS-02 in Trace
	OPS-03
	NFR-OPS-003
	✓ PASS
	v1.1.OPS-03 in Trace
	SEC-01
	NFR-SEC-001
	✓ PASS
	v1.1.SEC-01 in Trace
	SEC-02
	NFR-SEC-002, FR-GK-009
	✓ PASS
	v1.1.SEC-02 in Trace
	PROM-01
	FR-PROM-001
	✓ PASS
	v1.1.PROM-01 in Trace
	PROM-02
	FR-PROM-002
	✓ PASS
	v1.1.PROM-02 in Trace
	RD-01
	FR-PF-003
	✓ PASS
	v1.1.RD-01 in Trace
	RD-02
	FR-AR-001
	✓ PASS
	v1.1.RD-02 in Trace
	AUD-01
	NFR-AUD-001
	✓ PASS
	v1.1.AUD-01 in Trace
	AUD-02
	NFR-AUD-002
	✓ PASS
	v1.1.AUD-02 in Trace
	Coverage Rate: 100% (52/52)
T2: Architecture Trace（架構指南 → SRS）
AG Section
	must_hold
	SRS REQ-ID
	狀態
	AG-§1.1
	Fail-Closed
	INV-001, FR-GK-001
	✓ PASS
	AG-§2.1
	Dual Plane Separation
	FR-AR-001
	✓ PASS
	AG-§2.1.3
	Merge Queue
	FR-GV-001, EIR-001
	✓ PASS
	AG-§4
	Five-Stage Pipeline
	FR-AR-002
	✓ PASS
	AG-§5.2
	Router
	FR-RT-001~003
	✓ PASS
	AG-§5.3
	Profile Lanes
	FR-PF-001~003
	✓ PASS
	AG-§7.1
	GateKit
	FR-GK-001~008
	✓ PASS
	AG-§7.4
	Dual-Judge
	INV-010, FR-JD-001~004
	✓ PASS
	AG-§8.3
	Skill Registry
	FR-SK-001~005
	✓ PASS
	AG-§10.6
	Final Audit
	NFR-AUD-001
	✓ PASS
	AG-§13.4.2-D
	One-Writer
	INV-006, FR-PAR-001
	✓ PASS
	AG-§13.4.2-D
	Anti-Handwave
	INV-007, FR-EV-001
	✓ PASS
	AG-§13.4.2-D
	Tool Budget
	INV-008, NFR-OPS-001
	✓ PASS
	T3: Notes Import Trace（兩份筆記導入方案 → SRS）
Notes REQ-ID
	SRS REQ-ID
	狀態
	FR-MEM-001
	FR-MEM-001
	✓ PASS
	FR-MEM-002
	FR-MEM-002
	✓ PASS
	FR-MEM-003
	FR-MEM-003
	✓ PASS
	FR-PAR-001
	INV-006, FR-PAR-001
	✓ PASS
	FR-PAR-002
	FR-PAR-002
	✓ PASS
	FR-EV-001
	FR-EV-001
	✓ PASS
	FR-EV-002
	FR-EV-002
	✓ PASS
	FR-EV-003
	FR-EV-003
	✓ PASS
	FR-GK-001
	FR-GK-001
	✓ PASS
	FR-GK-003
	FR-GK-007
	✓ PASS
	FR-SK-001
	FR-SK-001
	✓ PASS
	FR-SK-002
	FR-SK-002
	✓ PASS
	NFR-OPS-001
	INV-008, NFR-OPS-001
	✓ PASS
	T4: Checks & Evidence Trace（REQ → CheckName → EvidencePointer）
REQ-ID
	CheckName
	EvidencePointer
	INV-001
	gate.fail_closed
	evidence/gates/fail_closed.json
	INV-002
	g0-input-seal
	evidence/gates/input_seal.json
	INV-003
	gate.id_addressability
	evidence/gates/id_check.json
	INV-004
	g2-trace
	evidence/gates/trace_map.json
	INV-005
	gate.evidence_replay
	evidence/gates/evidence_replay.json
	INV-006
	gate.one_writer
	evidence/gates/one_writer.json
	INV-007
	gate.verifier_report
	evidence/verifier/report.json
	INV-008
	gate.tool_budget
	evidence/gates/tool_budget.json
	INV-009
	g3-anti-platform
	evidence/gates/anti_platform.json
	INV-010
	g4-dual-judge
	evidence/judges/final_aggregate_verdict.json
	FR-GK-001
	gate.fail_closed
	evidence/gates/fail_closed.json
	FR-GK-002
	g1-coverage
	evidence/gates/coverage_map.json
	FR-GK-003
	g3-schema
	evidence/gates/schema_validation.json
	FR-GV-002
	gate.merge_group_self_check
	evidence/gates/merge_group_self_check.json
	FR-JD-003
	gate.swap_test
	evidence/judges/swap_consistency.json
	FR-EV-004
	gate.evidence_completeness
	evidence/index.json
	FR-EV-006
	gate.attestation_permissions
	evidence/workflow/permissions.json
	EIR-001
	gate.merge_group_trigger
	evidence/workflow/docops-gatekit.yml.evidence
	EIR-002
	gate.required_checks_config
	evidence/control_plane/required_checks.json
	EIR-003
	gate.devcontainer_presence
	evidence/execution_plane/devcontainer.json.evidence
	EIR-004
	gate.attestations
	evidence/attestations/provenance.json
	EIR-005
	gate.prebuild_no_secrets
	evidence/execution_plane/prebuild_config.json
	T5: Evidence Pointer Index
Canonical Path
	Alias
	說明
	evidence/index.json
	evidence_index.json
	證據總索引
	evidence/verdict.json
	final_verdict.json
	最終裁決
	evidence/input_manifest.json
	input_manifest.json
	輸入封印
	evidence/run_manifest.json
	run_manifest.json
	運行清單
	evidence/gates/coverage_map.json
	coverage_map.json
	覆蓋地圖
	evidence/gates/trace_map.json
	trace_map.json
	追溯地圖
	evidence/gates/fail_closed.json
	gate_report.json
	閘門報告
	evidence/judges/final_aggregate_verdict.json
	aggregate_verdict.json
	聚合裁決
	evidence/judges/swap_consistency.json
	swap_test.json
	Swap 測試結果
	evidence/verifier/report.json
	verifier_report.json
	Verifier 報告
	________________


附錄：Audit-Closure Ledger 完整處置表
A. 審查報告 A — Findings 完整處置
Finding-ID
	Severity
	Category
	問題摘要
	處置狀態
	修補位置
	A-F-001
	P0
	Destructive
	缺少 Attestations 權限需求
	FIXED
	FR-EV-006, EIR-004
	A-F-002
	P1
	Drift
	provenance vs SBOM 未區分
	CLARIFIED
	EIR-004
	A-F-003
	P0
	Destructive
	merge_group 自檢機制未需求化
	FIXED
	FR-GV-002
	A-F-004
	P1
	Destructive
	Vibe Lane 合流阻斷驗收不明
	CLARIFIED
	FR-GV-004
	A-F-005
	P1
	Logic
	Coverage Gate 門檻值 Phase 標記
	CLARIFIED
	FR-GK-002
	A-F-007
	P0
	Destructive
	One-Writer 缺 git 層驗證
	FIXED
	INV-006
	A-F-012
	P0
	Destructive
	Tool Budget 缺 stopline 觸發後行為
	FIXED
	INV-008
	A-F-015
	P0
	Destructive
	負向測試定義不足
	FIXED
	INV-007
	A-F-019
	P0
	Logic
	五階段流水線缺子驗收
	FIXED
	FR-AR-002
	A-F-023
	P0
	Drift
	Required Checks 命名不一致
	FIXED
	EIR-002, §10.2
	A-F-029
	P0
	Destructive
	Trace Map hash 格式未定義
	FIXED
	INV-004, §9.3
	A-F-034
	P0
	Logic
	Swap test 迭代次數未定義
	FIXED
	FR-JD-003
	A-F-038
	P0
	Destructive
	CLAUDE.md schema 缺失
	FIXED
	FR-MEM-004
	A-F-042
	P0
	Destructive
	Codespaces 可重現性檢查缺失
	FIXED
	EIR-003
	A-F-045
	P1
	Risk
	Prompt Injection 檢測缺失
	FIXED
	FR-GK-009, NFR-SEC-002
	A-F-048
	P1
	Logic
	Phase 0 Lanes 驗證方法不明
	CLARIFIED
	FR-PF-003
	A-F-052
	P1
	Coverage
	T1 表格缺 GAP 條目
	FIXED
	T1 Coverage Ledger
	A-F-055
	P2
	Polish
	Fail-Closed 條件缺優先級
	CLARIFIED
	§10.4
	A-F-058
	P1
	Destructive
	Evidence Bundle 必備檔案清單缺失
	FIXED
	FR-EV-004, §9.2
	B. 審查報告 B — Findings 完整處置
Finding-ID
	Severity
	Category
	問題摘要
	處置狀態
	修補位置
	B-F-001
	P0
	Structure
	頂層章節編號重複/不封閉
	FIXED
	§1.7 Document Structure Rule
	B-F-002
	P0
	Trace
	Coverage Ledger 宣告式未閉包
	FIXED
	T1 每條加 Trace 驗證欄
	B-F-003
	P1
	Drift
	關鍵字詞形漂移 (swap test/讀寫分流)
	FIXED
	§1.6 Keyword Alias Map
	B-F-004
	P1
	Risk
	merge_group 條文應提升為不可省略
	FIXED
	EIR-001
	B-F-005
	P1
	Risk
	Prebuild secrets 約束缺失
	FIXED
	EIR-005
	B-F-006
	P1
	Risk
	Tool allowlist 未強制執行
	FIXED
	FR-SK-005
	B-F-007
	P2
	Logic
	Verdict enum 缺 CR_OPEN
	FIXED
	§10.5 Verdict Enum
	B-F-008
	P2
	Polish
	Evidence pointer 路徑不一致
	FIXED
	§9.3, T5
	B-F-009
	P2
	Feasibility
	Attestations 應為可選
	CLARIFIED
	EIR-004 (Blocking=false)
	________________


END OF SRS v1.1.0
________________


本文件為 Reference/Contract 類型，符合 Diátaxis 框架。任何 How-to/Tutorial 內容請參閱外部 Runbook SSOT。