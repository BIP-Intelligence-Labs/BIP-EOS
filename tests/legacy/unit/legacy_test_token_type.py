"""
test_token_type.py

Unit tests for the BIP EOS compiler TokenType.
"""

from ueos.compiler.token_type import TokenType


def test_identifier_is_literal():
    assert TokenType.IDENTIFIER.is_literal()


def test_integer_is_literal():
    assert TokenType.INTEGER.is_literal()


def test_module_is_keyword():
    assert TokenType.MODULE.is_keyword()


def test_if_is_keyword():
    assert TokenType.IF.is_keyword()


def test_plus_is_operator():
    assert TokenType.PLUS.is_operator()


def test_assign_is_operator():
    assert TokenType.ASSIGN.is_operator()


def test_left_paren_is_delimiter():
    assert TokenType.LPAREN.is_delimiter()


def test_comma_is_delimiter():
    assert TokenType.COMMA.is_delimiter()


def test_eof_is_not_keyword():
    assert not TokenType.EOF.is_keyword()


def test_error_is_not_literal():
    assert not TokenType.ERROR.is_literal()
