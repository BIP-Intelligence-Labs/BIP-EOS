"""
token_type.py

BIP EOS Compiler
C03 — Token Types
"""

from __future__ import annotations

from enum import Enum, auto


class TokenType(Enum):
    """Enumeration of all lexical token types."""

    # Special
    EOF = auto()
    ERROR = auto()
    NEWLINE = auto()

    # Literals
    IDENTIFIER = auto()
    INTEGER = auto()
    FLOAT = auto()
    STRING = auto()
    BOOLEAN = auto()

    # Keywords
    MODULE = auto()
    ENGINE = auto()
    PLUGIN = auto()
    REPOSITORY = auto()
    REPORT = auto()
    BUILDER = auto()
    COMMUNITY = auto()
    IF = auto()
    ELSE = auto()
    RETURN = auto()
    TRUE = auto()
    FALSE = auto()
    NULL = auto()

    # Operators
    ASSIGN = auto()
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    EQUAL = auto()
    NOT_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()

    # Delimiters
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    COLON = auto()
    SEMICOLON = auto()
    COMMA = auto()
    DOT = auto()

    def is_literal(self) -> bool:
        return self in {
            TokenType.IDENTIFIER,
            TokenType.INTEGER,
            TokenType.FLOAT,
            TokenType.STRING,
            TokenType.BOOLEAN,
        }

    def is_keyword(self) -> bool:
        return self in {
            TokenType.MODULE,
            TokenType.ENGINE,
            TokenType.PLUGIN,
            TokenType.REPOSITORY,
            TokenType.REPORT,
            TokenType.BUILDER,
            TokenType.COMMUNITY,
            TokenType.IF,
            TokenType.ELSE,
            TokenType.RETURN,
            TokenType.TRUE,
            TokenType.FALSE,
            TokenType.NULL,
        }

    def is_operator(self) -> bool:
        return self in {
            TokenType.ASSIGN,
            TokenType.PLUS,
            TokenType.MINUS,
            TokenType.STAR,
            TokenType.SLASH,
            TokenType.EQUAL,
            TokenType.NOT_EQUAL,
            TokenType.GREATER,
            TokenType.GREATER_EQUAL,
            TokenType.LESS,
            TokenType.LESS_EQUAL,
        }

    def is_delimiter(self) -> bool:
        return self in {
            TokenType.LPAREN,
            TokenType.RPAREN,
            TokenType.LBRACE,
            TokenType.RBRACE,
            TokenType.LBRACKET,
            TokenType.RBRACKET,
            TokenType.COLON,
            TokenType.SEMICOLON,
            TokenType.COMMA,
            TokenType.DOT,
        }
