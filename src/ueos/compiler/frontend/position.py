from dataclasses import dataclass

@dataclass(slots=True)
class Position:
    line: int
    column: int
    offset: int
