"""
bootstrap/plugins/discovery/scheduler.py

Universal Discovery Engine Scheduler
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ScheduledJob:
    url: str
    queued_at: datetime = field(default_factory=datetime.utcnow)


class DiscoveryScheduler:
    """Simple FIFO scheduler for discovery jobs."""

    def __init__(self) -> None:
        self._queue: deque[ScheduledJob] = deque()

    def enqueue(self, url: str) -> None:
        self._queue.append(ScheduledJob(url=url))

    def dequeue(self) -> ScheduledJob | None:
        if not self._queue:
            return None
        return self._queue.popleft()

    def size(self) -> int:
        return len(self._queue)

    def is_empty(self) -> bool:
        return not self._queue

    def clear(self) -> None:
        self._queue.clear()


if __name__ == "__main__":
    scheduler = DiscoveryScheduler()
    print("=" * 40)
    print(" Bootstrap Discovery Scheduler")
    print("=" * 40)
    print(f"Queue Size: {scheduler.size()}")
