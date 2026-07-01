#!/usr/bin/env python3
"""
collector.py

EAuS-003
Collector Interface

Constitutional Object:
Defines the contract implemented by every Discovery Collector.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable

from discovery_context import DiscoveryContext
from discovery_result import DiscoveryResult


class Collector(ABC):
    """Abstract base class for all UEOS discovery collectors."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique collector name."""
        raise NotImplementedError

    @property
    @abstractmethod
    def version(self) -> str:
        """Collector version."""
        raise NotImplementedError

    @abstractmethod
    def discover(
        self,
        context: DiscoveryContext,
    ) -> Iterable[DiscoveryResult]:
        """
        Observe engineering reality and return DiscoveryResult objects.
        """
        raise NotImplementedError

    def validate(
        self,
        context: DiscoveryContext,
    ) -> bool:
        """
        Verify prerequisites before discovery begins.
        Override as needed.
        """
        return context.repository_root.exists()


class ExampleCollector(Collector):
    """Minimal reference implementation."""

    @property
    def name(self) -> str:
        return "example"

    @property
    def version(self) -> str:
        return "0.1.0"

    def discover(
        self,
        context: DiscoveryContext,
    ) -> Iterable[DiscoveryResult]:
        result = DiscoveryResult(
            collector=self.name,
            artifact_type="repository",
            artifact_id=context.execution_id,
            artifact_name=context.repository_root.name,
            location=str(context.repository_root),
        )
        result.add_evidence(
            source=self.name,
            description="Repository root observed.",
        )
        yield result


if __name__ == "__main__":
    from pathlib import Path

    ctx = DiscoveryContext(repository_root=Path(".").resolve())
    collector = ExampleCollector()

    if collector.validate(ctx):
        for item in collector.discover(ctx):
            print(item.to_dict())
