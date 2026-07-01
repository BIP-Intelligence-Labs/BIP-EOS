"""
========================================================================
ERS-001

Engineering Registry System

Registry Serializer
========================================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Any
import json

from .models import RegistryEntry


class RegistrySerializer:
    """
    Constitutional serialization service.

    Responsible ONLY for converting RegistryEntry objects
    to and from portable representations.

    No filesystem operations belong here.
    """

    # ==================================================================
    # Serialize
    # ==================================================================

    def serialize(
        self,
        entries: list[RegistryEntry],
    ) -> dict[str, Any]:
        """
        Convert RegistryEntry objects into a portable document.
        """

        return {

            "version": "1.0",

            "entries": [

                entry.to_dict()

                for entry in entries

            ]

        }

    # ==================================================================
    # Deserialize
    # ==================================================================

    def deserialize(
        self,
        document: dict[str, Any],
    ) -> list[RegistryEntry]:
        """
        Convert a document into RegistryEntry objects.
        """

        registry: list[RegistryEntry] = []

        for item in document.get("entries", []):

            registry.append(

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

        return registry

    # ==================================================================
    # JSON
    # ==================================================================

    def to_json(
        self,
        entries: list[RegistryEntry],
        *,
        indent: int = 4,
    ) -> str:

        return json.dumps(

            self.serialize(entries),

            indent=indent,

            sort_keys=False,

        )

    # ==================================================================

    def from_json(
        self,
        text: str,
    ) -> list[RegistryEntry]:

        document = json.loads(text)

        return self.deserialize(document)
