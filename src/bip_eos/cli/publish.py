"""
========================================================================
UEOS

EPF-001
Engineering Publishing Framework

Publishing CLI

UEOS M-003
========================================================================
"""

from __future__ import annotations


def help_command() -> None:
    print("=" * 72)
    print("EPF-001 Engineering Publishing Framework")
    print("=" * 72)
    print()
    print("Usage")
    print("    ueos publish <command>")
    print()
    print("Commands")
    print("    documentation")
    print("    reports")
    print("    academy")
    print("    website")
    print()
    print("Examples")
    print("    ueos publish documentation")
    print("    ueos publish reports")
    print("=" * 72)


def documentation() -> None:
    print("Documentation publisher not implemented yet.")


def reports() -> None:
    print("Report publisher not implemented yet.")


def academy() -> None:
    print("Academy publisher not implemented yet.")


def website() -> None:
    print("Website publisher not implemented yet.")


COMMANDS = {
    "documentation": documentation,
    "docs": documentation,
    "reports": reports,
    "academy": academy,
    "website": website,
}


def handle(command: str | None, args: list[str]) -> None:
    if command is None:
        help_command()
        return

    handler = COMMANDS.get(command.lower())

    if handler is None:
        print(f"Unknown publish command: {command}")
        help_command()
        return

    handler()
