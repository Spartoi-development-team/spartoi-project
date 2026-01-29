import json
from pathlib import Path
from jsonschema import Draft202012Validator

def run(task_dir: Path, schema_dir: Path):
    mapping = {
        "input_manifest.json": "input_manifest.schema.json",
        "run_manifest.json": "run_manifest.schema.json",
        "settings_evidence.json": "settings_evidence.schema.json",
    }
    errors, validated = [], []
    for inst, sch in mapping.items():
        ip, sp = task_dir / inst, schema_dir / sch
        if not ip.exists():
            errors.append(f"FAIL: missing {inst}")
            continue
        v = Draft202012Validator(json.loads(sp.read_text()))
        errs = list(v.iter_errors(json.loads(ip.read_text())))
        if errs:
            errors.extend([f"{inst}: {e.message}" for e in errs])
        else:
            validated.append(inst)
    return (len(errors) == 0), validated + errors
