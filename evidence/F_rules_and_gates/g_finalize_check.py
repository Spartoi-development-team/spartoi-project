"""
G_Finalize: Finalize Check Gate
驗證 required check 名稱與 workflow job 名稱一致（TVS v0.4.1 §9 A3）
"""
import json
from pathlib import Path

REQUIRED_CHECK_NAME = "docops-gatekit/finalize"

def run(task_dir: Path, repo_root: Path):
    """
    檢查 finalize check 名稱一致性
    Returns: (pass: bool, evidence: list[str])
    """
    results = []

    # 1. 檢查 workflow job name
    workflow_path = repo_root / ".github" / "workflows" / "docops-gatekit.yml"
    if not workflow_path.exists():
        return False, ["FAIL: docops-gatekit.yml not found"]

    content = workflow_path.read_text()
    job_name_in_workflow = f'name: {REQUIRED_CHECK_NAME}' in content

    if job_name_in_workflow:
        results.append(f"PASS: Workflow contains job name '{REQUIRED_CHECK_NAME}'")
    else:
        results.append(f"FAIL: Workflow missing job name '{REQUIRED_CHECK_NAME}'")

    # 2. 檢查 settings_evidence (v2)
    se_path = task_dir / "settings_evidence_v2.json"
    if se_path.exists():
        se = json.loads(se_path.read_text())
        contains_finalize = se.get("A3_required_status_checks", {}).get("contains_finalize", False)

        if contains_finalize:
            results.append("PASS: settings_evidence confirms finalize in required_status_checks")
        else:
            results.append("WARN: settings_evidence does not confirm finalize (may need ruleset update)")
    else:
        results.append("INFO: settings_evidence_v2.json not found, skipping check")

    all_pass = job_name_in_workflow
    return all_pass, results
