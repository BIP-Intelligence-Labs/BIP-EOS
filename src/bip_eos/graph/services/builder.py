#!/usr/bin/env python3
"""
========================================================================
UEG-001

Phase 3

Engineering Graph Builder
========================================================================
"""

from __future__ import annotations

from pathlib import Path

from bip_eos.graph.models import GraphModel, GraphNode


class GraphBuilder:
    """
    Discovers UEOS packages and builds an Engineering Graph.
    """

    def __init__(self, root: str | Path = "src/bip_eos") -> None:
        self.root = Path(root)

    def build(self) -> GraphModel:
        graph = GraphModel()
        nodes: dict[str, GraphNode] = {}

        if not self.root.exists():
            return graph

        for item in sorted(self.root.iterdir()):
            if not item.is_dir():
                continue

            if item.name.startswith("__"):
                continue

            node = graph.add_node(
                kind="Subsystem",
                name=item.name,
                path=str(item),
            )
            nodes[item.name] = node

        # Simple constitutional relationships
        if "registry" in nodes and "graph" in nodes:
            graph.add_edge(nodes["registry"], nodes["graph"], "feeds")

        if "graph" in nodes and "migration" in nodes:
            graph.add_edge(nodes["graph"], nodes["migration"], "supports")

        if "runtime" in nodes and "graph" in nodes:
            graph.add_edge(nodes["runtime"], nodes["graph"], "hosts")

        return graph


if __name__ == "__main__":
    builder = GraphBuilder()
    graph = builder.build()

    graph.summary()

    print("\nSubsystems\n")

    for node in graph.nodes.values():
        print(f"{node.id:12} {node.name}")

    print("\nRelationships\n")

    for edge in graph.edges.values():
        print(
            f"{edge.id} : "
            f"{edge.source} -> {edge.target} "
            f"({edge.relationship})"
        )
