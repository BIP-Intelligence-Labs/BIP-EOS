"""
========================================================================

BIP Engineering Labs
Engineering Operating System (EOS)

Bootstrap Script

Establishes the Engineering Truth and Public Documentation philosophy.

========================================================================
"""

from pathlib import Path

ROOT = Path.cwd()

DIRECTORIES = [
    "engineering/specifications",
    "docs/getting-started",
    "docs/installation",
    "docs/tutorials",
    "docs/user-guide",
    "docs/cli",
    "docs/api",
    "docs/examples",
    "docs/faq",
    "docs/releases",
    "docs/images",
]

FILES = {
    "engineering/README.md": """# Engineering

## Purpose

Engineering is the authoritative source of truth for the Engineering
Operating System (EOS).

Public documentation should be derived from governed engineering
artifacts whenever practical.
""",

    "engineering/specifications/README.md": """# Engineering Specifications

Specifications define the behavior, interfaces, responsibilities,
and contracts of EOS subsystems.
""",

    "docs/README.md": """# EOS Documentation

## Purpose

This directory contains published documentation for users.

Engineering knowledge originates in /engineering.
""",

    "docs/getting-started/README.md": "# Getting Started\n",
    "docs/installation/README.md": "# Installation Guide\n",
    "docs/tutorials/README.md": "# Tutorials\n",
    "docs/user-guide/README.md": "# User Guide\n",
    "docs/cli/README.md": "# CLI Guide\n",
    "docs/api/README.md": "# API Documentation\n",
    "docs/examples/README.md": "# Examples\n",
    "docs/faq/README.md": "# Frequently Asked Questions\n",
    "docs/releases/README.md": "# Release Notes\n",
    "docs/images/README.md": "# Images\n",
}

def create_directory(path: Path):
    if path.exists():
        print(f"[SKIP] {path}")
    else:
        path.mkdir(parents=True, exist_ok=True)
        print(f"[DIR ] {path}")

def create_file(path: Path, text: str):
    if path.exists():
        print(f"[SKIP] {path}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"[FILE] {path}")

def main():
    print("=" * 70)
    print("Engineering Truth Bootstrap")
    print("=" * 70)

    for d in DIRECTORIES:
        create_directory(ROOT / d)

    for f, t in FILES.items():
        create_file(ROOT / f, t)

    print("-" * 70)
    print("engineering/ -> Engineering Truth")
    print("docs/        -> Published Documentation")
    print("=" * 70)

if __name__ == "__main__":
    main()
