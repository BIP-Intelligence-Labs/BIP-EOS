
# UEG-001 Phase 6 - Graph Validator
from __future__ import annotations
from dataclasses import dataclass, field
from ueos.graph.models import GraphModel

@dataclass(slots=True)
class GraphValidationResult:
    passed: bool=True
    errors:list[str]=field(default_factory=list)
    warnings:list[str]=field(default_factory=list)

class GraphValidator:
    def validate(self, graph: GraphModel)->GraphValidationResult:
        result=GraphValidationResult()
        seen=set()
        for node in graph.nodes.values():
            key=node.name.lower()
            if key in seen:
                result.passed=False
                result.errors.append(f"Duplicate node name: {node.name}")
            seen.add(key)
        for edge in graph.edges.values():
            if edge.source not in graph.nodes:
                result.passed=False
                result.errors.append(f"Edge {edge.id} missing source node.")
            if edge.target not in graph.nodes:
                result.passed=False
                result.errors.append(f"Edge {edge.id} missing target node.")
            if edge.source==edge.target:
                result.warnings.append(f"Self-reference detected: {edge.id}")
        return result

    def summary(self,result:GraphValidationResult):
        print("="*72)
        print("UEG-001 Graph Validation")
        print("="*72)
        print("STATUS:", "PASS" if result.passed else "FAIL")
        for e in result.errors:
            print("ERROR:",e)
        for w in result.warnings:
            print("WARNING:",w)
        if not result.errors and not result.warnings:
            print("No validation issues detected.")
        print("="*72)
