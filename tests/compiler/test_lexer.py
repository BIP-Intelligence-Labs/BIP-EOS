from bip_eos.compiler.frontend.lexer import Lexer


def test_lexer_constructs():
    lexer = Lexer("")
    assert lexer.tokenize() == []
