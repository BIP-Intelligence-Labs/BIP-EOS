"""
========================================================================

BIP Engineering Labs
Engineering Operating System (EOS)

Bootstrap Cleanup Script

Removes all Python __pycache__ directories.

========================================================================
"""

from pathlib import Path
import shutil

ROOT = Path.cwd()


def remove_pycache(root: Path):
    removed = 0

    print("=" * 70)
    print("EOS Python Cache Cleanup")
    print("=" * 70)

    for directory in root.rglob("__pycache__"):
        try:
            shutil.rmtree(directory)
            removed += 1
            print(f"[DELETE] {directory}")
        except Exception as ex:
            print(f"[ERROR ] {directory}")
            print(f"         {ex}")

    print("-" * 70)
    print(f"Removed __pycache__ directories : {removed}")
    print("=" * 70)


if __name__ == "__main__":
    remove_pycache(ROOT)
