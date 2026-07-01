"""
cleanup_genesis_repository.py

UEOS Atlas
Post-Genesis repository cleanup.

This utility archives one-time migration/bootstrap scripts and removes
Python cache directories. It never deletes production source code.

Run:
    python cleanup_genesis_repository.py
"""

from pathlib import Path
import shutil

ROOT = Path.cwd()

ARCHIVE = ROOT / "tools" / "archive" / "genesis_migration_scripts"
ARCHIVE.mkdir(parents=True, exist_ok=True)

PATTERNS = (
    "merge_*.py",
    "migrate_*.py",
    "normalize_*.py",
    "rename_*.py",
    "bootstrap_m005_*.py",
)

print("=" * 72)
print("UEOS GENESIS CLEANUP")
print("=" * 72)

moved = 0

for pattern in PATTERNS:
    for file in ROOT.glob(pattern):
        destination = ARCHIVE / file.name
        if destination.exists():
            print(f"SKIP    : {file.name}")
            continue
        shutil.move(str(file), str(destination))
        moved += 1
        print(f"ARCHIVE : {file.name}")

removed = 0

for cache in ROOT.rglob("__pycache__"):
    shutil.rmtree(cache, ignore_errors=True)
    removed += 1
    print(f"REMOVE  : {cache.relative_to(ROOT)}")

print("-" * 72)
print(f"Archived scripts : {moved}")
print(f"Removed caches   : {removed}")
print()
print("Next recommended Git commands:")
print("  git add -A")
print('  git commit -m "chore(repository): post-Genesis cleanup"')
