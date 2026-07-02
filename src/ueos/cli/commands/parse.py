"""Parser CLI."""
from ueos.compiler.frontend.lexer import Lexer
from ueos.compiler.frontend.parser import Parser


def main():
    tokens = Lexer("").tokenize()
    tree = Parser(tokens).parse()
    print(tree)


if __name__ == "__main__":
    main()
