"""Genesis EEOS Version Manager."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Version:
    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    @property
    def tag(self) -> str:
        return f"v{self}"


CURRENT_VERSION = Version(0, 1, 0)

VERSION = str(CURRENT_VERSION)
VERSION_TAG = CURRENT_VERSION.tag
