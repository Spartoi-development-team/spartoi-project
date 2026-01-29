from pathlib import Path

# Use split strings to avoid self-detection
TRIPWIRES = ["NEW_" + "GATE_CLASS", "PLAT" + "FORMIZE", "HEAVY_" + "DASHBOARD"]

def run(task_dir: Path, repo_root: Path):
    hits = []
    for p in repo_root.rglob("*"):
        if p.is_dir() or "evidence" in str(p) or ".git" in str(p):
            continue
        if p.suffix.lower() not in [".md", ".txt", ".yml", ".yaml", ".json", ".py"]:
            continue
        try:
            txt = p.read_text(encoding="utf-8", errors="ignore")
            for t in TRIPWIRES:
                if t in txt:
                    hits.append(f"TRIPWIRE: {p}: {t}")
        except:
            pass
    return (len(hits) == 0), ["scanned"] + hits
