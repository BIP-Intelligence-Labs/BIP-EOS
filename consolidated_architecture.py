#!/usr/bin/env python3
"""
consolidated_architecture.py

Creates a recommended consolidated directory structure for Genesis/BIP EOS
without moving or deleting any existing files.
"""

from pathlib import Path

ROOT = Path.cwd()

STRUCTURE = [
    "src/genesis/core",
    "src/genesis/cli",
    "src/genesis/documentation",
    "src/genesis/plugins",
    "src/genesis/academy",
    "src/genesis/ai",
    "src/genesis/builders",
    "src/genesis/reports",
    "src/genesis/sales",
    "docs",
    "docs/adr",
    "docs/api",
    "docs/architecture",
    "docs/engineering",
    "plugins",
    "registry",
    "templates",
    "tests",
    "logs",
]

INIT_PACKAGES = [
    "src/genesis",
    "src/genesis/core",
    "src/genesis/cli",
    "src/genesis/documentation",
    "src/genesis/plugins",
    "src/genesis/academy",
    "src/genesis/ai",
    "src/genesis/builders",
    "src/genesis/reports",
    "src/genesis/sales",
]


def create():
    created = 0

    for folder in STRUCTURE:
        path = ROOT / folder
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created += 1

    for pkg in INIT_PACKAGES:
        init = ROOT / pkg / "__init__.py"
        if not init.exists():
            init.write_text('"""Genesis package."""\n', encoding="utf-8")

    readme = ROOT / "ARCHITECTURE.md"
    if not readme.exists():
        readme.write_text(
            """# Consolidated Architecture

Primary application code lives under:

    src/genesis/

Top-level folders such as docs/, plugins/, templates/, registry/, tests/,
and logs/ remain as project resources.

Legacy folders should be migrated into src/genesis over time.
""",
            encoding="utf-8",
        )

    print("=" * 60)
    print("Genesis Consolidated Architecture")
    print("=" * 60)
    print(f"Project Root : {ROOT}")
    print(f"Folders Created : {created}")
    print("Status : COMPLETE")
    print()
    print("NOTE: No files were moved or deleted.")


if __name__ == "__main__":
    create()
