#!/usr/bin/env python3
"""
safe_builder_cleanup.py

Production-safe cleanup utility for legacy builder folders.

Default: DRY RUN
"""

from pathlib import Path
import sys

ROOT = Path.cwd()

ALLOW_LIST = [
    ROOT / "src/bip_eos/builders/api",
    ROOT / "src/bip_eos/builders/models",
    ROOT / "src/bip_eos/builders/repositories",
    ROOT / "src/bip_eos/builders/reports",
    ROOT / "src/bip_eos/builders/services",
]

APPLY = "--apply" in sys.argv

print("=" * 70)
print("BIP EOS Safe Builder Cleanup")
print("=" * 70)
print(f"Mode: {'APPLY' if APPLY else 'DRY RUN'}")
print()

blocked = []
removed = []
skipped = []

for directory in ALLOW_LIST:
    if not directory.exists():
        print(f"[SKIP] {directory} (missing)")
        skipped.append(directory)
        continue

    entries = list(directory.iterdir())
    files = [p for p in entries if p.is_file()]
    dirs = [p for p in entries if p.is_dir()]

    if dirs:
        print(f"[BLOCKED] {directory}")
        print("          Reason: contains subdirectories.")
        blocked.append(directory)
        continue

    if len(files) != 1 or files[0].name != "__init__.py":
        print(f"[BLOCKED] {directory}")
        print("          Reason: contains files other than __init__.py.")
        blocked.append(directory)
        continue

    if not APPLY:
        print(f"[SAFE] {directory}")
        continue

    try:
        files[0].unlink()
        directory.rmdir()
        print(f"[REMOVED] {directory}")
        removed.append(directory)
    except Exception as exc:
        print(f"[ERROR] {directory}: {exc}")
        blocked.append(directory)

print("\n" + "-" * 70)
print(f"Removed : {len(removed)}")
print(f"Blocked : {len(blocked)}")
print(f"Skipped : {len(skipped)}")

if blocked:
    print("\nCleanup completed with blocked directories requiring review.")
    raise SystemExit(1)

print("\nCleanup completed successfully.")
