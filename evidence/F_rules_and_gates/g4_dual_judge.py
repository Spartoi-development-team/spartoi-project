import json
from pathlib import Path
from datetime import datetime, timezone

def judge_a(task_dir: Path) -> dict:
    gr = task_dir / "gate_report.json"
    if not gr.exists():
        return {"id": "judge_a", "status": "FAIL", "reason": "gate_report.json not found"}
    data = json.loads(gr.read_text())
    ok = data.get("summary", {}).get("status") == "PASS"
    return {"id": "judge_a", "status": "PASS" if ok else "FAIL", "reason": "gate_report must PASS"}

def judge_b(task_dir: Path) -> dict:
    cnc = task_dir / "check_name_consistency.txt"
    if not cnc.exists():
        return {"id": "judge_b", "status": "FAIL", "reason": "check_name_consistency.txt not found"}
    ok = "OK" in cnc.read_text()
    return {"id": "judge_b", "status": "PASS" if ok else "FAIL", "reason": "check name must be OK"}

def run(task_dir: Path):
    ja, jb = judge_a(task_dir), judge_b(task_dir)
    status = "PASS" if ja["status"] == "PASS" and jb["status"] == "PASS" else "FAIL"
    verdict = {"task_id": task_dir.name, "status": status, "judges": [ja, jb], "created_at": datetime.now(timezone.utc).isoformat()}
    (task_dir / "verdict.json").write_text(json.dumps(verdict, indent=2))
    return (status == "PASS"), ["verdict.json"]
