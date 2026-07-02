"""
========================================================================
INS-001
UEOS Installation Framework

Base Installer
========================================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class InstallationResult:
    success: bool
    subsystem: str
    message: str
    timestamp: datetime = datetime.now()


class Installer(ABC):
    """
    Base class for every UEOS constitutional installer.

    Every constitutional subsystem SHALL inherit from this class.
    """

    subsystem: str = "unknown"
    version: str = "0.1.0"

    @abstractmethod
    def install(self) -> InstallationResult:
        """Install the subsystem."""
        raise NotImplementedError

    @abstractmethod
    def verify(self) -> bool:
        """Verify installation integrity."""
        raise NotImplementedError

    @abstractmethod
    def update(self) -> InstallationResult:
        """Update the subsystem."""
        raise NotImplementedError

    @abstractmethod
    def repair(self) -> InstallationResult:
        """Repair the subsystem."""
        raise NotImplementedError

    @abstractmethod
    def uninstall(self) -> InstallationResult:
        """Remove the subsystem."""
        raise NotImplementedError

    def banner(self) -> None:
        print("=" * 72)
        print("UEOS Installation Framework")
        print("INS-001")
        print(f"Subsystem : {self.subsystem}")
        print("=" * 72)
