"""
move_legacy_core.py

Migrates legacy ./core packages into the new src/ueos layout.

Usage:
    python move_legacy_core.py
"""

from pathlib import Path
import shutil

ROOT = Path.cwd()

MAPPINGS = {
    ROOT / "core" / "ai": ROOT / "src" / "ueos" / "ai",
    ROOT / "core" / "logging": ROOT / "src" / "ueos" / "runtime" / "logging",
    ROOT / "core" / "health": ROOT / "src" / "ueos" / "runtime" / "health",
    ROOT / "core" / "version": ROOT / "src" / "ueos" / "runtime" / "version",
    ROOT / "core" / "plugins": ROOT / "src" / "ueos" / "plugins",
}

def merge_directory(src: Path, dst: Path):
    if not src.exists():
        print(f"[SKIP] {src} not found")
        return
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        target = dst / item.name
        if item.is_dir():
            merge_directory(item, target)
        else:
            if target.exists():
                print(f"[KEEP] {target}")
            else:
                shutil.move(str(item), str(target))
                print(f"[MOVE] {item} -> {target}")

def main():
    print("=== UEOS Legacy Core Migration ===")
    for src, dst in MAPPINGS.items():
        merge_directory(src, dst)

    print("\nManual review recommended for:")
    print("  core/docs")
    print("\nIf everything builds and tests pass, remove the legacy 'core' directory.")

if __name__ == "__main__":
    main()
