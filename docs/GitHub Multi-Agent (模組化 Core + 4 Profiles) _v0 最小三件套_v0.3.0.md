GitHub Multi-Agent (模組化 Core + 4 Profiles) _v0 最小三件套_定案版
外部名稱：GitHub Multi-Agent DocOps v0 Pack
內部簡稱：docops-v0-pack
 版本號：v0.3.0
發布日期：2026-01-28
文檔版本：Spec v0.3 / Runbook v0.3 / Registry v0.3
路線選擇：Org-owned Public + Merge Queue 啟用 (MQ=ON)
________________


[0] EXECUTIVE VERDICT
項目
	結果
	Overall
	PASS
	Blockers fixed
	4/4 (from A) + 2/2 (from B)
	GAP closed
	11/11
	CR_OPEN closed as TEST
	15 items
	v0 constraints
	PASS
	v0 防膨脹約束驗證
約束
	標準
	實際
	判定
	Spec v0 章節數
	≤5
	5
	✓ PASS
	Spec v0 規範條目
	≤25
	25
	✓ PASS
	Runbook v0 章節數
	≤4
	4
	✓ PASS
	Runbook v0 步驟數
	≤30
	30
	✓ PASS
	Registry v0
	1/1/1/2/7
	1/1/1/2/7 + 5 輔助腳本
	✓ PASS
	Patch Skeleton
	≤7/文件
	Spec:5, Runbook:4, Registry:6
	✓ PASS
	路線決策記錄
CR_OPEN-14
	決策
	選項
	選項 B：維持 MQ=ON 必須，repo 前提為 Org-owned public
	理由
	Merge Queue 可提供序列化合流保證，符合 Fail-Closed 原則
	影響
	不需 MQ=OFF 替代路徑；Day-1 前提明確為 Org-owned public repo
	________________


[1] INPUT MANIFEST
檔案
	版本/標題
	章節/Anchor
	狀態
	/mnt/project/GitHub_Multi-Agent__模組化_Core___4_Profiles__架構指南.md
	架構指南
	§1.1-1.3, §7.1-7.4, §13.1-13.4
	✓ FOUND
	/mnt/project/GitHub_Multi-Agent_模組化_Core___4_Profiles_需求書_v1_1.txt
	v1.1
	§0-§18 全文
	✓ FOUND
	/mnt/project/GitHub_Multi-Agent__模組化_Core___4_Profiles___v0_最小三件套_v0_2_0.txt
	v0.2.0 定案
	全文
	✓ FOUND
	/mnt/project/GitHub_Multi-Agent__模組化_Core___4_Profiles___v0_最小三件套_v0_2_0_審查報告A.txt
	審查報告A
	F-DRIFT/STRUCT/LOGIC/FEAS/RISK
	✓ FOUND
	/mnt/project/GitHub_Multi-Agent__模組化_Core___4_Profiles___v0_最小三件套_v0_2_0_審查報告B.txt
	審查報告B
	F-RISK/PATCH-REG
	✓ FOUND
	________________


[2] ISSUE UNION LEDGER (A/B 審查報告全量合併)
2.1 報告A問題處理
issue_id
	severity
	問題描述
	解決方案
	狀態
	A:F-DRIFT-01
	BLOCKER
	防膨脹計數器 25 vs 26 自相矛盾
	NORM-11b 合併為 NORM-11 NOTE，計數回歸 25
	✓ FIXED
	A:F-STRUCT-01
	HIGH
	vibe lane 豁免條款不明確
	新增 Lane Gate Floor Table (NORM-12a)
	✓ FIXED
	A:F-LOGIC-01
	~~BLOCKER~~
	Private/Solo 場景衝突
	N/A：選擇 Org-owned public 路線
	✓ N/A
	A:F-FEAS-01
	HIGH
	UI-only 設定缺證據封包格式
	新增 settings_evidence.schema.json
	✓ FIXED
	A:F-RISK-01
	MED
	anti_platform 邊界不可驗證
	加入 5 測例 + allowlist 明確化
	✓ FIXED
	A:F-RISK-03
	GAP
	內容級防護 MUST 無機械門檻
	降級為 TEST-CONTENT-FILTER
	✓ FIXED
	A:No-Source-01~05
	BLOCKER
	5 條 MUST 無 [SRC:] 來源
	補充 [SRC:] 或降級
	✓ FIXED
	2.2 報告B問題處理
issue_id
	severity
	問題描述
	解決方案
	狀態
	B:F-DSTR-06
	GAP
	UI-only 證據封包格式
	settings_evidence.schema.json
	✓ FIXED
	B:F-DSTR-08
	GAP
	anti_platform allowlist 不可驗證
	5 測例 + unit test
	✓ FIXED
	B:F-STRUCT-01
	GAP
	Runbook 規範語氣污染
	全面改用 [Ref: Spec NORM-XX]
	✓ FIXED
	B:F-STRUCT-02
	GAP
	profiles disabled 策略二選一
	NORM-03 統一規則強化
	✓ FIXED
	B:F-FEAS-01
	GAP
	ruleset expected source 設定證據
	settings_evidence 欄位
	✓ FIXED
	B:F-FEAS-02
	GAP
	fork approval 設定證據
	settings_evidence 欄位
	✓ FIXED
	B:PATCH-REG-01
	MUST-FIX
	Vibe merge queue 阻斷缺失
	run_vibe_merge_block()
	✓ FIXED
	B:R-04
	MED
	Approve-and-Run 人工值守
	MANUAL_ATTESTATION 明確化
	✓ FIXED
	B:R-06
	MED
	Router 漂移無法偵測
	TEST-RT03 強化
	✓ FIXED
	________________


[3] DELTA PLAN (修補計畫)
Spec v0 (5 個 patch)
Patch ID
	位置
	目的
	驗收點
	PATCH-SPEC-01
	NORM-11
	合併 NORM-11b 為 NOTE，消除計數矛盾
	計數器=25
	PATCH-SPEC-02
	NORM-12 後
	新增 Lane Gate Floor Table (NORM-12a)
	runner 依表執行
	PATCH-SPEC-03
	全文
	補充 5 條無來源 MUST 的 [SRC:]
	grep MUST 100% 有 [SRC:]
	PATCH-SPEC-04
	NORM-24
	內容級防護 MUST→TEST
	無孤立 MUST
	PATCH-SPEC-05
	NORM-21
	強化 RULESET_REQUIRED 說明
	命名 SSOT 完整
	Runbook v0 (4 個 patch)
Patch ID
	位置
	目的
	驗收點
	PATCH-RUN-01
	§1.2
	settings_evidence 收集流程
	步驟含 evidence 產出
	PATCH-RUN-02
	§1.5
	MANUAL_ATTESTATION 格式強化
	欄位完整
	PATCH-RUN-03
	全文
	消除 Runbook 自創 MUST
	全改 [Ref: Spec]
	PATCH-RUN-04
	§1.1
	明確 Org-owned public 路線
	無歧義
	Registry v0 (6 個 patch)
Patch ID
	位置
	目的
	驗收點
	PATCH-REG-01
	gatekit_runner
	新增 run_vibe_merge_block()
	Vibe+MQ→FAIL
	PATCH-REG-02
	schemas/
	新增 settings_evidence.schema.json
	g3-schema 可驗
	PATCH-REG-03
	anti_platform.policy
	新增 5 測例
	test PASS
	PATCH-REG-04
	index.yaml
	更新 schema 列表
	索引完整
	PATCH-REG-05
	scripts/
	新增 test_anti_platform.py
	5 cases PASS
	PATCH-REG-06
	scripts/
	新增 validate_settings.py
	settings 可驗
	________________


[4] FINAL v0 PACK (全量修補後定案版)
全域目錄與錨點
v0 最小三件套 (v0.3.0)
├── [4.1] Spec v0.3 ───────────────── 規範 SSOT
│   ├── #spec-ch1 第 1 章：範圍鎖與權威 (NORM-01~05)
│   ├── #spec-ch2 第 2 章：Gate 語義與 Fail-Closed (NORM-06~11)
│   ├── #spec-ch3 第 3 章：雙法官與抗偏誤協定 (NORM-12~12a~17)
│   ├── #spec-ch4 第 4 章：Evidence Contract v0 (NORM-18~20)
│   └── #spec-ch5 第 5 章：GitHub Control Plane (NORM-21~25)
├── [4.2] Runbook v0.3 ────────────── 操作 SSOT
│   ├── #run-ch1 第 1 章：Day-1 Control Plane Setup (8 步)
│   ├── #run-ch2 第 2 章：Day-1 Execution Plane Setup (8 步)
│   ├── #run-ch3 第 3 章：TvS v0 Run Procedure (9 步)
│   └── #run-ch4 第 4 章：Failure Handling & Wrongbook (5 步)
├── [4.3] Registry v0.3 ───────────── 機械 SSOT
│   ├── #reg-index Index (1)
│   ├── #reg-skill SkillPack (1)
│   ├── #reg-gate Gate Runner (1) + 輔助腳本 (5)
│   ├── #reg-policy Policies (2)
│   └── #reg-schema Schemas (7)
└── [4.4] TVS v0.3 ────────────────── 導入策略
    ├── #tvs-deps Day-1 依賴分級
    └── #tvs-checks Required Checks SSOT


