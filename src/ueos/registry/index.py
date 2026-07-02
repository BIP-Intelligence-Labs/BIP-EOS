"""
========================================================================
ERS-001

Engineering Registry System

Registry Index
========================================================================
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from .models import RegistryEntry


class RegistryIndex:
    """
    Constitutional Registry Index.

    Provides fast lookups over the Engineering Registry.
    """

    def __init__(self) -> None:

        self.clear()

    # ==================================================================

    def clear(self) -> None:

        self._by_id: dict[str, RegistryEntry] = {}

        self._by_path: dict[str, RegistryEntry] = {}

        self._by_name: dict[str, list[RegistryEntry]] = defaultdict(list)

        self._by_type: dict[str, list[RegistryEntry]] = defaultdict(list)

        self._by_checksum: dict[str, list[RegistryEntry]] = defaultdict(list)

    # ==================================================================

    def build(
        self,
        entries: list[RegistryEntry],
    ) -> None:

        self.clear()

        for entry in entries:

            self._by_id[entry.id] = entry

            self._by_path[str(Path(entry.path).resolve())] = entry

            self._by_name[entry.name].append(entry)

            self._by_type[entry.artifact_type].append(entry)

            self._by_checksum[entry.checksum].append(entry)

    # ==================================================================
    # Lookups
    # ==================================================================

    def by_id(
        self,
        engineering_id: str,
    ) -> RegistryEntry | None:

        return self._by_id.get(engineering_id)

    # ------------------------------------------------------------------

    def by_path(
        self,
        path: str | Path,
    ) -> RegistryEntry | None:

        return self._by_path.get(str(Path(path).resolve()))

    # ------------------------------------------------------------------

    def by_name(
        self,
        name: str,
    ) -> list[RegistryEntry]:

        return list(self._by_name.get(name, []))

    # ------------------------------------------------------------------

    def by_type(
        self,
        artifact_type: str,
    ) -> list[RegistryEntry]:

        return list(

            self._by_type.get(

                artifact_type,

                [],

            )

        )

    # ------------------------------------------------------------------

    def by_checksum(
        self,
        checksum: str,
    ) -> list[RegistryEntry]:

        return list(

            self._by_checksum.get(

                checksum,

                [],

            )

        )

    # ==================================================================

    def contains(
        self,
        engineering_id: str,
    ) -> bool:

        return engineering_id in self._by_id

    # ==================================================================

    def count(self) -> int:

        return len(self._by_id)

    # ==================================================================

    def statistics(self) -> dict[str, int]:

        return {

            "entries": len(self._by_id),

            "artifact_types": len(self._by_type),

            "checksums": len(self._by_checksum),

            "names": len(self._by_name),

        }

    # ==================================================================

    def summary(self) -> None:

        stats = self.statistics()

        print("=" * 72)
        print("ERS-001 Registry Index")
        print("=" * 72)

        print(f"Entries        : {stats['entries']}")
        print(f"Artifact Types : {stats['artifact_types']}")
        print(f"Checksums      : {stats['checksums']}")
        print(f"Names          : {stats['names']}")

        print("=" * 72)
