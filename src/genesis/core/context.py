
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from datetime import datetime
from typing import Any

class ContextError(Exception):
    pass

@dataclass
class Environment:
    python_version: str = "3.11+"
    engineering_standard: str = "EES-1.0"

@dataclass
class Configuration:
    values: dict[str, Any] = field(default_factory=dict)

@dataclass
class Session:
    started: datetime = field(default_factory=datetime.now)
    user: str = "engineer"

@dataclass
class ProjectContext:
    name: str
    root: Path

@dataclass
class BuildContext:
    project: ProjectContext
    environment: Environment = field(default_factory=Environment)
    configuration: Configuration = field(default_factory=Configuration)
    session: Session = field(default_factory=Session)

class ExecutionContext:
    def __init__(self, context: BuildContext):
        self.context = context

    @property
    def root(self) -> Path:
        return self.context.project.root

    def get(self, key: str, default=None):
        return self.context.configuration.values.get(key, default)

    def set(self, key: str, value):
        self.context.configuration.values[key] = value
