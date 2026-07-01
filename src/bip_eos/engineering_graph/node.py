"""
node.py

UEOS Atlas
M-006.5 Engineering Graph

Graph node model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class NodeType(str, Enum):
    REPOSITORY = "repository"
    PACKAGE = "package"
    MODULE = "module"
    FILE = "file"
    CLASS = "class"
    FUNCTION = "function"
    TEST = "test"
    DOCUMENT = "document"
    PLUGIN = "plugin"
    SERVICE = "service"
    AGENT = "agent"
    API = "api"
    ADR = "adr"
    PIPELINE = "pipeline"
    UNKNOWN = "unknown"


@dataclass(slots=True)
class Node:
    """Engineering graph node."""

    id: str
    name: str
    node_type: NodeType
    metadata: dict[str, object] = field(default_factory=dict)

    @property
    def label(self) -> str:
        return f"{self.node_type.value}:{self.name}"

    def add_metadata(self, key: str, value: object) -> None:
        self.metadata[key] = value

    def get(self, key: str, default: object | None = None) -> object | None:
        return self.metadata.get(key, default)

    def to_dict(self) -> dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "type": self.node_type.value,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Node":
        return cls(
            id=str(data["id"]),
            name=str(data["name"]),
            node_type=NodeType(str(data["type"])),
            metadata=dict(data.get("metadata", {})),
        )
