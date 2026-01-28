import json, hashlib
from pathlib import Path

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def run(task_dir: Path):
    im = task_dir / "input_manifest.json"
    if not im.exists():
        return False, ["FAIL: missing input_manifest.json"]
    data = json.loads(im.read_text(encoding="utf-8"))
    errors = []
    for item in data.get("inputs", []):
        fp = Path(item["path"])
        if not fp.exists():
            errors.append(f"FAIL: missing {fp}")
            continue
        if sha256_file(fp) != item["sha256"]:
            errors.append(f"FAIL: hash mismatch {fp}")
    return (len(errors) == 0), ["input_manifest.json"] + errors