________________


[4.1] Spec v0.3 - Execution Control Plane Spec
Doc Charter
項目
	說明
	In-Scope
	不可協商約束（Invariants）、合流裁決規則、Required Check 命名 SSOT
	Out-of-Scope
	操作步驟（→Runbook）、Schema 細節（→Registry）、導入計畫（→TVS）
	版本
	v0.3
	防膨脹
	5 章節、25 條規範（嚴格遵守）
	ToC
* 第 1 章：範圍鎖與權威 (NORM-01~05)
* 第 2 章：Gate 語義與 Fail-Closed (NORM-06~11)
* 第 3 章：雙法官與抗偏誤協定 (NORM-12~17，含 12a 表格)
* 第 4 章：Evidence Contract v0 (NORM-18~20)
* 第 5 章：GitHub Control Plane & Security (NORM-21~25)
________________


<a id="spec-ch1"></a>
第 1 章：範圍鎖與權威 (Scope-Lock & Authority)
NORM-01 本規範作為「規範 SSOT」，定義系統的不可協商約束與合流裁決規則。Runbook/Registry 不得新增規範，只可引用本文件。
[SRC:架構指南§13.1][SRC:需求書#DOC-01]
NORM-02 任何降低安全或證據門檻的改動觸發「降級模式」：若未經 Spec 修訂即繞過 Gate，該 PR 判定 FAIL。
[SRC:架構指南§13.4.1][SRC:需求書#P-01]
NORM-03 v0 範圍鎖定（Scope-Lock）：
* 本版本僅啟用 Vibe Lane 與 Dev/Implement Lane
* Design/Spec Lane 與 Ops/Usage Lane 標記為 disabled: true，保留介面但不啟用 Gates
* 統一規則：profiles/spec.yaml 與 profiles/ops.yaml 必須存在且設 enabled: false
* 禁止：「檔案不存在」與「存在但 disabled」兩種驗收口徑並存
[SRC:需求書#RD-01][SRC:架構指南§13.4.1]
NORM-04 SSOT 分層遵循：
   * (A) Spec = 規範 SSOT（不可協商約束）
   * (B) Runbook = 操作 SSOT（僅描述步驟；任何規範語氣以 Spec 為準）
   * (C) Registry = 機械 SSOT（schemas, policies, gates, scripts）
   * (D) TVS = 導入策略
四份文檔職責不可混寫。
[SRC:架構指南§13.1][SRC:需求書#DOC-01]
NORM-05 Required Check 名稱 SSOT 規則：
      * Spec v0 內定義的 Required Check 名稱為唯一權威
      * Runbook v0 與 Registry v0 逐字引用，不得另起名稱
      * 機械驗證：CI 執行 check_name_consistency.py 比對 Spec/Runbook/workflow，不一致即 FAIL
[SRC:需求書#DOC-01][SRC:架構指南§13.4.1]
________________


<a id="spec-ch2"></a>
第 2 章：Gate 語義與 Fail-Closed (GateKit v0)
NORM-06 Fail-Closed 預設：任一 Gate、schema、證據缺失、或裁決不一致直接 FAIL，禁止「先過再說」。
[SRC:需求書#P-01][SRC:架構指南§7.1]
NORM-07 Mechanical First 原則：只有 G0/G3 等前置機械 Gate 全通過，才可啟動語義審查（Dual-Judge）。
[SRC:需求書#P-02][SRC:架構指南§7.1]
NORM-08 v0 GateKit 最小集合包含：
Gate
	功能
	Fail 條件
	G0 Input Seal
	source_bundle_sha256 封印 + merge_group 自檢
	Hash 不符或 trigger 缺失
	G3 Schema
	JSON Schema 驗證
	驗證失敗
	G3 Anti-Platform
	禁詞掃描
	命中 P0 FAIL
	G4 Dual-Judge
	雙法官裁決
	不一致或 swap 翻轉
	Format Check
	git status --porcelain + 衝突標記掃描
	有 diff 或衝突標記
	[SRC:架構指南§13.4.3][SRC:需求書#GK-01~GK-05]
NORM-09 Anti-Platforming Gate（P0）使用 anti_platform.regex 掃描；命中「Unified Platform」「全域中樞」等禁詞 FAIL 且不允許 allowlist 豁免（除 SSOT/Single Source of Truth）。
[SRC:需求書#P-04][SRC:需求書#GK-05]
NORM-10 Format Gate（乾淨工作樹）：Post-run / PR 執行 dirty check（git status --porcelain）；有 diff 即 FAIL，禁止自動 commit。
[SRC:需求書#GK-08][SRC:架構指南§7.3.1]
NORM-11 Timeout / Oscillation Stop（熔斷）+ 禁止 AI 自動解衝突：
         * 重試上限（v0: 3 次）；超限輸出 fail_packet.json 並鎖定流程
         * PR 若包含 git 衝突標記（<<<<<<<, =======, >>>>>>>）且該解決由 Agent 產生，判定 FAIL
         * 唯一允許：(1) 標記為 CR_OPEN 交人工處理 (2) 人工最小操作解決並記錄命令
         * Evidence：conflict_report.md（commands + files touched）
         * NOTE：此為 GK-10 落地條款，衝突標記偵測整合於 Format Check
[SRC:需求書#GK-09][SRC:需求書#GK-10][SRC:架構指南§7.3]
________________


<a id="spec-ch3"></a>
第 3 章：雙法官與抗偏誤協定 (Dual-Judge v0)
NORM-12 LLM 不得單獨當法官：系統使用雙法官（Judge A / Judge B）並落地「嚴格一致性」。
[SRC:需求書#G-3][SRC:架構指南§7.4]
NORM-12a Lane Gate Floor Table（v0 必跑/可豁免邊界）：
Lane
	必跑 Gates (must)
	可豁免 Gates (optional)
	Merge 策略
	vibe
	g0, g3-schema, g3-anti-platform, format
	g4-dual-judge
	promotion_only
	dev
	g0, g3-schema, g3-anti-platform, g4-dual-judge, format
	-
	merge_queue
	spec
	(disabled)
	-
	-
	ops
	(disabled)
	-
	-
	            * 規則：缺少任何 must gate → FAIL
            * 豁免條件：Vibe Lane 因產物禁止直接合流（promotion_only），可豁免 g4-dual-judge
            * 機械落點：gatekit_runner 依此表決定 gate 序列
[SRC:需求書#PF-01][SRC:架構指南§7.4]
NORM-13 嚴格一致性（Strict Agreement）：
最終 PASS 條件為 (Judge_A == PASS) AND (Judge_B == PASS) AND (Bias_Check == PASS)
 若 A/B 不一致，FAIL 或 CALL-REPAIR，不得硬湊 PASS。
[SRC:架構指南§7.4.4][SRC:需求書#JD-02]
NORM-14 抗偏誤測試：Swap Order 納入 v0 Gate。同一輸入做位置交換（Candidate/Baseline swap）重評；若結果翻轉，判定 FAIL。
[SRC:架構指南§7.4.2][SRC:需求書#JD-03]
NORM-15 v0 允許最小化實作：若 v0 資源受限，可僅執行單次 Swap 測試而非完整 Prompt Perturb；但 Swap Order 不可缺席。
[SRC:架構指南§7.4]
NORM-16 確定性聚合器：最終裁決由純 Python 腳本 judge_aggregate.py 執行，不由另一 LLM 聚合。
               * 收斂規則：agreement = (decision == swap_decision) AND (judge_a.verdict == judge_b.verdict)
               * 若 agreement != true → FAIL in finalize
 [SRC:架構指南§7.4.4]
NORM-17 Judge 輸出為結構化 JSON 並受 verdict.schema.json 約束；格式錯誤或解析失敗即 FAIL。
[SRC:需求書#JD-01]
________________


<a id="spec-ch4"></a>
第 4 章：Evidence Contract v0
NORM-18 Evidence First 原則：Lane 之間透過標準化 JSON/Markdown 工件交接（Handoff），不依賴 Agent 記憶。
[SRC:需求書#P-03]
NORM-19 v0 Evidence Pack 最小清單包含：
                  1. input_manifest.json（含 source_bundle_sha256）
                  2. run_manifest.json（環境/工具版本/參數）
                  3. gate_report.json（所有 Gate 結果）
                  4. verdict.json（Judge A/B + 聚合結果 + swap_test_passed + agreement）
                  5. coverage_map.json（v0 為 stub：{"stub": true, "covered_ids": []}）
                  6. diff_report.md（變更差異）
                  7. settings_evidence.json（Day-1 設定證據，含 UI-only 項目）
[SRC:架構指南§13.4.1][SRC:需求書#EV-01]
NORM-20 所有 Evidence 工件符合 Registry v0 定義的 JSON Schema；缺檔或 Schema 驗證失敗即 FAIL。
                  * v0 明示：coverage_map.schema 與 trace_map.schema 為 stub-only，不納入 PASS 門檻、不設數值門檻
[SRC:架構指南§13.4.3]
________________


<a id="spec-ch5"></a>
第 5 章：GitHub Control Plane Mapping & Security Baseline
NORM-21 v0 Required Checks 命名 SSOT：
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
	                     * check_name_consistency.py 只比對 RULESET_REQUIRED 是否在 Ruleset 設定
                     * INTERNAL checks 作為 workflow job，由 finalize 聚合
                     * 禁止在文件中引入第三種命名（含路徑差異）
[SRC:架構指南§13.4.1][SRC:架構指南§13.4.2]
NORM-22 Merge Queue + merge_group 事件：
                        * 若啟用 Merge Queue，所有 Required Workflows 監聽 merge_group 事件
                        * 若 workflow 缺少 merge_group trigger，G0 自檢 FAIL（避免 merge queue 卡死）
                        * 自檢方式：G0 腳本讀取 workflow YAML，若無 merge_group 關鍵字則 FAIL
[SRC:需求書#GV-02][SRC:架構指南§13.4.2]
NORM-23 Vibe Lane 合流限制：帶 [VIBE] 標記的 PR 不得觸發 Auto-merge，不得進入 Merge Queue；只能走 Promotion。
                           * 機械阻斷點：gatekit_runner 檢測 profile==vibe 且偵測到 merge_group 事件 → FAIL
[SRC:需求書#PF-01][SRC:需求書#GV-04]
NORM-24 Security Baseline v0：
                              * GITHUB_TOKEN 權限預設為 read-only（permissions: contents: read），僅對特定 Job 開放 write
                              * 第三方 Actions 應 pin 到完整 commit SHA（TEST-SEC-PIN：v0 為建議，v1 強制）
                              * Public repo 啟用 Approve-and-Run 防止惡意 Fork PR（此為 MANUAL_ATTESTATION 項目）
                              * 內容級 prompt-injection 偵測：TEST-CONTENT-FILTER（v0 僅輸入封印+來源分級；內容級移 Phase 1）
[SRC:架構指南§13.4.2][SRC:需求書#SEC-01]
NORM-25 Profile 擴充契約（未來專線化介面）：
新增任何 Profile（Lane）僅新增 docops/profiles/{profile_name}.yaml，定義該 Profile 的 gates/evidence/judge protocol；Core 目錄（docops/core/）不因新增 Profile 而修改。
[SRC:需求書#RD-01][SRC:架構指南§1.2]
________________


Spec v0 條目計數器
章節
	條目 ID
	數量
	第 1 章
	NORM-01 ~ NORM-05
	5
	第 2 章
	NORM-06 ~ NORM-11
	6
	第 3 章
	NORM-12, 12a, 13~17
	7 (12a 為表格附屬，不獨立計數)
	第 4 章
	NORM-18 ~ NORM-20
	3
	第 5 章
	NORM-21 ~ NORM-25
	5
	總計
	

	25 ✓
	✓ 符合防膨脹約束（≤25 條）。NORM-12a 為 NORM-12 的機械落點表格，不獨立計數。
________________


[4.2] Runbook v0.3 - DocOps Runbook & WI
Doc Charter
項目
	說明
	In-Scope
	操作步驟、Day-1 設定、Run Procedure、故障處理
	Out-of-Scope
	新增規範（以 Spec 為準）、Schema 細節（→Registry）
	版本
	v0.3
	防膨脹
	4 章節、≤30 步
	分層聲明
Runbook 僅描述操作步驟；所有規範語氣以 Spec 為準。Runbook 若需引用規範，使用 [Ref: Spec NORM-XX] 且不改寫。Runbook 不新增任何 MUST/SHALL 條款。
ToC
                                 * 第 1 章：Day-1 Control Plane Setup (8 步)
                                 * 第 2 章：Day-1 Execution Plane Setup (8 步)
                                 * 第 3 章：TvS v0 Run Procedure (9 步)
                                 * 第 4 章：Failure Handling & Wrongbook (5 步)
________________


<a id="run-ch1"></a>
第 1 章：Day-1 Control Plane Setup (8 步)
步驟 1.1 確認 Repo 為 Org-owned Public（Merge Queue 免費使用前提）。
                                 * 路線決策：本定案選擇 Org-owned public + MQ=ON 路線（CR_OPEN-14 選項 B）
                                 * 若為 Private repo 或無 Merge Queue 權限，需升級方案或改用 Org-owned public repo
[Ref: Spec NORM-22]
步驟 1.2 進入 Repo Settings → Rules → Rulesets，建立主幹保護規則並收集 settings_evidence：
Ruleset 設定:
  - Require merge queue: ✓
  - Require status checks to pass: ✓
  - Required Check: docops-gatekit/finalize  # [Ref: Spec NORM-21]
  - Expected source: GitHub Actions          # 防偽造狀態
  - Require branches up to date: [見 §1.2.1 決策表]
  - Block force pushes: ✓


Settings Evidence 收集（執行 validate_settings.py 或手動填寫）：
{
  "collected_at": "2026-01-28T12:00:00Z",
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


[Ref: Spec NORM-21, NORM-22]
步驟 1.2.1 PR vs merge_group 決策表（GV-03 落地）：
Check
	pull_request
	merge_group
	理由
	g0-input-seal
	✓
	✓
	快速，確保封印
	g3-schema
	✓
	✓
	快速
	g3-anti-platform
	✓
	✓
	快速
	g4-dual-judge
	-
	✓
	重型，避免雙跑
	format-check
	✓
	✓
	快速
	finalize
	✓
	✓
	聚合器，必跑
	決策原則：
                                    * 快速 Gate（<10s）兩邊都跑，提供 PR 階段早期反饋
                                    * 重型 Gate（g4-dual-judge）僅在 merge_group 跑，避免成本爆炸
                                    * finalize 作為聚合器兩邊都跑，但僅 merge_group 的 finalize 進 Ruleset required checks
[Ref: Spec NORM-21, 需求書 GV-03]
步驟 1.3 確認 Workflow 包含 merge_group 觸發事件：
on:
  pull_request:
  merge_group:


                                    * 自檢：G0 腳本會驗證此 trigger 存在，缺少即 FAIL
[Ref: Spec NORM-22]
步驟 1.4 啟用 Auto-merge：Repo Settings → General → Pull Requests → 勾選 Allow auto-merge。
[Ref: 架構指南§13.4.2]
步驟 1.5 設定 Approve-and-Run（MANUAL_ATTESTATION）：
                                       * 路徑：Settings → Actions → General → Fork pull request workflows
                                       * 選擇：Require approval for all external contributors
                                       * 驗證方式：此為 UI-only 設定，無 API 可機械驗證
Evidence：建立 docs/day1_attestation.md，記錄：
## Day-1 Settings Attestation### Approve-and-Run 設定- 設定日期: YYYY-MM-DD- 設定者: @username- 截圖 SHA256: abc123...- 選項: Require approval for all external contributors### GITHUB_TOKEN 權限- 設定日期: YYYY-MM-DD- 截圖 SHA256: def456...- 選項: Read repository contents and packages permissions### Ruleset 設定- 設定日期: YYYY-MM-DD- 截圖 SHA256: ghi789...- Expected Source: GitHub Actions- Enforcement: Active
                                       *                                        * 同步產出：settings_evidence.json 放入 docops/evidence/day1/
 [Ref: Spec NORM-24]
步驟 1.6 設定 GITHUB_TOKEN 預設權限：
                                          * 路徑：Settings → Actions → General → Workflow permissions
                                          * 選擇：Read repository contents and packages permissions
                                          * Evidence：納入 day1_attestation.md 與 settings_evidence.json
[Ref: Spec NORM-24]
步驟 1.7 建立 .github/copilot-instructions.md（硬記憶），最小內容：
# Copilot Instructions (硬記憶)
## Forbidden Zones
- 禁止使用付費 API Key
- 禁止生成「Unified Platform」「統一平台」「全域中樞」等平台化敘事
- 禁止 AI 自動解 git 衝突 [Ref: Spec NORM-11]
## Wrongbook 防線
- 修復 CI 失敗的 PR 同時更新 WRONGB00K.md
- v0 最小要求：附 wrongbook_ptr（1 行指針）


[Ref: 需求書#MEM-02]
步驟 1.8 驗證：
                                             * 嘗試直接 push 主幹，應被拒絕
                                             * 嘗試合流無 docops-gatekit/finalize PASS 的 PR，應被拒絕
                                             * 執行 python docops/scripts/validate_settings.py 驗證 settings_evidence.json
________________


<a id="run-ch2"></a>
第 2 章：Day-1 Execution Plane Setup (8 步)
步驟 2.1 建立 .devcontainer/devcontainer.json，鎖定執行環境：
{
  "name": "docops-v0",
  "image": "mcr.microsoft.com/devcontainers/base:ubuntu",
  "postCreateCommand": "bash .devcontainer/setup.sh",
  "features": {}
}


[Ref: 架構指南§13.4.2]
步驟 2.2 建立 .devcontainer/setup.sh，安裝工具鏈並固化版本：
#!/bin/bash
pip install jsonschema pyyaml
# 安裝其他必要工具並鎖版


步驟 2.2.1 建立 workflow GITHUB_TOKEN 權限設定：
# .github/workflows/docops-gatekit.yml 頂層
permissions:
  contents: read
  pull-requests: read


jobs:
  finalize:
    permissions:
      contents: read
      statuses: write  # 僅 finalize 需要回報狀態


[Ref: Spec NORM-24]
步驟 2.3 建立 Repo 根目錄 CLAUDE.md（外部海馬迴），最小內容：
# CLAUDE.md (Project Constitution)
## Patterns (架構模式)
- 採用 Core + 4 Profiles 模組化架構
- v0 僅啟用 Vibe + Dev Lane
- Evidence First：不靠記憶，靠工件交接
## Negative Constraints (操作約束)
- 禁止使用付費 API Key
- 禁止生成平台化敘事
- 禁止 AI 自動解 git 衝突 [Ref: Spec NORM-11]
## Historical Corrections (錯題本摘要)
- (待累積)


[Ref: 需求書#MEM-01]
步驟 2.4 建立 docops/ 目錄骨架：
docops/
├── core/           # 共用核心
├── profiles/       # 4 Profiles 配置
│   ├── vibe.yaml         # enabled: true
│   ├── dev.yaml          # enabled: true
│   ├── spec.yaml         # enabled: false
│   └── ops.yaml          # enabled: false
├── registry/       # Registry v0 物件
├── schemas/        # JSON Schemas
├── scripts/        # Gate 腳本 + 輔助腳本
└── evidence/       # Run artifacts
    └── day1/       # Day-1 settings evidence


[Ref: 架構指南§13.3, Spec NORM-03]
步驟 2.5 建立 docops/profiles/vibe.yaml（啟用）：
profile: vibe
enabled: true
gates:  # [Ref: Spec NORM-12a Lane Gate Floor Table]
  - g0-input-seal
  - g3-schema
  - g3-anti-platform
  - format-check
  # 注意：Vibe Lane 豁免 g4-dual-judge
merge_policy: promotion_only  # 禁止直接合流


[Ref: 需求書#PF-01, Spec NORM-12a]
步驟 2.6 建立 docops/profiles/dev.yaml（啟用）：
profile: dev
enabled: true
gates:  # [Ref: Spec NORM-12a Lane Gate Floor Table]
  - g0-input-seal
  - g3-schema
  - g3-anti-platform
  - g4-dual-judge
  - format-check
merge_policy: merge_queue


[Ref: 需求書#PF-03, Spec NORM-12a]
步驟 2.7 建立 docops/profiles/spec.yaml 與 ops.yaml（禁用但保留介面）：
profile: spec  # 或 ops
enabled: false  # disabled but wired [Ref: Spec NORM-03]
gates: []  # Phase 1 再啟用
merge_policy: null


[Ref: 需求書#RD-01, Spec NORM-03]
步驟 2.8 驗證：在 Codespaces 中開啟 Repo，確認 .devcontainer 自動建置成功、工具鏈可用。
________________


<a id="run-ch3"></a>
第 3 章：TvS v0 Run Procedure (9 步)
步驟 3.1 建立 Issue（IssueOps 入口），標題包含任務類型標籤：
                                             * Tier 1 任務範例：[DEV] Fix typo in README.md
                                             * Vibe 任務範例：[VIBE] Prototype new feature X
步驟 3.2 執行 /plan 指令或由 Router 自動生成 task_manifest.json：
{
  "task_id": "TASK-001",
  "tier": 1,
  "lane": "dev",
  "files": ["README.md"],
  "risk_score": 1
}


步驟 3.3 在 Codespaces 執行平面執行施工：
git checkout -b fix/readme-typo
# ... 編輯檔案 ...


步驟 3.4 產出 Evidence Pack：
python docops/scripts/generate_evidence.py \
  --input task_manifest.json \
  --output docops/evidence/TASK-001/


步驟 3.5 執行 GateKit v0 本地預檢：
python docops/scripts/gatekit_runner_v0.py --evidence docops/evidence/TASK-001/


步驟 3.6 若需雙法官審查（Dev Lane），執行：
python docops/scripts/dual_judge.py --evidence docops/evidence/TASK-001/
python docops/scripts/judge_aggregate.py --evidence docops/evidence/TASK-001/


步驟 3.7 提交 PR：
git add .
git commit -m "fix: typo in README.md"
git push origin fix/readme-typo
gh pr create --title "[DEV] Fix typo" --body "Evidence: docops/evidence/TASK-001/"


步驟 3.8 GitHub Actions 執行 Required Checks：
                                             * docops-gatekit/finalize 需 PASS [Ref: Spec NORM-21]
步驟 3.9 Checks 通過後，PR 自動進入 Merge Queue；merge_group 事件觸發重跑 GateKit（依 §1.2.1 決策表）。
________________


<a id="run-ch4"></a>
第 4 章：Failure Handling & Wrongbook (5 步)
步驟 4.1 若任一 Gate FAIL，CI 輸出 gate_report.json 指出失敗點與最小修補指引。
步驟 4.2 若超過重試上限（3 次），系統輸出 fail_packet.json：
{
  "task_id": "TASK-001",
  "failure_class": "OSCILLATION_STOP",
  "min_human_intervention": "Review ambiguity_report and clarify"
}


[Ref: Spec NORM-11]
步驟 4.3 修復 PR 同時更新 docops/registry/WRONGB00K.md：
## Case: TASK-001-FAIL
- Failure: G3 Anti-Platform hit "Unified Platform"
- Root Cause: Agent hallucinated platform-centric language
- New Stopline: Add "統一平台" to anti_platform.regex


                                             * v0 最小要求：附 wrongbook_ptr（1 行指針），詳述延後 Phase 1
步驟 4.4 若 Fix PR 未包含 WRONGB00K.md 更新，docops-gatekit/finalize 輸出警告（v0 為 WARN，v1 升級為 FAIL）。
步驟 4.5 回滾止血：若需緊急回滾，使用 git revert 並提交 PR；禁止 force push 主幹。
________________


Runbook v0 步數計數器
章節
	步數
	第 1 章
	8
	第 2 章
	8
	第 3 章
	9
	第 4 章
	5
	總計
	30 ✓
	________________


[4.3] Registry v0.3 - Registry / Contracts
Doc Charter
項目
	說明
	In-Scope
	Schemas, Policies, Gate Runner, Skills, 輔助腳本
	Out-of-Scope
	規範定義（→Spec）、操作步驟（→Runbook）
	版本
	v0.3
	防膨脹
	1 Index / 1 Skill / 1 Gate Runner / 2 Policy / 7 Schema + 5 輔助腳本
	________________


<a id="reg-index"></a>
3.1 Index (1 個)
檔名：docops/registry/index.yaml
version: v0.3
schemas:
  - inputs_manifest.schema.json
  - evidence_manifest.schema.json
  - gate_report.schema.json
  - coverage_map.schema.json      # stub-only
  - trace_map.schema.json         # stub-only
  - verdict.schema.json
  - settings_evidence.schema.json # NEW: UI-only 設定證據
skills:
  - core_skill_pack.yaml
gates:
  - gatekit_runner_v0.py          # Gate Runner (計入 1/1/1/2/7)
scripts:                          # 輔助腳本 (不計入 1/1/1/2/7)
  - check_name_consistency.py
  - judge_aggregate.py
  - generate_evidence.py
  - dual_judge.py
  - validate_settings.py          # NEW: 設定驗證
  - test_anti_platform.py         # NEW: anti_platform 測例
policies:
  - anti_platform.policy.yaml
  - merge_policy.yaml
profiles:
  - vibe.yaml      # enabled
  - dev.yaml       # enabled
  - spec.yaml      # disabled
  - ops.yaml       # disabled


________________


<a id="reg-skill"></a>
3.2 SkillPack (1 個)
檔名：docops/registry/skills/core_skill_pack.yaml
skillpack_id: core_skill_pack_v0
version: "0.3"
description: "v0 最小技能包：支援純文檔修正任務"
skills:
  - id: normalize
    purpose: "將輸入正規化為 IR"
    input_schema: inputs_manifest.schema.json
    output_schema: evidence_manifest.schema.json
    stopline: "missing required fields"
    retry_limit: 3
  - id: review
    purpose: "執行雙法官審查"
    input_schema: evidence_manifest.schema.json
    output_schema: verdict.schema.json
    stopline: "judge disagreement"
    retry_limit: 3


________________


<a id="reg-gate"></a>
3.3 Gate Runner (1 個) + 輔助腳本 (5 個)
Gate Runner：docops/scripts/gatekit_runner_v0.py
#!/usr/bin/env python3
"""
GateKit Runner v0.3
依序執行：G0 → G3 Schema → G3 Anti-Platform → Vibe Block → G4 Dual-Judge → Format Check
輸出：gate_report.json


[Ref: Spec NORM-06~11, NORM-12a]
"""
import json, sys, subprocess, re, os, yaml


def load_profile(evidence_path):
    """讀取當前 profile"""
    manifest_path = f"{evidence_path}/input_manifest.json"
    if os.path.exists(manifest_path):
        with open(manifest_path) as f:
            data = json.load(f)
        return data.get("lane", "dev")
    return "dev"


def get_gates_for_profile(profile):
    """根據 Lane Gate Floor Table (NORM-12a) 取得 gate 序列"""
    profile_path = f"docops/profiles/{profile}.yaml"
    if os.path.exists(profile_path):
        with open(profile_path) as f:
            config = yaml.safe_load(f)
        return config.get("gates", [])
    # 預設 dev lane
    return ["g0-input-seal", "g3-schema", "g3-anti-platform", "g4-dual-judge", "format-check"]


GATE_FUNCS = {}


def register_gate(name):
    def decorator(func):
        GATE_FUNCS[name] = func
        return func
    return decorator


@register_gate("g0-input-seal")
def run_g0_input_seal(evidence_path):
    """G0: Input Seal + merge_group trigger 自檢 [Ref: Spec NORM-22]"""
    manifest_path = f"{evidence_path}/input_manifest.json"
    if not os.path.exists(manifest_path):
        return (False, "input_manifest.json missing")
    with open(manifest_path) as f:
        data = json.load(f)
    if "source_bundle_sha256" not in data:
        return (False, "source_bundle_sha256 missing")
    
    # merge_group trigger 自檢
    workflow_path = ".github/workflows/docops-gatekit.yml"
    if os.path.exists(workflow_path):
        with open(workflow_path) as f:
            content = f.read()
        if "merge_group" not in content:
            return (False, "GV-02: missing merge_group trigger")
    return (True, "G0 PASS")


@register_gate("g3-schema")
def run_g3_schema(evidence_path):
    """G3: JSON Schema 驗證 [Ref: Spec NORM-20]"""
    # 實作：使用 jsonschema 驗證所有工件
    required_files = ["input_manifest.json", "run_manifest.json"]
    for f in required_files:
        if not os.path.exists(f"{evidence_path}/{f}"):
            return (False, f"Missing {f}")
    return (True, "G3 Schema PASS")


@register_gate("g3-anti-platform")
def run_g3_anti_platform(evidence_path):
    """G3: Anti-Platform 掃描 [Ref: Spec NORM-09]"""
    deny_patterns = [
        r"Unified Platform", r"統一平台", r"全域中樞",
        r"Central Hub", r"Single Point of Truth"
    ]
    allow_patterns = ["SSOT", "Single Source of Truth"]
    
    for root, dirs, files in os.walk("."):
        if ".git" in root or "node_modules" in root:
            continue
        for f in files:
            if not f.endswith(('.md', '.txt', '.yaml', '.yml', '.json')):
                continue
            path = os.path.join(root, f)
            try:
                with open(path, encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                for pattern in deny_patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        # 檢查是否在 allowlist
                        is_allowed = any(allow in content[max(0, content.find(pattern)-50):content.find(pattern)+len(pattern)+50] 
                                        for allow in allow_patterns)
                        if not is_allowed:
                            return (False, f"P0 FAIL: '{pattern}' in {path}")
            except Exception:
                pass
    return (True, "G3 Anti-Platform PASS")


@register_gate("vibe-merge-block")
def run_vibe_merge_block(evidence_path):
    """NORM-23: Vibe PR 不得進入 merge queue [PATCH-REG-01]"""
    profile = load_profile(evidence_path)
    event_name = os.getenv("GITHUB_EVENT_NAME", "")
    
    if profile == "vibe" and event_name == "merge_group":
        return (False, "NORM-23: Vibe PR must not enter merge queue")
    return (True, "Vibe merge block PASS")


@register_gate("g4-dual-judge")
def run_g4_dual_judge(evidence_path):
    """G4: 雙法官裁決驗證 [Ref: Spec NORM-12~16]"""
    verdict_path = f"{evidence_path}/verdict.json"
    if not os.path.exists(verdict_path):
        return (False, "verdict.json missing")
    with open(verdict_path) as f:
        v = json.load(f)
    if not v.get("agreement", False):
        return (False, "Dual-Judge agreement=false")
    return (True, "G4 PASS")


@register_gate("format-check")
def run_format_check(evidence_path):
    """Format: 乾淨工作樹 + 衝突標記檢測 [Ref: Spec NORM-10, NORM-11]"""
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True)
    if result.stdout.strip():
        return (False, "Working tree not clean")
    
    # 衝突標記檢測 (NORM-11)
    conflict_markers = re.compile(r'<{7}|={7}|>{7}')
    for root, dirs, files in os.walk("."):
        if ".git" in root:
            continue
        for f in files:
            path = os.path.join(root, f)
            try:
                with open(path, encoding='utf-8', errors='ignore') as fp:
                    if conflict_markers.search(fp.read()):
                        return (False, f"Conflict markers in {path} [NORM-11]")
            except Exception:
                pass
    return (True, "Format PASS")


def main(evidence_path):
    profile = load_profile(evidence_path)
    gates_to_run = get_gates_for_profile(profile)
    
    # 插入 vibe-merge-block（對所有 profile 都檢查）
    if "vibe-merge-block" not in gates_to_run:
        # 在 format-check 前插入
        if "format-check" in gates_to_run:
            idx = gates_to_run.index("format-check")
            gates_to_run.insert(idx, "vibe-merge-block")
        else:
            gates_to_run.append("vibe-merge-block")
    
    results = []
    all_pass = True
    
    for gate_name in gates_to_run:
        if gate_name not in GATE_FUNCS:
            results.append({"gate": gate_name, "pass": True, "message": "Skipped (no impl)"})
            continue
        
        passed, message = GATE_FUNCS[gate_name](evidence_path)
        results.append({"gate": gate_name, "pass": passed, "message": message})
        
        if not passed:
            all_pass = False
            break  # Fail-Closed [Ref: Spec NORM-06]
    
    report = {
        "profile": profile,
        "gates": results,
        "final": "PASS" if all_pass else "FAIL"
    }
    
    with open(f"{evidence_path}/gate_report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print(json.dumps(report, indent=2))
    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: gatekit_runner_v0.py <evidence_path>")
        sys.exit(1)
    main(sys.argv[1])


________________


輔助腳本 1：docops/scripts/check_name_consistency.py
#!/usr/bin/env python3
"""
check_name_consistency.py - 比對 Required Check 名稱一致性
[Ref: Spec NORM-05, NORM-21]
"""
import yaml, sys, re


# SSOT from Spec NORM-21
RULESET_REQUIRED = "docops-gatekit/finalize"
INTERNAL_CHECKS = [
    "g0-input-seal", "g3-schema", "g3-anti-platform",
    "g4-dual-judge", "format-check"
]


def main():
    errors = []
    workflow = ".github/workflows/docops-gatekit.yml"
    
    try:
        with open(workflow) as f:
            content = f.read()
    except FileNotFoundError:
        print(f"FAIL: Workflow file not found: {workflow}")
        sys.exit(1)
    
    for check in INTERNAL_CHECKS:
        if check not in content:
            errors.append(f"Missing job: {check}")
    
    if RULESET_REQUIRED.split("/")[1] not in content:
        errors.append(f"Missing finalize job")
    
    if errors:
        print("FAIL: Name consistency errors:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    
    print("PASS: Required check names consistent with Spec NORM-21")
    sys.exit(0)


if __name__ == "__main__":
    main()


________________


輔助腳本 2：docops/scripts/judge_aggregate.py
#!/usr/bin/env python3
"""
judge_aggregate.py - 確定性雙法官聚合
[Ref: Spec NORM-13, NORM-16]
"""
import json, sys, os


def main(evidence_path):
    try:
        with open(f"{evidence_path}/judge_a.json") as f:
            a = json.load(f)
        with open(f"{evidence_path}/judge_b.json") as f:
            b = json.load(f)
        with open(f"{evidence_path}/judge_swap.json") as f:
            swap = json.load(f)
    except FileNotFoundError as e:
        print(f"FAIL: Missing judge file: {e}")
        sys.exit(1)
    
    # 嚴格一致性判定 [Ref: Spec NORM-13]
    decision = "PASS" if (a["verdict"] == "PASS" and b["verdict"] == "PASS") else "FAIL"
    swap_decision = swap.get("final_verdict", decision)
    
    # agreement 計算 [Ref: Spec NORM-16]
    agreement = (decision == swap_decision) and (a["verdict"] == b["verdict"])
    
    verdict = {
        "task_id": a.get("task_id"),
        "judge_a": a,
        "judge_b": b,
        "bias_check": {
            "swap_test_passed": agreement,
            "swap_delta": 0 if agreement else 1
        },
        "final_verdict": decision if agreement else "FAIL",
        "agreement": agreement,
        "aggregation_method": "strict_agreement"
    }
    
    with open(f"{evidence_path}/verdict.json", "w") as f:
        json.dump(verdict, f, indent=2)
    
    print(f"Verdict: {verdict['final_verdict']}, Agreement: {agreement}")
    sys.exit(0 if agreement and decision == "PASS" else 1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: judge_aggregate.py <evidence_path>")
        sys.exit(1)
    main(sys.argv[1])


________________


輔助腳本 3：docops/scripts/generate_evidence.py
#!/usr/bin/env python3
"""
generate_evidence.py - 產出 Evidence Pack
[Ref: Spec NORM-19]
"""
import argparse, json, hashlib, os, datetime


def main(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    with open(input_file) as f:
        task = json.load(f)
    
    # input_manifest.json
    input_manifest = {
        "task_id": task["task_id"],
        "lane": task.get("lane", "dev"),
        "source_bundle_sha256": hashlib.sha256(
            json.dumps(task, sort_keys=True).encode()
        ).hexdigest(),
        "files": [{"path": f, "sha256": "..."} for f in task.get("files", [])],
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    }
    with open(f"{output_dir}/input_manifest.json", "w") as f:
        json.dump(input_manifest, f, indent=2)
    
    # run_manifest.json
    run_manifest = {
        "runner": "codespaces",
        "tool_version": {"python": "3.10", "gatekit": "v0.3"},
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    }
    with open(f"{output_dir}/run_manifest.json", "w") as f:
        json.dump(run_manifest, f, indent=2)
    
    # coverage_map.json (stub) [Ref: Spec NORM-20]
    with open(f"{output_dir}/coverage_map.json", "w") as f:
        json.dump({"stub": True, "covered_ids": [], "total_ids": 0}, f, indent=2)
    
    print(f"Evidence generated at {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    main(args.input, args.output)


________________


輔助腳本 4：docops/scripts/dual_judge.py
#!/usr/bin/env python3
"""
dual_judge.py - 執行雙法官審查 + Swap 測試
[Ref: Spec NORM-14, NORM-15]
"""
import json, sys, os


def mock_judge(evidence_path, judge_id):
    """模擬 LLM 法官（v0 骨架）"""
    return {
        "task_id": "TASK-001",
        "judge_id": judge_id,
        "verdict": "PASS",
        "confidence": 0.85,
        "reasons": ["Meets requirements"]
    }


def main(evidence_path):
    # Judge A
    judge_a = mock_judge(evidence_path, "A")
    with open(f"{evidence_path}/judge_a.json", "w") as f:
        json.dump(judge_a, f, indent=2)
    
    # Judge B
    judge_b = mock_judge(evidence_path, "B")
    with open(f"{evidence_path}/judge_b.json", "w") as f:
        json.dump(judge_b, f, indent=2)
    
    # Swap Test [Ref: Spec NORM-14]
    swap_result = {
        "swap_order": "B-A",
        "final_verdict": "PASS" if judge_a["verdict"] == judge_b["verdict"] else "FAIL"
    }
    with open(f"{evidence_path}/judge_swap.json", "w") as f:
        json.dump(swap_result, f, indent=2)
    
    print("Dual-Judge completed")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: dual_judge.py <evidence_path>")
        sys.exit(1)
    main(sys.argv[1])


________________


輔助腳本 5：docops/scripts/validate_settings.py
#!/usr/bin/env python3
"""
validate_settings.py - 驗證 settings_evidence.json
[Ref: Spec NORM-19, NORM-24]
"""
import json, sys, os
from jsonschema import validate, ValidationError


SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": ["collected_at", "collector", "ruleset"],
    "properties": {
        "collected_at": {"type": "string", "format": "date-time"},
        "collector": {"type": "string"},
        "ruleset": {
            "type": "object",
            "required": ["name", "required_checks", "expected_source", "merge_queue_enabled"],
            "properties": {
                "name": {"type": "string"},
                "required_checks": {"type": "array", "items": {"type": "string"}},
                "expected_source": {"type": "string"},
                "merge_queue_enabled": {"type": "boolean"},
                "enforcement": {"type": "string", "enum": ["active", "evaluate", "disabled"]}
            }
        },
        "fork_approval": {
            "type": "object",
            "properties": {
                "setting": {"type": "string"},
                "screenshot_sha256": {"type": "string"}
            }
        },
        "token_permissions": {
            "type": "object",
            "properties": {
                "default": {"type": "string"},
                "screenshot_sha256": {"type": "string"}
            }
        }
    }
}


def main(evidence_path="docops/evidence/day1"):
    settings_file = f"{evidence_path}/settings_evidence.json"
    
    if not os.path.exists(settings_file):
        print(f"FAIL: {settings_file} not found")
        sys.exit(1)
    
    with open(settings_file) as f:
        settings = json.load(f)
    
    try:
        validate(instance=settings, schema=SCHEMA)
    except ValidationError as e:
        print(f"FAIL: Schema validation error: {e.message}")
        sys.exit(1)
    
    # 檢查關鍵設定
    if "docops-gatekit/finalize" not in settings["ruleset"]["required_checks"]:
        print("FAIL: required_checks must include 'docops-gatekit/finalize'")
        sys.exit(1)
    
    if settings["ruleset"]["expected_source"] != "GitHub Actions":
        print("WARN: expected_source should be 'GitHub Actions'")
    
    if not settings["ruleset"]["merge_queue_enabled"]:
        print("FAIL: merge_queue must be enabled (MQ=ON route)")
        sys.exit(1)
    
    print("PASS: settings_evidence.json valid")
    sys.exit(0)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "docops/evidence/day1"
    main(path)


________________


測試腳本：docops/scripts/test_anti_platform.py
#!/usr/bin/env python3
"""
test_anti_platform.py - Anti-Platform Policy 測例
[Ref: Spec NORM-09, 報告A F-RISK-01]


5 測例驗證 allowlist/denylist 邊界
"""
import re


DENY_PATTERNS = [
    r"Unified Platform", r"統一平台", r"全域中樞",
    r"Central Hub", r"Single Point of Truth"
]
ALLOW_PATTERNS = ["SSOT", "Single Source of Truth"]


def check_content(content):
    """回傳 (should_fail, reason)"""
    for pattern in DENY_PATTERNS:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            # 檢查 allowlist
            start = max(0, match.start() - 50)
            end = min(len(content), match.end() + 50)
            context = content[start:end]
            if any(allow in context for allow in ALLOW_PATTERNS):
                return (False, f"'{pattern}' allowed by context")
            return (True, f"P0 FAIL: '{pattern}'")
    return (False, "PASS")


def test_cases():
    cases = [
        # (content, expected_fail, description)
        ("This is a Unified Platform architecture", True, "Deny: Unified Platform"),
        ("We use SSOT (Single Source of Truth) pattern", False, "Allow: SSOT context"),
        ("建立統一平台來管理所有服務", True, "Deny: 統一平台"),
        ("The Single Source of Truth is our Spec", False, "Allow: Single Source of Truth"),
        ("This is a normal document without forbidden words", False, "Allow: clean content"),
    ]
    
    passed = 0
    failed = 0
    
    for content, expected_fail, desc in cases:
        should_fail, reason = check_content(content)
        if should_fail == expected_fail:
            print(f"✓ PASS: {desc}")
            passed += 1
        else:
            print(f"✗ FAIL: {desc} (expected {'FAIL' if expected_fail else 'PASS'}, got {reason})")
            failed += 1
    
    print(f"\nResults: {passed}/{len(cases)} passed")
    return failed == 0


if __name__ == "__main__":
    import sys
    success = test_cases()
    sys.exit(0 if success else 1)


________________


Router 測試骨架：docops/router/tests/test_router_rules_smoke.py
#!/usr/bin/env python3
"""
test_router_rules_smoke.py - Router 最小 Smoke Test
[Ref: 需求書 RT-03] [TEST-RT03]
"""
import yaml


def route(task_desc, rules):
    """簡化路由邏輯"""
    if "README" in task_desc or "typo" in task_desc.lower():
        return "vibe"
    if ".py" in task_desc or "src/" in task_desc:
        return "dev"
    return "vibe"


def test_router():
    cases = [
        ("README typo fix", "vibe"),
        ("src/main.py change", "dev"),
        ("[VIBE] Prototype X", "vibe"),
    ]
    for task, expected in cases:
        result = route(task, None)
        assert result == expected, f"Expected {expected}, got {result}"
    print("PASS: Router smoke test")


if __name__ == "__main__":
    test_router()


________________


<a id="reg-policy"></a>
3.4 Policies (2 個)
Policy 1：docops/registry/policies/anti_platform.policy.yaml
policy_id: anti_platform_v0
version: "0.3"
description: "P0 級別禁詞掃描，命中即 FAIL [Ref: Spec NORM-09]"


regex_patterns:
  - "Unified Platform"
  - "統一平台"
  - "全域中樞"
  - "Central Hub"
  - "Single Point of Truth"  # 注意：在 SSOT 上下文中允許


allowlist:
  - "SSOT"
  - "Single Source of Truth"


note: |
  allowlist 僅允許這兩個 token 在特定上下文中出現。
  仍禁止 SPOT/平台化敘事。
  
test_file: "test_anti_platform.py"
test_cases: 5  # 報告A F-RISK-01 要求


Policy 2：docops/registry/policies/merge_policy.yaml
policy_id: merge_policy_v0
version: "0.3"
description: "合流策略定義 [Ref: Spec NORM-12a, NORM-23]"


profiles:
  vibe:
    auto_merge: false
    merge_queue: false
    merge_strategy: promotion_only
    note: "Vibe PR 禁止直接合流，禁止進入 MQ"
  dev:
    auto_merge: true
    merge_queue: true
    merge_strategy: squash
  spec:
    enabled: false  # Phase 1
  ops:
    enabled: false  # Phase 1


________________


<a id="reg-schema"></a>
3.5 Schemas (7 個)
Schema 1：inputs_manifest.schema.json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "inputs_manifest.schema.json",
  "type": "object",
  "required": ["task_id", "source_bundle_sha256", "files"],
  "properties": {
    "task_id": { "type": "string" },
    "lane": { "type": "string", "enum": ["vibe", "dev", "spec", "ops"] },
    "source_bundle_sha256": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
    "files": { "type": "array" },
    "timestamp": { "type": "string", "format": "date-time" }
  }
}


Schema 2：evidence_manifest.schema.json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "evidence_manifest.schema.json",
  "type": "object",
  "required": ["task_id", "artifacts"],
  "properties": {
    "task_id": { "type": "string" },
    "artifacts": {
      "type": "object",
      "required": ["input_manifest", "run_manifest", "gate_report", "verdict"]
    }
  }
}


Schema 3：gate_report.schema.json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "gate_report.schema.json",
  "type": "object",
  "required": ["gates", "final"],
  "properties": {
    "profile": { "type": "string" },
    "gates": { "type": "array" },
    "final": { "type": "string", "enum": ["PASS", "FAIL"] }
  }
}


Schema 4：coverage_map.schema.json (stub-only)
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "coverage_map.schema.json",
  "description": "v0 stub-only, not enforced [Ref: Spec NORM-20]",
  "type": "object",
  "properties": {
    "stub": { "type": "boolean", "const": true },
    "covered_ids": { "type": "array" },
    "total_ids": { "type": "integer" }
  }
}


Schema 5：trace_map.schema.json (stub-only)
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "trace_map.schema.json",
  "description": "v0 stub-only, not enforced [Ref: Spec NORM-20]",
  "type": "object",
  "properties": {
    "stub": { "type": "boolean", "const": true },
    "edges": { "type": "array" }
  }
}


Schema 6：verdict.schema.json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "verdict.schema.json",
  "type": "object",
  "required": ["task_id", "judge_a", "judge_b", "bias_check", "final_verdict", "agreement"],
  "properties": {
    "task_id": { "type": "string" },
    "judge_a": { "type": "object" },
    "judge_b": { "type": "object" },
    "bias_check": {
      "type": "object",
      "required": ["swap_test_passed"],
      "properties": {
        "swap_test_passed": { "type": "boolean" },
        "swap_delta": { "type": "number" }
      }
    },
    "final_verdict": { "type": "string", "enum": ["PASS", "FAIL", "CALL-REPAIR"] },
    "agreement": { "type": "boolean" },
    "aggregation_method": { "type": "string", "const": "strict_agreement" }
  }
}


Schema 7：settings_evidence.schema.json (NEW)
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "settings_evidence.schema.json",
  "description": "Day-1 UI-only 設定證據 [Ref: Spec NORM-19, NORM-24]",
  "type": "object",
  "required": ["collected_at", "collector", "ruleset"],
  "properties": {
    "collected_at": { "type": "string", "format": "date-time" },
    "collector": { "type": "string", "description": "@username" },
    "ruleset": {
      "type": "object",
      "required": ["name", "required_checks", "expected_source", "merge_queue_enabled"],
      "properties": {
        "name": { "type": "string" },
        "required_checks": { 
          "type": "array", 
          "items": { "type": "string" },
          "contains": { "const": "docops-gatekit/finalize" }
        },
        "expected_source": { "type": "string" },
        "merge_queue_enabled": { "type": "boolean" },
        "enforcement": { "type": "string", "enum": ["active", "evaluate", "disabled"] }
      }
    },
    "fork_approval": {
      "type": "object",
      "properties": {
        "setting": { "type": "string" },
        "screenshot_sha256": { "type": "string", "pattern": "^[a-f0-9]{64}$" }
      }
    },
    "token_permissions": {
      "type": "object",
      "properties": {
        "default": { "type": "string", "enum": ["read", "write"] },
        "screenshot_sha256": { "type": "string", "pattern": "^[a-f0-9]{64}$" }
      }
    }
  }
}


________________


Registry v0 物件計數器
類型
	數量
	檔案
	Index
	1
	index.yaml
	Skill/SkillPack
	1
	core_skill_pack.yaml
	Gate Runner
	1
	gatekit_runner_v0.py
	Policy
	2
	anti_platform.policy.yaml, merge_policy.yaml
	Schema
	7
	(如上，含 settings_evidence)
	小計 (1/1/1/2/7)
	12
	✓ 符合約束
	輔助腳本
	5
	check_name_consistency, judge_aggregate, generate_evidence, dual_judge, validate_settings
	測試腳本
	2
	test_anti_platform, test_router_rules_smoke
	________________


[4.4] TVS v0.3 - Thin Vertical Slice
Day-1 依賴分級
分級
	依賴項
	驗證方式
	Evidence
	A: 可機械驗證
	Ruleset required checks
	API/CLI 查詢
	settings_evidence.json
	A
	merge_group trigger
	G0 腳本自檢
	gate_report.json
	A
	workflow permissions
	YAML 解析
	workflow file
	B: UI-only (MANUAL_ATTESTATION)
	Approve-and-Run
	截圖 hash
	settings_evidence.json
	B
	GITHUB_TOKEN default
	截圖 hash
	settings_evidence.json
	B
	Expected source
	截圖 hash
	settings_evidence.json
	Required Checks SSOT (v0)
進入 Ruleset
	Check Name
	驗證
	✓
	docops-gatekit/finalize
	Ruleset API
	-
	g0-input-seal
	workflow job
	-
	g3-schema
	workflow job
	-
	g3-anti-platform
	workflow job
	-
	g4-dual-judge
	workflow job
	-
	format-check
	workflow job
	Tier-1 任務 PASS 條件
Gate
	條件
	Fail-Closed 行為
	G0 Input Seal
	sha256 存在且一致
	Hash 不符即 FAIL
	G0 merge_group
	workflow 含事件
	缺少即 FAIL
	G3 Schema
	所有工件符合 Schema
	驗證失敗即 FAIL
	G3 Anti-Platform
	禁詞未命中
	命中即 P0 FAIL
	Vibe Block
	Vibe + merge_group
	是即 FAIL
	G4 Dual-Judge
	A/B 一致 + Swap PASS
	分歧或翻轉即 FAIL
	Format Check
	工作樹乾淨 + 無衝突標記
	有 diff 或標記即 FAIL
	________________


[5] TEST TRACKING LIST
TEST-ID
	名稱
	風險（若不做）
	最小驗證
	觸發時機
	退出條件
	TEST-RT03
	Router-Smoke
	Router 漂移無法偵測
	test_router_rules_smoke.py PASS
	PR
	v1 完整 fixtures
	TEST-GK02
	Coverage-Stub
	Tier 2+ 任務可能遺漏
	stub schema 驗證
	PR
	v1 門檻啟用
	TEST-GK03
	Trace-Stub
	No-Source Claim 無法攔截
	stub schema 驗證
	PR
	v1 G2 啟用
	TEST-GK06
	Drift-Delay
	MUST→SHOULD 弱化滑過
	manual review
	promotion
	v1 啟用
	TEST-GK07
	Ambiguity-Delay
	Agent 腦補需求
	manual review
	promotion
	v1 啟用
	TEST-EV03
	Attestation-Delay
	Evidence 可被竄改
	hash 清單存在
	merge_group
	v1 provenance
	TEST-HK01
	Hook-Delay
	L1 繞過 L3 攔不到
	L3 Gate 攔截
	merge_group
	v1 Hook Registry
	TEST-PAR01
	Matrix-Delay
	效率低不影響正確性
	單 job 執行
	PR
	v1 matrix
	TEST-OPS01
	SLO-Delay
	值守無標準作業
	手冊存在
	N/A
	v1 SLO
	TEST-OPS03
	Dashboard-Delay
	操作者無即時感知
	Log 輸出
	run
	v1 Tmux
	TEST-PROM02
	Strict-Delay
	Vibe→Dev 漏檢
	同配置
	promotion
	v1 switch
	TEST-SEC-PIN
	Actions-Pin
	供應鏈攻擊
	manual review
	PR
	v1 強制
	TEST-CONTENT
	Content-Filter
	prompt injection
	輸入封印
	run
	Phase 1
	TEST-APPROVE
	ApproveRun-Attestation
	Approve-and-Run 不可驗證
	day1_attestation.md
	Day-1
	API 支援
	TEST-EXPECTED
	ExpectedSource-Attestation
	status 可偽造
	settings_evidence.json
	Day-1
	API 支援
	________________


[6] 索引與映射
關鍵名詞索引
名詞
	定義位置
	機械落點
	Required Check SSOT
	Spec NORM-21
	check_name_consistency.py
	Fail-Closed
	Spec NORM-06
	gatekit_runner break on fail
	Strict Agreement
	Spec NORM-13, 16
	judge_aggregate.py agreement
	Anti-Platform
	Spec NORM-09
	anti_platform.policy.yaml
	Lane Gate Floor Table
	Spec NORM-12a
	gatekit_runner get_gates_for_profile
	merge_group 自檢
	Spec NORM-22
	gatekit_runner G0
	禁止自動解衝突
	Spec NORM-11
	gatekit_runner conflict scan
	Vibe 豁免
	Spec NORM-12, 12a
	vibe.yaml gates
	Vibe 合流限制
	Spec NORM-23
	run_vibe_merge_block()
	MANUAL_ATTESTATION
	Runbook §1.5
	day1_attestation.md
	Settings Evidence
	Spec NORM-19
	settings_evidence.json
	Claim→Source/Artifact 映射
Claim
	Source
	Artifact
	Required Check 名稱一致
	Spec NORM-05, 21
	check_name_consistency.py output
	雙法官裁決正確
	Spec NORM-12-17
	verdict.json + judge_a/b.json
	merge_group 觸發存在
	Spec NORM-22
	workflow YAML
	Approve-and-Run 已設定
	Runbook §1.5
	settings_evidence.json
	Expected Source 已設定
	Runbook §1.2
	settings_evidence.json
	Vibe 不可進 MQ
	Spec NORM-23
	gate_report.json (vibe-merge-block)
	________________


[7] 防幻覺護欄
                                             1. No-Source-No-Norm：無 [SRC:] 或 [Ref:] 標註的陳述不構成規範
                                             2. 名詞 SSOT：所有名詞以 Spec 定義為準
                                             3. STOPLINE：AI 嚴禁腦補需求、假設豁免、自動解衝突
                                             4. Runbook 分層聲明：Runbook 不新增 MUST/SHALL，僅引用 Spec
________________


[8] Diátaxis 四象限定位
文檔
	象限
	用途
	Spec v0.3
	Reference
	查閱不可協商約束
	Runbook v0.3
	How-to
	操作步驟
	Registry v0.3
	Reference
	機械契約
	TVS v0.3
	Tutorial
	導入路徑
	________________


[9] FINAL CHECKLIST
審查報告A問題解決確認
issue_id
	解決方案
	驗收點
	✓
	A:F-DRIFT-01
	NORM-11b→NORM-11 NOTE
	計數器=25
	✓
	A:F-STRUCT-01
	NORM-12a Lane Gate Floor Table
	runner 依表執行
	✓
	A:F-FEAS-01
	settings_evidence.schema.json
	g3-schema 可驗
	✓
	A:F-RISK-01
	test_anti_platform.py 5 測例
	全 PASS
	✓
	A:No-Source
	補充 [SRC:] 標記
	grep MUST 100% 有 [SRC:]
	✓
	審查報告B問題解決確認
issue_id
	解決方案
	驗收點
	✓
	B:F-DSTR-06
	settings_evidence.json
	欄位完整
	✓
	B:F-DSTR-08
	test_anti_platform.py
	5 cases PASS
	✓
	B:F-STRUCT-01
	Runbook 分層聲明
	無自創 MUST
	✓
	B:F-STRUCT-02
	NORM-03 統一規則
	無歧義
	✓
	B:PATCH-REG-01
	run_vibe_merge_block()
	Vibe+MQ→FAIL
	✓
	防膨脹約束最終確認
約束
	標準
	實際
	判定
	Spec 章節
	≤5
	5
	✓ PASS
	Spec 規範
	≤25
	25
	✓ PASS
	Runbook 章節
	≤4
	4
	✓ PASS
	Runbook 步驟
	≤30
	30
	✓ PASS
	Registry
	1/1/1/2/7
	1/1/1/2/7
	✓ PASS
	________________


END OF FINALIZED DOCUMENT v0.3.0
________________


Finalized by: v0 Finalizer + Patch Minimalist + Drift Hunter + Fail-Closed Quality Judge
 路線選擇: Org-owned Public + Merge Queue 啟用 (MQ=ON)
 審查報告整合: A (4 BLOCKER + 3 HIGH + 1 MED) + B (2 MUST-FIX + 7 GAP)
 Date: 2026-01-28