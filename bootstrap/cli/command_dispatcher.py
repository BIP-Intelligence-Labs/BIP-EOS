"""
bootstrap/cli/command_dispatcher.py

Dispatches Bootstrap CLI commands.
"""

from __future__ import annotations

from typing import Callable


class CommandDispatcher:
    """Simple command dispatcher."""

    def __init__(self) -> None:
        self._commands: dict[str, Callable[[], None]] = {}

    def register(self, name: str, handler: Callable[[], None]) -> None:
        self._commands[name] = handler

    def dispatch(self, name: str) -> None:
        if name not in self._commands:
            available = ", ".join(sorted(self._commands)) or "<none>"
            raise ValueError(
                f"Unknown command '{name}'. Available: {available}"
            )
        self._commands[name]()

    def list_commands(self) -> list[str]:
        return sorted(self._commands.keys())


if __name__ == "__main__":
    dispatcher = CommandDispatcher()
    print("Bootstrap Command Dispatcher")
    print("============================")
    print("Registered commands:", dispatcher.list_commands())
