"""
reorganize_toolchain.py

Genesis EEOS
Toolchain Reorganizer

Organizes engineering tools into the recommended layout.

Run from the repository root:

    python reorganize_toolchain.py
"""

from pathlib import Path
import shutil

ROOT = Path(".")

TARGETS = {
    "create_repository_structure.py": "tools/generators",
    "create_sprint_001.py": "tools/generators",

    "create_github_foundation.py": "tools/installers",
    "create_repository_engine_package.py": "tools/installers",

    "rename_engineering_ids.py": "tools/migrations",

    "archive_legacy_installers.py": "tools/cleanup",
    "create_repository_cleanup.py": "tools/cleanup",
}

print("=" * 60)
print("Genesis EEOS Toolchain Reorganization")
print("=" * 60)

moved = 0
skipped = 0

for filename, destination in TARGETS.items():
    src = ROOT / filename
    dst_dir = ROOT / destination
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / filename

    if dst.exists():
        print(f"SKIP   {filename} (already organized)")
        skipped += 1
        continue

    if not src.exists():
        print(f"SKIP   {filename} (not found)")
        skipped += 1
        continue

    shutil.move(str(src), str(dst))
    print(f"MOVED  {filename} -> {destination}")
    moved += 1

print("\n" + "=" * 60)
print(f"Moved   : {moved}")
print(f"Skipped : {skipped}")
print("=" * 60)

print("""
Recommended layout

tools/
├── generators/
│   ├── create_repository_structure.py
│   └── create_sprint_001.py
│
├── installers/
│   ├── create_github_foundation.py
│   └── create_repository_engine_package.py
│
├── migrations/
│   └── rename_engineering_ids.py
│
├── cleanup/
│   ├── archive_legacy_installers.py
│   └── create_repository_cleanup.py
│
└── archive/

Next:

git status
git add .
git commit -m "refactor(repository): reorganize engineering toolchain"
""")
