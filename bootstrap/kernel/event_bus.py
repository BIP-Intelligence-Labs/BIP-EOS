"""
bootstrap/kernel/event_bus.py

Production Event Bus for Bootstrap Kernel.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Callable


class EventBus:
    """Simple synchronous publish/subscribe event bus."""

    def __init__(self) -> None:
        self._handlers: dict[str, list[Callable[..., Any]]] = defaultdict(list)

    def subscribe(self, event: str, handler: Callable[..., Any]) -> None:
        """Register a handler for an event."""
        if handler not in self._handlers[event]:
            self._handlers[event].append(handler)

    # Friendly alias
    on = subscribe

    def unsubscribe(self, event: str, handler: Callable[..., Any]) -> None:
        """Remove a handler."""
        if handler in self._handlers[event]:
            self._handlers[event].remove(handler)

    def emit(self, event: str, **payload: Any) -> None:
        """Publish an event."""
        for handler in list(self._handlers.get(event, [])):
            handler(**payload)

    def listeners(self, event: str) -> int:
        """Return number of listeners for an event."""
        return len(self._handlers.get(event, []))

    def clear(self) -> None:
        """Remove all subscriptions."""
        self._handlers.clear()
