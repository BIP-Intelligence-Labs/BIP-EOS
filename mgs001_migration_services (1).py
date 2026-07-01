
#!/usr/bin/env python3
"""
UEOS MGS-001
Migration Services Skeleton (v0.2)

Implements:
- Copier
- Validator
- Report Generator
- Cleanup Engine
- Rollback Engine

Safe by default.
"""

from __future__ import annotations

import json
import shutil
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class MigrationTask:
    source: Path
    destination: Path


class MigrationCopier:
    def __init__(self):
        self.manifest: list[dict] = []

    def execute(self, tasks: list[MigrationTask], root: Path):
        for task in tasks:
            src = root / task.source
            dst = root / task.destination

            if not src.exists():
                continue

            dst.parent.mkdir(parents=True, exist_ok=True)

            if src.is_dir():
                shutil.copytree(src, dst, dirs_exist_ok=True)
            else:
                shutil.copy2(src, dst)

            self.manifest.append(
                {
                    "source": str(src),
                    "destination": str(dst),
                    "type": "directory" if src.is_dir() else "file",
                    "timestamp": datetime.utcnow().isoformat(),
                }
            )

        return self.manifest


class MigrationValidator:
    def validate(self, tasks: list[MigrationTask], root: Path):
        failures = []

        for task in tasks:
            src = root / task.source
            dst = root / task.destination

            if src.exists() and not dst.exists():
                failures.append(str(task.destination))

        return len(failures) == 0, failures


class MigrationReporter:
    def generate(self, manifest: list[dict], output: Path):
        output.parent.mkdir(parents=True, exist_ok=True)

        report = {
            "generated": datetime.utcnow().isoformat(),
            "entries": manifest,
        }

        output.write_text(
            json.dumps(report, indent=4),
            encoding="utf-8",
        )

        return output


class CleanupEngine:
    def cleanup(self, tasks: list[MigrationTask], root: Path):
        removed = []

        for task in tasks:
            src = root / task.source

            if src.is_dir():
                try:
                    next(src.iterdir())
                except StopIteration:
                    src.rmdir()
                    removed.append(str(src))

        return removed


class RollbackEngine:
    def rollback(self, manifest: list[dict]):
        for entry in reversed(manifest):
            dst = Path(entry["destination"])

            if dst.is_file():
                dst.unlink(missing_ok=True)

            elif dst.is_dir():
                shutil.rmtree(dst, ignore_errors=True)


if __name__ == "__main__":
    print("=" * 72)
    print("UEOS MGS-001 Migration Services")
    print("=" * 72)
    print("This module provides:")
    print("  • MigrationCopier")
    print("  • MigrationValidator")
    print("  • MigrationReporter")
    print("  • CleanupEngine")
    print("  • RollbackEngine")
    print("=" * 72)
