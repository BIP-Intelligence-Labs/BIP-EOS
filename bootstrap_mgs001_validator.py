#!/usr/bin/env python3
"""
========================================================================
UEOS
MGS-001 Migration Validator
========================================================================

Validates a repository migration plan before execution.

This validator DOES NOT move files.
"""

from pathlib import Path

ROOT = Path(".")

MIGRATIONS = {
    "ai": "src/bip_eos/ai",
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

def validate():
    print("=" * 72)
    print("UEOS MGS-001")
    print("Migration Validator")
    print("=" * 72)

    passed = True

    for src, dst in MIGRATIONS.items():
        s = ROOT / src
        d = ROOT / dst

        if not s.exists():
            print(f"[WARN ] Missing source      : {src}")
            continue

        if not d.exists():
            print(f"[FAIL ] Missing destination : {dst}")
            passed = False
        else:
            print(f"[ OK ] {src:<12} -> {dst}")

    print("=" * 72)
    if passed:
        print("VALIDATION RESULT : PASS")
        print("Repository is ready for Migration Executor.")
    else:
        print("VALIDATION RESULT : FAIL")
        print("Resolve missing destinations before executing migration.")
    print("=" * 72)

if __name__ == "__main__":
    validate()
