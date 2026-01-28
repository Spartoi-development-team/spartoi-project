"""
G_Lane_Router: Lane 路由決策 Gate
需求書 RD-01: 敏感路徑命中 → 不能走 Vibe
"""
import fnmatch
import json
import subprocess
from pathlib import Path
import yaml

def get_changed_files(base_branch: str = "main") -> list:
    """取得變更的檔案清單"""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", base_branch],
            capture_output=True, text=True
        )
        return [f for f in result.stdout.strip().split("\n") if f]
    except:
        return []

def load_router_rules() -> dict:
    """載入路由規則"""
    rule_file = Path("docops/registry/rules/lane_router.yaml")
    if rule_file.exists():
        return yaml.safe_load(rule_file.read_text())
    return {}

def check_sensitive_paths(changed_files: list, rules: dict) -> list:
    """檢查是否命中敏感路徑"""
    hits = []
    sensitive_paths = rules.get("sensitive_paths", [])

    for sp in sensitive_paths:
        pattern = sp.get("pattern", "")
        for cf in changed_files:
            if fnmatch.fnmatch(cf, pattern):
                hits.append({
                    "file": cf,
                    "pattern": pattern,
                    "description": sp.get("description"),
                    "required_lane": sp.get("required_lane"),
                    "block_vibe": sp.get("block_vibe", False)
                })
    return hits

def run(task_dir: Path, lane: str = "dev"):
    """
    檢查 Lane 路由是否正確
    Returns: (pass: bool, evidence: list[str])
    """
    results = []
    rules = load_router_rules()

    if not rules:
        results.append("FAIL: lane_router.yaml not found")
        return False, results

    results.append("PASS: lane_router.yaml loaded")

    # 檢查敏感路徑定義
    sensitive_paths = rules.get("sensitive_paths", [])
    if len(sensitive_paths) >= 4:
        results.append(f"PASS: {len(sensitive_paths)} sensitive paths defined")
    else:
        results.append(f"WARN: Only {len(sensitive_paths)} sensitive paths defined")

    # 檢查 Lane 矩陣
    lane_matrix = rules.get("lane_matrix", {})
    if "vibe" in lane_matrix and "dev" in lane_matrix:
        results.append("PASS: vibe and dev lanes defined in matrix")
    else:
        results.append("FAIL: lane_matrix incomplete")
        return False, results

    # 檢查 Vibe 不能 merge
    if lane_matrix.get("vibe", {}).get("merge_allowed") == False:
        results.append("PASS: vibe.merge_allowed = false")
    else:
        results.append("FAIL: vibe.merge_allowed should be false")
        return False, results

    # 檢查 Dev 必須經過 gates
    dev_gates = lane_matrix.get("dev", {}).get("required_gates", [])
    if len(dev_gates) >= 4:
        results.append(f"PASS: dev lane requires {len(dev_gates)} gates")
    else:
        results.append("FAIL: dev lane should require more gates")
        return False, results

    return True, results

if __name__ == "__main__":
    ok, evidence = run(Path("."))
    print(f"Result: {'PASS' if ok else 'FAIL'}")
    for e in evidence:
        print(f"  {e}")
