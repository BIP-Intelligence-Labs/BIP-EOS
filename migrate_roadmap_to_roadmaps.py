"""
migrate_roadmap_to_roadmaps.py

Migrates the legacy engineering/roadmap directory into
engineering/roadmaps, preserving existing files and avoiding overwrites.

Usage:
    python migrate_roadmap_to_roadmaps.py
"""

from pathlib import Path
import shutil

ROOT = Path.cwd()
OLD = ROOT / "engineering" / "roadmap"
NEW = ROOT / "engineering" / "roadmaps"

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
                print(f"[KEEP] {target}")
            else:
                shutil.move(str(item), str(target))
                print(f"[MOVE] {item} -> {target}")

def main():
    if not OLD.exists():
        print("[OK] No legacy engineering/roadmap directory found.")
        return

    print("=" * 60)
    print("UEOS Roadmap Migration")
    print("=" * 60)

    merge(OLD, NEW)

    try:
        if not any(OLD.iterdir()):
            OLD.rmdir()
            print(f"[REMOVE] {OLD}")
        else:
            print(f"[REVIEW] {OLD} still contains files.")
    except OSError:
        print(f"[REVIEW] Unable to remove {OLD}")

    print("\nMigration complete.")
    print("Verify with:")
    print("  tree engineering\\roadmaps /F")
    print("  git diff")
    print("  git status")

if __name__ == "__main__":
    main()
