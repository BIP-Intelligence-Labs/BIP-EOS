"""Repository domain models for Genesis EEOS."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Repository:
    name: str
    path: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    initialized: bool = False
    version: str = "0.1.0"

    def initialize(self) -> None:
        self.initialized = True


@dataclass(slots=True)
class RepositoryManifest:
    repository: str
    engine_version: str
    created_at: datetime = field(default_factory=datetime.utcnow)
