"""
UEOS Enterprise Command Dispatcher

M-006.2

Responsible for:

- Registering commands
- Alias resolution
- Dispatching commands
- Listing commands
"""

from __future__ import annotations

from typing import Dict, Iterable, List, Optional, Protocol


class Command(Protocol):
    """Interface implemented by every UEOS command."""

    name: str
    description: str
    aliases: List[str]

    def execute(self, args: List[str]) -> int:
        ...


class CommandDispatcher:
    """
    Enterprise command dispatcher.

    All UEOS commands are registered here.
    Runtime never contains command-specific logic.
    """

    def __init__(self) -> None:
        self._commands: Dict[str, Command] = {}

    # ---------------------------------------------------------
    # Registration
    # ---------------------------------------------------------

    def register(self, command: Command) -> None:
        """
        Register a command and all of its aliases.
        """

        self._commands[command.name.lower()] = command

        for alias in getattr(command, "aliases", []):
            self._commands[alias.lower()] = command

    # ---------------------------------------------------------
    # Lookup
    # ---------------------------------------------------------

    def find(self, name: str) -> Optional[Command]:
        return self._commands.get(name.lower())

    # ---------------------------------------------------------
    # Dispatch
    # ---------------------------------------------------------

    def dispatch(self, line: str) -> int:

        line = line.strip()

        if not line:
            return 0

        parts = line.split()

        command_name = parts[0]

        args = parts[1:]

        command = self.find(command_name)

        if command is None:

            print(f'Unknown command "{command_name}"')

            print('Type "help" for available commands.')

            return 1

        return command.execute(args)

    # ---------------------------------------------------------
    # Metadata
    # ---------------------------------------------------------

    def commands(self) -> Iterable[Command]:
        """
        Returns unique commands.
        """

        unique = {}

        for command in self._commands.values():
            unique[command.name] = command

        return sorted(unique.values(), key=lambda c: c.name)

    def command_names(self) -> List[str]:
        return [command.name for command in self.commands()]
