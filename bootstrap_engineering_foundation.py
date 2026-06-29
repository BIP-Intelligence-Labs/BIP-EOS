"""
========================================================================

BIP Engineering Labs
Engineering Operating System (EOS)

Bootstrap Script

Creates project-wide engineering decisions, standards, glossary,
and templates.

========================================================================
"""

from pathlib import Path

ROOT = Path.cwd()

DIRECTORIES = [
    "engineering/decisions",
    "engineering/glossary",
    "engineering/standards",
    "engineering/templates",
]

FILES = {
    "engineering/decisions/README.md":
        "# Engineering Decision Records (ADRs)\n",

    "engineering/decisions/ADR-0001-BIP-Architecture.md":
        "# ADR-0001 BIP Architecture\n",

    "engineering/decisions/ADR-0002-EOS-as-a-Platform.md":
        "# ADR-0002 EOS as a Platform\n",

    "engineering/decisions/ADR-0003-Compiler-First.md":
        "# ADR-0003 Compiler First Strategy\n",

    "engineering/glossary/README.md":
        "# Engineering Glossary\n",

    "engineering/standards/README.md":
        "# Engineering Standards\n",

    "engineering/templates/README.md":
        "# Engineering Templates\n",
}


def create_dir(path: Path):
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
    print("Engineering Foundation Bootstrap")
    print("=" * 70)

    for d in DIRECTORIES:
        create_dir(ROOT / d)

    for f, t in FILES.items():
        create_file(ROOT / f, t)

    print("-" * 70)
    print(f"Directories : {len(DIRECTORIES)}")
    print(f"Files       : {len(FILES)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
