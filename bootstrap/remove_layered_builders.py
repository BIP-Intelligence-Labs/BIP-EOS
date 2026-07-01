#!/usr/bin/env python3
"""
remove_layered_builders.py

Removes the old layer-based Builder directories after the
domain-driven architecture has been adopted.

Safe:
- Dry run by default
- Removes only empty directories unless --force is supplied
"""

from pathlib import Path
import shutil
import sys

ROOT = Path.cwd()

LEGACY = [
    "src/bip_eos/home_builders/api",
    "src/bip_eos/home_builders/crm",
    "src/bip_eos/home_builders/models",
    "src/bip_eos/home_builders/repositories",
    "src/bip_eos/home_builders/reports",
    "src/bip_eos/home_builders/services",
]

force = "--force" in sys.argv
dry_run = "--apply" not in sys.argv

print("=" * 70)
print("BIP EOS Builder Architecture Cleanup")
print("=" * 70)
print(f"Mode: {'DRY RUN' if dry_run else 'APPLY'}")
print()

for rel in LEGACY:
    path = ROOT / rel
    if not path.exists():
        print(f"[SKIP] {path} (missing)")
        continue

    if dry_run:
        print(f"[REMOVE] {path}")
        continue

    try:
        path.rmdir()
        print(f"[REMOVED] {path}")
    except OSError:
        if force:
            shutil.rmtree(path)
            print(f"[FORCE ] {path}")
        else:
            print(f"[NOT EMPTY] {path} (use --force to remove recursively)")

print("-" * 70)
print("Domain-driven architecture is now the preferred structure.")
