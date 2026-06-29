"""
========================================================================

BIP Engineering Labs
Engineering Operating System (EOS)

Bootstrap Script

Creates the Engineering Governance documentation structure.

========================================================================
"""

from pathlib import Path

ROOT = Path.cwd()

DIRECTORIES = [
    "engineering/governance",
    "engineering/governance/Templates",
]

FILES = {
    "engineering/governance/README.md":
        "# Engineering Governance\n\nDefines the engineering governance framework for EOS.\n",

    "engineering/governance/EOS-Engineering-Constitution.md":
        "# EOS Engineering Constitution\n",

    "engineering/governance/Engineering-Principles.md":
        "# Engineering Principles\n",

    "engineering/governance/Coding-Standards.md":
        "# Coding Standards\n",

    "engineering/governance/Documentation-Standards.md":
        "# Documentation Standards\n",

    "engineering/governance/Testing-Standards.md":
        "# Testing Standards\n",

    "engineering/governance/Versioning-Policy.md":
        "# Versioning Policy\n",

    "engineering/governance/Branching-Strategy.md":
        "# Branching Strategy\n",

    "engineering/governance/Review-Checklist.md":
        "# Review Checklist\n",

    "engineering/governance/Definition-of-Done.md":
        "# Definition of Done\n",

    "engineering/governance/Templates/Specification-Template.md":
        "# Specification Template\n",

    "engineering/governance/Templates/ADR-Template.md":
        "# ADR Template\n",

    "engineering/governance/Templates/Sprint-Template.md":
        "# Sprint Template\n",

    "engineering/governance/Templates/Milestone-Template.md":
        "# Milestone Template\n",

    "engineering/governance/Templates/Release-Template.md":
        "# Release Template\n",
}


def create_directory(path: Path):
    if path.exists():
        print(f"[SKIP] {path}")
    else:
        path.mkdir(parents=True, exist_ok=True)
        print(f"[DIR ] {path}")


def create_file(path: Path, content: str):
    if path.exists():
        print(f"[SKIP] {path}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"[FILE] {path}")


def main():
    print("=" * 70)
    print("Engineering Governance Bootstrap")
    print("=" * 70)

    for directory in DIRECTORIES:
        create_directory(ROOT / directory)

    for filename, content in FILES.items():
        create_file(ROOT / filename, content)

    print("-" * 70)
    print(f"Directories : {len(DIRECTORIES)}")
    print(f"Files       : {len(FILES)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
