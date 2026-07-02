"""
========================================================================
MGS-001

Migration & Governance System

Public API
========================================================================
"""

from .engine import MigrationEngine

from .services import (
    MigrationAction,
    MigrationPlan,
    MigrationPlanner,
    ValidationIssue,
    ValidationResult,
    MigrationValidator,
    ExecutionResult,
    MigrationExecutor,
    MigrationReport,
    MigrationReporter,
    RollbackResult,
    RollbackEngine,
)

__version__ = "0.1.0"

__all__ = [

    # Engine
    "MigrationEngine",

    # Planner
    "MigrationAction",
    "MigrationPlan",
    "MigrationPlanner",

    # Validator
    "ValidationIssue",
    "ValidationResult",
    "MigrationValidator",

    # Executor
    "ExecutionResult",
    "MigrationExecutor",

    # Reporter
    "MigrationReport",
    "MigrationReporter",

    # Rollback
    "RollbackResult",
    "RollbackEngine",
]
