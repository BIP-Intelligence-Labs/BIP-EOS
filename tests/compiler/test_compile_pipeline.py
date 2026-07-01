from bip_eos.compiler.frontend.lexer import Lexer
from bip_eos.compiler.frontend.parser import Parser

def test_compile_pipeline():
    tokens = Lexer("").tokenize()
    ast = Parser(tokens).parse()
    assert tokens == []
    assert ast is None
