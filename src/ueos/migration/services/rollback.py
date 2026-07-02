#!/usr/bin/env python3
"""
========================================================================
MGS-001

Rollback Engine

Constitutional Recovery Service
========================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import shutil

from .executor import ExecutionResult


@dataclass(slots=True)
class RollbackResult:
    success: bool = True
    restored: list[tuple[Path, Path]] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


class RollbackEngine:
    """
    Restores repository state from an ExecutionResult.

    Assumes the execution recorded each successful move.
    """

    def rollback(self, execution: ExecutionResult) -> RollbackResult:

        result = RollbackResult()

        for source, destination in reversed(execution.moved):
            try:
                source.parent.mkdir(parents=True, exist_ok=True)

                if destination.exists():
                    shutil.move(str(destination), str(source))
                    result.restored.append((destination, source))
                else:
                    result.success = False
                    result.errors.append(
                        f"Missing destination for rollback: {destination}"
                    )

            except Exception as ex:
                result.success = False
                result.errors.append(str(ex))

        return result

    def summary(self, result: RollbackResult) -> None:

        print("=" * 72)
        print("MGS-001 Rollback Engine")
        print("=" * 72)
        print(f"Success  : {result.success}")
        print(f"Restored : {len(result.restored)}")
        print()

        for frm, to in result.restored:
            print("[RESTORE]")
            print(f"  FROM : {frm}")
            print(f"  TO   : {to}")

        if result.errors:
            print("\nErrors")
            for err in result.errors:
                print(f" - {err}")

        print("=" * 72)
