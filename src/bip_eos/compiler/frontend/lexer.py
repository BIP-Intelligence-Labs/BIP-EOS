"""
lexer.py

BIP EOS Compiler
C04 — Lexer

Converts characters from a Scanner into immutable Token objects.
"""

from __future__ import annotations

from typing import Iterator

from .scanner import Scanner
from .token import Token
from .token_type import TokenType
from .keywords import resolve_identifier


class Lexer:
    """Simple production-ready lexer foundation."""

    def __init__(self, scanner: Scanner):
        self.scanner = scanner

    def tokenize(self) -> Iterator[Token]:
        """Yield tokens until EOF."""
        while True:
            token = self.next_token()
            yield token
            if token.token_type == TokenType.EOF:
                break

    def next_token(self) -> Token:
        """
        Placeholder implementation.

        C04 will incrementally add:
        - whitespace skipping
        - identifiers/keywords
        - numeric literals
        - string literals
        - operators
        - delimiters
        """
        if self.scanner.is_at_end():
            return Token(
                token_type=TokenType.EOF,
                lexeme="",
                value=None,
                span=self.scanner.current_span(),
            )

        ch = self.scanner.advance()

        if ch.isalpha() or ch == "_":
            lexeme = ch
            while (
                not self.scanner.is_at_end()
                and (self.scanner.peek().isalnum() or self.scanner.peek() == "_")
            ):
                lexeme += self.scanner.advance()

            token_type = resolve_identifier(lexeme)

            return Token(
                token_type=token_type,
                lexeme=lexeme,
                value=lexeme,
                span=self.scanner.current_span(),
            )

        return Token(
            token_type=TokenType.ERROR,
            lexeme=ch,
            value=f"Unexpected character: {ch}",
            span=self.scanner.current_span(),
        )
