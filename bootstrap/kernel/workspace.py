"""
bootstrap/kernel/workspace.py

Production Workspace Manager.
"""

from __future__ import annotations

from pathlib import Path


class Workspace:
    """Manages the Bootstrap workspace."""

    def __init__(self, path: str = "./workspace") -> None:
        self.path = Path(path)
        self.path.mkdir(parents=True, exist_ok=True)

    def resolve(self, *parts: str) -> Path:
        return self.path.joinpath(*parts)

    def ensure(self, *folders: str) -> None:
        for folder in folders:
            self.resolve(folder).mkdir(parents=True, exist_ok=True)

    def exists(self, *parts: str) -> bool:
        return self.resolve(*parts).exists()

    def create_file(self, name: str, content: str = "") -> Path:
        file = self.resolve(name)
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content, encoding="utf-8")
        return file

    def __str__(self) -> str:
        return str(self.path)
