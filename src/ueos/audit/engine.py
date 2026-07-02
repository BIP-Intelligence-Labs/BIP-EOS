"""
========================================================================
EAuS-001
Engineering Audit System

Audit Engine
========================================================================
"""

from __future__ import annotations

from pathlib import Path
from collections import Counter

from .repository import RepositoryDiscovery


class AuditEngine:
    """
    Coordinates repository discovery and produces an audit summary.
    """

    def __init__(self, root: str | Path = "."):
        self.root = Path(root).resolve()

    def discover(self):
        print("=" * 72)
        print("UEOS Engineering Audit System")
        print("EAuS-001")
        print("=" * 72)
        print(f"Repository : {self.root}")
        print()

        discovery = RepositoryDiscovery(self.root)
        evidence = discovery.discover()

        counts = Counter(item.language for item in evidence)

        print("Engineering Evidence Generated")
        print()

        print("=" * 72)
        print("Repository Summary")
        print("=" * 72)
        print(f"Artifacts : {len(evidence)}")

        for language, total in sorted(counts.items()):
            print(f"{language:<12}: {total}")

        print("=" * 72)
        print("Discovery Complete")
        print("=" * 72)

        return evidence
