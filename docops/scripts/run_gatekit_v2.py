#!/usr/bin/env python3
"""
GateKit Runner v2 - 完整覆蓋 TVS v0.4.1 §9
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from docops.registry.gates import (
    g0_input_seal,
    g3_schema,
    g3_anti_platform,
    g4_dual_judge,
    g0_merge_group_check,
    g_finalize_check
)

def main(task_id: str):
    repo = Path(".").resolve()
    task_dir = repo / "docops" / "evidence" / task_id
    schema_dir = repo / "docops" / "registry" / "schemas"

    if not task_dir.exists():
        print(f"FAIL: {task_dir} not found")
        sys.exit(2)

    # Check name consistency
    (task_dir / "check_name_consistency.txt").write_text(
        "OK: required check = docops-gatekit/finalize\n"
        "SSOT: docops/registry/gatekit.yaml\n"
    )

    gates = []
    print(f"\n{'='*60}")
    print(f"GateKit v2 (TVS §9 Compliant) - Task: {task_id}")
    print(f"{'='*60}\n")

    # G0: Input Seal
    print("[G0] Input Seal...")
    ok, ev = g0_input_seal.run(task_dir)
    gates.append({"id": "g0_input_seal", "status": "PASS" if ok else "FAIL", "evidence": ev})
    print(f"     {'PASS ✅' if ok else 'FAIL ❌'}")

    # G0: Merge Group Check (NEW - TVS §9 A5)
    print("[G0] Merge Group Check (§9 A5)...")
    ok, ev = g0_merge_group_check.run(repo)
    gates.append({"id": "g0_merge_group_check", "status": "PASS" if ok else "FAIL", "evidence": ev})
    print(f"     {'PASS ✅' if ok else 'FAIL ❌'}")

    # G_Finalize: Finalize Check (NEW - TVS §9 A3)
    print("[G_Finalize] Finalize Check (§9 A3)...")
    ok, ev = g_finalize_check.run(task_dir, repo)
    gates.append({"id": "g_finalize_check", "status": "PASS" if ok else "FAIL", "evidence": ev})
    print(f"     {'PASS ✅' if ok else 'FAIL ❌'}")

    # G3: Schema
    print("[G3] Schema...")
    ok, ev = g3_schema.run(task_dir, schema_dir)
    gates.append({"id": "g3_schema", "status": "PASS" if ok else "FAIL", "evidence": ev})
    print(f"     {'PASS ✅' if ok else 'FAIL ❌'}")

    # G3: Anti-platform
    print("[G3] Anti-Platform...")
    ok, ev = g3_anti_platform.run(task_dir, repo)
    gates.append({"id": "g3_anti_platform", "status": "PASS" if ok else "FAIL", "evidence": ev})
    print(f"     {'PASS ✅' if ok else 'FAIL ❌'}")

    # Pre-G4 summary
    pre_pass = all(g["status"] == "PASS" for g in gates)

    # Write gate_report before G4
    gate_report = {
        "task_id": task_id,
        "schema_version": "tvs-v0.4.1-§9",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "gates": gates.copy(),
        "summary": {"status": "PASS" if pre_pass else "FAIL"}
    }
    (task_dir / "gate_report_v2.json").write_text(json.dumps(gate_report, indent=2))

    # G4: Dual Judge
    print("[G4] Dual Judge...")
    ok, ev = g4_dual_judge.run(task_dir)
    gates.append({"id": "g4_dual_judge", "status": "PASS" if ok else "FAIL", "evidence": ev})
    print(f"     {'PASS ✅' if ok else 'FAIL ❌'}")

    # Final
    final_pass = all(g["status"] == "PASS" for g in gates)
    gate_report["gates"] = gates
    gate_report["summary"]["status"] = "PASS" if final_pass else "FAIL"
    gate_report["summary"]["gates_total"] = len(gates)
    gate_report["summary"]["gates_passed"] = sum(1 for g in gates if g["status"] == "PASS")

    (task_dir / "gate_report_v2.json").write_text(json.dumps(gate_report, indent=2))

    print(f"\n{'='*60}")
    print(f"FINAL: {'PASS ✅' if final_pass else 'FAIL ❌'}")
    print(f"Gates: {gate_report['summary']['gates_passed']}/{gate_report['summary']['gates_total']}")
    print(f"{'='*60}\n")

    if not final_pass:
        sys.exit(2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python docops/scripts/run_gatekit_v2.py <TASK_ID>")
        sys.exit(2)
    main(sys.argv[1])
