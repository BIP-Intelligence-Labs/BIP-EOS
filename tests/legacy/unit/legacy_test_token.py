"""
test_token.py

Unit tests for the BIP EOS compiler Token.
"""

from ueos.compiler.frontend.position import Position
from ueos.compiler.frontend.span import Span
from ueos.compiler.token import Token
from ueos.compiler.token_type import TokenType


def make_span() -> Span:
    start = Position(line=1, column=1, offset=0)
    end = Position(line=1, column=7, offset=6)
    return Span(start=start, end=end)


def test_token_properties():
    token = Token(
        token_type=TokenType.IDENTIFIER,
        lexeme="builder",
        value="builder",
        span=make_span(),
    )

    assert token.type == TokenType.IDENTIFIER
    assert token.is_identifier
    assert token.is_literal
    assert not token.is_keyword
    assert not token.is_operator
    assert not token.is_delimiter
    assert not token.is_eof


def test_keyword_token():
    token = Token(
        token_type=TokenType.MODULE,
        lexeme="module",
        value=None,
        span=make_span(),
    )

    assert token.is_keyword
    assert not token.is_identifier


def test_eof_token():
    token = Token(
        token_type=TokenType.EOF,
        lexeme="",
        value=None,
        span=make_span(),
    )

    assert token.is_eof


def test_string_representation():
    token = Token(
        token_type=TokenType.INTEGER,
        lexeme="42",
        value=42,
        span=make_span(),
    )

    text = str(token)
    assert "INTEGER" in text
    assert "42" in text


def test_repr_contains_type():
    token = Token(
        token_type=TokenType.STRING,
        lexeme='"hello"',
        value="hello",
        span=make_span(),
    )

    assert "STRING" in repr(token)
