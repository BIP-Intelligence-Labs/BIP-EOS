#!/usr/bin/env python3
"""
foundation_migrator.py

Phase 1 Migration:
    src/genesis/core
        ├── repository
        ├── registry
        ├── logging
        └── version
            ↓
    src/bip_eos/core

Default: dry-run
Use --execute to copy files.
"""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path.cwd()

MODULES = [
    "repository",
    "registry",
    "logging",
    "version",
]

OLD = ROOT / "src" / "genesis" / "core"
NEW = ROOT / "src" / "bip_eos" / "core"


def rewrite_imports(text: str) -> str:
    return (
        text.replace("from genesis", "from bip_eos")
            .replace("import genesis", "import bip_eos")
            .replace("genesis.", "bip_eos.")
    )


def migrate_directory(src: Path, dst: Path, execute: bool, report: list):
    if not src.exists():
        return

    dst.mkdir(parents=True, exist_ok=True)

    for item in src.rglob("*"):
        rel = item.relative_to(src)
        target = dst / rel

        if item.is_dir():
            if execute:
                target.mkdir(parents=True, exist_ok=True)
            continue

        report.append({
            "source": str(item.relative_to(ROOT)),
            "target": str(target.relative_to(ROOT))
        })

        print(f"[COPY] {item.relative_to(ROOT)} -> {target.relative_to(ROOT)}")

        if not execute:
            continue

        target.parent.mkdir(parents=True, exist_ok=True)

        if item.suffix == ".py":
            text = item.read_text(encoding="utf-8")
            target.write_text(rewrite_imports(text), encoding="utf-8")
        else:
            shutil.copy2(item, target)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--execute", action="store_true")
    args = ap.parse_args()

    print("=" * 70)
    print("BIP EOS Foundation Migrator")
    print("=" * 70)
    print("Mode:", "EXECUTE" if args.execute else "DRY RUN")

    report = []

    for module in MODULES:
        migrate_directory(
            OLD / module,
            NEW / module,
            args.execute,
            report
        )

    manifest = {
        "phase": "Foundation",
        "generated": datetime.now().isoformat(),
        "mode": "EXECUTE" if args.execute else "DRY_RUN",
        "items": report
    }

    out = ROOT / "reports" / "foundation_migration_report.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print("-" * 70)
    print("Modules processed :", len(MODULES))
    print("Items discovered  :", len(report))
    print("Report            :", out.relative_to(ROOT))
    print("=" * 70)


if __name__ == "__main__":
    main()
