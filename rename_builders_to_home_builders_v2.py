"""
rename_builders_to_home_builders.py

Enterprise repository migration for UEOS.

Run from repository root:

    python rename_builders_to_home_builders.py

Features
--------
✓ Renames every directory named "builders" -> "home_builders"
✓ Renames every Python file named builders.py -> home_builders.py
✓ Updates imports
✓ Updates package names
✓ Updates markdown/docs
✓ Updates Windows & POSIX paths
✓ Updates dotted module paths
✓ Dry-run support

Usage
-----
python rename_builders_to_home_builders.py
python rename_builders_to_home_builders.py --dry-run
"""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path.cwd()

TEXT_EXTENSIONS = {
    ".py", ".md", ".txt", ".toml", ".json",
    ".yaml", ".yml", ".ini", ".cfg", ".rst"
}

REPLACEMENTS = [
    ("bip.home_builders", "bip.home_builders"),
    ("bip_eos.home_builders", "bip_eos.home_builders"),
    ("from builders", "from home_builders"),
    ("import builders", "import home_builders"),
    ("/builders/", "/home_builders/"),
    ("\\builders\\", "\\home_builders\\"),
    ("/builders", "/home_builders"),
    ("\\builders", "\\home_builders"),
    ("builders.", "home_builders."),
    ("builders/", "home_builders/"),
]

parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()

renamed_dirs = 0
renamed_files = 0
updated_files = 0

# deepest first
for d in sorted(ROOT.rglob("builders"), key=lambda p: len(p.parts), reverse=True):
    if d.is_dir():
        target = d.with_name("home_builders")
        if target.exists():
            print(f"SKIP DIR : {target}")
            continue
        print(f"DIR  : {d.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
        renamed_dirs += 1
        if not args.dry_run:
            d.rename(target)

for f in sorted(ROOT.rglob("builders.py"), key=lambda p: len(p.parts), reverse=True):
    target = f.with_name("home_builders.py")
    if target.exists():
        print(f"SKIP FILE: {target}")
        continue
    print(f"FILE : {f.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
    renamed_files += 1
    if not args.dry_run:
        f.rename(target)

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        continue

    try:
        original = path.read_text(encoding="utf-8")
    except Exception:
        continue

    updated = original
    for old, new in REPLACEMENTS:
        updated = updated.replace(old, new)

    if updated != original:
        print(f"UPDATE: {path.relative_to(ROOT)}")
        updated_files += 1
        if not args.dry_run:
            path.write_text(updated, encoding="utf-8")

print("\n====================================")
print("Migration Summary")
print("====================================")
print(f"Directories renamed : {renamed_dirs}")
print(f"Files renamed       : {renamed_files}")
print(f"Files updated       : {updated_files}")
print("Done.")
