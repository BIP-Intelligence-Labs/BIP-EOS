"""
========================================================================

BIP Engineering Labs
Engineering Operating System (EOS)

Bootstrap Script

Creates the Engineering Milestones roadmap.

========================================================================
"""

from pathlib import Path

ROOT = Path.cwd()

DIRECTORIES = [
    "engineering/roadmap/milestones",
]

FILES = {
    "engineering/roadmap/milestones/M-001-Compiler-Frontend.md":
        "# M-001 Compiler Frontend\n\nMilestone for completing the EOS Compiler Front-End.\n",

    "engineering/roadmap/milestones/M-002-Engineering-Model.md":
        "# M-002 Engineering Model\n\nMilestone for the canonical Engineering Model (IR).\n",

    "engineering/roadmap/milestones/M-003-Validation.md":
        "# M-003 Validation\n\nMilestone for validation and diagnostics.\n",

    "engineering/roadmap/milestones/M-004-Emitters.md":
        "# M-004 Emitters\n\nMilestone for Python, SQL, OpenAPI, documentation, and test emitters.\n",

    "engineering/roadmap/milestones/M-005-EOS-v1.0.md":
        "# M-005 EOS v1.0\n\nMilestone for the first complete Engineering Operating System release.\n",
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
    print("Engineering Milestones Bootstrap")
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
