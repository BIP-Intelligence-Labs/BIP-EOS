from ueos.compiler.frontend.lexer import Lexer
from ueos.compiler.frontend.parser import Parser

def test_compile_pipeline():
    tokens = Lexer("").tokenize()
    ast = Parser(tokens).parse()
    assert tokens == []
    assert ast is None
