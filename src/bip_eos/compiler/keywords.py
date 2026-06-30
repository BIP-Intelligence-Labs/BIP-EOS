"""
keywords.py

BIP EOS Compiler
C03 — Keyword Registry
"""

from __future__ import annotations

from .token_type import TokenType

KEYWORDS: dict[str, TokenType] = {
    "module": TokenType.MODULE,
    "engine": TokenType.ENGINE,
    "plugin": TokenType.PLUGIN,
    "repository": TokenType.REPOSITORY,
    "report": TokenType.REPORT,
    "builder": TokenType.BUILDER,
    "community": TokenType.COMMUNITY,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "return": TokenType.RETURN,
    "true": TokenType.TRUE,
    "false": TokenType.FALSE,
    "null": TokenType.NULL,
}


def is_keyword(text: str) -> bool:
    """Return True if text is a reserved keyword."""
    return text in KEYWORDS


def keyword_type(text: str) -> TokenType:
    """
    Return the TokenType for a keyword.

    Raises:
        KeyError: if text is not a keyword.
    """
    return KEYWORDS[text]


def resolve_identifier(text: str) -> TokenType:
    """
    Resolve an identifier to either its keyword token
    or IDENTIFIER.
    """
    return KEYWORDS.get(text, TokenType.IDENTIFIER)
