#!/usr/bin/env python3
"""
========================================================================
UEOS
Repository Constitutional Hierarchy Installer
========================================================================

Creates the constitutional top-level repository structure.

Safe to run multiple times.
"""

from pathlib import Path

ROOT = Path(".")

DIRECTORIES = [
    "src/bip_eos",
    "engineering",
    "bootstrap",
    "docs",
    "tests",
    "tools",
    "assets",
    "config",
    "scripts",
    "research",
    "archive",
]

README = {
    "engineering": "# Engineering\n\nEngineering architecture, governance, standards, and specifications.\n",
    "bootstrap": "# Bootstrap\n\nInstallers, generators, scaffolding, and repository bootstrap.\n",
    "docs": "# Documentation\n\nEnd-user documentation.\n",
    "tests": "# Tests\n\nAutomated test suites.\n",
    "tools": "# Tools\n\nDeveloper utilities.\n",
    "assets": "# Assets\n\nStatic assets.\n",
    "config": "# Configuration\n\nConfiguration files.\n",
    "scripts": "# Scripts\n\nOne-off automation and migration scripts.\n",
    "research": "# Research\n\nExperiments, prototypes, benchmarks, and whitepapers.\n",
    "archive": "# Archive\n\nHistorical and deprecated material.\n",
}

def ensure(path: Path):
    path.mkdir(parents=True, exist_ok=True)
    print(f"[ OK ] {path}")

def main():
    print("="*72)
    print("UEOS Constitutional Repository")
    print("="*72)

    for d in DIRECTORIES:
        ensure(ROOT / d)

    for folder, text in README.items():
        readme = ROOT / folder / "README.md"
        if not readme.exists():
            readme.write_text(text, encoding="utf-8")
            print(f"[CREATE ] {readme}")
        else:
            print(f"[EXISTS ] {readme}")

    print("="*72)
    print("Recommended Top-Level Layout")
    print("="*72)
    print(r"""
genesis/
├── src/
│   └── bip_eos/
├── engineering/
├── bootstrap/
├── docs/
├── tests/
├── tools/
├── assets/
├── config/
├── scripts/
├── research/
└── archive/
""")
    print("="*72)
    print("NOTE:")
    print("This installer creates the constitutional hierarchy only.")
    print("It does not move or delete existing folders.")
    print("="*72)

if __name__ == "__main__":
    main()
