"""
bootstrap/kernel/registry.py

Production Command Registry for Bootstrap Kernel.
"""

from __future__ import annotations

from typing import Any, Callable


class CommandRegistry:
    """Registers and executes Bootstrap commands."""

    def __init__(self) -> None:
        self._commands: dict[str, Callable[..., Any]] = {}

    def register(self, name: str, handler: Callable[..., Any]) -> None:
        if name in self._commands:
            raise ValueError(f"Command already registered: {name}")
        self._commands[name] = handler

    def unregister(self, name: str) -> None:
        self._commands.pop(name, None)

    def execute(self, name: str, *args: Any, **kwargs: Any) -> Any:
        if name not in self._commands:
            raise KeyError(f"Unknown command: {name}")
        return self._commands[name](*args, **kwargs)

    def exists(self, name: str) -> bool:
        return name in self._commands

    def list(self) -> list[str]:
        return sorted(self._commands.keys())

    def clear(self) -> None:
        self._commands.clear()
