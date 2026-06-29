"""Canonical EOS Version Information"""

from dataclasses import dataclass

@dataclass(frozen=True)
class EOSVersion:
    version: str = "0.1.0"
    codename: str = "Genesis"
    platform: str = "Engineering Operating System"
    release: str = "Development"

EOS_VERSION = EOSVersion()
