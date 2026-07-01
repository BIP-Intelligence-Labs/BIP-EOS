#!/usr/bin/env python3
"""
discovery_context.py

EAuS-003
Discovery Context

Constitutional Object:
Represents a single discovery execution session.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import uuid


@dataclass(slots=True)
class DiscoveryContext:
    """Execution context shared by all discovery collectors."""

    repository_root: Path
    execution_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    started_utc: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    subsystem: str = "EAuS-003"
    architecture_version: str = "1.0"
    constitution_version: str = "EA-001"

    metadata: dict[str, Any] = field(default_factory=dict)
    options: dict[str, Any] = field(default_factory=dict)

    def add_metadata(self, key: str, value: Any) -> None:
        self.metadata[key] = value

    def add_option(self, key: str, value: Any) -> None:
        self.options[key] = value

    def to_dict(self) -> dict[str, Any]:
        return {
            "execution_id": self.execution_id,
            "started_utc": self.started_utc.isoformat(),
            "repository_root": str(self.repository_root),
            "subsystem": self.subsystem,
            "architecture_version": self.architecture_version,
            "constitution_version": self.constitution_version,
            "metadata": self.metadata,
            "options": self.options,
        }


if __name__ == "__main__":
    ctx = DiscoveryContext(repository_root=Path(".").resolve())
    print("EAuS Discovery Context")
    print("----------------------")
    for k, v in ctx.to_dict().items():
        print(f"{k}: {v}")
