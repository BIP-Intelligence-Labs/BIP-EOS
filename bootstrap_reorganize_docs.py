"""
========================================================================

BIP Engineering Labs
Engineering Operating System (EOS)

Repository Reorganization Bootstrap

Moves engineering documentation from docs/
to engineering/ while preserving existing files.

Engineering/ = Engineering Truth
docs/        = Published Documentation

========================================================================
"""

from pathlib import Path
import shutil

ROOT = Path.cwd()

MOVES = [
    ("docs/architecture", "engineering/architecture"),
    ("docs/engineering", "engineering"),
    ("docs/governance", "engineering/governance"),
    ("docs/roadmap", "engineering/roadmap"),
    ("docs/decisions", "engineering/decisions"),
]

PUBLIC_DOCS = [
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


def merge(src: Path, dst: Path):
    if not src.exists():
        print(f"[SKIP] {src}")
        return

    dst.mkdir(parents=True, exist_ok=True)

    for item in src.iterdir():
        target = dst / item.name

        if item.is_dir():
            merge(item, target)
        else:
            if target.exists():
                print(f"[KEEP ] {target}")
            else:
                shutil.move(str(item), str(target))
                print(f"[MOVE ] {item} -> {target}")

    try:
        src.rmdir()
        print(f"[REMOVE] {src}")
    except OSError:
        pass


def verify_public_docs():
    print("-" * 70)
    print("Verifying Public Documentation")
    print("-" * 70)

    for folder in PUBLIC_DOCS:
        path = ROOT / folder
        if path.exists():
            print(f"[ OK  ] {path}")
        else:
            path.mkdir(parents=True, exist_ok=True)
            print(f"[CREATE] {path}")


def main():
    print("=" * 70)
    print("EOS Engineering Truth Bootstrap")
    print("=" * 70)

    for src, dst in MOVES:
        merge(ROOT / src, ROOT / dst)

    verify_public_docs()

    print("-" * 70)
    print("Engineering Truth : engineering/")
    print("Published Docs    : docs/")
    print("=" * 70)


if __name__ == "__main__":
    main()
