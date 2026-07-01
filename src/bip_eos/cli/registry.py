"""
========================================================================
UEOS

ERS-001
Engineering Registry System

Registry CLI

UEOS M-003
========================================================================
"""

from __future__ import annotations


def help_command() -> None:
    print("=" * 72)
    print("ERS-001 Engineering Registry System")
    print("=" * 72)
    print()
    print("Usage")
    print("    ueos registry <command>")
    print()
    print("Commands")
    print("    build")
    print("    verify")
    print("    export")
    print("    status")
    print()
    print("Examples")
    print("    ueos registry build")
    print("    ueos registry verify")
    print("=" * 72)


# ============================================================================
# COMMANDS
# ============================================================================

def build() -> None:
    print("ERS-001 Registry Builder not implemented yet.")


def verify() -> None:
    print("ERS-001 Registry Verification not implemented yet.")


def export() -> None:
    print("ERS-001 Registry Export not implemented yet.")


def status() -> None:
    print("ERS-001 Registry Status not implemented yet.")


# ============================================================================
# COMMAND TABLE
# ============================================================================

COMMANDS = {
    "build": build,
    "verify": verify,
    "export": export,
    "status": status,
}


# ============================================================================
# ENTRY POINT
# ============================================================================

def handle(command: str | None, args: list[str]) -> None:
    """
    Handle

        ueos registry <command>
    """

    if command is None:
        help_command()
        return

    command = command.lower()

    handler = COMMANDS.get(command)

    if handler is None:
        print(f"Unknown registry command: {command}")
        print()
        help_command()
        return

    handler()
