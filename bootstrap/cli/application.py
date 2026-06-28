"""
bootstrap/cli/application.py

Bootstrap CLI Application
"""

from __future__ import annotations

from typing import Any

from .commands import Commands


class BootstrapApplication:
    """Application layer for the Bootstrap CLI."""

    def __init__(self) -> None:
        self.commands = Commands()

    def run(self, command: str, *args: Any) -> int:
        """Execute a Bootstrap command."""

        match command:
            case "doctor":
                return self.commands.doctor()

            case "repair":
                self.commands.repair()

            case "release":
                self.commands.release()

            case "new-plugin":
                if not args:
                    raise ValueError("Plugin name is required.")
                self.commands.new_plugin(str(args[0]))

            case "root":
                from .project_locator import ProjectLocator
                print(ProjectLocator.find_root())

            case _:
                raise ValueError(f"Unknown Bootstrap command: {command}")

        return 0


if __name__ == "__main__":
    app = BootstrapApplication()
    print("=" * 40)
    print(" Bootstrap CLI Application")
    print("=" * 40)
    print("Ready to execute commands.")
