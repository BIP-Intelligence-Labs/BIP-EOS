#!/usr/bin/env python3
"""
bootstrap_runtime_reorganization_v1.py

UEOS Bootstrap Program

Purpose
-------
Safely migrate runtime package names to the official UEOS Runtime
Architecture v1.0.

Changes
-------
src/bip_eos/core      -> src/bip_eos/runtime
src/bip_eos/config    -> src/bip_eos/runtime/configuration
src/bip_eos/database  -> src/bip_eos/storage

Safe by default:
- Dry run unless --apply is specified.
- Never overwrites existing files.
- Uses only the Python Standard Library.
"""

from pathlib import Path
import shutil
import sys

MAPPINGS = [
    ("src/bip_eos/core", "src/bip_eos/runtime"),
    ("src/bip_eos/config", "src/bip_eos/runtime/configuration"),
    ("src/bip_eos/database", "src/bip_eos/storage"),
]


def find_root(start: Path) -> Path:
    cur = start.resolve()
    while cur != cur.parent:
        if (cur / "src").exists() and (cur / "engineering").exists():
            return cur
        cur = cur.parent
    raise RuntimeError("UEOS repository root not found.")


def move(src: Path, dst: Path, apply: bool):
    if not src.exists():
        print(f"[SKIP   ] {src} (missing)")
        return

    if dst.exists():
        print(f"[SKIP   ] {dst} (destination exists)")
        return

    print(f"[MOVE   ] {src} -> {dst}")

    if apply:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))


def main():
    apply = "--apply" in sys.argv
    root = find_root(Path(__file__).parent)

    print("=" * 72)
    print("UEOS Runtime Reorganization v1.0")
    print(f"Mode: {'APPLY' if apply else 'DRY RUN'}")
    print("=" * 72)

    for s, d in MAPPINGS:
        move(root / s, root / d, apply)

    print("=" * 72)
    if apply:
        print("Runtime reorganization complete.")
    else:
        print("Dry run complete. Re-run with --apply to perform changes.")
    print("=" * 72)


if __name__ == "__main__":
    main()
