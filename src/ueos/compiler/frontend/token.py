"""Compiler token model."""
from dataclasses import dataclass
from .token_type import TokenType

@dataclass(slots=True,frozen=True)
class Token:
    token_type: TokenType
    lexeme: str
    line: int
    column: int
