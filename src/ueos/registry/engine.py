"""
========================================================================
ERS-001

Engineering Registry System

Registry Engine

Constitutional Orchestrator
========================================================================
"""

from __future__ import annotations

from pathlib import Path

from ueos.audit.engine import AuditEngine

from .ids import EngineeringIDGenerator
from .index import RegistryIndex
from .models import RegistryEntry
from .resolver import IdentityResolver
from .serializer import RegistrySerializer
from .store import RegistryStore
from .validator import RegistryValidator


class RegistryEngine:
    """
    Constitutional Engineering Registry.

    Coordinates all Registry services.

    RegistryEngine intentionally contains almost no business logic.
    """

    def __init__(
        self,
        root: str | Path = ".",
    ) -> None:

        self.root = Path(root).resolve()

        #
        # Constitutional Services
        #

        self.store = RegistryStore()

        self.serializer = RegistrySerializer()

        self.validator = RegistryValidator()

        self.index = RegistryIndex()

        self.ids = EngineeringIDGenerator()

        self.resolver = IdentityResolver(
            self.ids,
        )

    # ==================================================================

    def build(
        self,
    ) -> list[RegistryEntry]:

        print("=" * 72)
        print("ERS-001")
        print("Engineering Registry System")
        print("=" * 72)
        print()

        #
        # Load Existing Registry
        #

        existing = self.store.load()

        #
        # Repository Discovery
        #

        evidence = AuditEngine(self.root).discover()

        #
        # Identity Resolution
        #

        registry = self.resolver.resolve(

            evidence,

            existing,

        )

        #
        # Registry Validation
        #

        self.validator.validate(registry)

        #
        # Persist Registry
        #

        self.store.save(registry)

        #
        # Build Runtime Index
        #

        self.index.build(registry)

        #
        # Summary
        #

        self.summary()

        return registry

    # ==================================================================

    def load(
        self,
    ) -> list[RegistryEntry]:

        registry = self.store.load()

        self.index.build(registry)

        return registry

    # ==================================================================

    def summary(
        self,
    ) -> None:

        stats = self.index.statistics()

        print("=" * 72)
        print("Engineering Registry")
        print("=" * 72)

        print(f"Entries        : {stats['entries']}")
        print(f"Artifact Types : {stats['artifact_types']}")
        print(f"Checksums      : {stats['checksums']}")
        print(f"Names          : {stats['names']}")

        print("=" * 72)

    # ==================================================================

    def by_id(
        self,
        engineering_id: str,
    ):

        return self.index.by_id(engineering_id)

    # ==================================================================

    def by_path(
        self,
        path,
    ):

        return self.index.by_path(path)

    # ==================================================================

    def by_type(
        self,
        artifact_type: str,
    ):

        return self.index.by_type(artifact_type)

    # ==================================================================

    def by_name(
        self,
        name: str,
    ):

        return self.index.by_name(name)
