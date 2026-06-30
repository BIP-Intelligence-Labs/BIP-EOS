"""
bootstrap_migrate_compiler_docs.py

Moves compiler documentation from:
    bootstrap/compiler/docs/

to the canonical engineering location:
    engineering/compiler/specifications/
"""

from pathlib import Path
import shutil
import sys

ROOT = Path.cwd()

OLD = ROOT / "bootstrap" / "compiler" / "docs"
NEW = ROOT / "engineering" / "compiler" / "specifications"

print("=" * 60)
print("BIP EOS")
print("Compiler Documentation Migration")
print("=" * 60)

NEW.mkdir(parents=True, exist_ok=True)

if not OLD.exists():
    print("[OK] bootstrap/compiler/docs does not exist.")
    sys.exit(0)

moved = 0
skipped = 0

for item in sorted(OLD.iterdir()):
    destination = NEW / item.name

    if destination.exists():
        print(f"[SKIP] {item.name}")
        skipped += 1
        continue

    shutil.move(str(item), str(destination))
    print(f"[MOVE] {item.name}")
    moved += 1

try:
    OLD.rmdir()
    print("[REMOVE] bootstrap/compiler/docs")
except OSError:
    print("[INFO] bootstrap/compiler/docs not empty (contains subfolders or remaining files).")

print("-" * 60)
print(f"Moved   : {moved}")
print(f"Skipped : {skipped}")
print("Canonical location:")
print(NEW)
