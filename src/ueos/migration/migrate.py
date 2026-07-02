"""
========================================================================
UEOS

Migration CLI

MGS-001
========================================================================
"""

from __future__ import annotations

import argparse

from ueos.migration import MigrationEngine


def command_plan(args):

    engine = MigrationEngine()
    engine.plan()


def command_validate(args):

    engine = MigrationEngine()

    plan = engine.plan()

    engine.validate(plan)


def command_execute(args):

    engine = MigrationEngine()

    plan = engine.plan()

    validation = engine.validate(plan)

    if not validation.passed:
        print("\nMigration aborted.")
        return

    result = engine.execute(plan)

    engine.report(result)


def command_rollback(args):

    print(
        "Rollback requires an ExecutionResult "
        "from a previous transaction."
    )


def register(subparsers):

    parser = subparsers.add_parser(
        "migrate",
        help="Migration & Governance System",
    )

    commands = parser.add_subparsers(dest="migration_command")

    p = commands.add_parser("plan")
    p.set_defaults(func=command_plan)

    v = commands.add_parser("validate")
    v.set_defaults(func=command_validate)

    e = commands.add_parser("execute")
    e.set_defaults(func=command_execute)

    r = commands.add_parser("rollback")
    r.set_defaults(func=command_rollback)
