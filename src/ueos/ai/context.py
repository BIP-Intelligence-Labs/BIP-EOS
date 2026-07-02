"""
M-006.7.2 - Context Engine (Starter)

Collects engineering context that will later be supplied to the AI Kernel.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class AIContext:
    repository: str = ""
    root: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


class ContextEngine:
    """Builds an AIContext from the current repository."""

    def build(self, root: str | Path) -> AIContext:
        path = Path(root).resolve()
        return AIContext(
            repository=path.name,
            root=str(path),
            metadata={
                "git": (path / ".git").exists(),
                "src": (path / "src").exists(),
                "docs": (path / "docs").exists(),
            },
        )


if __name__ == "__main__":
    ctx = ContextEngine().build(".")
    print(ctx)
