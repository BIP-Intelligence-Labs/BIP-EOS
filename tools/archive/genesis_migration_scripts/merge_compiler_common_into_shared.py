"""
merge_compiler_common_into_shared.py

UEOS Atlas

Safely merges:

    bootstrap/compiler/common

into

    bootstrap/compiler/shared

Creates a backup before moving files and only removes the
'common' directory if it becomes empty.

Run:

    python merge_compiler_common_into_shared.py
"""

from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path.cwd()

COMMON = ROOT / "bootstrap" / "compiler" / "common"
SHARED = ROOT / "bootstrap" / "compiler" / "shared"

BACKUP = (
    ROOT
    / ".backup"
    / f"compiler_common_merge_{datetime.now():%Y%m%d_%H%M%S}"
)

print("=" * 72)
print("UEOS COMPILER COMMON → SHARED MIGRATION")
print("=" * 72)

if not COMMON.exists():
    print("Nothing to migrate.")
    raise SystemExit(0)

BACKUP.mkdir(parents=True, exist_ok=True)

print(f"Backup : {BACKUP.relative_to(ROOT)}")

shutil.copytree(COMMON, BACKUP / "common")

SHARED.mkdir(parents=True, exist_ok=True)

moved = 0
kept = 0

for item in COMMON.rglob("*"):
    if item.is_dir():
        continue

    rel = item.relative_to(COMMON)
    dst = SHARED / rel
    dst.parent.mkdir(parents=True, exist_ok=True)

    if dst.exists():
        kept += 1
        print(f"KEEP   : {rel}")
        continue

    shutil.move(str(item), str(dst))
    moved += 1
    print(f"MOVE   : {rel}")

# Remove empty directories from deepest first
for directory in sorted(COMMON.rglob("*"), reverse=True):
    if directory.is_dir():
        try:
            directory.rmdir()
        except OSError:
            pass

try:
    COMMON.rmdir()
    print("\nREMOVE : bootstrap/compiler/common")
except OSError:
    print("\nNOTICE : common still contains files; review manually.")

print("-" * 72)
print(f"Moved : {moved}")
print(f"Kept  : {kept}")
print("Migration complete.")
