"""
graph_engine.py

UEOS Atlas
M-006.5 Engineering Graph

Core graph engine for representing engineering knowledge.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class GraphNode:
    id: str
    kind: str
    metadata: dict[str, object] = field(default_factory=dict)


@dataclass(slots=True, frozen=True)
class GraphEdge:
    source: str
    target: str
    relationship: str
    metadata: dict[str, object] = field(default_factory=dict)


class EngineeringGraph:
    """Core in-memory engineering graph."""

    def __init__(self) -> None:
        self._nodes: dict[str, GraphNode] = {}
        self._edges: list[GraphEdge] = []
        self._adjacency: dict[str, list[GraphEdge]] = defaultdict(list)

    def add_node(self, node: GraphNode) -> None:
        self._nodes[node.id] = node

    def add_edge(self, edge: GraphEdge) -> None:
        if edge.source not in self._nodes:
            raise KeyError(f"Unknown source node: {edge.source}")
        if edge.target not in self._nodes:
            raise KeyError(f"Unknown target node: {edge.target}")
        self._edges.append(edge)
        self._adjacency[edge.source].append(edge)

    def get_node(self, node_id: str) -> GraphNode | None:
        return self._nodes.get(node_id)

    def neighbors(self, node_id: str) -> list[GraphNode]:
        return [self._nodes[e.target] for e in self._adjacency.get(node_id, [])]

    def outgoing(self, node_id: str) -> list[GraphEdge]:
        return list(self._adjacency.get(node_id, []))

    def node_count(self) -> int:
        return len(self._nodes)

    def edge_count(self) -> int:
        return len(self._edges)

    def stats(self) -> dict[str, int]:
        return {"nodes": self.node_count(), "edges": self.edge_count()}
