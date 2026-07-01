#!/usr/bin/env python3
"""
========================================================================
UEG-001

Phase 4

Engineering Graph Query Engine
========================================================================
"""

from __future__ import annotations

from typing import List, Optional

from bip_eos.graph.models import GraphModel, GraphNode, GraphEdge


class GraphQueryEngine:
    """
    Query service for the Engineering Graph.
    """

    def __init__(self, graph: GraphModel) -> None:
        self.graph = graph

    def find_node(self, name: str) -> Optional[GraphNode]:
        for node in self.graph.nodes.values():
            if node.name.lower() == name.lower():
                return node
        return None

    def nodes_by_kind(self, kind: str) -> List[GraphNode]:
        return [
            n for n in self.graph.nodes.values()
            if n.kind.lower() == kind.lower()
        ]

    def outgoing(self, node: GraphNode) -> List[GraphEdge]:
        return [
            e for e in self.graph.edges.values()
            if e.source == node.id
        ]

    def incoming(self, node: GraphNode) -> List[GraphEdge]:
        return [
            e for e in self.graph.edges.values()
            if e.target == node.id
        ]

    def neighbors(self, node: GraphNode) -> List[GraphNode]:
        ids = {
            e.target for e in self.outgoing(node)
        } | {
            e.source for e in self.incoming(node)
        }

        return [
            self.graph.nodes[nid]
            for nid in ids
            if nid in self.graph.nodes
        ]

    def orphan_nodes(self) -> List[GraphNode]:
        return [
            node
            for node in self.graph.nodes.values()
            if not self.incoming(node) and not self.outgoing(node)
        ]

    def summary(self) -> None:
        print("=" * 72)
        print("UEG-001 Query Engine")
        print("=" * 72)
        print(f"Nodes : {len(self.graph.nodes)}")
        print(f"Edges : {len(self.graph.edges)}")
        print("=" * 72)
