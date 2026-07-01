#!/usr/bin/env python3
"""
sprint_two_bootstrap.py

BIP EOS - Sprint 2 Bootstrap

Creates the Builder Intelligence Platform foundation.
"""

from pathlib import Path

DIRECTORIES = [
    "src/bip_eos/home_builders/models",
    "src/bip_eos/home_builders/services",
    "src/bip_eos/home_builders/repositories",
    "src/bip_eos/home_builders/api",
    "src/bip_eos/home_builders/questionnaire",
    "src/bip_eos/home_builders/recommendation",
    "src/bip_eos/home_builders/reports",
    "src/bip_eos/home_builders/crm",
    "src/bip_eos/database",
    "src/bip_eos/integrations",
]

FILES = {
    "src/bip_eos/home_builders/__init__.py": "# Builder Intelligence Platform\n",
    "src/bip_eos/database/__init__.py": "# Database package\n",
    "src/bip_eos/integrations/__init__.py": "# Integrations package\n",
    "engineering/sprints/SPRINT_02.md": """# Sprint 2

## Goal
Build the Builder Intelligence Platform.

## Deliverables
- CRM
- Questionnaire Engine
- Recommendation Engine
- Builder Matching
- Community Matching
- Inventory Matching
- Buyer Reports
- Supabase Integration
""",
}


def create(path: Path):
    path.mkdir(parents=True, exist_ok=True)
    print(f"[DIR ] {path}")


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(text, encoding="utf-8")
        print(f"[FILE] {path}")
    else:
        print(f"[SKIP] {path}")


def main():
    root = Path.cwd()

    print("=" * 70)
    print("BIP EOS Sprint 2 Bootstrap")
    print("=" * 70)

    for d in DIRECTORIES:
        create(root / d)

    for name, text in FILES.items():
        write(root / name, text)

    print("-" * 70)
    print("Sprint 2 foundation created.")
    print("Next milestone: Builder Intelligence Platform")


if __name__ == "__main__":
    main()
