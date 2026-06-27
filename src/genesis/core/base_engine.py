"""
GEB-001.002
base_engine.py

Genesis EEOS
Base Engine

Save to:
src/genesis/core/base_engine.py
"""

from __future__ import annotations

import logging
from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import Any


LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class EngineMetadata:
    """Immutable metadata shared by all Genesis engines."""

    name: str
    version: str
    description: str
    initialized: bool
    started_at: datetime | None


class BaseEngine(ABC):
    """
    Common lifecycle implementation for every Genesis engine.

    All engines should inherit from this class.
    """

    NAME = "Base Engine"
    VERSION = "0.1.0"
    DESCRIPTION = "Genesis EEOS Base Engine"

    def __init__(self) -> None:
        self._initialized = False
        self._started_at: datetime | None = None

    def initialize(self) -> None:
        """Initialize the engine."""
        if self._initialized:
            LOGGER.debug("%s already initialized.", self.NAME)
            return

        self._initialized = True
        self._started_at = datetime.utcnow()
        LOGGER.info("%s initialized.", self.NAME)

    def shutdown(self) -> None:
        """Shutdown the engine."""
        if not self._initialized:
            return

        LOGGER.info("%s shutdown.", self.NAME)
        self._initialized = False

    @property
    def initialized(self) -> bool:
        return self._initialized

    @property
    def started_at(self) -> datetime | None:
        return self._started_at

    def metadata(self) -> EngineMetadata:
        """Return immutable engine metadata."""
        return EngineMetadata(
            name=self.NAME,
            version=self.VERSION,
            description=self.DESCRIPTION,
            initialized=self._initialized,
            started_at=self._started_at,
        )

    def health(self) -> dict[str, Any]:
        """Return basic engine health."""
        return {
            "engine": self.NAME,
            "version": self.VERSION,
            "status": "healthy" if self._initialized else "offline",
        }
