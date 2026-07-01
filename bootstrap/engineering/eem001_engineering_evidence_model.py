#!/usr/bin/env python3
"""
EEM-001 — Engineering Evidence Model
BIP Universal Engineering Operating System (UEOS)

Constitutional Purpose
----------------------
The Engineering Evidence Model (EEM) is the canonical representation
of engineering evidence throughout UEOS.

Engineering Flow

Reality
    ↓
EAuS
    ↓
Engineering Evidence Model (EEM)
    ↓
ERS
    ↓
Engineering Truth
    ↓
ECS
    ↓
Unified Engineering Graph
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Dict, List, Optional
import hashlib
import json
import uuid


class EvidenceSeverity(str, Enum):
    INFO = "INFO"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class EvidenceConfidence(str, Enum):
    OBSERVED = "OBSERVED"
    VERIFIED = "VERIFIED"
    CORRELATED = "CORRELATED"
    INFERRED = "INFERRED"


@dataclass(frozen=True)
class EvidenceReference:
    evidence_id: str
    relationship: str


@dataclass
class EngineeringEvidence:
    evidence_id: str = field(default_factory=lambda: f"EVD-{uuid.uuid4()}")

    collector: str = ""
    source: str = ""
    subsystem: str = ""
    category: str = ""
    object_type: str = ""
    object_id: str = ""

    title: str = ""
    finding: str = ""
    recommendation: str = ""

    severity: EvidenceSeverity = EvidenceSeverity.INFO
    confidence: EvidenceConfidence = EvidenceConfidence.OBSERVED

    timestamp: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    metadata: Dict[str, str] = field(default_factory=dict)
    relationships: List[EvidenceReference] = field(default_factory=list)

    checksum: Optional[str] = None

    def calculate_checksum(self) -> str:
        payload = {
            "collector": self.collector,
            "source": self.source,
            "subsystem": self.subsystem,
            "category": self.category,
            "object_type": self.object_type,
            "object_id": self.object_id,
            "title": self.title,
            "finding": self.finding,
            "recommendation": self.recommendation,
            "severity": self.severity.value,
            "confidence": self.confidence.value,
            "metadata": self.metadata,
        }

        digest = hashlib.sha256(
            json.dumps(payload, sort_keys=True).encode("utf-8")
        ).hexdigest()

        self.checksum = digest
        return digest

    def validate(self) -> None:
        required = [
            self.collector,
            self.source,
            self.subsystem,
            self.category,
            self.title,
            self.finding,
        ]
        if any(not x for x in required):
            raise ValueError("Evidence record is missing required fields.")

    def summary(self) -> str:
        return (
            f"[{self.severity.value}] "
            f"{self.title} "
            f"({self.collector})"
        )


@dataclass
class EvidenceCollection:
    collection_id: str = field(default_factory=lambda: f"COL-{uuid.uuid4()}")
    created: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    evidence: List[EngineeringEvidence] = field(default_factory=list)

    def add(self, item: EngineeringEvidence) -> None:
        item.validate()
        item.calculate_checksum()
        self.evidence.append(item)

    def report(self) -> None:
        print("=" * 72)
        print("Engineering Evidence Collection")
        print("=" * 72)
        print("Collection :", self.collection_id)
        print("Evidence   :", len(self.evidence))
        print("=" * 72)
        for item in self.evidence:
            print(item.summary())


def demo():
    collection = EvidenceCollection()

    ev = EngineeringEvidence(
        collector="RepositoryCollector",
        source="Repository",
        subsystem="EAuS",
        category="Repository",
        object_type="Directory",
        object_id="src",
        title="Repository Structure Observed",
        finding="Repository successfully discovered.",
        recommendation="Continue engineering audit.",
    )

    collection.add(ev)
    collection.report()


if __name__ == "__main__":
    demo()
