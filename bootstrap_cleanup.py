"""
bootstrap_cleanup.py

Removes temporary backup and duplicate upgrade files after a successful
Bootstrap upgrade.

Run:
    python bootstrap_cleanup.py
"""

from pathlib import Path

ROOT = Path("bootstrap")
PATTERNS = ("*.py.bak", "* (1).py")

deleted = 0

print("=" * 55)
print(" Bootstrap Cleanup")
print("=" * 55)

for pattern in PATTERNS:
    for path in ROOT.rglob(pattern):
        try:
            path.unlink()
            print(f"🗑  Deleted: {path}")
            deleted += 1
        except Exception as exc:
            print(f"✗ Failed : {path} ({exc})")

print("-" * 55)
print(f"Files deleted: {deleted}")
print("Repository cleanup complete.")
