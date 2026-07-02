#!/usr/bin/env python3
"""
========================================================================
UEG-001

Phase 2

Engineering Graph Models
========================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class GraphNode:
    id: str
    kind: str
    name: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class GraphEdge:
    id: str
    source: str
    target: str
    relationship: str
    metadata: dict[str, Any] = field(default_factory=dict)


class GraphModel:
    """
    In-memory Engineering Graph.
    """

    def __init__(self) -> None:
        self.created = datetime.utcnow().isoformat()
        self.nodes: dict[str, GraphNode] = {}
        self.edges: dict[str, GraphEdge] = {}

    def add_node(self, kind: str, name: str, **metadata) -> GraphNode:
        node = GraphNode(
            id=f"N-{uuid4().hex[:8].upper()}",
            kind=kind,
            name=name,
            metadata=metadata,
        )
        self.nodes[node.id] = node
        return node

    def add_edge(
        self,
        source: GraphNode,
        target: GraphNode,
        relationship: str,
        **metadata,
    ) -> GraphEdge:

        edge = GraphEdge(
            id=f"E-{uuid4().hex[:8].upper()}",
            source=source.id,
            target=target.id,
            relationship=relationship,
            metadata=metadata,
        )

        self.edges[edge.id] = edge
        return edge

    def summary(self) -> None:
        print("=" * 72)
        print("UEG-001 Engineering Graph")
        print("=" * 72)
        print(f"Nodes : {len(self.nodes)}")
        print(f"Edges : {len(self.edges)}")
        print("=" * 72)


if __name__ == "__main__":
    graph = GraphModel()

    registry = graph.add_node("Subsystem", "ERS-001")
    migration = graph.add_node("Subsystem", "MGS-001")

    graph.add_edge(
        registry,
        migration,
        "supports",
    )

    graph.summary()
