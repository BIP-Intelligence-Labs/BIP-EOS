#!/usr/bin/env python3
"""
discovery_result.py

EAuS-003
Discovery Result

Constitutional Object:
Represents the observed engineering reality produced by a collector.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass(slots=True)
class DiscoveryResult:
    """Normalized output produced by a discovery collector."""

    collector: str
    artifact_type: str
    artifact_id: str
    artifact_name: str

    status: str = "discovered"
    confidence: float = 1.0

    observed_utc: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    location: str | None = None
    checksum: str | None = None

    attributes: dict[str, Any] = field(default_factory=dict)
    relationships: list[dict[str, Any]] = field(default_factory=list)
    evidence: list[dict[str, Any]] = field(default_factory=list)

    def add_attribute(self, name: str, value: Any) -> None:
        self.attributes[name] = value

    def add_relationship(
        self,
        relationship_type: str,
        target_id: str,
    ) -> None:
        self.relationships.append(
            {
                "type": relationship_type,
                "target": target_id,
            }
        )

    def add_evidence(
        self,
        source: str,
        description: str,
    ) -> None:
        self.evidence.append(
            {
                "source": source,
                "description": description,
            }
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "collector": self.collector,
            "artifact_type": self.artifact_type,
            "artifact_id": self.artifact_id,
            "artifact_name": self.artifact_name,
            "status": self.status,
            "confidence": self.confidence,
            "observed_utc": self.observed_utc.isoformat(),
            "location": self.location,
            "checksum": self.checksum,
            "attributes": self.attributes,
            "relationships": self.relationships,
            "evidence": self.evidence,
        }


if __name__ == "__main__":
    result = DiscoveryResult(
        collector="filesystem",
        artifact_type="directory",
        artifact_id="src",
        artifact_name="src",
        location="src",
    )

    result.add_attribute("exists", True)
    result.add_attribute("language", "python")
    result.add_evidence(
        source="filesystem",
        description="Directory discovered during repository scan.",
    )

    from pprint import pprint
    pprint(result.to_dict())
