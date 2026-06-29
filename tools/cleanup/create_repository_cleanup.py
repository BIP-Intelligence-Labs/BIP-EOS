"""
create_repository_cleanup.py

Genesis EEOS
Repository Cleanup Utility

Performs:
- Removes *.bak files
- Removes duplicate Windows downloads like "file (1).py"
- Creates/updates .gitignore with recommended entries
- Moves legacy create_geb_*.py installers into tools/archive/legacy_installers

Run from repository root:

    python create_repository_cleanup.py
"""

from pathlib import Path
import shutil

ROOT = Path(".")
ARCHIVE = ROOT / "tools" / "archive" / "legacy_installers"
ARCHIVE.mkdir(parents=True, exist_ok=True)

removed = []
moved = []

# ------------------------------------------------------
# Remove backup files
# ------------------------------------------------------
for bak in ROOT.rglob("*.bak"):
    try:
        bak.unlink()
        removed.append(str(bak))
    except Exception as exc:
        print(f"Could not remove {bak}: {exc}")

# ------------------------------------------------------
# Remove duplicate Windows downloads
# ------------------------------------------------------
for dup in ROOT.rglob("* (1).py"):
    try:
        dup.unlink()
        removed.append(str(dup))
    except Exception as exc:
        print(f"Could not remove {dup}: {exc}")

# ------------------------------------------------------
# Archive legacy installers
# ------------------------------------------------------
for script in ROOT.glob("create_geb_*.py"):
    destination = ARCHIVE / script.name
    try:
        shutil.move(str(script), str(destination))
        moved.append((script.name, destination))
    except Exception as exc:
        print(f"Could not move {script}: {exc}")

# ------------------------------------------------------
# Update .gitignore
# ------------------------------------------------------
gitignore = ROOT / ".gitignore"

entries = [
    "",
    "# Genesis cleanup",
    "*.bak",
    "* (1).py",
    "",
    "# Python cache",
    "__pycache__/",
    "*.pyc",
]

existing = ""
if gitignore.exists():
    existing = gitignore.read_text(encoding="utf-8")

with gitignore.open("a", encoding="utf-8") as f:
    for line in entries:
        if line and line in existing:
            continue
        f.write(line + "\n")

# ------------------------------------------------------
# Summary
# ------------------------------------------------------
print("=" * 60)
print("BIP EOS Repository Cleanup Complete")
print("=" * 60)

print(f"\nRemoved : {len(removed)}")
for item in removed:
    print("  -", item)

print(f"\nArchived : {len(moved)}")
for name, dest in moved:
    print(f"  - {name} -> {dest}")

print("\nNext Steps")
print("-----------")
print("git status")
print('git add .')
print('git commit -m "chore(repository): clean engineering artifacts"')
print("git tag v0.2.0")
