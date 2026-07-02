"""
command_loader.py

UEOS M-006.2
Automatic command discovery and registration.

Place in:
    src/bip_eos/cli/command_loader.py
"""

from __future__ import annotations

import importlib
import inspect
import pkgutil
from pathlib import Path
from types import ModuleType

from ueos.cli.command import Command
from ueos.cli.dispatcher import CommandDispatcher


class CommandLoader:
    """Discovers and registers CLI commands."""

    def __init__(
        self,
        dispatcher: CommandDispatcher,
        package: str = "ueos.cli.commands",
    ) -> None:
        self.dispatcher = dispatcher
        self.package = package

    def load(self) -> int:
        """Load every Command subclass from the commands package."""
        package = importlib.import_module(self.package)
        count = 0

        for _, module_name, is_pkg in pkgutil.iter_modules(package.__path__):
            if is_pkg:
                continue

            module = importlib.import_module(f"{self.package}.{module_name}")
            count += self._register_from_module(module)

        return count

    def _register_from_module(self, module: ModuleType) -> int:
        loaded = 0

        for _, obj in inspect.getmembers(module, inspect.isclass):
            if obj is Command:
                continue

            if not issubclass(obj, Command):
                continue

            try:
                # Commands that need the dispatcher can declare:
                # __init__(self, dispatcher)
                sig = inspect.signature(obj)
                if len(sig.parameters) == 1:
                    instance = obj(self.dispatcher)
                else:
                    instance = obj()

                self.dispatcher.register(instance)
                loaded += 1

            except Exception as exc:
                print(f"[WARN] Failed to load {obj.__name__}: {exc}")

        return loaded


if __name__ == "__main__":
    from ueos.cli.dispatcher import CommandDispatcher

    dispatcher = CommandDispatcher()
    loader = CommandLoader(dispatcher)

    total = loader.load()

    print(f"Loaded {total} commands")

    for command in dispatcher.commands():
        print(f" - {command.name}")
