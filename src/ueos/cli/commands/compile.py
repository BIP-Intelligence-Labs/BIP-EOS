"""Compiler CLI."""
from ueos.compiler.frontend.lexer import Lexer
from ueos.compiler.frontend.parser import Parser


def main():
    source = ""
    tokens = Lexer(source).tokenize()
    ast = Parser(tokens).parse()
    print("Compilation complete")
    return ast


if __name__ == "__main__":
    main()
