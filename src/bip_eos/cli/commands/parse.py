"""Parser CLI."""
from bip_eos.compiler.frontend.lexer import Lexer
from bip_eos.compiler.frontend.parser import Parser


def main():
    tokens = Lexer("").tokenize()
    tree = Parser(tokens).parse()
    print(tree)


if __name__ == "__main__":
    main()
