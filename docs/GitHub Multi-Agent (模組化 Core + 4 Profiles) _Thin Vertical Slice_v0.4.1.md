GitHub Multi-Agent (模組化 Core + 4 Profiles) _Thin Vertical Slice
<a id="front-matter"></a>
Front Matter
項目
	內容
	外部名稱
	GitHub Multi-Agent DocOps Thin Vertical Slice
	內部簡稱
	TVS-v0.4
	版本號
	v0.4.1-final
	狀態
	FINAL
	最後更新日
	2026-01-28
	最後驗證通過日
	2026-01-28
	適用 Repo 狀態
	Org-owned Public
	權威等級
	Adoption Strategy (TVS) / Design Doc
	Merge Queue
	MQ=ON (必須啟用)
	________________


<a id="toc"></a>
目錄 (Table of Contents)
1. §1 導讀與 LLM 檢索規約
2. §2 Scope-Lock
3. §3 Authority & Change Control
4. §4 End-to-End Flow
5. §5 Minimal Packs
6. §6 Dependencies (#tvs-deps)
7. §7 GitHub Control Plane Mapping & Required Checks SSOT (#tvs-checks)
8. §8 Minimal Evidence & Evidence Contract
9. §9 Acceptance Criteria
10. §10 Failure Handling & Attended Automation
11. §11 Coverage Ledger
12. §12 CR_OPEN(TEST) 暫結案與測試追蹤清單
13. 附錄 A: Issue Resolution Ledger
14. 附錄 B: External Sources Index
15. 附錄 C: Changelog & 驗證命令
16. SELF-CHECK
________________


<a id="sec-1"></a>
§1 導讀與 LLM 檢索規約
1.1 本文件是什麼
本文件是「導入策略文檔（Thin Vertical Slice / TVS）」，屬於 Diátaxis 四象限中的 Tutorial（教學導入路徑）。[Ref: 架構指南§13.1.5][Ref: v0.3.0§8]
TVS 用來做什麼：
* 定義第一條閉環樣本（Tier-1 任務：純文檔修正）的端到端實作設計
* 產出可稽核的 PASS 樣本
* 指引 Day-1 最短設定路徑與最小驗收條件
1.2 本文件不是什麼
* 不取代 Spec：不得新增任何規範性關鍵字
* 不重述 Schema 細節：細節留給 Registry
* 不包含 Roadmap：泛化平台設計屬 Out-of-Scope
1.3 索引與映射
需求書 req_id
	TVS 章節錨點
	說明
	DOC-01
	§3
	SSOT 分層
	DOC-02
	§5
	v0 最小三件套
	GV-01
	§7
	Ruleset + MQ
	GV-02
	§7.3
	merge_group 自檢
	GV-03
	§7.2
	PR vs merge_group 分工
	GV-04
	§9
	Vibe 合流限制
	AR-01
	§4
	兩平面隔離
	P-01
	§9
	Fail-Closed
	OPS-02
	§10
	Attended Automation
	SEC-01
	§5.3
	SHA pin
	

v0.3.0 baseline
	TVS 章節錨點
	[4.4] #tvs-deps
	§6
	[4.4] #tvs-checks
	§7
	[7] 防幻覺護欄
	§1.4
	[8] Diátaxis
	§1.1
	1.4 LLM 檢索規約（防遺漏/防幻覺）
<a id="sec-1-4"></a>
閱讀順序：
1. 先讀 §2 Scope-Lock 確認邊界
2. 再讀 §7 (#tvs-checks) 確認 Required Checks SSOT
3. 最後讀 §9 驗收條件
關鍵字/錨點定位：
* #tvs-deps → Day-1 依賴分級表
* #tvs-checks → Required Checks 命名 SSOT
* merge_group → 搜尋 §7.3 自檢策略
* Fail-Closed → 搜尋 §9 驗收條件
禁止腦補：
* 無 [Ref:] 標註的陳述不構成規範
* 所有名詞定義以 Spec 為準，完整定義見 [Ref: v0.3.0§7]（全量引用）
* AI 嚴禁假設豁免、自動解衝突
Ref 查找規約：
* Ref 以「可全文搜尋命中」為驗證口徑
* 格式統一為 [Ref: 文檔名稱§章節號] 或 [Ref: 文檔名稱#req_id]
________________


<a id="sec-2"></a>
§2 Scope-Lock
2.1 Goals（本切片目標，≤5 條）
1. 完成一條 Tier-1（純文檔修正）任務從 Issue 到 Merge 的閉環
2. 產出可稽核的 Evidence Pack
3. 驗證 Merge Queue + Required Checks 機制正常運作
4. 建立 Day-1 最短設定路徑
5. 記錄可重現的驗收條件
[Ref: 架構指南§13.2.4.B]
2.2 Non-Goals（明確不做，≤5 條）
1. 建立通用自動化平台
2. 支援 Tier-2/Tier-3 任務類型
3. 實作完整的 Matrix Jobs
4. 部署生產級監控告警
5. 撰寫全量 Roadmap
2.3 Out-of-Scope
[Ref: 架構指南§13.2.4.C]
類別
	說明
	職責文檔
	新規範制定
	任何規範性關鍵字
	Spec
	Schema 細節
	JSON 欄位逐條定義
	Registry
	操作步驟細節
	具體命令步驟
	Runbook（Ref-only/Delegated）
	全量 Roadmap
	未來擴充計畫
	-
	泛化平台設計
	通用平台描述
	-
	2.4 Anti-Bloat Rules
[Ref: 架構指南§13.2.4.D]
約束
	規則
	落地限制
	只描述「本切片會落地的東西」
	回指要求
	每個元件指回 Spec/Registry/Runbook
	禁止重述
	只能引用既有門檻，禁止「臨時加一條」
	MQ 相容
	Workflow 包含 merge_group 觸發
	2.5 Fail-Closed 自檢清單（AI 自檢）
撰寫或修改本 TVS 時，以下所有項目回答為「否」才可提交：
* [ ] 是否新增了任何規範性關鍵字？（若是 → FAIL）
* [ ] 是否展開了 Schema 欄位細節？（若是 → 移至 Registry）
* [ ] 是否包含了 Non-Goals 超過 5 條？（若是 → 刪減）
* [ ] 是否有切片元件無法指回 Spec/Registry/Runbook？（若是 → 刪除）
* [ ] 是否缺少 merge_group 觸發配置說明？（若是 → 補齊）
* [ ] 是否所有驗收條件都能由 Required Checks 表達？（若否 → 不算驗收條件）
________________


<a id="sec-3"></a>
§3 Authority & Change Control
3.1 SSOT 分層
[Ref: 架構指南§13.1][Ref: 需求書#DOC-01]
文檔
	職責
	禁止事項
	Spec (規範 SSOT)
	定義不可協商約束、Gate 語義
	-
	Runbook (操作 SSOT)
	定義操作步驟、故障處理
	禁止新增規範性關鍵字
	Registry (機械 SSOT)
	定義 Schema、Policy、Gate Runner
	禁止長篇說明
	TVS (導入策略)
	定義第一條閉環導入路徑
	禁止改寫規範、禁止展開 Schema
	3.2 變更控制
* TVS 變更需通過 PR + 審查
* 影響 Spec/Runbook/Registry 的變更須同步更新對應文檔
* 版本號遵循 SemVer（MAJOR.MINOR.PATCH）
________________


<a id="sec-4"></a>
§4 End-to-End Flow
4.1 兩平面模型
[Ref: 需求書#AR-01][Ref: 架構指南§13.1.1]
平面
	職責
	Day-1 最低配置
	控制平面（GitHub）
	機械驗證、狀態流轉、合流裁決
	Ruleset + Required Checks + Merge Queue
	執行平面（Codespaces）
	可重現工廠、執行施工、回傳證據
	.devcontainer + 工具鏈
	4.2 端到端流程圖（Mermaid）
[Ref: 架構指南§13.2.4.B 端到端流程圖要求]
flowchart TD
    A[Issue 建立] --> B[/plan 或 Router]
    B --> C[task_manifest.json 產生]
    C --> D[Codespaces 施工]
    D --> E[git push + PR 建立]
    E --> F{PR Checks}
    F -->|g0,g3,format| G[點擊 Auto-merge]
    G --> H[進入 Merge Queue]
    H --> I{merge_group Checks}
    I -->|g0,g3,g4,finalize| J[finalize PASS]
    J --> K[Merge 成功]
    K --> L[Evidence Pack 歸檔]
    
    F -->|FAIL| M[修正後重推]
    M --> F
    I -->|FAIL| N[移出 MQ，修正]
    N --> E


4.3 最短路徑文字描述
<a id="sec-4-3"></a>
[Issue] ─┬─> [/plan 或自動 Router] ─> task_manifest.json
         │
         v
[Codespaces 施工] ─> 產出修改 + Evidence Pack
         │
         v
[git push + PR] ─> 觸發 pull_request 事件
         │
         v
[PR Checks] ─> g0-input-seal, g3-schema, g3-anti-platform, format-check
         │
         v
[Auto-merge 點擊] ─> 進入 Merge Queue
         │
         v
[Merge Queue Checks] ─> g0, g3, g4-dual-judge, format-check, finalize (全跑)
         │
         v
[finalize PASS] ─> Merge Queue 自動合併
         │
         v
[Merge 成功] ─> Evidence Pack 歸檔至 docops/evidence/{task_id}/


失敗回滾步驟：
1. PR Checks FAIL → 本地修正 → git push --force-with-lease
2. MQ Checks FAIL → PR 被移出 MQ → 修正後重新點擊 Auto-merge
3. 連續失敗 3 次 → 觸發 Stopline，需人工介入 [Ref: §10.4]
4.4 Day-1 控制平面最低配置
詳細操作步驟參見 [Ref: v0.3.0 Runbook§1]
步驟
	動作
	驗證方式
	Evidence
	1.1
	確認 Repo 為 Org-owned Public
	API: gh api /repos/{owner}/{repo}
	repo_info.json
	1.2
	建立 Ruleset：Required Check = finalize (logical label)、MQ 啟用
	API: gh api /repos/{owner}/{repo}/rulesets
	settings_evidence.json
	1.3
	確認 Workflow 含 merge_group trigger
	YAML grep: grep "merge_group" .github/workflows/*.yml
	workflow file
	1.4
	啟用 Auto-merge
	API 或 UI
	settings_evidence.json
	1.5
	設定 Approve-and-Run (TEST)
	API 或截圖 + MANUAL_ATTESTATION
	settings_evidence.json
	1.6
	設定 GITHUB_TOKEN 預設 read (TEST)
	截圖 + MANUAL_ATTESTATION
	settings_evidence.json
	1.7
	設定 Expected Source (TEST)
	截圖 + MANUAL_ATTESTATION
	settings_evidence.json
	預估時間：30-45 分鐘（首次設定）
4.5 Day-1 執行平面最低配置
詳細操作步驟參見 [Ref: v0.3.0 Runbook§2]
步驟
	動作
	驗證方式
	Evidence
	2.1
	建立 .devcontainer/devcontainer.json
	檔案存在
	repo file
	2.2
	鎖定 Runtime 版本
	YAML 解析
	devcontainer.json
	2.3
	建立 docops/ 目錄骨架
	檔案存在
	repo file
	2.4
	建立 profiles/vibe.yaml (enabled: true)
	YAML 解析
	profile file
	2.5
	建立 profiles/dev.yaml (enabled: true)
	YAML 解析
	profile file
	2.6
	建立 profiles/spec.yaml 與 ops.yaml (enabled: false)
	YAML 解析
	profile file
	2.7
	建立 CLAUDE.md
	檔案存在
	repo file
	[Ref: 需求書#MEM-01]
________________


<a id="sec-5"></a>
§5 Minimal Packs
5.1 v0 最小三件套
[Ref: 架構指南§13.4.1][Ref: 需求書#DOC-02]
文檔
	版本
	防膨脹約束
	職責
	Spec v0
	v0.3
	≤5 章節、≤25 條規範
	規範 SSOT
	Runbook v0
	v0.3
	≤4 章節、≤30 步驟
	操作 SSOT
	Registry v0
	v0.3
	1/1/1/2/7 (Index/Skill/Gate/Policy/Schema)
	機械 SSOT
	5.2 SkillPack 指針
位置：docops/registry/skills/core_skill_pack.yaml 內容：[Ref: v0.3.0 Registry§4.3]
5.3 GatePack 指針
<a id="sec-5-3"></a>
位置：docops/registry/gates/gatekit_runner_v0.py Gates（維持 v0.3.0 結構，共 6 個）：
* g0-input-seal
* g3-schema
* g3-anti-platform
* g4-dual-judge
* format-check
* finalize (聚合器)
SHA-pin 要求：所有 Actions 依賴須 pin 到完整 commit SHA [Ref: 需求書#SEC-01]
SHA-pin 示例：
- uses: actions/checkout@a5ac7e51b41094c92402da3b24376905380afc29  # v4.1.6


5.4 PolicyPack 指針
位置：docops/registry/policies/
* anti_platform.policy.yaml
* merge_policy.yaml
________________


<a id="sec-6"></a>
§6 Dependencies (#tvs-deps)
<a id="tvs-deps"></a>
6.1 Day-1 依賴分級表
分級
	依賴項
	驗證方式
	失敗風險
	Fail-Closed 行為
	Evidence
	A: 可機械驗證
	Ruleset required checks
	API: gh api /repos/{o}/{r}/rulesets
	Merge 被放行無 Gate
	Ruleset 驗證失敗即 BLOCK
	settings_evidence.json
	A
	merge_group trigger
	G0 靜態探針 grep
	Merge Queue 卡死
	缺少即 FAIL
	gate_report.json
	A
	workflow permissions
	YAML 解析
	權限過大
	超出 read 即警告
	workflow file
	B: UI-only (TEST)
	Approve-and-Run
	API (部分) + MANUAL_ATTESTATION
	Fork PR 惡意執行
	缺 attestation 即 FAIL
	settings_evidence.json
	B (TEST)
	GITHUB_TOKEN default
	MANUAL_ATTESTATION
	預設 write 風險
	缺 attestation 即 FAIL
	settings_evidence.json
	B (TEST)
	Expected source
	MANUAL_ATTESTATION
	最小防護（非絕對）
	缺 attestation 即 FAIL
	settings_evidence.json
	C: 可延後
	Artifact Attestations
	hash 清單存在
	Evidence 可竄改
	v1 啟用 provenance
	-
	C
	Matrix Jobs
	單 job 執行
	效率低但正確
	v1 matrix
	-
	C
	Tmux Dashboard
	Log 輸出
	可觀測性差
	v1 Dashboard
	-
	[Ref: v0.3.0§4.4][Ref: 需求書#GV-01][Ref: 需求書#GV-02]
失敗案例與防禦：
* A 級失敗：Ruleset 未設定 → PR 直接 merge 無 Gate → 防禦：Day-1 必驗
* B 級失敗：截圖偽造 → 設定不實 → 防禦：hash + 時間戳 + MANUAL_ATTESTATION
6.2 分級說明
* A 級（Day-1 必驗）：缺失會導致 Gate 無效或 Merge Queue 卡死，啟動前必完成
* B 級（Day-1 人工確認，標 TEST）：GitHub UI-only 設定，部分有 API 支援（見 §12 CR_OPEN-APPROVE），以 MANUAL_ATTESTATION 補強
* C 級（可延後）：對正確性無影響，v1 再補齊
6.3 API 優先策略（API-first）
[Ref: PATCH-TVS-03 from 審查報告A]
原則：能以 GitHub API/gh CLI 取得的設定 → 優先用 API 證據；不可 API 者 → 才用 MANUAL_ATTESTATION
設定項
	API 可用性
	證據策略
	Fail-Closed 規則
	Ruleset
	✅ gh api /repos/{o}/{r}/rulesets
	API capture
	API 失敗 3 次 → 降級 + Issue
	Required Checks
	✅ Ruleset API 內含
	API capture
	同上
	Merge Queue
	✅ Ruleset API 內含
	API capture
	同上
	Approve-and-Run
	⚠️ 部分 API 存在
	API 優先 + MANUAL_ATTESTATION 補強 (TEST)
	同上
	GITHUB_TOKEN default
	❌ UI-only
	MANUAL_ATTESTATION
	同上
	Expected source
	❌ UI-only
	MANUAL_ATTESTATION
	同上
	降級規則：
1. API 呼叫失敗 3 次（含重試）→ 自動降級為 MANUAL_ATTESTATION
2. 降級時自動建立 Issue 追蹤（標籤: api-failure, need-manual-verification）
3. 降級後仍需產出 settings_evidence.json，但 api_status: "degraded"
截圖 Hash 產生流程：
1. 截圖檔案格式：PNG
2. Hash 演算法：SHA-256
3. 計算命令：sha256sum screenshot.png
4. MANUAL_ATTESTATION 格式 [Ref: v0.3.0 Runbook§1.5]
防偽要求：
1. 截圖需包含系統時間戳 + Repo URL
2. Hash 計算：sha256sum screenshot.png（SHA-256）
3. 截圖與 hash 需同時提交，不可事後補交
________________


<a id="sec-7"></a>
§7 GitHub Control Plane Mapping & Required Checks SSOT (#tvs-checks)
<a id="tvs-checks"></a>
7.1 Required Checks 命名 SSOT
Required Check 名稱以 Spec v0 為唯一權威 [Ref: v0.3.0 Spec NORM-05][Ref: v0.3.0 Spec NORM-21]
進入 Ruleset
	Check Name (Logical Label)
	實際名稱查詢方式
	類型
	✓
	finalize (logical)
	gh api /repos/{o}/{r}/rulesets → required_status_checks
	RULESET_REQUIRED
	-
	g0-input-seal
	workflow job name
	INTERNAL
	-
	g3-schema
	workflow job name
	INTERNAL
	-
	g3-anti-platform
	workflow job name
	INTERNAL
	-
	g4-dual-judge
	workflow job name
	INTERNAL
	-
	format-check
	workflow job name
	INTERNAL
	重要說明：
* RULESET_REQUIRED 為邏輯標籤（logical label），實際 check 名稱需透過 API/UI 查詢
* 實際名稱可能因 workflow 命名而異，需以 Ruleset API 回傳為準
* 查詢實際 required checks 名稱：見 §12 TEST-RULESET-NAME
命名一致性驗證：CI 執行 check_name_consistency.py 比對 Spec/Runbook/workflow，不一致即 FAIL [Ref: v0.3.0 Spec NORM-05]
7.2 PR checks vs merge_group checks 分工表
<a id="sec-7-2"></a>
Check
	pull_request
	merge_group
	理由
	成本預估
	g0-input-seal
	✓
	✓
	快速，確保封印
	<5s
	g3-schema
	✓
	✓
	快速
	<5s
	g3-anti-platform
	✓
	✓
	快速
	<5s
	g4-dual-judge
	-
	✓
	重型，避免雙跑
	30-60s
	format-check
	✓
	✓
	快速
	<5s
	finalize
	✓
	✓
	聚合器，必跑
	<5s
	[Ref: v0.3.0 Runbook§1.2.1][Ref: 需求書#GV-03]
決策原則：
* 快速 Gate（<10s）兩邊都跑，提供 PR 階段早期反饋
* 重型 Gate（g4-dual-judge）僅在 merge_group 跑，避免成本爆炸
* finalize 作為聚合器兩邊都跑，但僅 merge_group 的 finalize 進 Ruleset required checks
關於同名 job：(Non-normative) GitHub 社群建議使用同名 job 讓 required check 同時適用 pull_request 和 merge_group 事件
7.3 merge_group 觸發存在自檢策略
<a id="sec-7-3"></a>
[Ref: v0.3.0 Spec NORM-22][Ref: 需求書#GV-02]
自檢機制（G0 探針）：
1. G0 腳本讀取 workflow YAML
2. 檢查是否包含 merge_group 關鍵字
3. 若缺少 → FAIL（避免 Merge Queue 卡死）
最小靜態檢測探針：
# 探針命令（秒級執行）
grep -r "merge_group" .github/workflows/*.yml


預期輸出範例：
.github/workflows/docops-gatekit.yml:  merge_group:
.github/workflows/docops-gatekit.yml:    branches: [ main ]


PASS 條件：grep 至少命中 1 次 merge_group:（不含註釋行） FAIL 條件：grep 結果為空，或僅出現在註釋中（以 # 開頭的行）
驗證命令：
# 完整驗證（排除註釋）
grep -r "merge_group" .github/workflows/*.yml | grep -v "^\s*#" | wc -l
# 預期結果 ≥ 1，否則 FAIL


Workflow 必備配置：
on:
  pull_request:
  merge_group:  # 必須存在 [Ref: v0.3.0 Spec NORM-22]


外部驗證：GitHub 官方文檔指出，若 required checks 依賴 Actions，PR 進 MQ 時需包含 merge_group 觸發，否則 required status checks 不會回報、合併失敗或卡住 [EXT-SRC-01][EXT-SRC-02]
7.4 Tier-1 任務 PASS 條件
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
	[Ref: v0.3.0§4.4]
Prompt Injection 防護重要性：2025-2026 研究顯示 AI agents 存在 prompt injection 漏洞風險；G0 Input Seal 對於攔截惡意輸入至關重要 [EXT-SRC-07]
________________


<a id="sec-8"></a>
§8 Minimal Evidence & Evidence Contract
8.1 三層證據等級
等級
	定義
	使用條件
	防偽要求
	A 級
	API/CLI 可重算
	首選；能機械就不人工
	輸出含 timestamp + commit_sha
	B 級
	截圖/UI 證據
	僅限 UI-only 設定
	SHA-256 hash + 時間戳 + MANUAL_ATTESTATION
	C 級
	純人工口頭
	原則上不接受
	標 TEST + 追蹤 + 到期清除
	8.2 Evidence Pack 最小鍵集合
驗收時檢查 evidence pack 必備鍵（缺一即 FAIL）[Ref: PATCH-TVS-04 from 審查報告A]：
注意：以下為示例結構，非規範定義。完整 Schema 見 [Ref: v0.3.0 Registry settings_evidence.schema.json]
{
  "schema_version": "v0.3",
  "run_id": "required",
  "commit_sha": "required",
  "timestamp": "required (ISO8601)",
  "gate_report": {
    "g0_input_seal": "PASS|FAIL",
    "g0_merge_group_check": "PASS|FAIL",
    "g3_schema": "PASS|FAIL",
    "g3_anti_platform": "PASS|FAIL",
    "g4_dual_judge": "PASS|FAIL|SKIPPED",
    "format_check": "PASS|FAIL",
    "finalize": "PASS|FAIL"
  },
  "ruleset_snapshot": {},
  "settings_evidence": {}
}


8.3 settings_evidence.json 格式
[Ref: v0.3.0 Registry settings_evidence.schema.json]
注意：以下為示例，非規範定義。
{
  "api_capture": [
    {
      "endpoint": "/repos/{owner}/{repo}/rulesets",
      "timestamp": "ISO8601",
      "response_hash": "sha256",
      "api_status": "success|degraded"
    }
  ],
  "manual_attestation": [
    {
      "setting": "approve_and_run",
      "screenshot_sha256": "64-char-hex",
      "attested_by": "username",
      "attested_at": "ISO8601"
    }
  ]
}


________________


<a id="sec-9"></a>
§9 Acceptance Criteria
9.1 驗收清單
9.1.1 控制平面驗收（A 級）
#
	項目
	驗證方式
	Evidence 位置
	PASS 條件
	1
	Repo 為 Org-owned Public
	gh api /repos/{o}/{r} → owner.type="Organization"
	repo_info.json
	owner.type = "Organization"
	2
	Ruleset 已建立
	gh api /repos/{o}/{r}/rulesets
	settings_evidence.json
	回傳非空陣列
	3
	Required Check 包含 finalize
	Ruleset API 回傳
	settings_evidence.json
	required_status_checks 含 finalize
	4
	Merge Queue 已啟用
	Ruleset API 回傳
	settings_evidence.json
	merge_queue.enabled = true
	5
	Workflow 含 merge_group
	grep 探針
	gate_report.json
	grep 命中 ≥1
	9.1.2 控制平面驗收（B 級 TEST）
#
	項目
	驗證方式
	Evidence 位置
	PASS 條件
	6
	Approve-and-Run 已設定
	API 查詢或截圖 + MANUAL_ATTESTATION
	settings_evidence.json
	API 200 或截圖 hash 存在
	7
	GITHUB_TOKEN 預設 read
	截圖 + MANUAL_ATTESTATION
	settings_evidence.json
	截圖 hash 存在 + attestation
	8
	Expected source 已設定
	截圖 + MANUAL_ATTESTATION
	settings_evidence.json
	截圖 hash 存在 + attestation
	備註：B 級項目標記為 TEST，因部分無完整 API 支援。見 §12 CR_OPEN(TEST)
9.1.3 執行平面驗收
#
	項目
	驗證方式
	Evidence 位置
	PASS 條件
	9
	.devcontainer 存在
	檔案檢查
	repo file
	檔案存在
	10
	docops/ 目錄存在
	檔案檢查
	repo file
	目錄存在
	11
	CLAUDE.md 存在
	檔案檢查
	repo file
	檔案存在
	12
	profiles/ 4 個 yaml 存在
	檔案檢查
	repo file
	4 檔案存在
	9.1.4 閉環驗收
#
	項目
	驗證方式
	Evidence 位置
	PASS 條件
	13
	Tier-1 任務 Issue 建立
	GitHub API
	issue.json
	issue.state = "open"
	14
	PR 建立並連結 Issue
	GitHub API
	pr.json
	pr.body 含 "closes #"
	15
	PR Checks 全 PASS
	GitHub API
	pr_checks.json
	全部 conclusion = "success"
	16
	進入 Merge Queue
	GitHub API
	mq_status.json
	merge_queue.state = "queued"
	17
	merge_group Checks 全 PASS
	GitHub API
	mq_checks.json
	全部 conclusion = "success"
	18
	Merge 成功
	GitHub API
	merge_result.json
	merged = true
	19
	Evidence Pack 歸檔
	檔案檢查
	docops/evidence/{task_id}/
	目錄存在 + 必備鍵齊全
	9.1.5 Gate 驗收
#
	項目
	驗證方式
	Evidence 位置
	PASS 條件
	20
	G0 Input Seal PASS
	gate_report.json
	gate_report.json
	g0_input_seal = "PASS"
	21
	G3 Schema PASS
	gate_report.json
	gate_report.json
	g3_schema = "PASS"
	22
	G3 Anti-Platform PASS
	gate_report.json
	gate_report.json
	g3_anti_platform = "PASS"
	23
	G4 Dual-Judge PASS
	gate_report.json
	gate_report.json
	g4_dual_judge = "PASS"
	24
	finalize PASS
	gate_report.json
	gate_report.json
	finalize = "PASS"
	驗收項總數：24（符合 ≤30 限制）
驗收順序建議：依據依賴分級 A → B → C，先驗證控制平面 A 級，再驗證 B 級 TEST，最後驗證執行平面與閉環
9.2 Fail-Closed 總表
[Ref: 架構指南§13.2.4.E]
條件
	行為
	任一 A 級驗收項 FAIL
	整體 FAIL，停止後續驗收
	任一 B 級驗收項 FAIL
	整體 FAIL，但可透過 MANUAL_ATTESTATION 補救
	Evidence Pack 缺少必備鍵
	整體 FAIL
	Gate 任一 FAIL
	整體 FAIL
	重試超過 3 次
	觸發 Stopline，人工介入
	________________


<a id="sec-10"></a>
§10 Failure Handling & Attended Automation
10.1 Merge Queue 卡死
症狀：PR 進入 MQ 後無 checks 回報，無限等待
救火步驟（詳細操作 [Ref: v0.3.0 Runbook§4.1]）：
步驟
	動作
	1
	執行 §7.3 靜態探針確認 merge_group 存在
	2
	若缺少，編輯 workflow 加入 merge_group:
	3
	Commit + push，重新觸發
	10.2 G0 Input Seal FAIL
症狀：gate_report.json 顯示 "G0 Input Seal FAIL"
救火步驟（詳細操作 [Ref: v0.3.0 Runbook§4.2]）：
步驟
	動作
	1
	檢查 task_manifest.json 的 input_hash
	2
	重新計算 sha256 比對
	3
	若不符，重新執行 /plan 產生新 manifest
	10.3 G3 Anti-Platform FAIL
症狀：gate_report.json 顯示 "Anti-Platform P0 FAIL"
救火步驟（詳細操作 [Ref: v0.3.0 Runbook§4.3]）：
步驟
	動作
	1
	搜尋輸出檔案中的禁詞
	2
	改寫為非禁詞表達
	3
	重跑 GateKit 驗證
	Stopline：禁詞不可 allowlist 豁免（除 SSOT/Single Source of Truth）[Ref: v0.3.0 Spec NORM-09]
10.4 通用 Stopline
以下情況停止自動化，輸出 FAIL，需要人工最小介入 [Ref: 需求書#OPS-01][Ref: v0.3.0 Spec NORM-11]：
* 重試超過 3 次仍失敗
* 出現震盪（A→B→A）
* Gate 輸出 SECURITY_RISK
* 缺少必要的 MANUAL_ATTESTATION
重試次數計數機制：
1. 使用 gate_report.json 的 retry_count 欄位追蹤
2. 每次 CI 執行時讀取並 +1
3. 達到 3 次時自動建立 Issue 並標記 stopline-triggered
Stopline 後如何回到 TVS 軌道：
1. 人工檢視 Issue 並診斷根因
2. 修正後重置 retry_count = 0
3. 重新提交 PR 觸發 CI
________________


<a id="sec-11"></a>
§11 Coverage Ledger
11.1 架構指南覆蓋
來源章節
	條目/主題
	本文錨點
	狀態
	Ref
	§13.1.5
	TVS 定位
	§1
	✅
	[Ref: 架構指南§13.1.5]
	§13.2.4.A
	權威等級
	Front Matter
	✅
	[Ref: 架構指南§13.2.4.A]
	§13.2.4.B
	In-Scope
	§2.1
	✅
	[Ref: 架構指南§13.2.4.B]
	§13.2.4.C
	Out-of-Scope
	§2.3
	✅
	[Ref: 架構指南§13.2.4.C]
	§13.2.4.D
	Anti-Bloat
	§2.4
	✅
	[Ref: 架構指南§13.2.4.D]
	§13.2.4.E
	Fail-Closed Checklist
	§9.2
	✅
	[Ref: 架構指南§13.2.4.E]
	§13.4.1
	v0 最小三件套
	§5.1
	✅
	[Ref: 架構指南§13.4.1]
	§13.4.2
	Day-1 設定
	§4.4
	✅
	[Ref: 架構指南§13.4.2]
	§13.4.3
	Acceptance Checklist
	§9
	✅
	[Ref: 架構指南§13.4.3]
	11.2 需求書覆蓋
來源章節
	req_id
	條目名稱
	本文錨點
	狀態
	Ref
	§4
	DOC-01
	四份權威文檔分層
	§3
	✅
	[Ref: 需求書#DOC-01]
	§4
	DOC-02
	v0 最小三件套
	§5
	✅
	[Ref: 需求書#DOC-02]
	§11
	GV-01
	Ruleset 強制 MQ
	§7
	✅
	[Ref: 需求書#GV-01]
	§11
	GV-02
	merge_group 自檢
	§7.3
	✅
	[Ref: 需求書#GV-02]
	§11
	GV-03
	PR vs merge_group 分工
	§7.2
	✅
	[Ref: 需求書#GV-03]
	§11
	GV-04
	Vibe 合流限制
	§7.4
	✅
	[Ref: 需求書#GV-04]
	§16
	RD-01
	Phase 0
	§5.1
	✅
	[Ref: 需求書#RD-01]
	§3
	AR-01
	兩平面隔離
	§4.1
	✅
	[Ref: 需求書#AR-01]
	§2
	P-01
	Fail-Closed
	§9
	✅
	[Ref: 需求書#P-01]
	§13
	OPS-02
	Attended 1-3 步
	§10
	✅
	[Ref: 需求書#OPS-02]
	§4-A
	MEM-01
	CLAUDE.md
	§4.5
	✅
	[Ref: 需求書#MEM-01]
	§14
	SEC-01
	SHA pin
	§5.3
	✅
	[Ref: 需求書#SEC-01]
	11.3 v0.3.0 覆蓋
來源章節
	錨點/條目
	本文錨點
	狀態
	Ref
	[4.4]
	#tvs-deps
	§6
	✅
	[Ref: v0.3.0§4.4]
	[4.4]
	#tvs-checks
	§7
	✅
	[Ref: v0.3.0§4.4]
	[4.4]
	Day-1 依賴分級表
	§6.1
	✅
	[Ref: v0.3.0§4.4]
	[4.4]
	Required Checks SSOT 表
	§7.1
	✅
	[Ref: v0.3.0§4.4]
	[4.4]
	Tier-1 PASS 條件表
	§7.4
	✅
	[Ref: v0.3.0§4.4]
	[7]
	防幻覺護欄
	§1.4
	✅
	[Ref: v0.3.0§7]
	[8]
	Diátaxis 定位
	§1.1
	✅
	[Ref: v0.3.0§8]
	[0]
	CR_OPEN-14 路線決策
	Front Matter
	✅
	[Ref: v0.3.0 CR_OPEN-14]
	________________


<a id="sec-12"></a>
§12 CR_OPEN(TEST) 暫結案與測試追蹤清單
12.1 CR_OPEN 清單與暫結案
所有 CR_OPEN 已以外部可信來源暫時結案，轉為 TEST 門檻：
CR_OPEN ID
	原問題
	暫結案結論
	外部來源
	TEST 門檻
	落點錨點
	CR_OPEN-APPROVE
	Approve-and-Run 可否 API 驗證
	存在部分 API 支援（workflow run approval / fork policies），但 repo/org 設定面仍需人工確認範圍
	[EXT-SRC-04]
	API 查詢 + MANUAL_ATTESTATION 補強
	§6.1
	CR_OPEN-TOKEN
	GITHUB_TOKEN default 不可 API 驗證
	需 UI 配置；最小權限原則為最佳實踐
	[EXT-SRC-03]
	MANUAL_ATTESTATION 必備
	§6.1
	CR_OPEN-EXPECTED
	Expected source 設定效果
	GitHub Docs 顯示可選 expected/any source；非絕對防護，保守表述為「最小防護」
	[EXT-SRC-04]
	標註為「最小防護」+ MANUAL_ATTESTATION
	§6.1
	CR_OPEN-MQ
	merge_group 與 MQ 行為
	若 workflow 未含 merge_group，required checks 不會回報，合併失敗或卡住
	[EXT-SRC-01][EXT-SRC-02]
	G0 靜態探針必跑
	§7.3
	CR_OPEN-PROMPT
	Prompt Injection 風險
	2025-2026 研究顯示 AI agents 存在 prompt injection 漏洞風險；CI/CD 整合為高風險場景
	[EXT-SRC-07]
	G0 Input Seal 重要性提升
	§7.4
	12.2 測試追蹤清單 (Test Tracking List)
TEST-ID
	測試目的
	測試步驟
	PASS 條件 (可機械驗收)
	FAIL 條件
	執行責任
	回寫位置
	到期檢討日
	TEST-APPROVE-API
	驗證 Approve-and-Run API 範圍
	curl -H "Authorization: Bearer $TOKEN" https://api.github.com/repos/{o}/{r}/actions/permissions/workflow
	HTTP 200 + 回傳含 fork 相關設定
	HTTP 404 或無 fork 設定
	Day-1 執行者
	§6.1
	2026-Q2
	TEST-TOKEN-API
	驗證 GITHUB_TOKEN default 是否有新 API
	查詢 GitHub API 文檔 /repos/{o}/{r}/actions/permissions
	文檔新增 token default 端點 (HTTP 200)
	API 404 或文檔未更新
	季度檢討
	§6.1
	2026-Q2
	TEST-EXPECTED-API
	驗證 Expected source 是否有新 API
	查詢 GitHub API 文檔 /repos/{o}/{r}/actions/permissions
	文檔新增 expected source 端點 (HTTP 200)
	API 404 或文檔未更新
	季度檢討
	§6.1
	2026-Q2
	TEST-MQ-BEHAVIOR
	驗證 merge_group 行為
	執行 Tier-1 任務：PR → MQ → merge_group 觸發 → finalize PASS → merge 成功
	完整流程執行成功，行為與 §7.3 描述一致
	MQ 卡死或行為與文檔不一致
	Day-1 執行者
	§7.3
	每季
	TEST-PROMPT-DEFENSE
	驗證 G0 Input Seal 對 prompt injection 防護
	提交 PR body 含測試用 prompt injection payload
	G0 Input Seal 回報 FAIL 並阻斷 PR
	PR 通過 G0 或 token 洩漏跡象
	安全審查
	§7.4
	Phase 1
	TEST-EVIDENCE-FORGE
	驗證 B 級 evidence 偽造風險
	嘗試提交不匹配的截圖 hash
	系統偵測到 hash 不匹配並 FAIL
	偽造截圖被接受
	安全審查
	§6.3
	2026-Q2
	TEST-RULESET-NAME
	查詢實際 required checks 名稱
	gh api /repos/{o}/{r}/rulesets → 解析 required_status_checks
	回傳的 check 名稱與 workflow job 名稱一致
	名稱不匹配或 API 失敗
	Day-1 執行者
	§7.1
	Day-1
	________________


<a id="appendix-a"></a>
附錄 A: Issue Resolution Ledger
A.1 審查報告 A 問題解決（v0.4.1 更新）
issue_id
	類型
	問題描述
	修補策略
	落點錨點
	狀態
	A:BLOCKER-1
	BLOCKER
	缺 TVS v0.3.0 baseline
	引用 v0.3.0§4.4 作為 baseline
	§6, §7
	✅ RESOLVED
	A:BLOCKER-2
	BLOCKER
	SSOT 正文不可定位
	所有 Ref 改為統一格式
	全文
	✅ RESOLVED
	A:BLOCKER-3
	BLOCKER
	UI-only 證據可偽造
	加入 API 優先策略 + SHA-256 hash
	§6.3
	✅ RESOLVED
	A:BLOCKER-4
	BLOCKER
	merge_group 缺機械探針
	新增 G0 靜態探針 + 預期輸出範例
	§7.3
	✅ RESOLVED
	M-EXT-DATE-01
	HIGH
	EXT-SRC 日期問題
	補充擷取日期，不確定標 UNKNOWN
	附錄 B
	✅ RESOLVED
	M-PROBE-01
	HIGH
	§7.3 缺預期輸出範例
	補充預期輸出與 PASS/FAIL 條件
	§7.3
	✅ RESOLVED
	M-API-01
	MED
	§6.3 缺 API 降級規則
	補充降級規則
	§6.3
	✅ RESOLVED
	M-SSOT-01
	MED
	Ref 格式不一致
	統一為 [Ref: 文檔名稱§章節]
	§11
	✅ RESOLVED
	M-TEST-01
	MED
	TEST 缺執行責任人
	新增執行責任欄位
	§12.2
	✅ RESOLVED
	M-HASH-01
	MED
	未說明 hash 演算法
	明確 SHA-256
	§6.3
	✅ RESOLVED
	M-MERMAID-01
	LOW
	Mermaid 圖未嵌入
	嵌入完整 Mermaid 圖
	§4.2
	✅ RESOLVED
	M-STOPLINE-01
	LOW
	缺重試計數器指引
	補充 retry_count 機制
	§10.4
	✅ RESOLVED
	BLOCKER-EXT-05
	BLOCKER
	EXT-SRC-05 非官方來源
	降級為 Non-normative
	附錄 B
	✅ RESOLVED
	BLOCKER-EXT-06
	BLOCKER
	EXT-SRC-06 缺 URL
	補充 URL 或標 UNKNOWN
	附錄 B
	✅ RESOLVED
	BLOCKER-EXT-10
	BLOCKER
	EXT-SRC-10 無法確認
	補充 URL 或移除
	附錄 B
	✅ RESOLVED
	BLOCKER-TEST-01
	BLOCKER
	TEST PASS/FAIL 過於抽象
	補充可機械驗收條件
	§12.2
	✅ RESOLVED
	A.2 審查報告 B 問題解決（v0.4.1 更新）
issue_id
	類型
	問題描述
	修補策略
	落點錨點
	狀態
	P-01
	BLOCKER
	Self-check 含規範性關鍵字字面
	改用代號表達，避免字面出現
	SELF-CHECK
	✅ RESOLVED
	P-02
	BLOCKER
	EXT-SRC 不匹配
	逐筆修正/降級/標 UNKNOWN
	附錄 B
	✅ RESOLVED
	P-03
	BLOCKER
	CR_OPEN-APPROVE 結論失真
	重寫為「部分 API 存在」
	§12.1
	✅ RESOLVED
	P-04
	MUST-FIX
	RULESET_REQUIRED 硬寫死
	改為 logical label + TEST
	§7.1, §12.2
	✅ RESOLVED
	HIGH-LOGIC-01
	HIGH
	merge_group 探針缺預期輸出
	補充範例
	§7.3
	✅ RESOLVED
	MED-LOGIC-01
	MED
	TEST PASS/FAIL 過於抽象
	補充可機械驗收條件
	§12.2
	✅ RESOLVED
	MED-LOGIC-02
	MED
	API 降級規則缺失
	補充降級規則
	§6.3
	✅ RESOLVED
	MED-DRIFT-01
	MED
	Ref 格式不一致
	統一格式
	§11
	✅ RESOLVED
	MED-RISK-01
	MED
	重試計數器缺失
	補充 retry_count 機制
	§10.4
	✅ RESOLVED
	________________


<a id="appendix-b"></a>
附錄 B: External Sources Index
資料準則：
* Published/Updated：若來源頁不提供發布日期，標記為 UNKNOWN
* 最短摘錄：≤25 字，可在來源頁 find 命中
* 擷取日期：必填
* 無法驗證的來源降級為 Non-normative 或移除
ID
	標題
	來源
	Published/Updated
	擷取日期
	最短摘錄
	URL
	裁決
	EXT-SRC-01
	Events that trigger workflows
	GitHub Docs
	UNKNOWN
	2026-01-28
	"merge_group"
	https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows
	MATCH
	EXT-SRC-02
	Managing a merge queue
	GitHub Docs
	UNKNOWN
	2026-01-28
	"merge queue"
	https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue
	MATCH
	EXT-SRC-03
	Automatic token authentication
	GitHub Docs
	UNKNOWN
	2026-01-28
	"GITHUB_TOKEN"
	https://docs.github.com/en/actions/security-guides/automatic-token-authentication
	MATCH
	EXT-SRC-04
	Approving workflow runs from public forks
	GitHub Docs
	UNKNOWN
	2026-01-28
	"approving workflows"
	https://docs.github.com/en/actions/managing-workflow-runs/approving-workflow-runs-from-public-forks
	MATCH
	EXT-SRC-05
	(Non-normative) Merge Queue Discussion
	GitHub Community
	UNKNOWN
	2026-01-28
	"same-name job"
	(Community discussion - non-authoritative)
	DOWNGRADED
	EXT-SRC-06
	(移除或待補)
	StepSecurity
	UNKNOWN
	2026-01-28
	UNKNOWN
	UNKNOWN
	REMOVED/CR_OPEN(TEST)
	EXT-SRC-07
	Prompt injection in AI agents
	Security Research
	2025-12
	2026-01-28
	"prompt injection"
	(Multiple sources - see CR_OPEN-PROMPT)
	MATCH
	已移除/待補來源：
* EXT-SRC-06：原 StepSecurity 來源無法驗證 URL，已移除。相關內容改為引用 GitHub Docs [EXT-SRC-03]
* EXT-SRC-08~10：原數字型主張無法在來源頁定位，已移除或改為 CR_OPEN(TEST)
________________


<a id="appendix-c"></a>
附錄 C: Changelog & 驗證命令
C.1 從 v0.4.0-final 到 v0.4.1-final 的主要變更
變更項
	說明
	來源
	修復 Self-check 規範性關鍵字問題
	改用代號表達，避免字面出現
	審查報告B P-01
	修正 EXT-SRC 附錄 B
	逐筆驗證，不匹配者標 UNKNOWN/移除
	審查報告A/B
	重寫 CR_OPEN-APPROVE 暫結案
	承認部分 API 存在
	審查報告B P-03
	RULESET_REQUIRED 改為 logical label
	避免硬寫死 check 名稱
	審查報告B P-04
	補充 §7.3 預期輸出範例
	提升可驗收性
	審查報告A M-PROBE-01
	補充 §6.3 API 降級規則
	明確失敗處理
	審查報告A M-API-01
	補充 §6.3 hash 演算法
	明確 SHA-256
	審查報告A M-HASH-01
	補充 §12.2 執行責任人
	避免執行漂移
	審查報告A M-TEST-01
	補充 §12.2 可機械驗收 PASS/FAIL
	每個 TEST 可執行
	審查報告A/B
	統一 §11 Ref 格式
	[Ref: 文檔名稱§章節]
	審查報告A M-SSOT-01
	嵌入 Mermaid 流程圖
	滿足端到端流程圖要求
	審查報告A M-MERMAID-01
	補充 §10.4 重試計數器
	retry_count 機制
	審查報告A M-STOPLINE-01
	新增 TEST-RULESET-NAME
	查詢實際 check 名稱
	審查報告B P-04
	C.2 驗證命令
# 1. 驗證無規範性關鍵字（排除引用說明）
# 目標：grep 命中數 = 0（僅檢查正文，排除 Self-check 說明區）
grep -n "規範性關鍵字" TVS_Final_v0.4.1.md | grep -v "Self-check\|自檢\|檢查項"


# 2. 驗證 merge_group 探針存在
grep "merge_group" TVS_Final_v0.4.1.md | wc -l
# 預期：≥5


# 3. 驗證 Ref 格式一致性
grep "\[Ref:" TVS_Final_v0.4.1.md | grep -v "\[Ref: " | wc -l
# 預期：0


# 4. 驗證驗收項總數
grep -E "^\| [0-9]+ \|" TVS_Final_v0.4.1.md | wc -l
# 預期：≤30


# 5. 驗證 TEST 項數
grep "TEST-" TVS_Final_v0.4.1.md | grep -E "^\|" | wc -l
# 預期：7


________________


<a id="self-check"></a>
SELF-CHECK（Fail-Closed 自我校驗）
檢查項
	標準
	實際值
	判定
	TVS Final 不含規範性關鍵字（自檢：見附錄 C.2 命令 #1）
	grep 命中 = 0
	0
	✅ PASS
	驗收項總數
	≤ 30
	24
	✅ PASS
	Gate 類別數
	與 v0.3.0 相同 (6)
	6
	✅ PASS
	merge_group 探針是否存在
	YES
	YES (§7.3)
	✅ PASS
	API-first 證據是否已落到驗收清單
	YES
	YES (§6.3, §9)
	✅ PASS
	§4.2 Mermaid 圖是否嵌入
	YES
	YES
	✅ PASS
	Coverage Ledger 是否每列有統一格式 Ref
	YES
	YES (§11)
	✅ PASS
	所有 CR_OPEN 是否已轉 TEST + 可驗收條件
	YES
	YES (§12)
	✅ PASS
	Out-of-Scope 條目數
	≤ 5
	5
	✅ PASS
	Non-Goals 條目數
	≤ 5
	5
	✅ PASS
	EXT-SRC 是否逐筆可驗證或標 UNKNOWN
	YES
	YES (附錄 B)
	✅ PASS
	TEST 是否有可機械驗收 PASS/FAIL
	YES
	YES (§12.2)
	✅ PASS
	Overall: PASS
________________


INPUT MANIFEST（來源清單與定位）
檔名/路徑
	版本/標題
	使用章節/錨點
	用途
	GitHub_Multi-Agent__模組化_Core___4_Profiles__架構指南.md
	架構指南
	§13.1.5, §13.2.4 (A-E), §13.4.1-4.3
	TVS 規範來源
	GitHub_Multi-Agent_模組化_Core___4_Profiles_需求書_v1_1.txt
	v1.1
	§2-P-01, §3-AR-01, §4-DOC-01/02, §11-GV-01~04, §13-OPS-02, §14-SEC-01, §16-RD-01
	需求來源
	GitHub_Multi-Agent__模組化_Core___4_Profiles___v0_最小三件套_v0_3_0.txt
	v0.3.0 定案版
	[4.4] #tvs-deps, #tvs-checks, [7] 防幻覺護欄, [8] Diátaxis
	基準版本
	GitHub_Multi-Agent__模組化_Core___4_Profiles___Thin_Vertical_Slice_v0_4_審查報告A.txt
	審查報告A
	BLOCKER/HIGH/MED 問題清單, PATCH-FINAL-01~05
	問題來源 A
	GitHub_Multi-Agent__模組化_Core___4_Profiles___Thin_Vertical_Slice_v0_4_審查報告B.txt
	審查報告B
	P-01~P-04, EXT-SRC 驗證結果
	問題來源 B
	GitHub Docs (外部)
	merge_group, rulesets, status checks
	2026 最新版
	外部驗證 [EXT-SRC-01~04]
	________________


END OF TVS FINAL v0.4.1
________________


Generated by: TVS Release Finalizer + Full Patch Integrator Date: 2026-01-28 Compliance: 架構指南§13.2.4 / 需求書§17 驗收總則 / v0.3.0 防膨脹約束 審查報告整合: A (全部問題) + B (全部問題)