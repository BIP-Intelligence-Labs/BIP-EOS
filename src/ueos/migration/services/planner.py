#!/usr/bin/env python3
"""
========================================================================
MGS-001

Migration Planner

Constitutional Planning Service
========================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from datetime import datetime
from typing import List


@dataclass(slots=True)
class MigrationAction:
    source: Path
    destination: Path
    operation: str = "MOVE"
    approved: bool = False


@dataclass(slots=True)
class MigrationPlan:
    plan_id: str
    created: str
    actions: List[MigrationAction] = field(default_factory=list)

    def add(self, source: str | Path, destination: str | Path,
            operation: str = "MOVE") -> None:
        self.actions.append(
            MigrationAction(
                source=Path(source),
                destination=Path(destination),
                operation=operation,
            )
        )

    @property
    def total_actions(self) -> int:
        return len(self.actions)


class MigrationPlanner:
    """
    MGS-001 Constitutional Planning Service.

    Builds a migration plan only.
    Does not modify the repository.
    """

    def __init__(self, root: str | Path = ".") -> None:
        self.root = Path(root).resolve()

    def build_repository_plan(self) -> MigrationPlan:
        plan = MigrationPlan(
            plan_id=f"MGS-{datetime.now():%Y%m%d-%H%M%S}",
            created=datetime.now().isoformat(timespec="seconds"),
        )

        mappings = {
            "ai": "src/bip_eos/ai",
            "cli": "src/bip_eos/cli",
            "core": "src/bip_eos/runtime",
            "discovery": "src/bip_eos/audit",
            "plugins": "src/bip_eos/plugins",
            "registry": "src/bip_eos/registry",
            "reports": "engineering/reports",
            "shared": "src/bip_eos/common",
            "templates": "bootstrap/templates",
            "Lab": "research",
        }

        for src, dst in mappings.items():
            source = self.root / src
            if source.exists():
                plan.add(source, self.root / dst)

        return plan

    def summary(self, plan: MigrationPlan) -> None:
        print("=" * 72)
        print("MGS-001 Migration Plan")
        print("=" * 72)
        print(f"Plan ID : {plan.plan_id}")
        print(f"Created : {plan.created}")
        print(f"Actions : {plan.total_actions}")
        print("=" * 72)

        for action in plan.actions:
            print(f"[{action.operation}]")
            print(f"  FROM : {action.source}")
            print(f"  TO   : {action.destination}")
            print()

        print("=" * 72)
        print("Planning Complete")
        print("=" * 72)


if __name__ == "__main__":
    planner = MigrationPlanner()
    plan = planner.build_repository_plan()
    planner.summary(plan)
