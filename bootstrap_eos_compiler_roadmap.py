"""
========================================================================

BIP Engineering Labs
Engineering Operating System (EOS)

Bootstrap Script

Creates the EOS Compiler roadmap documentation.

========================================================================
"""

from pathlib import Path

ROOT = Path.cwd()

DIRECTORIES = [
    "engineering/compiler/roadmap",
]

FILES = {
    "engineering/compiler/roadmap/README.md":
        "# EOS Compiler Roadmap\n\n"
        "Tracks implementation milestones for the EOS Compiler.\n",

    "engineering/compiler/roadmap/Sprint-01-Lexer.md":
        "# Sprint 01 - EOS Lexer\n",

    "engineering/compiler/roadmap/Sprint-02-Parser.md":
        "# Sprint 02 - EOS Parser\n",

    "engineering/compiler/roadmap/Sprint-03-AST.md":
        "# Sprint 03 - Engineering AST\n",

    "engineering/compiler/roadmap/Sprint-04-Engineering-Model.md":
        "# Sprint 04 - Engineering Model\n",

    "engineering/compiler/roadmap/Sprint-05-Dependency.md":
        "# Sprint 05 - Dependency Manager\n",

    "engineering/compiler/roadmap/Sprint-06-Validator.md":
        "# Sprint 06 - Validator\n",

    "engineering/compiler/roadmap/Sprint-07-Emitters.md":
        "# Sprint 07 - Emitters\n",

    "engineering/compiler/roadmap/Sprint-08-Runtime.md":
        "# Sprint 08 - Runtime\n",
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
    print("EOS Compiler Roadmap Bootstrap")
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
