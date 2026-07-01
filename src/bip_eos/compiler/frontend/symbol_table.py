"""Symbol table."""
class SymbolTable:
    def __init__(self): self._symbols={}
    def define(self,name,value): self._symbols[name]=value
    def resolve(self,name): return self._symbols.get(name)
