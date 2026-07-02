"""Token types."""
from enum import Enum
class TokenType(str,Enum):
    IDENTIFIER="IDENTIFIER"
    NUMBER="NUMBER"
    STRING="STRING"
    KEYWORD="KEYWORD"
    OPERATOR="OPERATOR"
    EOF="EOF"
