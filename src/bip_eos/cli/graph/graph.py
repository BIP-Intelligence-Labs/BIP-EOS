
"""
========================================================================
UEOS

Graph CLI

UEG-001 Constitutional CLI Integration
========================================================================
"""

from __future__ import annotations

from bip_eos.graph.services.builder import GraphBuilder
from bip_eos.graph.services.validator import GraphValidator
from bip_eos.graph.services.query import GraphQueryEngine
from bip_eos.graph.services.traversal import GraphTraversalEngine
from bip_eos.graph.services.reporter import GraphReporter


def handle(command: str | None, args: list[str]) -> None:
    builder = GraphBuilder()
    graph = builder.build()

    command = (command or "").lower()

    if command == "build":
        graph.summary()
        return

    if command == "validate":
        validator = GraphValidator()
        result = validator.validate(graph)
        validator.summary(result)
        return

    if command == "report":
        reporter = GraphReporter()
        report = reporter.build(graph)
        reporter.summary(report)
        reporter.save_json(report, "reports/engineering_graph.json")
        return

    if command == "query":
        if not args:
            print("Usage: ueos graph query <node>")
            return

        engine = GraphQueryEngine(graph)
        node = engine.find_node(args[0])

        if node is None:
            print("Node not found.")
            return

        print(f"\nNode: {node.name}\n")
        print("Neighbors:")
        for neighbor in engine.neighbors(node):
            print(f"  - {neighbor.name}")
        return

    if command == "traverse":
        if not args:
            print("Usage: ueos graph traverse <node>")
            return

        query = GraphQueryEngine(graph)
        node = query.find_node(args[0])

        if node is None:
            print("Node not found.")
            return

        traversal = GraphTraversalEngine(graph)

        print("\nDependency Chain\n")
        for item in traversal.dependency_chain(node):
            print(f"  - {item.name}")
        return

    print("=" * 72)
    print("UEG-001 Engineering Graph")
    print("=" * 72)
    print("Commands")
    print("  build")
    print("  validate")
    print("  query <node>")
    print("  traverse <node>")
    print("  report")
    print("=" * 72)
