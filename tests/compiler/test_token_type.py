from ueos.compiler.frontend.token_type import TokenType


def test_identifier_exists():
    assert TokenType.IDENTIFIER.value == "IDENTIFIER"
