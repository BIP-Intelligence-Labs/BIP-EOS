"""
bootstrap/kernel/configuration.py

Production Configuration Manager.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class Configuration:
    """Simple configuration manager."""

    def __init__(self, config_file: str | None = None) -> None:
        self._settings: dict[str, Any] = {
            "environment": "development",
            "workspace": "./workspace",
            "log_level": "INFO",
        }

        if config_file:
            self.load(config_file)

    def load(self, filename: str) -> None:
        path = Path(filename)
        if path.exists():
            self._settings.update(json.loads(path.read_text(encoding="utf-8")))

    def save(self, filename: str) -> None:
        Path(filename).write_text(
            json.dumps(self._settings, indent=4),
            encoding="utf-8",
        )

    def get(self, key: str, default: Any = None) -> Any:
        return self._settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._settings[key] = value

    def all(self) -> dict[str, Any]:
        return dict(self._settings)
