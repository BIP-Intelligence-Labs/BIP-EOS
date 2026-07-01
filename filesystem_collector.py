#!/usr/bin/env python3
"""
filesystem_collector.py

EAuS-003
Filesystem Collector

Constitutional Purpose:
Observe the repository filesystem and emit DiscoveryResult objects.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from collector import Collector
from discovery_context import DiscoveryContext
from discovery_result import DiscoveryResult


class FilesystemCollector(Collector):
    """Discovers files and directories within the repository."""

    EXCLUDED = {
        ".git",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
    }

    @property
    def name(self) -> str:
        return "filesystem"

    @property
    def version(self) -> str:
        return "0.1.0"

    def discover(
        self,
        context: DiscoveryContext,
    ) -> Iterable[DiscoveryResult]:

        root = context.repository_root

        for path in root.rglob("*"):
            if any(part in self.EXCLUDED for part in path.parts):
                continue

            relative = path.relative_to(root)

            artifact_type = "directory" if path.is_dir() else "file"

            result = DiscoveryResult(
                collector=self.name,
                artifact_type=artifact_type,
                artifact_id=str(relative),
                artifact_name=path.name,
                location=str(relative),
            )

            result.add_attribute("exists", True)
            result.add_attribute("size_bytes", path.stat().st_size if path.is_file() else 0)
            result.add_attribute("suffix", path.suffix)
            result.add_attribute("depth", len(relative.parts))

            if relative.parent != Path("."):
                result.add_relationship(
                    "contained_in",
                    str(relative.parent),
                )

            result.add_evidence(
                source="filesystem",
                description="Observed during filesystem traversal.",
            )

            yield result


if __name__ == "__main__":
    ctx = DiscoveryContext(repository_root=Path(".").resolve())
    collector = FilesystemCollector()

    count = 0

    for item in collector.discover(ctx):
        print(item.to_dict())
        count += 1
        if count >= 10:
            break

    print(f"\nDisplayed first {count} discovery results.")
