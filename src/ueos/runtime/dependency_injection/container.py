
from dataclasses import dataclass
from typing import Any, Callable

@dataclass
class ServiceDescriptor:
    factory: Callable[[], Any]
    singleton: bool=True
    instance: Any=None

class ServiceContainer:
    def __init__(self):
        self._services={}
    def register(self,name,factory,singleton=True):
        self._services[name]=ServiceDescriptor(factory,singleton)
    def resolve(self,name):
        d=self._services[name]
        if d.singleton:
            if d.instance is None:
                d.instance=d.factory()
            return d.instance
        return d.factory()
