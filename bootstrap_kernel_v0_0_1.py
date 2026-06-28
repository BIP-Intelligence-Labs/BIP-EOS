from __future__ import annotations
from abc import ABC,abstractmethod
from dataclasses import dataclass,field
from typing import Dict,List,Callable,Any
import logging
logging.basicConfig(level=logging.INFO,format="%(levelname)s | %(message)s")
class BootstrapPlugin(ABC):
    name="unnamed"
    @abstractmethod
    def register(self,kernel):...
    def start(self):pass
    def stop(self):pass
class EventBus:
    def __init__(self): self.h={}
    def subscribe(self,e,f): self.h.setdefault(e,[]).append(f)
    def emit(self,e,**p):
        logging.info(f"EVENT -> {e}")
        [f(**p) for f in self.h.get(e,[])]
class CommandRegistry:
    def __init__(self): self.c={}
    def register(self,n,f): self.c[n]=f
    def execute(self,n,*a,**k): return self.c[n](*a,**k)
@dataclass
class BootstrapKernel:
    plugins:Dict[str,BootstrapPlugin]=field(default_factory=dict)
    def __post_init__(self): self.events=EventBus(); self.commands=CommandRegistry()
    def install(self,p): p.register(self); self.plugins[p.name]=p
    def boot(self):
        logging.info("Booting Bootstrap Kernel")
        [p.start() for p in self.plugins.values()]
        self.events.emit("kernel.booted")
class HelloPlugin(BootstrapPlugin):
    name="hello"
    def register(self,k):
        k.commands.register("hello",self.hello)
        k.events.subscribe("kernel.booted",lambda: logging.info("Hello Plugin Ready"))
    def hello(self):
        print("Bootstrap Engineering Factory\n\nBuilt with\n1s\n0s\nCoffee\nTwo Chiefs\n\nReady to do some more damage.")
if __name__=="__main__":
    k=BootstrapKernel(); k.install(HelloPlugin()); k.boot(); k.commands.execute("hello")
