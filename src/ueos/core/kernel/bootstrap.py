"""UEOS Bootstrap"""

from .kernel import Kernel

def bootstrap() -> Kernel:
    return Kernel()
