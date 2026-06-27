
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from functools import total_ordering

class ReleaseStage(Enum):
    ALPHA = "alpha"
    BETA = "beta"
    RC = "rc"
    STABLE = "stable"

@total_ordering
@dataclass(frozen=True)
class SemanticVersion:
    major: int
    minor: int
    patch: int
    stage: ReleaseStage = ReleaseStage.STABLE

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}-{self.stage.value}"

    def __eq__(self, other):
        if not isinstance(other, SemanticVersion):
            return NotImplemented
        return (self.major, self.minor, self.patch) == (other.major, other.minor, other.patch)

    def __lt__(self, other):
        if not isinstance(other, SemanticVersion):
            return NotImplemented
        return (self.major, self.minor, self.patch) < (other.major, other.minor, other.patch)

class VersionManager:
    def __init__(self):
        self.current = SemanticVersion(0, 1, 0)

    def bump_patch(self):
        self.current = SemanticVersion(
            self.current.major,
            self.current.minor,
            self.current.patch + 1,
            self.current.stage,
        )

    def bump_minor(self):
        self.current = SemanticVersion(
            self.current.major,
            self.current.minor + 1,
            0,
            self.current.stage,
        )

    def bump_major(self):
        self.current = SemanticVersion(
            self.current.major + 1,
            0,
            0,
            self.current.stage,
        )

    def version(self) -> str:
        return str(self.current)
