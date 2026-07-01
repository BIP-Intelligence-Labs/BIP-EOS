#!/usr/bin/env python3
"""
discovery_engine.py

EAuS-003
Discovery Engine

Constitutional Purpose:
Coordinate discovery collectors and aggregate DiscoveryResult objects.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import List

from collector import Collector
from discovery_context import DiscoveryContext
from discovery_result import DiscoveryResult


class DiscoveryEngine:
    """Coordinates execution of discovery collectors."""

    def __init__(self) -> None:
        self._collectors: List[Collector] = []

    def register(self, collector: Collector) -> None:
        """Register a discovery collector."""
        self._collectors.append(collector)

    @property
    def collectors(self) -> tuple[Collector, ...]:
        return tuple(self._collectors)

    def execute(
        self,
        context: DiscoveryContext,
    ) -> list[DiscoveryResult]:
        """
        Execute all registered collectors and return aggregated
        DiscoveryResult objects.
        """
        results: list[DiscoveryResult] = []

        for collector in self._collectors:
            if not collector.validate(context):
                continue

            for result in collector.discover(context):
                results.append(result)

        context.add_metadata("collector_count", len(self._collectors))
        context.add_metadata("result_count", len(results))

        return results

    def execute_iter(
        self,
        context: DiscoveryContext,
    ) -> Iterable[DiscoveryResult]:
        """Yield results as they are discovered."""
        for collector in self._collectors:
            if not collector.validate(context):
                continue

            yield from collector.discover(context)


if __name__ == "__main__":
    from pathlib import Path

    from filesystem_collector import FilesystemCollector
    from repository_collector import RepositoryCollector

    ctx = DiscoveryContext(repository_root=Path(".").resolve())

    engine = DiscoveryEngine()
    engine.register(RepositoryCollector())
    engine.register(FilesystemCollector())

    results = engine.execute(ctx)

    print("EAuS Discovery Engine")
    print("---------------------")
    print(f"Collectors : {len(engine.collectors)}")
    print(f"Results    : {len(results)}")
    print(f"Execution  : {ctx.execution_id}")

    for item in results[:10]:
        print(f"- [{item.collector}] {item.artifact_type}: {item.artifact_name}")
