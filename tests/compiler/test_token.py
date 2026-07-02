from ueos.compiler.frontend.token import Token
from ueos.compiler.frontend.token_type import TokenType


def test_token_creation():
    token = Token(TokenType.IDENTIFIER, "value", 1, 1)
    assert token.lexeme == "value"
