#!/usr/bin/env python3
from pathlib import Path

FRAMEWORK = {
    "__init__.py": '\"\"\"UEOS CLI Framework\"\"\"\n',
    "command.py": 'from abc import ABC, abstractmethod\n\nclass Command(ABC):\n    name=\"\"\n    @abstractmethod\n    def execute(self,args)->int: raise NotImplementedError\n',
    "parser.py": 'import argparse\n\ndef create_parser():\n    return argparse.ArgumentParser(prog=\"ueos\")\n',
    "dispatcher.py": 'from .registry import CommandRegistry\n\ndef dispatch(name,args):\n    cmd=CommandRegistry.get(name)\n    if cmd is None: raise KeyError(name)\n    return cmd.execute(args)\n',
    "registry.py": 'class CommandRegistry:\n    _commands={}\n    @classmethod\n    def register(cls,c): cls._commands[c.name]=c\n    @classmethod\n    def get(cls,n): return cls._commands.get(n)\n',
    "help.py": 'def show_help():\n    print(\"UEOS Constitutional CLI\")\n',
    "output.py": 'def info(msg):\n    print(msg)\n',
    "errors.py": 'class UEOSCLIError(Exception):\n    pass\n',
}
SUBSYSTEMS=[\"audit\",\"registry\",\"graph\",\"compiler\",\"publish\",\"knowledge\",\"academy\",\"runtime\"]

def write(p,t):
    p.parent.mkdir(parents=True,exist_ok=True)
    if not p.exists():
        p.write_text(t,encoding='utf-8')
        print('[CREATE]',p)
    else:
        print('[EXISTS]',p)

root=Path.cwd()
cli=root/'src'/'bip_eos'/'cli'
fw=cli/'framework'
for n,t in FRAMEWORK.items():
    write(fw/n,t)
write(cli/'ueos.py','from bip_eos.cli.framework.parser import create_parser\n\nif __name__==\"__main__\":\n    p=create_parser();p.add_argument(\"system\",nargs=\"?\");print(p.parse_args())\n')
for s in SUBSYSTEMS:
    d=cli/s
    write(d/'__init__.py',f'\"\"\"{s.title()} CLI\"\"\"\n')
    write(d/'commands.py',f'\"\"\"{s.title()} command registry.\"\"\"\n')
print('UEOS CLI Framework initialized.')
