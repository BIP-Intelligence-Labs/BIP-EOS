#!/usr/bin/env python3
"""
engineering_evidence_pipeline.py

EAuS-003
Engineering Evidence Pipeline

Constitutional Purpose
----------------------
Transform DiscoveryResult objects into normalized EngineeringEvidence
objects that can be consumed by the Engineering Registry System (ERS).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Iterable
import hashlib

from discovery_result import DiscoveryResult


@dataclass(slots=True)
class EngineeringEvidence:
    """Canonical evidence produced by EAuS."""

    evidence_id: str
    evidence_type: str
    source_collector: str
    artifact_id: str
    artifact_type: str
    observed_utc: datetime
    confidence: float

    attributes: dict[str, Any] = field(default_factory=dict)
    relationships: list[dict[str, Any]] = field(default_factory=list)
    provenance: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "evidence_id": self.evidence_id,
            "evidence_type": self.evidence_type,
            "source_collector": self.source_collector,
            "artifact_id": self.artifact_id,
            "artifact_type": self.artifact_type,
            "observed_utc": self.observed_utc.isoformat(),
            "confidence": self.confidence,
            "attributes": self.attributes,
            "relationships": self.relationships,
            "provenance": self.provenance,
        }


class EngineeringEvidencePipeline:
    """Converts DiscoveryResult objects into EngineeringEvidence."""

    @staticmethod
    def _make_id(result: DiscoveryResult) -> str:
        key = f"{result.collector}|{result.artifact_type}|{result.artifact_id}"
        return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]

    def transform(
        self,
        results: Iterable[DiscoveryResult],
    ) -> list[EngineeringEvidence]:

        evidence_items: list[EngineeringEvidence] = []

        for result in results:
            evidence = EngineeringEvidence(
                evidence_id=self._make_id(result),
                evidence_type="engineering_observation",
                source_collector=result.collector,
                artifact_id=result.artifact_id,
                artifact_type=result.artifact_type,
                observed_utc=result.observed_utc,
                confidence=result.confidence,
                attributes=dict(result.attributes),
                relationships=list(result.relationships),
                provenance=list(result.evidence),
            )
            evidence_items.append(evidence)

        return evidence_items


if __name__ == "__main__":
    sample = DiscoveryResult(
        collector="filesystem",
        artifact_type="file",
        artifact_id="README.md",
        artifact_name="README.md",
    )

    sample.add_attribute("extension", ".md")
    sample.add_evidence(
        source="filesystem",
        description="Observed during filesystem traversal.",
    )

    pipeline = EngineeringEvidencePipeline()
    evidence = pipeline.transform([sample])

    print("Engineering Evidence Pipeline")
    print("-----------------------------")
    print(evidence[0].to_dict())
