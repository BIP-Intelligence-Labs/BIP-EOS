"""
token.py

BIP EOS Compiler
C03 — Token
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .token_type import TokenType
from .frontend.span import Span


@dataclass(frozen=True, slots=True)
class Token:
    """
    Immutable lexical token produced by the compiler.
    """

    token_type: TokenType
    lexeme: str
    value: Any
    span: Span

    @property
    def type(self) -> TokenType:
        return self.token_type

    @property
    def is_identifier(self) -> bool:
        return self.token_type == TokenType.IDENTIFIER

    @property
    def is_keyword(self) -> bool:
        return self.token_type.is_keyword()

    @property
    def is_literal(self) -> bool:
        return self.token_type.is_literal()

    @property
    def is_operator(self) -> bool:
        return self.token_type.is_operator()

    @property
    def is_delimiter(self) -> bool:
        return self.token_type.is_delimiter()

    @property
    def is_eof(self) -> bool:
        return self.token_type == TokenType.EOF

    def __str__(self) -> str:
        return (
            f"{self.token_type.name}"
            f"('{self.lexeme}') "
            f"{self.span}"
        )

    def __repr__(self) -> str:
        return (
            "Token("
            f"type={self.token_type.name}, "
            f"lexeme={self.lexeme!r}, "
            f"value={self.value!r}, "
            f"span={self.span!r}"
            ")"
        )
