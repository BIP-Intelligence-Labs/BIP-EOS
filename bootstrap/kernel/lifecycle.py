"""
bootstrap/kernel/lifecycle.py

Production Lifecycle Manager.
"""

from __future__ import annotations

from enum import Enum, auto


class KernelState(Enum):
    CREATED = auto()
    STARTING = auto()
    RUNNING = auto()
    STOPPING = auto()
    STOPPED = auto()


class LifecycleManager:
    """Tracks Bootstrap Kernel lifecycle."""

    def __init__(self) -> None:
        self.state = KernelState.CREATED

    def startup(self) -> None:
        self.state = KernelState.STARTING
        self.state = KernelState.RUNNING

    def shutdown(self) -> None:
        self.state = KernelState.STOPPING
        self.state = KernelState.STOPPED

    @property
    def running(self) -> bool:
        return self.state is KernelState.RUNNING

    def status(self) -> str:
        return self.state.name
