"""
G0: Merge Group Check Gate
驗證 workflow 包含 merge_group 觸發器（TVS v0.4.1 §9 A5）
"""
from pathlib import Path
import re

def run(repo_root: Path):
    """
    檢查所有 workflow 是否包含 merge_group 觸發器
    Returns: (pass: bool, evidence: list[str])
    """
    workflows_dir = repo_root / ".github" / "workflows"

    if not workflows_dir.exists():
        return False, ["FAIL: .github/workflows directory not found"]

    results = []
    has_merge_group = False
    has_finalize_job = False

    for wf in workflows_dir.glob("*.yml"):
        content = wf.read_text()

        # 檢查 merge_group 觸發器
        if "merge_group" in content:
            has_merge_group = True
            results.append(f"PASS: {wf.name} contains merge_group trigger")

        # 檢查 finalize job name
        if "docops-gatekit/finalize" in content:
            has_finalize_job = True
            results.append(f"PASS: {wf.name} contains docops-gatekit/finalize job")

        # 檢查 on: 區塊結構
        on_match = re.search(r'on:\s*\n((?:\s+.+\n)*)', content)
        if on_match:
            on_block = on_match.group(1)
            if 'pull_request' in on_block:
                results.append(f"INFO: {wf.name} triggers on pull_request")
            if 'merge_group' in on_block:
                results.append(f"INFO: {wf.name} triggers on merge_group")

    all_pass = has_merge_group and has_finalize_job

    if not has_merge_group:
        results.append("FAIL: No workflow contains merge_group trigger")
    if not has_finalize_job:
        results.append("FAIL: No workflow contains docops-gatekit/finalize job name")

    return all_pass, results
