"""Compiler diagnostics."""
from dataclasses import dataclass
@dataclass(slots=True)
class Diagnostic:
    severity:str
    message:str
    line:int=0
    column:int=0
