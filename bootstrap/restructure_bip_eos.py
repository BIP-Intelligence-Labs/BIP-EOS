#!/usr/bin/env python3
"""
restructure_bip_eos.py

Restructures the BIP EOS package into the Sprint 2 layout.
Safe operation:
- Creates missing directories
- Creates __init__.py files
- Does NOT delete or move existing files
"""

from pathlib import Path

ROOT = Path.cwd()

DIRS = [
    "src/bip_eos/core",
    "src/bip_eos/database",
    "src/bip_eos/integrations",

    "src/bip_eos/home_builders",
    "src/bip_eos/home_builders/api",
    "src/bip_eos/home_builders/crm",
    "src/bip_eos/home_builders/models",
    "src/bip_eos/home_builders/questionnaire",
    "src/bip_eos/home_builders/recommendation",
    "src/bip_eos/home_builders/reports",
    "src/bip_eos/home_builders/repositories",
    "src/bip_eos/home_builders/services",
]

def ensure_package(path: Path):
    path.mkdir(parents=True, exist_ok=True)
    init = path / "__init__.py"
    if not init.exists():
        init.write_text('"""BIP EOS package."""\n', encoding="utf-8")
        print(f"[FILE] {init}")
    else:
        print(f"[SKIP] {init}")

def main():
    print("=" * 70)
    print("BIP EOS Sprint 2 Restructure")
    print("=" * 70)

    for d in DIRS:
        ensure_package(ROOT / d)

    print("-" * 70)
    print("Structure verified.")
    print("No files were moved or deleted.")
    print("=" * 70)

if __name__ == "__main__":
    main()
