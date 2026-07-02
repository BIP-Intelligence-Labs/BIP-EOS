"""
========================================================================
EAuS-001
Engineering Audit System

Engineering Evidence
========================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any
import hashlib


@dataclass(slots=True, frozen=True)
class EngineeringEvidence:
    """
    Canonical engineering evidence produced by EAuS-001.
    """

    id: str
    kind: str
    path: Path
    extension: str
    language: str
    size: int
    checksum: str
    metadata: dict[str, Any] = field(default_factory=dict)
    discovered_at: datetime = field(default_factory=datetime.utcnow)

    @classmethod
    def from_file(
        cls,
        evidence_id: str,
        file_path: str | Path,
        kind: str,
        language: str,
    ) -> "EngineeringEvidence":

        path = Path(file_path)

        digest = hashlib.sha256(path.read_bytes()).hexdigest()

        return cls(
            id=evidence_id,
            kind=kind,
            path=path,
            extension=path.suffix.lower(),
            language=language,
            size=path.stat().st_size,
            checksum=digest,
        )

    @property
    def filename(self) -> str:
        return self.path.name

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "kind": self.kind,
            "path": str(self.path),
            "extension": self.extension,
            "language": self.language,
            "size": self.size,
            "checksum": self.checksum,
            "metadata": self.metadata,
            "discovered_at": self.discovered_at.isoformat(),
        }

    def __str__(self) -> str:
        return (
            f"{self.id} | {self.kind} | "
            f"{self.path} | {self.size} bytes"
        )
