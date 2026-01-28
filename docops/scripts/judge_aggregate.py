#!/usr/bin/env python3
"""
Judge Aggregate - 確定性雙法官聚合器
依據架構指南表 7-4：雙法官裁決矩陣
"""
import json
from pathlib import Path
from datetime import datetime, timezone

def main(task_id: str):
    task_dir = Path("docops/evidence") / task_id
    
    # 讀取雙法官判決
    ja_path = task_dir / "judge_a_verdict.json"
    jb_path = task_dir / "judge_b_verdict.json"
    
    if not ja_path.exists():
        print(f"❌ FAIL: judge_a_verdict.json not found")
        return False
    if not jb_path.exists():
        print(f"❌ FAIL: judge_b_verdict.json not found")
        return False
    
    ja = json.loads(ja_path.read_text())
    jb = json.loads(jb_path.read_text())
    
    print("=" * 60)
    print("雙法官聚合裁決 (Deterministic Aggregator)")
    print("=" * 60)
    print(f"\nTASK_ID: {task_id}")
    print(f"\n📋 Judge A (Codex) - 結構審計:")
    print(f"   Final Verdict: {ja['final_verdict']}")
    print(f"   Checks: {sum(1 for v in ja['checks'].values() if v == 'PASS')}/{len(ja['checks'])} PASS")
    
    print(f"\n📋 Judge B (Claude) - 語義審計:")
    print(f"   Final Verdict: {jb['final_verdict']}")
    print(f"   Checks: {sum(1 for v in jb['checks'].values() if v == 'PASS')}/{len(jb['checks'])} PASS")
    
    # 裁決矩陣（表 7-4）
    ja_pass = ja["final_verdict"] == "PASS"
    jb_pass = jb["final_verdict"] == "PASS"
    
    if ja_pass and jb_pass:
        final = "PASS"
        action = "進入 Merge Queue ✅"
    elif ja_pass and not jb_pass:
        final = "FAIL"
        action = "退回 Repair Loop (Judge B 語義問題)"
    elif not ja_pass and jb_pass:
        final = "FAIL"
        action = "退回 Repair Loop (Judge A 結構問題)"
    else:
        final = "FAIL"
        action = "退回 Repair Loop (雙法官皆 FAIL)"
    
    print(f"\n{'=' * 60}")
    print(f"裁決矩陣結果:")
    print(f"  Judge A: {ja['final_verdict']}")
    print(f"  Judge B: {jb['final_verdict']}")
    print(f"  ─────────────────")
    print(f"  FINAL:   {final}")
    print(f"  ACTION:  {action}")
    print(f"{'=' * 60}\n")
    
    # 產出聚合判決
    aggregate = {
        "task_id": task_id,
        "aggregator": "judge_aggregate.py (deterministic)",
        "judge_a": {
            "id": ja["judge_id"],
            "verdict": ja["final_verdict"],
            "timestamp": ja["timestamp"]
        },
        "judge_b": {
            "id": jb["judge_id"],
            "verdict": jb["final_verdict"],
            "timestamp": jb["timestamp"]
        },
        "final_verdict": final,
        "action": action,
        "aggregated_at": datetime.now(timezone.utc).isoformat()
    }
    
    out_path = task_dir / "final_aggregate_verdict.json"
    out_path.write_text(json.dumps(aggregate, indent=2, ensure_ascii=False))
    print(f"✅ 聚合判決已寫入: {out_path}")
    
    return final == "PASS"

if __name__ == "__main__":
    import sys
    task_id = sys.argv[1] if len(sys.argv) > 1 else "tvs-20260128-001"
    success = main(task_id)
    sys.exit(0 if success else 2)
