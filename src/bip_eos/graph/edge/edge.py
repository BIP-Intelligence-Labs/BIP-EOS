"""
edge.py

UEOS Atlas
M-006.5 Engineering Graph
"""

from dataclasses import dataclass, field
from enum import Enum

class EdgeType(str, Enum):
    DEPENDS_ON="depends_on"
    IMPORTS="imports"
    REFERENCES="references"
    TESTS="tests"
    IMPLEMENTS="implements"
    DOCUMENTS="documents"
    OWNS="owns"

@dataclass(slots=True)
class Edge:
    source:str
    target:str
    edge_type:EdgeType
    metadata:dict[str,object]=field(default_factory=dict)
