"""
bootstrap/plugins/discovery/kernel_events.py

Universal Discovery Engine - Kernel Events
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class DiscoveryEvent:
    name: str
    url: str
    timestamp: datetime = datetime.utcnow()


class DiscoveryKernelEvents:
    """Publishes Discovery lifecycle events."""

    STARTED = "discovery.started"
    PAGE_FETCHED = "discovery.page_fetched"
    EXTRACTED = "discovery.extracted"
    VALIDATED = "discovery.validated"
    STORED = "discovery.stored"
    COMPLETED = "discovery.completed"

    @staticmethod
    def emit(event_name: str, url: str) -> DiscoveryEvent:
        event = DiscoveryEvent(name=event_name, url=url)
        print(f"[EVENT] {event.name} -> {event.url}")
        return event


if __name__ == "__main__":
    DiscoveryKernelEvents.emit(
        DiscoveryKernelEvents.STARTED,
        "https://example.com",
    )
