#!/usr/bin/env python3
"""
========================================================================
MGS-001

Migration Executor

Constitutional Execution Service
========================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
import shutil

from .planner import MigrationPlan
from .validator import MigrationValidator


@dataclass(slots=True)
class ExecutionResult:
    transaction_id: str
    moved: list[tuple[Path, Path]] = field(default_factory=list)
    success: bool = True
    errors: list[str] = field(default_factory=list)


class MigrationExecutor:
    """
    Executes an APPROVED MigrationPlan.

    The executor validates the plan before performing any move.
    """

    def execute(self, plan: MigrationPlan) -> ExecutionResult:

        validator = MigrationValidator()
        validation = validator.validate(plan)

        tx = ExecutionResult(
            transaction_id=f"TX-{datetime.now():%Y%m%d-%H%M%S}"
        )

        if not validation.passed:
            tx.success = False
            tx.errors = [
                issue.message
                for issue in validation.issues
                if issue.severity == "ERROR"
            ]
            return tx

        for action in plan.actions:
            try:
                action.destination.parent.mkdir(parents=True, exist_ok=True)

                shutil.move(
                    str(action.source),
                    str(action.destination),
                )

                tx.moved.append(
                    (action.source, action.destination)
                )

            except Exception as ex:
                tx.success = False
                tx.errors.append(str(ex))
                break

        return tx

    def summary(self, result: ExecutionResult) -> None:

        print("=" * 72)
        print("MGS-001 Migration Executor")
        print("=" * 72)
        print(f"Transaction : {result.transaction_id}")
        print(f"Success     : {result.success}")
        print(f"Moved       : {len(result.moved)}")
        print()

        for src, dst in result.moved:
            print(f"[MOVE]")
            print(f"  FROM : {src}")
            print(f"  TO   : {dst}")

        if result.errors:
            print()
            print("Errors")
            for err in result.errors:
                print(f" - {err}")

        print("=" * 72)
        print("Execution Complete")
        print("=" * 72)
