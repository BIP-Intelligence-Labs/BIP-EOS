#!/usr/bin/env python3
"""
EAuS-001 — Engineering Audit Kernel
BIP Universal Engineering Operating System (UEOS)

Purpose
-------
The Engineering Audit Kernel is the runtime foundation of the
Engineering Audit System (EAuS).

Mission
-------
Observe reality.
Collect evidence.
Never make engineering decisions.

This implementation is intentionally minimal and establishes the
constitutional interfaces for Sprint 2.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Dict, List
import uuid


class AuditEvent(Enum):
    AUDIT_STARTED = "audit.started"
    DISCOVERY_STARTED = "discovery.started"
    DISCOVERY_COMPLETED = "discovery.completed"
    EVIDENCE_COLLECTED = "evidence.collected"
    AUDIT_COMPLETED = "audit.completed"


@dataclass(frozen=True)
class Evidence:
    evidence_id: str
    collector: str
    category: str
    source: str
    finding: str
    severity: str = "INFO"
    confidence: float = 1.0
    timestamp: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


@dataclass
class AuditSession:
    session_id: str
    repository: Path
    started: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    evidence: List[Evidence] = field(default_factory=list)
    events: List[AuditEvent] = field(default_factory=list)


class EventBus:
    def publish(self, session: AuditSession, event: AuditEvent):
        session.events.append(event)
        print(f"[EVENT] {event.value}")


class RepositoryDiscovery:

    def discover(self, repository: Path) -> Dict[str, int]:
        directories = 0
        files = 0

        for item in repository.rglob("*"):
            if item.is_dir():
                directories += 1
            elif item.is_file():
                files += 1

        return {
            "directories": directories,
            "files": files,
        }


class RepositoryCollector:

    def collect(self, repository: Path) -> List[Evidence]:
        discovery = RepositoryDiscovery().discover(repository)

        return [
            Evidence(
                evidence_id=str(uuid.uuid4()),
                collector="RepositoryCollector",
                category="Repository",
                source=str(repository),
                finding=(
                    f"Repository contains "
                    f"{discovery['directories']} directories and "
                    f"{discovery['files']} files."
                ),
            )
        ]


class EngineeringAuditKernel:

    def __init__(self):
        self.bus = EventBus()
        self.collectors = [
            RepositoryCollector(),
        ]

    def run(self, repository: Path) -> AuditSession:

        session = AuditSession(
            session_id=f"AUD-{uuid.uuid4()}",
            repository=repository,
        )

        self.bus.publish(session, AuditEvent.AUDIT_STARTED)
        self.bus.publish(session, AuditEvent.DISCOVERY_STARTED)

        for collector in self.collectors:
            evidence = collector.collect(repository)
            session.evidence.extend(evidence)

            for _ in evidence:
                self.bus.publish(session, AuditEvent.EVIDENCE_COLLECTED)

        self.bus.publish(session, AuditEvent.DISCOVERY_COMPLETED)
        self.bus.publish(session, AuditEvent.AUDIT_COMPLETED)

        return session


def find_repo_root(start: Path) -> Path:
    current = start.resolve()

    while current != current.parent:
        if (
            (current / "bootstrap").exists()
            and (current / "engineering").exists()
            and (current / "src").exists()
        ):
            return current
        current = current.parent

    raise RuntimeError("Unable to locate UEOS repository root.")


def main():

    repository = find_repo_root(Path(__file__).parent)

    kernel = EngineeringAuditKernel()

    session = kernel.run(repository)

    print("\n" + "=" * 72)
    print("EAuS-001 Engineering Audit Kernel")
    print("=" * 72)
    print("Repository :", session.repository)
    print("Session    :", session.session_id)
    print("Evidence   :", len(session.evidence))
    print("Events     :", len(session.events))
    print("=" * 72)

    for evidence in session.evidence:
        print(f"[{evidence.category}] {evidence.finding}")


if __name__ == "__main__":
    main()
