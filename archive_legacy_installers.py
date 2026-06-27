"""
archive_legacy_installers.py

Archives legacy create_geb_*.py installer scripts.

Run from the Genesis repository root:

    python archive_legacy_installers.py
"""

from pathlib import Path
import shutil

ROOT = Path(".")
ARCHIVE = ROOT / "tools" / "archive" / "legacy_installers"
ARCHIVE.mkdir(parents=True, exist_ok=True)

moved = 0

print("=" * 60)
print("Archiving Legacy GEB Installer Scripts")
print("=" * 60)

for script in sorted(ROOT.glob("create_geb_*.py")):
    destination = ARCHIVE / script.name

    if destination.exists():
        print(f"SKIP   {script.name} (already archived)")
        continue

    shutil.move(str(script), str(destination))
    print(f"MOVED  {script.name}")
    moved += 1

print()
print("=" * 60)
print(f"Archived: {moved} installer(s)")
print(f"Location : {ARCHIVE}")
print("=" * 60)

print("\nNext Steps")
print("----------")
print("git status")
print("git add .")
print('git commit -m "chore(repository): archive legacy GEB installers"')
