"""
========================================================================
EAuS-001
Engineering Audit System

Filesystem Collector
========================================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterator


DEFAULT_IGNORE = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "node_modules",
    ".idea",
    ".vscode",
    "dist",
    "build",
}


class FilesystemCollector:
    """
    Collects files from a repository while honoring ignore rules.
    """

    def __init__(self, root: str | Path, ignore: set[str] | None = None):
        self.root = Path(root).resolve()
        self.ignore = ignore or DEFAULT_IGNORE

    def collect(self) -> list[Path]:
        """
        Return all collected files.
        """
        return list(self.iter_files())

    def iter_files(self) -> Iterator[Path]:
        """
        Lazily iterate over repository files.
        """
        for path in self.root.rglob("*"):
            if not path.is_file():
                continue

            if any(part in self.ignore for part in path.parts):
                continue

            yield path

    def summary(self) -> dict[str, int]:
        """
        Return a simple filesystem summary.
        """
        files = self.collect()

        return {
            "directories": sum(
                1
                for p in self.root.rglob("*")
                if p.is_dir()
                and not any(part in self.ignore for part in p.parts)
            ),
            "files": len(files),
        }
