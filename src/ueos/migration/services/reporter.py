#!/usr/bin/env python3
"""
========================================================================
MGS-001

Migration Reporter

Constitutional Reporting Service
========================================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import json

from .executor import ExecutionResult


@dataclass(slots=True)
class MigrationReport:
    transaction_id: str
    generated: str
    success: bool
    moved: int
    errors: list[str]


class MigrationReporter:
    """
    Produces migration reports.

    Reporting only.
    Never executes migrations.
    """

    def build(self, result: ExecutionResult) -> MigrationReport:
        return MigrationReport(
            transaction_id=result.transaction_id,
            generated=datetime.now().isoformat(timespec="seconds"),
            success=result.success,
            moved=len(result.moved),
            errors=list(result.errors),
        )

    def to_dict(self, report: MigrationReport) -> dict:
        return {
            "transaction_id": report.transaction_id,
            "generated": report.generated,
            "success": report.success,
            "moved": report.moved,
            "errors": report.errors,
        }

    def save_json(
        self,
        report: MigrationReport,
        output: str | Path,
    ) -> Path:
        output = Path(output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(self.to_dict(report), indent=4),
            encoding="utf-8",
        )
        return output

    def summary(self, report: MigrationReport) -> None:
        print("=" * 72)
        print("MGS-001 Migration Report")
        print("=" * 72)
        print(f"Transaction : {report.transaction_id}")
        print(f"Generated   : {report.generated}")
        print(f"Success     : {report.success}")
        print(f"Items Moved : {report.moved}")
        if report.errors:
            print("\nErrors")
            for err in report.errors:
                print(f" - {err}")
        else:
            print("\nNo execution errors.")
        print("=" * 72)
