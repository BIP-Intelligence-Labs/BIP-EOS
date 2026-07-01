"""
========================================================================
UEOS

EAuS-001
Engineering Audit System

Audit CLI

UEOS M-003
========================================================================
"""

from __future__ import annotations

from bip_eos.audit.engine import AuditEngine


def help_command() -> None:
    print("=" * 72)
    print("EAuS-001 Engineering Audit System")
    print("=" * 72)
    print()
    print("Usage")
    print("    ueos audit <command>")
    print()
    print("Commands")
    print("    discover")
    print("    analyze")
    print("    validate")
    print("    report")
    print()
    print("Examples")
    print("    ueos audit discover")
    print("=" * 72)


def discover() -> None:
    """
    Execute repository discovery.
    """
    engine = AuditEngine(".")
    engine.discover()


def analyze() -> None:
    print("Analyze engine not implemented yet.")


def validate() -> None:
    print("Validation engine not implemented yet.")


def report() -> None:
    print("Reporting engine not implemented yet.")


COMMANDS = {
    "discover": discover,
    "analyze": analyze,
    "validate": validate,
    "report": report,
}


def handle(command: str | None, args: list[str]) -> None:
    """
    Handle

        ueos audit <command>
    """

    if command is None:
        help_command()
        return

    command = command.lower()

    handler = COMMANDS.get(command)

    if handler is None:
        print(f"Unknown audit command: {command}")
        print()
        help_command()
        return

    handler()
