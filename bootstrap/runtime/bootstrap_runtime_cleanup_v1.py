#!/usr/bin/env python3
"""
bootstrap_runtime_cleanup_v1.py

UEOS Runtime Cleanup

Removes duplicate runtime service directories that were superseded by
src/bip_eos/services/.

Default: DRY RUN
Use --apply to perform deletion.

Standard Library only.
"""

from pathlib import Path
import shutil
import sys

REMOVE = [
    "src/bip_eos/runtime/documentation",
    "src/bip_eos/runtime/logging",
    "src/bip_eos/runtime/repository",
]

def find_root(start: Path) -> Path:
    cur = start.resolve()
    while cur != cur.parent:
        if (cur / "src").exists() and (cur / "engineering").exists():
            return cur
        cur = cur.parent
    raise RuntimeError("UEOS repository root not found.")

def main():
    apply = "--apply" in sys.argv
    root = find_root(Path(__file__).parent)

    print("="*72)
    print("UEOS Runtime Cleanup v1.0")
    print(f"Mode: {'APPLY' if apply else 'DRY RUN'}")
    print("="*72)

    removed = 0
    skipped = 0

    for rel in REMOVE:
        target = root / rel
        if not target.exists():
            print(f"[SKIP   ] {rel} (not found)")
            skipped += 1
            continue

        print(f"[REMOVE ] {rel}")

        if apply:
            shutil.rmtree(target)
            removed += 1

    print("="*72)
    if apply:
        print(f"Directories removed : {removed}")
    else:
        print("No changes made.")
        print("Re-run with --apply to remove directories.")
    print(f"Directories skipped : {skipped}")
    print("="*72)

if __name__ == "__main__":
    main()
