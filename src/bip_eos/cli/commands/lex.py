"""Lexer CLI."""
from bip_eos.compiler.frontend.lexer import Lexer


def main():
    tokens = Lexer("").tokenize()
    print(tokens)


if __name__ == "__main__":
    main()
