"""
========================================================================
UEOS

ECS-001
Engineering Compiler System

Compiler CLI

UEOS M-003
========================================================================
"""

from __future__ import annotations


def help_command() -> None:
    print("=" * 72)
    print("ECS-001 Engineering Compiler System")
    print("=" * 72)
    print()
    print("Usage")
    print("    ueos compiler <command>")
    print()
    print("Commands")
    print("    compile")
    print("    emit")
    print("    verify")
    print("    package")
    print()
    print("Examples")
    print("    ueos compiler compile")
    print("    ueos compiler verify")
    print("=" * 72)


# ============================================================================
# COMMANDS
# ============================================================================

def compile() -> None:
    print("ECS-001 Compiler not implemented yet.")


def emit() -> None:
    print("ECS-001 Artifact Emitter not implemented yet.")


def verify() -> None:
    print("ECS-001 Compiler Verification not implemented yet.")


def package() -> None:
    print("ECS-001 Packaging not implemented yet.")


# ============================================================================
# COMMAND TABLE
# ============================================================================

COMMANDS = {
    "compile": compile,
    "emit": emit,
    "verify": verify,
    "package": package,
}


# ============================================================================
# ENTRY POINT
# ============================================================================

def handle(command: str | None, args: list[str]) -> None:
    """
    Handle

        ueos compiler <command>
    """

    if command is None:
        help_command()
        return

    command = command.lower()

    handler = COMMANDS.get(command)

    if handler is None:
        print(f"Unknown compiler command: {command}")
        print()
        help_command()
        return

    handler()
