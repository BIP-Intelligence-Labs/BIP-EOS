#!/usr/bin/env python3
"""
migrate_repository.py

Safe migration engine for Genesis.
Default mode is --dry-run.
No files are moved unless --execute is supplied.

Usage:
    python migrate_repository.py
    python migrate_repository.py --dry-run
    python migrate_repository.py --execute
"""

from pathlib import Path
import argparse
import json
import shutil
from datetime import datetime

ROOT = Path.cwd()
REPORTS = ROOT / "reports"

PLAN_FILE = REPORTS / "migration_plan.json"

def load_plan():
    if not PLAN_FILE.exists():
        raise SystemExit("Run repository_analyzer.py first.")
    return json.loads(PLAN_FILE.read_text(encoding="utf-8"))

def backup_dir():
    d = ROOT / "migration_backups" / datetime.now().strftime("%Y%m%d_%H%M%S")
    d.mkdir(parents=True, exist_ok=True)
    return d

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    execute = args.execute
    plan = load_plan()

    print("="*60)
    print("Genesis Migration Engine")
    print("="*60)
    print("Mode:", "EXECUTE" if execute else "DRY RUN")

    backup = backup_dir() if execute else None
    moved = 0

    log = []

    for item in plan:
        src = ROOT / item["item"]
        dst = ROOT / item["recommended_destination"]

        entry = {
            "source": str(src),
            "target": str(dst),
            "action": item["action"]
        }
        log.append(entry)

        print(f"{item['action']:8} {src} -> {dst}")

        if execute:
            if src.exists():
                backup_target = backup / src.name
                if src.is_file():
                    shutil.copy2(src, backup_target)
                # Real move intentionally disabled until v2.
                # shutil.move(str(src), str(dst))
                moved += 1

    (REPORTS / "migration_execution_log.json").write_text(
        json.dumps(log, indent=2), encoding="utf-8"
    )

    print("-"*60)
    print("Items in plan :", len(plan))
    print("Processed     :", moved if execute else 0)
    print("Execution log :", REPORTS / "migration_execution_log.json")
    if execute:
        print("Backups       :", backup)
        print("NOTE: Physical moves are intentionally disabled in this version.")

if __name__ == "__main__":
    main()
