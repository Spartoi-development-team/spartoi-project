#!/usr/bin/env python3
import json, subprocess, hashlib, sys
from pathlib import Path
from datetime import datetime, timezone

def sh(cmd): 
    try: return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.DEVNULL).strip()
    except: return ""

def main(task_id: str, repo_full: str):
    task_dir = Path("docops/evidence") / task_id
    task_dir.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat()
    
    # run_manifest
    run_manifest = {
        "task_id": task_id,
        "runner": {"env": "codespaces", "python": sh("python3 --version")},
        "git": {"branch": sh("git rev-parse --abbrev-ref HEAD") or "main", "commit": sh("git rev-parse HEAD") or "unknown"},
        "created_at": now
    }
    (task_dir / "run_manifest.json").write_text(json.dumps(run_manifest, indent=2))
    print("✅ run_manifest.json")
    
    # settings_evidence
    try:
        rulesets = json.loads(subprocess.check_output(f"gh api repos/{repo_full}/rulesets", shell=True, stderr=subprocess.DEVNULL))
    except:
        rulesets = []
    settings = {"task_id": task_id, "repo": repo_full, "captured_at": now, "rulesets": {"repo_rulesets": rulesets}, "attestations": []}
    (task_dir / "settings_evidence.json").write_text(json.dumps(settings, indent=2))
    print("✅ settings_evidence.json")
    
    print(f"\n📦 Evidence at: {task_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python docops/scripts/generate_evidence.py <TASK_ID> <OWNER/REPO>")
        sys.exit(2)
    main(sys.argv[1], sys.argv[2])
