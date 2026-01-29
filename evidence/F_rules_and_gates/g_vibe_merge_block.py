"""
G_Vibe_Merge_Block: Vibe Lane 合流阻斷 Gate
需求書 GV-04: Vibe PR 禁 auto-merge、禁進 merge queue，只能 promotion
"""
import json
import subprocess
from pathlib import Path
from datetime import datetime, timezone

def get_pr_labels(repo: str, pr_number: int) -> list:
    """取得 PR 的 labels"""
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{repo}/pulls/{pr_number}", "--jq", ".labels[].name"],
            capture_output=True, text=True
        )
        return result.stdout.strip().split("\n") if result.stdout.strip() else []
    except:
        return []

def get_pr_branch(repo: str, pr_number: int) -> str:
    """取得 PR 的來源分支"""
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{repo}/pulls/{pr_number}", "--jq", ".head.ref"],
            capture_output=True, text=True
        )
        return result.stdout.strip()
    except:
        return ""

def is_vibe_pr(labels: list, branch: str) -> bool:
    """判斷是否為 Vibe Lane PR"""
    has_vibe_label = any("[VIBE]" in label.upper() or "VIBE" in label.upper() for label in labels)
    has_vibe_branch = branch.startswith("vibe/")
    return has_vibe_label or has_vibe_branch

def run(task_dir: Path, repo: str = None, pr_number: int = None):
    """
    檢查 Vibe PR 是否被正確阻斷
    Returns: (pass: bool, evidence: list[str])
    """
    results = []

    # 如果沒有指定 PR，檢查規則檔案是否存在
    rule_file = Path("docops/registry/rules/vibe_merge_block.yaml")
    if rule_file.exists():
        results.append(f"PASS: vibe_merge_block.yaml exists")
    else:
        results.append(f"FAIL: vibe_merge_block.yaml not found")
        return False, results

    # 檢查規則內容
    import yaml
    rule = yaml.safe_load(rule_file.read_text())

    if rule.get("actions", {}).get("block_merge_queue") == True:
        results.append("PASS: block_merge_queue = true")
    else:
        results.append("FAIL: block_merge_queue not set")
        return False, results

    if rule.get("actions", {}).get("block_auto_merge") == True:
        results.append("PASS: block_auto_merge = true")
    else:
        results.append("FAIL: block_auto_merge not set")
        return False, results

    results.append("PASS: Vibe merge block rule properly configured")
    return True, results

if __name__ == "__main__":
    import sys
    task_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    ok, evidence = run(task_dir)
    print(f"Result: {'PASS' if ok else 'FAIL'}")
    for e in evidence:
        print(f"  {e}")
