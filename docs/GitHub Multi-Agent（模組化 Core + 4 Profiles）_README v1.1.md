GitHub Multi-Agent（模組化 Core + 4 Profiles）_README v1.1
外部名稱：GitHub Multi-Agent DocOps Framework
內部簡稱：GMA / docops-core
對應規格：SRS v1.1.0 ｜ TVS v0.4.1 ｜ v0 Pack v0.3.0
證據驅動的多代理 DevOps 治理框架，以機械閘門取代人工審查，實現可稽核、可回放的自動化流程。
Contents: §1 Overview · §2 Scope · §3 Architecture · §4 Layout · §5 Quickstart · §6 Contribute · §7 Docs · §8 Safety · §9 License
________________


1. Overview
控制平面（Actions）與執行平面（Codespaces）物理隔離；模組化 Core + 4 Profiles（Vibe/Dev/Spec/Ops）設計；Fail-Closed Gate + Evidence Bundle 約束多代理協作。v0 僅啟用 Vibe + Dev Lane。詳見 SRS。
________________


2. Scope & Non-Goals
In-Scope
* 機械閘門驅動 PR 驗收
* Evidence Bundle 產生
* Codespaces-first 執行環境
* Org-owned Public Repo（MQ 前提）
* Vibe + Dev Lane（v0 範圍）
Non-Goals
* 建立通用自動化平台
* 支援付費 API 依賴
* 在 README 定義新規範
________________


3. Architecture-at-a-Glance
┌─────────────────────────────────────────────────┐
│              Control Plane (Actions)            │
│  ┌─────────┐  ┌─────────┐  ┌─────────────────┐  │
│  │ Ruleset │→ │  Gates  │→ │  Merge Queue    │  │
│  └─────────┘  └─────────┘  └─────────────────┘  │
└───────────────────────┬─────────────────────────┘
                        ↓ Evidence
┌───────────────────────┴─────────────────────────┐
│            Execution Plane (Codespaces)         │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐           │
│  │ Vibe │ │ Dev  │ │ Spec │ │ Ops  │ ← Lanes   │
│  └──────┘ └──────┘ └──────┘ └──────┘           │
└─────────────────────────────────────────────────┘


↓ = Evidence 流向；Control Plane 執行 Gate 驗證後觸發 Merge Queue
________________


4. Repository Layout
路徑
	職責
	docops/registry/
	立法層：Skills、Gates、Policies、Rules
	docops/schemas/
	契約層：JSON Schema 定義
	evidence/
	稽核層：執行證據與驗收包（canonical）
	.github/workflows/
	Actions 與 Required Checks（須含 merge_group）
	.devcontainer/
	Codespaces 環境配置
	________________


5. Quickstart (Codespaces-first)
* Step 1: Fork/Clone 本 Repo（須為 Org-owned Public）
* Step 2: 點擊 Code → Codespaces → Create
* Step 3: 等待 devcontainer 自動建置完成
* Step 4: 建立分支並修改檔案
* Step 5: 提交 PR，等待 docops-gatekit/finalize 通過
* Step 6: Merge Queue 自動合流（需 Ruleset 啟用 MQ + workflow 監聽 merge_group）
故障處理見 Runbook；Codespaces 安全注意事項見 GitHub Docs: Security in Codespaces
________________


6. How to Develop / Contribute
合流由機械 Gate 裁決，預設零人工；若觸發 CR_OPEN/stopline 例外，依 SRS/TVS 指引人工介入。
* PR 觸發 Required Checks（docops-gatekit/finalize 為 Ruleset Required Check）
* Gates 驗證 Schema、禁詞、覆蓋率
* 產出 Evidence Bundle 供稽核
* 合流規則見 TVS §7
________________


7. Docs & SSOT Map
文檔
	角色
	位置
	SRS v1.1.0
	需求總契約（What/Why）
	SRS
	架構指南
	設計意圖與分層說明
	Architecture Guide
	v0 最小三件套
	Spec/Runbook/Registry v0 閉環
	v0 Pack
	TVS v0.4.1
	導入策略與薄垂直切片
	TVS
	Evidence 三件套
	驗收證據
	evidence/evidence_index.json（看 verdict）、tvs_section9_verdict.json、tvs_v0.4.1_complete_evidence_bundle_v2.json
	Diátaxis 映射: Tutorial=TVS · How-to=Runbook · Reference=SRS/Registry · Explanation=架構指南
AI Retrieval Rules
檢索優先：SRS → TVS → evidence_index → tvs_section9_verdict → bundle。
路徑 canonical：evidence/index.json（alias: evidence_index.json）。
缺源不得下結論；找不到標示 UNVERIFIED。
________________


8. Safety / Policy Pointers
檔案
	說明
	CLAUDE.md
	Agent 行為準則（需符合 schema，見 SRS FR-MEM-006）
	.github/copilot-instructions.md
	硬記憶：禁區、Wrongbook 防線
	docops/registry/policies/
	必備：anti_platform.policy.yaml、merge_policy.yaml
	Codespaces/Prebuild 安全：避免 secrets 落入 logs/prebuild，見 GitHub Docs。
Merge Queue 須 workflow 監聽 merge_group 事件，見 GitHub Docs: Managing a merge queue。
________________


9. License / Code of Conduct / Security
* LICENSE / CODE_OF_CONDUCT.md / SECURITY.md（若 repo 已提供）
________________


README v1.1 ｜ 升級自 v1.0 ｜ 依據審查報告 A/B 修補