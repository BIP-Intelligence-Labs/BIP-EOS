"""
M-006.7.3 - Memory Manager (Starter)

Persistent engineering memory abstraction.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class MemoryRecord:
    key: str
    value: Any
    tags: list[str] = field(default_factory=list)


class MemoryManager:
    """In-memory starter implementation."""

    def __init__(self) -> None:
        self._memory: dict[str, MemoryRecord] = {}

    def put(self, key: str, value: Any, tags: list[str] | None = None) -> None:
        self._memory[key] = MemoryRecord(key, value, tags or [])

    def get(self, key: str) -> Any | None:
        record = self._memory.get(key)
        return None if record is None else record.value

    def exists(self, key: str) -> bool:
        return key in self._memory

    def clear(self) -> None:
        self._memory.clear()


if __name__ == "__main__":
    mm = MemoryManager()
    mm.put("project", "Genesis", ["demo"])
    print(mm.get("project"))
