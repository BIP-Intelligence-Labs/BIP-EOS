"""
bootstrap/kernel/plugin_loader.py

Production Plugin Loader.
"""

from __future__ import annotations

import importlib
from typing import Iterable


class PluginLoader:
    """Loads Bootstrap plugins dynamically."""

    def __init__(self) -> None:
        self._loaded: dict[str, object] = {}

    def load(self, module_name: str):
        """Import a plugin module."""
        if module_name in self._loaded:
            return self._loaded[module_name]

        module = importlib.import_module(module_name)
        self._loaded[module_name] = module
        return module

    def discover(self) -> list[str]:
        """Placeholder for future plugin discovery."""
        return list(self._loaded.keys())

    def loaded_plugins(self) -> Iterable[str]:
        return tuple(self._loaded.keys())

    def unload(self, module_name: str) -> None:
        self._loaded.pop(module_name, None)

    def clear(self) -> None:
        self._loaded.clear()
