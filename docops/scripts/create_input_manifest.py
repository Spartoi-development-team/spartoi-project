#!/usr/bin/env python3
import json, hashlib, sys
from pathlib import Path
from datetime import datetime, timezone

def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1024*1024), b""): h.update(chunk)
    return h.hexdigest()

def main(task_id, *files):
    task_dir = Path("docops/evidence") / task_id
    task_dir.mkdir(parents=True, exist_ok=True)
    inputs = []
    for f in (files or ["README.md"]):
        p = Path(f)
        if p.exists():
            inputs.append({"name": p.stem, "path": str(p), "sha256": sha256_file(p)})
    manifest = {"task_id": task_id, "created_at": datetime.now(timezone.utc).isoformat(), "inputs": inputs}
    (task_dir / "input_manifest.json").write_text(json.dumps(manifest, indent=2))
    print(f"✅ input_manifest.json ({len(inputs)} files)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python docops/scripts/create_input_manifest.py <TASK_ID> [files...]")
        sys.exit(2)
    main(sys.argv[1], *sys.argv[2:])
