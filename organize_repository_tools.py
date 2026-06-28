"""
organize_repository_tools.py

Genesis EEOS
Repository Tool Organizer

Moves existing engineering utilities into the new repository structure.

Run from repository root:

    python organize_repository_tools.py
"""

from pathlib import Path
import shutil

ROOT = Path(".")

RULES = {
    "tools/generators": [
        "create_*.py",
    ],
    "tools/migrations": [
        "rename_*.py",
    ],
    "tools/cleanup": [
        "archive_*.py",
        "*cleanup*.py",
    ],
    "tools/installers": [
        "*foundation*.py",
        "*package*.py",
    ],
}

# Don't move this organizer itself
EXCLUDE = {
    "organize_repository_tools.py",
}

moved = []

for destination, patterns in RULES.items():
    dest = ROOT / destination
    dest.mkdir(parents=True, exist_ok=True)

    for pattern in patterns:
        for file in ROOT.glob(pattern):
            if not file.is_file():
                continue
            if file.name in EXCLUDE:
                continue
            target = dest / file.name

            # Skip if already organized
            if file.parent == dest:
                continue

            # Prevent overwrite
            if target.exists():
                print(f"SKIP   {file.name} (already exists)")
                continue

            shutil.move(str(file), str(target))
            moved.append((file.name, destination))
            print(f"MOVED  {file.name} -> {destination}")

print("\n" + "=" * 60)
print(f"Moved {len(moved)} file(s)")
print("=" * 60)

print("""
Recommended verification:

git status

git diff

git add .

git commit -m "refactor(repository): organize engineering tools"
""")
