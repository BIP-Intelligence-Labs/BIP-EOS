"""
========================================================================
INS-001
UEOS Installation Framework

Installer Registry
========================================================================
"""

from __future__ import annotations

from typing import Dict, Type

from .installer import Installer


class InstallerRegistry:
    """
    Registry of all UEOS constitutional installers.
    """

    def __init__(self) -> None:
        self._installers: Dict[str, Type[Installer]] = {}

    def register(self, name: str, installer: Type[Installer], *aliases: str) -> None:
        """
        Register an installer class with optional aliases.
        """
        names = (name, *aliases)
        for item in names:
            self._installers[item.lower()] = installer

    def unregister(self, name: str) -> None:
        """
        Remove an installer.
        """
        self._installers.pop(name.lower(), None)

    def exists(self, name: str) -> bool:
        """
        Determine whether an installer exists.
        """
        return name.lower() in self._installers

    def get(self, name: str) -> Type[Installer]:
        """
        Return the installer class.

        Raises:
            KeyError if not registered.
        """
        key = name.lower()

        if key not in self._installers:
            raise KeyError(f"No installer registered for '{name}'.")

        return self._installers[key]

    def names(self) -> list[str]:
        """
        Return all registered names and aliases.
        """
        return sorted(self._installers.keys())

    def count(self) -> int:
        """
        Return number of registered names.
        """
        return len(self._installers)
