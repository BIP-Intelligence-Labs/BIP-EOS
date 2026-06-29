from dataclasses import dataclass
from typing import Any
@dataclass
class Result:
    success: bool
    message: str = ""
    data: Any = None
