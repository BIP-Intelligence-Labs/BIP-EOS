"""
runtime_state_machine.py

UEOS Runtime State Machine
"""

from __future__ import annotations

from enum import Enum, auto


class RuntimeState(Enum):
    CREATED = auto()
    BOOTING = auto()
    RUNNING = auto()
    STOPPING = auto()
    STOPPED = auto()
    FAILED = auto()


class RuntimeStateMachine:
    """Simple runtime state machine for the UEOS kernel."""

    _ALLOWED = {
        RuntimeState.CREATED: {RuntimeState.BOOTING},
        RuntimeState.BOOTING: {RuntimeState.RUNNING, RuntimeState.FAILED},
        RuntimeState.RUNNING: {RuntimeState.STOPPING, RuntimeState.FAILED},
        RuntimeState.STOPPING: {RuntimeState.STOPPED},
        RuntimeState.STOPPED: {RuntimeState.BOOTING},
        RuntimeState.FAILED: {RuntimeState.STOPPED},
    }

    def __init__(self) -> None:
        self._state = RuntimeState.CREATED

    @property
    def state(self) -> RuntimeState:
        return self._state

    def transition(self, new_state: RuntimeState) -> None:
        allowed = self._ALLOWED[self._state]
        if new_state not in allowed:
            raise ValueError(
                f"Invalid transition: {self._state.name} -> {new_state.name}"
            )
        self._state = new_state

    def reset(self) -> None:
        self._state = RuntimeState.CREATED
