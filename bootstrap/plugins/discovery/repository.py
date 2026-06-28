"""
bootstrap/plugins/discovery/repository.py

Universal Discovery Engine Repository
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from .extractor import ExtractedDocument


@dataclass
class RepositoryRecord:
    url: str
    document: ExtractedDocument
    discovered_at: datetime = field(default_factory=datetime.utcnow)


class DiscoveryRepository:
    """In-memory repository for discovered documents.

    This is the initial implementation. Later versions can persist
    records to Supabase, PostgreSQL, or other storage backends.
    """

    def __init__(self) -> None:
        self._records: list[RepositoryRecord] = []

    def save(self, url: str, document: ExtractedDocument) -> RepositoryRecord:
        record = RepositoryRecord(
            url=url,
            document=document,
        )
        self._records.append(record)
        return record

    def all(self) -> list[RepositoryRecord]:
        return list(self._records)

    def count(self) -> int:
        return len(self._records)

    def clear(self) -> None:
        self._records.clear()


if __name__ == "__main__":
    repo = DiscoveryRepository()
    print("=" * 40)
    print(" Bootstrap Discovery Repository")
    print("=" * 40)
    print(f"Records: {repo.count()}")
