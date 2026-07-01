"""
test_lexer.py

Unit tests for the BIP EOS compiler lexer.

C04 — Lexer
"""

from bip_eos.compiler.frontend.lexer import Lexer
from bip_eos.compiler.frontend.scanner import Scanner
from bip_eos.compiler.frontend.source_file import SourceFile
from bip_eos.compiler.frontend.position import Position


def make_lexer(text: str) -> Lexer:
    source = SourceFile(
        name="test.bip",
        text=text,
    )
    scanner = Scanner(source)
    return Lexer(scanner)


def test_identifier():
    token = make_lexer("builder").next_token()

    assert token.lexeme == "builder"
    assert token.is_identifier


def test_keyword():
    token = make_lexer("module").next_token()

    assert token.is_keyword


def test_integer():
    token = make_lexer("12345").next_token()

    assert token.value == 12345


def test_float():
    token = make_lexer("3.14").next_token()

    assert abs(token.value - 3.14) < 1e-9


def test_string():
    token = make_lexer('"hello"').next_token()

    assert token.value == "hello"


def test_eof():
    lexer = make_lexer("")
    token = lexer.next_token()

    assert token.is_eof
