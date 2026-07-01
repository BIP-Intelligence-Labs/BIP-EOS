from bip_eos.compiler.frontend.parser import Parser


def test_parser_constructs():
    parser = Parser([])
    assert parser.parse() is None
