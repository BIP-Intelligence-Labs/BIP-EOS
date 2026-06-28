"""
bootstrap_upgrade.py

Upgrade scaffold placeholders with newer "(1).py" implementations.

Run from the Genesis repository root:
    python bootstrap_upgrade.py
"""

from pathlib import Path

ROOT = Path("bootstrap")
updated = 0

for new_file in ROOT.rglob("* (1).py"):
    old_file = new_file.with_name(new_file.name.replace(" (1)", ""))

    if old_file.exists():
        old_file.unlink()
        print(f"🗑  Removed : {old_file.relative_to(ROOT.parent)}")

    new_file.rename(old_file)
    print(f"⬆️  Upgraded: {old_file.relative_to(ROOT.parent)}")
    updated += 1

print("\n===================================")
print(" Bootstrap Upgrade Complete")
print("===================================")
print(f"Files upgraded: {updated}")

if updated == 0:
    print("Nothing to upgrade. Repository is already current.")
