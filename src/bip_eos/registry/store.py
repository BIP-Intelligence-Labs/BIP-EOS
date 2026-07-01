"""
========================================================================
ERS-001

Engineering Registry System

Registry Store
========================================================================
"""

from __future__ import annotations

import json
from pathlib import Path

from .models import RegistryEntry


DEFAULT_REGISTRY = Path("engineering/registry/registry.json")


class RegistryStore:
    """
    Persistent Engineering Registry.

    Stores constitutional RegistryEntry objects.
    """

    def __init__(self, registry_file: Path | str = DEFAULT_REGISTRY):

        self.registry_file = Path(registry_file)

        self.registry_file.parent.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------

    def exists(self) -> bool:

        return self.registry_file.exists()

    # ------------------------------------------------------------------

    def load(self) -> list[RegistryEntry]:

        if not self.exists():
            return []

        data = json.loads(self.registry_file.read_text(encoding="utf-8"))

        entries = []

        for item in data.get("entries", []):

            entries.append(

                RegistryEntry(

                    id=item["id"],

                    artifact_type=item["artifact_type"],

                    name=item["name"],

                    path=Path(item["path"]),

                    checksum=item["checksum"],

                    version=item.get("version", "1.0"),

                    metadata=item.get("metadata", {}),

                )

            )

        return entries

    # ------------------------------------------------------------------

    def save(self, entries: list[RegistryEntry]) -> None:

        document = {

            "version": "1.0",

            "entries": [

                entry.to_dict()

                for entry in entries

            ]

        }

        self.registry_file.write_text(

            json.dumps(

                document,

                indent=4,

                sort_keys=False,

            ),

            encoding="utf-8",

        )

    # ------------------------------------------------------------------

    def append(self, entry: RegistryEntry) -> None:

        entries = self.load()

        entries.append(entry)

        self.save(entries)

    # ------------------------------------------------------------------

    def count(self) -> int:

        return len(self.load())
