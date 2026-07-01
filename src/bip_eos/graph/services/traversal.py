
#!/usr/bin/env python3
"""
========================================================================
UEG-001

Phase 5

Engineering Graph Traversal Engine
========================================================================
"""

from __future__ import annotations

from collections import deque

from bip_eos.graph.models import GraphModel, GraphNode


class GraphTraversalEngine:
    """
    Traverses Engineering Graph relationships.
    """

    def __init__(self, graph: GraphModel) -> None:
        self.graph = graph

    def depth_first(self, start: GraphNode) -> list[GraphNode]:
        visited = set()
        order = []

        def visit(node_id: str):
            if node_id in visited:
                return
            visited.add(node_id)
            node = self.graph.nodes[node_id]
            order.append(node)

            for edge in self.graph.edges.values():
                if edge.source == node_id and edge.target in self.graph.nodes:
                    visit(edge.target)

        visit(start.id)
        return order

    def breadth_first(self, start: GraphNode) -> list[GraphNode]:
        visited = {start.id}
        queue = deque([start.id])
        order = []

        while queue:
            node_id = queue.popleft()
            order.append(self.graph.nodes[node_id])

            for edge in self.graph.edges.values():
                if edge.source == node_id and edge.target not in visited:
                    if edge.target in self.graph.nodes:
                        visited.add(edge.target)
                        queue.append(edge.target)

        return order

    def dependency_chain(self, start: GraphNode) -> list[GraphNode]:
        return self.depth_first(start)

    def impact_analysis(self, start: GraphNode) -> list[GraphNode]:
        return self.breadth_first(start)

    def summary(self) -> None:
        print("=" * 72)
        print("UEG-001 Traversal Engine")
        print("=" * 72)
        print("Traversal services available:")
        print("  - depth_first()")
        print("  - breadth_first()")
        print("  - dependency_chain()")
        print("  - impact_analysis()")
        print("=" * 72)
