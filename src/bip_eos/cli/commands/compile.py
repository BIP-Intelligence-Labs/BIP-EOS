"""Compiler CLI."""
from bip_eos.compiler.frontend.lexer import Lexer
from bip_eos.compiler.frontend.parser import Parser


def main():
    source = ""
    tokens = Lexer(source).tokenize()
    ast = Parser(tokens).parse()
    print("Compilation complete")
    return ast


if __name__ == "__main__":
    main()
