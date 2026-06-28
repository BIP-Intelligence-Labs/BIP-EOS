"""
bootstrap_upgrade_discovery.py

Upgrades the Discovery plugin by replacing minimal placeholder
implementations with richer "(1).py" implementations when available.

Run:
    python bootstrap_upgrade_discovery.py
"""

from pathlib import Path
import shutil

DISCOVERY = Path("bootstrap/plugins/discovery")

FILES = [
    "extractor.py",
    "validator.py",
    "repository.py",
    "scheduler.py",
]

print("=" * 55)
print(" Bootstrap Upgrade - Discovery")
print("=" * 55)

upgraded = 0

for filename in FILES:
    current = DISCOVERY / filename
    rich = DISCOVERY / filename.replace(".py", " (1).py")

    if not rich.exists():
        print(f"• {filename:<15} No upgrade available")
        continue

    if not current.exists():
        shutil.copy2(rich, current)
        print(f"✓ Installed {filename}")
        upgraded += 1
        continue

    current_size = current.stat().st_size
    rich_size = rich.stat().st_size

    if rich_size > current_size:
        backup = current.with_suffix(".py.bak")
        shutil.copy2(current, backup)
        shutil.copy2(rich, current)
        print(f"⬆ Upgraded {filename}")
        print(f"  Backup : {backup.name}")
        upgraded += 1
    else:
        print(f"✓ {filename:<15} Already current")

print("-" * 55)
print(f"Modules upgraded : {upgraded}")
print("Upgrade complete.")
