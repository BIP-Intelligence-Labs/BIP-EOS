#!/usr/bin/env python3
"""
========================================================================
UEOS MGS-001

Migration Executor

Executes constitutional repository migrations.
========================================================================
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class MigrationTask:
    source: Path
    destination: Path


class MigrationExecutor:
    def __init__(self, root: Path | None = None) -> None:
        self.root = root or Path.cwd()

    def execute(self, tasks: list[MigrationTask], dry_run: bool = True) -> None:
        print("=" * 72)
        print("UEOS MGS-001")
        print("Migration Executor")
        print("=" * 72)

        for task in tasks:
            src = self.root / task.source
            dst = self.root / task.destination

            if not src.exists():
                print(f"[SKIP ] {task.source} (missing)")
                continue

            print(f"[MOVE ] {task.source} -> {task.destination}")

            if dry_run:
                continue

            dst.parent.mkdir(parents=True, exist_ok=True)

            if src.is_dir():
                shutil.copytree(src, dst, dirs_exist_ok=True)
            else:
                shutil.copy2(src, dst)

        print("=" * 72)
        print("Mode :", "DRY RUN" if dry_run else "EXECUTED")
        print("=" * 72)


def default_tasks() -> list[MigrationTask]:
    return [
        MigrationTask(Path("ai"), Path("src/bip_eos/ai")),
        MigrationTask(Path("cli"), Path("src/bip_eos/cli")),
        MigrationTask(Path("core"), Path("src/bip_eos/runtime")),
        MigrationTask(Path("discovery"), Path("src/bip_eos/audit")),
        MigrationTask(Path("plugins"), Path("src/bip_eos/plugins")),
        MigrationTask(Path("registry"), Path("src/bip_eos/registry")),
        MigrationTask(Path("shared"), Path("src/bip_eos/common")),
    ]


if __name__ == "__main__":
    executor = MigrationExecutor()

    # Change to False after reviewing the dry-run output.
    executor.execute(default_tasks(), dry_run=True)
