#!/usr/bin/env python3
"""
========================================================================
UEOS M-004

Repository Consolidation

Constitutional Migration Preparation
========================================================================
"""

from pathlib import Path

ROOT = Path.cwd()

MIGRATIONS = {
    "ai": "src/bip_eos/ai",
    "bip": "SPLIT_REQUIRED",
    "cli": "src/bip_eos/cli",
    "core": "src/bip_eos/runtime",
    "discovery": "src/bip_eos/audit",
    "plugins": "src/bip_eos/plugins",
    "registry": "src/bip_eos/registry",
    "shared": "src/bip_eos/common",
}


def ensure(path: str) -> None:
    if path == "SPLIT_REQUIRED":
        return
    (ROOT / path).mkdir(parents=True, exist_ok=True)


def main() -> None:
    print("=" * 72)
    print("UEOS M-004")
    print("Repository Consolidation")
    print("=" * 72)
    print()

    for source, destination in MIGRATIONS.items():
        src = ROOT / source

        if not src.exists():
            print(f"[SKIP ] {source:<12} Missing")
            continue

        if destination == "SPLIT_REQUIRED":
            print(f"[PLAN ] {source:<12} Split Required")
            continue

        ensure(destination)
        print(f"[READY] {source:<12} -> {destination}")

    print()
    print("=" * 72)
    print("NEXT")
    print("=" * 72)
    print("1. Execute migration")
    print("2. Validate imports")
    print("3. Remove empty legacy folders")
    print("=" * 72)


if __name__ == "__main__":
    main()
