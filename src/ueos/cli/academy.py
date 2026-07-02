"""
========================================================================
UEOS

EAS-001
Engineering Academy System

Academy CLI

UEOS M-003
========================================================================
"""

from __future__ import annotations


def help_command() -> None:
    print("=" * 72)
    print("EAS-001 Engineering Academy System")
    print("=" * 72)
    print()
    print("Usage")
    print("    ueos academy <command>")
    print()
    print("Commands")
    print("    curriculum")
    print("    labs")
    print("    exams")
    print("    certifications")
    print("=" * 72)


def curriculum() -> None:
    print("Curriculum engine not implemented yet.")


def labs() -> None:
    print("Labs engine not implemented yet.")


def exams() -> None:
    print("Exam engine not implemented yet.")


def certifications() -> None:
    print("Certification engine not implemented yet.")


COMMANDS = {
    "curriculum": curriculum,
    "labs": labs,
    "exams": exams,
    "certifications": certifications,
}


def handle(command: str | None, args: list[str]) -> None:
    if command is None:
        help_command()
        return

    handler = COMMANDS.get(command.lower())

    if handler is None:
        print(f"Unknown academy command: {command}")
        help_command()
        return

    handler()
