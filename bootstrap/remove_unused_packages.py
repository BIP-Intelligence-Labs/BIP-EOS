#!/usr/bin/env python3
"""
remove_unused_packages.py

Removes verified-unused top-level BIP EOS packages.

Safety:
- Dry run by default
- Removes ONLY approved packages
- Removes ONLY if they contain exactly one __init__.py
"""

from pathlib import Path
import sys

ROOT = Path.cwd()
APPLY = "--apply" in sys.argv

PACKAGES = [
    ROOT / "src/bip_eos/services",
    ROOT / "src/bip_eos/reports",
    ROOT / "src/bip_eos/utils",
]

print("=" * 70)
print("BIP EOS Unused Package Cleanup")
print("=" * 70)
print(f"Mode: {'APPLY' if APPLY else 'DRY RUN'}")
print()

removed = 0
skipped = 0
blocked = 0

for pkg in PACKAGES:
    if not pkg.exists():
        print(f"[SKIP] {pkg} (missing)")
        skipped += 1
        continue

    entries = list(pkg.iterdir())
    files = [p for p in entries if p.is_file()]
    dirs = [p for p in entries if p.is_dir()]

    if dirs:
        print(f"[BLOCKED] {pkg}")
        print("          Contains subdirectories.")
        blocked += 1
        continue

    if len(files) != 1 or files[0].name != "__init__.py":
        print(f"[BLOCKED] {pkg}")
        print("          Contains files other than __init__.py.")
        blocked += 1
        continue

    if not APPLY:
        print(f"[SAFE] {pkg}")
        continue

    try:
        files[0].unlink()
        pkg.rmdir()
        print(f"[REMOVED] {pkg}")
        removed += 1
    except Exception as exc:
        print(f"[ERROR] {pkg}: {exc}")
        blocked += 1

print("-" * 70)
print(f"Removed : {removed}")
print(f"Blocked : {blocked}")
print(f"Skipped : {skipped}")

if blocked:
    raise SystemExit(1)

print("Cleanup completed successfully.")
