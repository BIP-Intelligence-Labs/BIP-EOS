#!/usr/bin/env python3
"""
========================================================================
UEOS
MGS-001 Repository Migration Planner
========================================================================

Generates a constitutional migration plan for legacy top-level folders.

This script DOES NOT move, rename, or delete anything.
It produces a migration plan for review.
"""

from pathlib import Path

ROOT = Path(".")

MIGRATIONS = {
    "ai": "src/bip_eos/ai",
    "bip": "SPLIT (src/bip_eos OR engineering)",
    "cli": "src/bip_eos/cli",
    "core": "src/bip_eos/runtime",
    "discovery": "src/bip_eos/audit",
    "plugins": "src/bip_eos/plugins",
    "registry": "src/bip_eos/registry",
    "reports": "engineering/reports",
    "shared": "src/bip_eos/common",
    "templates": "bootstrap/templates",
    "Lab": "research",
}

def main():
    print("=" * 72)
    print("UEOS MGS-001")
    print("Repository Migration Plan")
    print("=" * 72)

    existing = []
    missing = []

    for source, target in MIGRATIONS.items():
        if (ROOT / source).exists():
            existing.append((source, target))
        else:
            missing.append(source)

    print("\nLEGACY DIRECTORIES FOUND\n")

    for source, target in existing:
        print(f"[PLAN] {source:<12} --> {target}")

    if missing:
        print("\nNOT FOUND\n")
        for name in missing:
            print(f"  - {name}")

    print("\n" + "=" * 72)
    print("NEXT PHASE")
    print("=" * 72)
    print("1. Review migration plan")
    print("2. Resolve 'bip/' split destination")
    print("3. Execute migration with MGS-001 executor")
    print("4. Validate imports")
    print("5. Remove empty legacy directories")
    print("=" * 72)
    print("NOTE: No files or folders were modified.")
    print("=" * 72)

if __name__ == "__main__":
    main()
