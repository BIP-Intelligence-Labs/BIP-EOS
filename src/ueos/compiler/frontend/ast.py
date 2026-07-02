"""AST scaffold."""
from dataclasses import dataclass, field
@dataclass
class ASTNode:
    kind:str
    children:list=field(default_factory=list)
