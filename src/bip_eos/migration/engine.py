"""
========================================================================
MGS-001

Migration & Governance System

Constitutional Orchestrator
========================================================================
"""

from __future__ import annotations

from pathlib import Path

from bip_eos.migration.services.planner import MigrationPlanner
from bip_eos.migration.services.validator import MigrationValidator
from bip_eos.migration.services.executor import MigrationExecutor
from bip_eos.migration.services.reporter import MigrationReporter
from bip_eos.migration.services.rollback import RollbackEngine


class MigrationEngine:
    """
    Constitutional orchestrator for MGS-001.

    Coordinates the migration lifecycle.
    """

    def __init__(self, root: str | Path = ".") -> None:

        self.root = Path(root).resolve()

        self.planner = MigrationPlanner(self.root)
        self.validator = MigrationValidator()
        self.executor = MigrationExecutor()
        self.reporter = MigrationReporter()
        self.rollback = RollbackEngine()

    # --------------------------------------------------------------

    def plan(self):

        plan = self.planner.build_repository_plan()
        self.planner.summary(plan)

        return plan

    # --------------------------------------------------------------

    def validate(self, plan):

        result = self.validator.validate(plan)
        self.validator.summary(result)

        return result

    # --------------------------------------------------------------

    def execute(self, plan):

        result = self.executor.execute(plan)
        self.executor.summary(result)

        return result

    # --------------------------------------------------------------

    def report(
        self,
        execution_result,
        output="reports/migration_report.json",
    ):

        report = self.reporter.build(execution_result)

        self.reporter.summary(report)

        self.reporter.save_json(report, output)

        return report

    # --------------------------------------------------------------

    def rollback_transaction(self, execution_result):

        result = self.rollback.rollback(execution_result)

        self.rollback.summary(result)

        return result


if __name__ == "__main__":

    engine = MigrationEngine()

    plan = engine.plan()

    validation = engine.validate(plan)

    if validation.passed:

        print()
        print("Repository is ready for execution.")
        print("Run:")
        print("    engine.execute(plan)")

    else:

        print()
        print("Migration validation failed.")
