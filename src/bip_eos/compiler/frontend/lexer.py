"""
lexer.py

BIP EOS Compiler
C04 — Lexer
"""

from __future__ import annotations

from typing import Iterator

from .scanner import Scanner
from .token import Token
from .token_type import TokenType
from .keywords import resolve_identifier


class Lexer:
    """
    BIP EOS lexical analyzer.

    Current capabilities

    ✓ EOF
    ✓ Whitespace
    ✓ Identifiers
    ✓ Keywords
    ✓ Integer literals
    ✓ Floating-point literals

    Planned

    □ Strings
    □ Operators
    □ Delimiters
    □ Comments
    """

    def __init__(self, scanner: Scanner):
        self.scanner = scanner

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def tokenize(self) -> Iterator[Token]:
        while True:

            token = self.next_token()

            yield token

            if token.is_eof:
                break

    # ---------------------------------------------------------
    # Core
    # ---------------------------------------------------------

    def next_token(self) -> Token:

        self.skip_whitespace()

        if self.scanner.is_at_end():

            return Token(
                token_type=TokenType.EOF,
                lexeme="",
                value=None,
                span=self.scanner.current_span(),
            )

        ch = self.scanner.advance()

        #
        # Identifier
        #

        if ch.isalpha() or ch == "_":
            return self.read_identifier(ch)

        #
        # Number
        #

        if ch.isdigit():
            return self.read_number(ch)

        #
        # Unknown
        #

        return Token(
            token_type=TokenType.ERROR,
            lexeme=ch,
            value=f"Unexpected character '{ch}'",
            span=self.scanner.current_span(),
        )

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def skip_whitespace(self) -> None:

        while not self.scanner.is_at_end():

            ch = self.scanner.peek()

            if ch in (" ", "\t", "\r", "\n"):

                self.scanner.advance()
                continue

            break

    def read_identifier(self, first: str) -> Token:

        lexeme = first

        while (
            not self.scanner.is_at_end()
            and (
                self.scanner.peek().isalnum()
                or self.scanner.peek() == "_"
            )
        ):
            lexeme += self.scanner.advance()

        token_type = resolve_identifier(lexeme)

        return Token(
            token_type=token_type,
            lexeme=lexeme,
            value=lexeme,
            span=self.scanner.current_span(),
        )

    def read_number(self, first: str) -> Token:
        """
        Read an integer or floating-point literal.
        """

        lexeme = first
        is_float = False

        while not self.scanner.is_at_end():

            ch = self.scanner.peek()

            if ch.isdigit():
                lexeme += self.scanner.advance()
                continue

            if (
                ch == "."
                and not is_float
            ):
                is_float = True
                lexeme += self.scanner.advance()
                continue

            break

        if is_float:
            token_type = TokenType.FLOAT
            value = float(lexeme)
        else:
            token_type = TokenType.INTEGER
            value = int(lexeme)

        return Token(
            token_type=token_type,
            lexeme=lexeme,
            value=value,
            span=self.scanner.current_span(),
        )
