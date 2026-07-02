"""
namespace_migrator_v3.py

Enterprise Namespace Migration Engine

Features
--------
* Dry-run by default
* --apply to modify files
* Automatic backups (.migration_backup/)
* Include/Exclude filtering
* Markdown migration report
* Validation scan for remaining legacy namespace references

Usage
-----
python namespace_migrator_v3.py --dry-run
python namespace_migrator_v3.py --apply
"""

from pathlib import Path
import argparse
import shutil

INCLUDE = ["src", "tests", ".github", "engineering", "pyproject.toml"]
EXCLUDE = {
    ".git", ".venv", "venv", "__pycache__", "build", "dist",
    "archive", "tools/archive", "tools/migrations", "reports",
    ".migration_backup"
}

TEXT_EXTS = {
    ".py", ".md", ".toml", ".yaml", ".yml",
    ".json", ".ini", ".cfg", ".txt"
}

REPLACEMENTS = [
    ("from bip_eos", "from ueos"),
    ("import bip_eos", "import ueos"),
    ("bip_eos.", "ueos."),
    ("\"bip_eos\"", "\"ueos\""),
    ("'bip_eos'", "'ueos'")
]

ROOT = Path.cwd()
BACKUP = ROOT / ".migration_backup"
REPORT = ROOT / "reports" / "namespace_migration_v3.md"

def included(rel: Path):
    s = rel.as_posix()
    if s == "pyproject.toml":
        return True
    return any(s.startswith(p + "/") for p in INCLUDE if p != "pyproject.toml")

def excluded(rel: Path):
    s = rel.as_posix()
    return any(part in EXCLUDE for part in rel.parts) or any(s.startswith(e + "/") for e in EXCLUDE)

def backup(path: Path):
    target = BACKUP / path.relative_to(ROOT)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, target)

def migrate_file(path: Path, apply=False):
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return False
    updated = text
    changed = False
    for old, new in REPLACEMENTS:
        if old in updated:
            updated = updated.replace(old, new)
            changed = True
    if changed and apply:
        backup(path)
        path.write_text(updated, encoding="utf-8")
    return changed

def validate():
    remaining = []
    for f in ROOT.rglob("*"):
        if not f.is_file():
            continue
        rel = f.relative_to(ROOT)
        if excluded(rel):
            continue
        if f.suffix.lower() not in TEXT_EXTS:
            continue
        try:
            txt = f.read_text(encoding="utf-8")
        except Exception:
            continue
        if "bip_eos" in txt:
            remaining.append(rel.as_posix())
    return remaining

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    REPORT.parent.mkdir(exist_ok=True)
    changed = []

    for f in ROOT.rglob("*"):
        if not f.is_file():
            continue
        rel = f.relative_to(ROOT)
        if excluded(rel):
            continue
        if not included(rel):
            continue
        if f.suffix.lower() not in TEXT_EXTS and rel.name != "pyproject.toml":
            continue
        if migrate_file(f, args.apply):
            changed.append(rel.as_posix())
            print(("[UPDATE]" if args.apply else "[WOULD UPDATE]"), rel)

    remaining = validate()

    with REPORT.open("w", encoding="utf-8") as r:
        r.write("# Namespace Migration v3\n\n")
        r.write(f"Mode: {'APPLY' if args.apply else 'DRY RUN'}\n\n")
        r.write(f"Files changed: {len(changed)}\n\n")
        r.write("## Modified Files\n")
        for item in changed:
            r.write(f"- {item}\n")
        r.write("\n## Remaining 'bip_eos' References\n")
        if remaining:
            for item in remaining:
                r.write(f"- {item}\n")
        else:
            r.write("None\n")

    print(f"\nReport written to: {REPORT}")
    if args.apply:
        print(f"Backups stored in: {BACKUP}")

if __name__ == "__main__":
    main()
