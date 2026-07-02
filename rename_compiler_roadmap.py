"""
rename_compiler_roadmap.py

M-008 Repository Cleanup

Renames:

    engineering/compiler/roadmap

to:

    engineering/compiler/roadmaps

Safely merges if the destination already exists.

Usage:
    python rename_compiler_roadmap.py
"""

from pathlib import Path
import shutil

ROOT = Path.cwd()
OLD = ROOT / "engineering" / "compiler" / "roadmap"
NEW = ROOT / "engineering" / "compiler" / "roadmaps"


def merge(src: Path, dst: Path):
    dst.mkdir(parents=True, exist_ok=True)

    for item in src.iterdir():
        target = dst / item.name

        if item.is_dir():
            merge(item, target)
            try:
                if not any(item.iterdir()):
                    item.rmdir()
            except OSError:
                pass
        else:
            if target.exists():
                print(f"[KEEP] {target.relative_to(ROOT)}")
            else:
                shutil.move(str(item), str(target))
                print(f"[MOVE] {item.relative_to(ROOT)} -> {target.relative_to(ROOT)}")


def main():
    print("=" * 64)
    print("UEOS Compiler Roadmap Rename")
    print("=" * 64)

    if not OLD.exists():
        print("[OK] Legacy directory not found.")
        return

    merge(OLD, NEW)

    try:
        if not any(OLD.iterdir()):
            OLD.rmdir()
            print(f"[REMOVE] {OLD.relative_to(ROOT)}")
        else:
            print(f"[REVIEW] {OLD.relative_to(ROOT)} still contains files.")
    except OSError:
        print(f"[REVIEW] Unable to remove {OLD.relative_to(ROOT)}")

    print("\nDone.")
    print("Verify:")
    print("  tree engineering\\compiler /F")
    print("  git diff")
    print("  git status")


if __name__ == "__main__":
    main()
