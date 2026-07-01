#!/usr/bin/env python3
"""
repository_collector.py

EAuS-003
Repository Collector

Constitutional Purpose:
Observe repository-level engineering artifacts and emit DiscoveryResult
objects describing the engineering structure rather than individual files.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from collector import Collector
from discovery_context import DiscoveryContext
from discovery_result import DiscoveryResult


class RepositoryCollector(Collector):
    """Discovers repository-level engineering artifacts."""

    MARKERS = (
        ".git",
        "pyproject.toml",
        "requirements.txt",
        "README.md",
        "engineering",
        "bootstrap",
        "src",
        "tests",
        "docs",
    )

    @property
    def name(self) -> str:
        return "repository"

    @property
    def version(self) -> str:
        return "0.1.0"

    def discover(
        self,
        context: DiscoveryContext,
    ) -> Iterable[DiscoveryResult]:

        root = context.repository_root

        repo = DiscoveryResult(
            collector=self.name,
            artifact_type="repository",
            artifact_id=root.name,
            artifact_name=root.name,
            location=str(root),
        )

        repo.add_attribute("repository_name", root.name)
        repo.add_attribute("repository_root", str(root))
        repo.add_attribute("marker_count", len(self.MARKERS))

        yield repo

        for marker in self.MARKERS:
            target = root / marker
            if not target.exists():
                continue

            artifact_type = "directory" if target.is_dir() else "file"

            result = DiscoveryResult(
                collector=self.name,
                artifact_type=artifact_type,
                artifact_id=marker,
                artifact_name=marker,
                location=str(target.relative_to(root)),
            )

            result.add_attribute("engineering_marker", True)
            result.add_attribute("exists", True)

            result.add_relationship(
                relationship_type="belongs_to_repository",
                target_id=root.name,
            )

            result.add_evidence(
                source="repository",
                description=f"Repository marker '{marker}' observed.",
            )

            yield result


if __name__ == "__main__":
    ctx = DiscoveryContext(repository_root=Path(".").resolve())
    collector = RepositoryCollector()

    for item in collector.discover(ctx):
        print(item.to_dict())
