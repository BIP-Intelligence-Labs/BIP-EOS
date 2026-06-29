"""
========================================================================

BIP Engineering Labs
Engineering Operating System (EOS)

Bootstrap Script

Creates the Engineering Roadmap structure.

========================================================================
"""

from pathlib import Path

ROOT = Path.cwd()

DIRECTORIES = [
    "engineering/roadmap",
    "engineering/roadmap/EOS",
    "engineering/roadmap/BIP",
    "engineering/roadmap/releases",
]

FILES = {
    "engineering/roadmap/EOS/EOS-Platform-Roadmap.md":
        "# EOS Platform Roadmap\n\nTracks the implementation of the Engineering Operating System.\n",

    "engineering/roadmap/EOS/EOS-Compiler-Roadmap.md":
        "# EOS Compiler Roadmap\n\nTracks compiler development milestones.\n",

    "engineering/roadmap/BIP/Builder-Intelligence-Roadmap.md":
        "# Builder Intelligence Roadmap\n",

    "engineering/roadmap/BIP/Academy-Roadmap.md":
        "# BIP Academy Roadmap\n",

    "engineering/roadmap/BIP/AI-Roadmap.md":
        "# BIP AI Roadmap\n",

    "engineering/roadmap/BIP/Future-Products.md":
        "# Future Products Roadmap\n",

    "engineering/roadmap/releases/Genesis-0.1.md":
        "# Genesis 0.1 Release\n",

    "engineering/roadmap/releases/Genesis-0.2.md":
        "# Genesis 0.2 Release\n",

    "engineering/roadmap/releases/Genesis-0.3.md":
        "# Genesis 0.3 Release\n",

    "engineering/roadmap/releases/EOS-1.0.md":
        "# EOS 1.0 Release\n",
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
    print("Engineering Roadmap Bootstrap")
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
