"""
========================================================================
EAuS-001
Engineering Audit System

Repository Discovery
========================================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from .evidence import EngineeringEvidence


IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "node_modules",
    ".idea",
    ".vscode",
}


LANGUAGE_MAP = {
    ".py": ("python", "Python"),
    ".md": ("markdown", "Markdown"),
    ".json": ("json", "JSON"),
    ".yaml": ("yaml", "YAML"),
    ".yml": ("yaml", "YAML"),
    ".toml": ("toml", "TOML"),
    ".xml": ("xml", "XML"),
    ".html": ("html", "HTML"),
    ".css": ("css", "CSS"),
    ".js": ("javascript", "JavaScript"),
}


class RepositoryDiscovery:
    """
    Walks a repository and produces EngineeringEvidence objects.
    """

    def __init__(self, root: str | Path):
        self.root = Path(root).resolve()

    def discover(self) -> list[EngineeringEvidence]:
        evidence: list[EngineeringEvidence] = []
        counter = 1

        for path in self._files():
            kind, language = self._classify(path)
            evidence.append(
                EngineeringEvidence.from_file(
                    evidence_id=f"EV-{counter:06d}",
                    file_path=path,
                    kind=kind,
                    language=language,
                )
            )
            counter += 1

        return evidence

    def _files(self) -> Iterable[Path]:
        for path in self.root.rglob("*"):
            if not path.is_file():
                continue

            if any(part in IGNORE_DIRS for part in path.parts):
                continue

            yield path

    @staticmethod
    def _classify(path: Path) -> tuple[str, str]:
        return LANGUAGE_MAP.get(
            path.suffix.lower(),
            ("file", "Unknown"),
        )
