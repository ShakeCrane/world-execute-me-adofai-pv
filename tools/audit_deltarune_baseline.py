"""Static, lyric-free inventory; does not import the production render chain."""
from pathlib import Path
import ast
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASELINE = "cb63fb6ba5832da38d79f95b8469464c1e2ddbf4"


def main():
    # Read Git objects, not the changing worktree. New DR files never enter this
    # inventory; rerunning after implementation preserves the same baseline.
    names = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", BASELINE], cwd=ROOT).decode().splitlines()
    files = [ROOT / p for p in names if p.endswith(".py") and
             (p == "build.py" or p.startswith(("film/", "tools/")))]
    rows = []
    for path in files:
        if any(p in path.parts for p in ("vendor", "__pycache__", "cache", "pv_cache")):
            continue
        raw = subprocess.check_output(["git", "show", f"{BASELINE}:{path.relative_to(ROOT).as_posix()}"], cwd=ROOT)
        tree = ast.parse(raw.decode("utf-8-sig"), filename=str(path))
        imports, symbols, tables = [], [], {}
        for node in tree.body:
            if isinstance(node, ast.Import):
                imports.extend(a.name for a in node.names)
            elif isinstance(node, ast.ImportFrom):
                imports.append(node.module or "")
            elif isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                symbols.append({"name": node.name, "line": node.lineno})
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id in {
                        "CUTS", "REPLACE", "SPLIT", "FULL_ART", "SHELL", "HIDE_HER", "OVERLAY", "OWN", "STUB"}:
                        # Keys/symbol names only: never copy lyric cues or dialogue values.
                        value = node.value
                        keys = value.keys if isinstance(value, ast.Dict) else getattr(value, "elts", [])
                        tables[target.id] = [ast.unparse(k) for k in keys if k is not None]
        rows.append({"path": path.relative_to(ROOT).as_posix(), "sha256": hashlib.sha256(raw).hexdigest(),
                     "lf_sha256": hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest(),
                     "lines": len(raw.splitlines()), "imports": imports, "symbols": symbols, "tables": tables})
    target = ROOT / "data/deltarune/baseline_inventory.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps({"schema_version": 1, "method": "static AST; imports are not resolved runtime edges",
                                  "baseline_commit": BASELINE, "source": "Git objects at baseline, excluding all new work", "files": rows},
                                 ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Inventoried {len(rows)} Python files -> {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
