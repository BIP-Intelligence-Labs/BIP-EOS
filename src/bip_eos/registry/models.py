"""
========================================================================
ERS-001

Engineering Registry System

Registry Models
========================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class RegistryEntry:
    """
    Constitutional engineering registry entry.

    Every engineering artifact known to UEOS SHALL be represented by a
    RegistryEntry.
    """

    #
    # Constitutional Identity
    #

    id: str

    #
    # Classification
    #

    artifact_type: str

    name: str

    #
    # Location
    #

    path: Path

    #
    # Integrity
    #

    checksum: str

    version: str = "1.0"

    #
    # Lifecycle
    #

    created: datetime = field(default_factory=datetime.utcnow)

    modified: datetime = field(default_factory=datetime.utcnow)

    #
    # Extensible Metadata
    #

    metadata: dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------------------

    @property
    def filename(self) -> str:
        return self.path.name

    @property
    def extension(self) -> str:
        return self.path.suffix.lower()

    # ------------------------------------------------------------------

    def to_dict(self) -> dict[str, Any]:

        return {

            "id": self.id,

            "artifact_type": self.artifact_type,

            "name": self.name,

            "path": str(self.path),

            "checksum": self.checksum,

            "version": self.version,

            "created": self.created.isoformat(),

            "modified": self.modified.isoformat(),

            "metadata": self.metadata,

        }

    # ------------------------------------------------------------------

    @classmethod
    def from_evidence(cls, evidence):

        """
        Create a registry entry from EngineeringEvidence.
        """

        return cls(

            id=evidence.id,

            artifact_type=evidence.kind,

            name=evidence.filename,

            path=evidence.path,

            checksum=evidence.checksum,

        )

    # ------------------------------------------------------------------

    def __str__(self) -> str:

        return (

            f"{self.id:<12}"

            f"{self.artifact_type:<15}"

            f"{self.filename}"

        )
