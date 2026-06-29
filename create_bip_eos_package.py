#!/usr/bin/env python3
"""
create_bip_eos_package.py

Creates the production BIP EOS package structure.
Safe to run multiple times.
"""

from pathlib import Path

ROOT = Path.cwd()

DIRS = [
    "src/bip_eos",
    "src/bip_eos/core",
    "src/bip_eos/core/repository",
    "src/bip_eos/core/plugins",
    "src/bip_eos/core/documentation",
    "src/bip_eos/core/registry",
    "src/bip_eos/core/version",
    "src/bip_eos/core/logging",
    "src/bip_eos/cli",
    "src/bip_eos/cli/commands",
    "src/bip_eos/plugins",
    "src/bip_eos/builders",
    "src/bip_eos/academy",
    "src/bip_eos/ai",
    "src/bip_eos/reports",
    "src/bip_eos/services",
    "src/bip_eos/utils",
]

INITS = [
    "src/bip_eos",
    "src/bip_eos/core",
    "src/bip_eos/core/repository",
    "src/bip_eos/core/plugins",
    "src/bip_eos/core/documentation",
    "src/bip_eos/core/registry",
    "src/bip_eos/core/version",
    "src/bip_eos/core/logging",
    "src/bip_eos/cli",
    "src/bip_eos/cli/commands",
    "src/bip_eos/plugins",
    "src/bip_eos/builders",
    "src/bip_eos/academy",
    "src/bip_eos/ai",
    "src/bip_eos/reports",
    "src/bip_eos/services",
    "src/bip_eos/utils",
]

README = """# BIP EOS

Engineering Operating System

Version: 0.1.0
Codename: Genesis
"""

def main():
    created_dirs = 0
    created_files = 0

    print("=" * 70)
    print("BIP EOS Package Bootstrap")
    print("=" * 70)

    for d in DIRS:
        p = ROOT / d
        if not p.exists():
            p.mkdir(parents=True, exist_ok=True)
            created_dirs += 1
            print("[DIR ]", d)

    for pkg in INITS:
        init = ROOT / pkg / "__init__.py"
        if not init.exists():
            init.write_text('"""BIP EOS package."""\n', encoding="utf-8")
            created_files += 1
            print("[FILE]", init.relative_to(ROOT))

    readme = ROOT / "src" / "bip_eos" / "README.md"
    if not readme.exists():
        readme.write_text(README, encoding="utf-8")
        created_files += 1

    print("-" * 70)
    print("Directories created :", created_dirs)
    print("Files created       :", created_files)
    print("Status              : COMPLETE")
    print("=" * 70)
    print("Next step:")
    print("Move modules from src/genesis into src/bip_eos incrementally.")

if __name__ == "__main__":
    main()
