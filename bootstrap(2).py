#!/usr/bin/env python3
"""
bootstrap.py

UEOS Bootstrap Launcher
=======================

Single entry point for all UEOS bootstrap operations.

Examples
--------
py bootstrap.py architecture
py bootstrap.py engineering
py bootstrap.py runtime
py bootstrap.py registry
py bootstrap.py builders
py bootstrap.py migrations
"""

from __future__ import annotations

import argparse
import runpy
import sys
from pathlib import Path

BOOTSTRAPS = {
    "architecture": "bootstrap/architecture/bootstrap_ea001_constitution_v1.py",
    "engineering": "bootstrap/engineering/bootstrap_engineering_foundation_v1.py",
    "runtime": "bootstrap/runtime/bootstrap_runtime_reorganization_v1.py",
    "registry": "bootstrap/registry/bootstrap_registry_v3.py",
    "builders": "bootstrap/home_builders/bootstrap_bfs001_bootstrap_framework.py",
    "migrations": "bootstrap/migrations/migrate_egf_to_epf.py",
}

def repo_root() -> Path:
    return Path(__file__).resolve().parent

def main() -> int:
    parser = argparse.ArgumentParser(
        description="UEOS Bootstrap Launcher"
    )
    parser.add_argument(
        "target",
        nargs="?",
        help="Bootstrap target"
    )

    args = parser.parse_args()

    if not args.target:
        print("UEOS Bootstrap Launcher\n")
        print("Available targets:")
        for name in sorted(BOOTSTRAPS):
            print(f"  - {name}")
        return 0

    target = args.target.lower()

    if target not in BOOTSTRAPS:
        print(f"Unknown target: {target}")
        print("\nAvailable targets:")
        for name in sorted(BOOTSTRAPS):
            print(f"  - {name}")
        return 1

    script = repo_root() / BOOTSTRAPS[target]

    if not script.exists():
        print(f"Bootstrap not found:\n{script}")
        return 2

    print("=" * 72)
    print("UEOS Bootstrap Launcher")
    print(f"Target : {target}")
    print(f"Script : {script.relative_to(repo_root())}")
    print("=" * 72)

    sys.argv = [str(script)]
    runpy.run_path(str(script), run_name="__main__")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
