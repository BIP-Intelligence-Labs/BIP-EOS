#!/usr/bin/env python3
from pathlib import Path

SYSTEMS=["audit","registry","graph","compiler","publish","knowledge","academy","runtime"]

FRAMEWORK={
"__init__.py":'"""UEOS CLI Framework"""\n',
"command.py":'class Command:\n    name=""\n    def execute(self,args):\n        raise NotImplementedError\n',
"parser.py":'import argparse\n\ndef create_parser():\n    p=argparse.ArgumentParser(prog="ueos")\n    p.add_argument("system",nargs="?")\n    p.add_argument("command",nargs="?")\n    p.add_argument("arguments",nargs="*")\n    return p\n',
"dispatcher.py":'"""Dispatcher."""\n',
"registry.py":'"""Registry."""\n',
"help.py":'"""Help."""\n',
"output.py":'"""Output."""\n',
"errors.py":'class UEOSCLIError(Exception):\n    pass\n'
}

ROUTER = '"""\nUEOS Constitutional Router\n"""\n\nfrom bip_eos.cli.framework.parser import create_parser\n\ndef main():\n    parser = create_parser()\n    args = parser.parse_args()\n\n    if not args.system:\n        print("UEOS Constitutional CLI")\n        print("Systems:")\n        for s in ("audit","registry","graph","compiler","publish","knowledge","academy","runtime"):\n            print(" -", s)\n        return\n\n    print(f"System  : {args.system}")\n    print(f"Command : {args.command}")\n    print(f"Args    : {args.arguments}")\n\nif __name__ == "__main__":\n    main()\n'

def write(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    if not path.exists():
        path.write_text(text,encoding="utf-8")
        print("[CREATE]",path)
    else:
        print("[EXISTS]",path)

root=Path.cwd()
cli=root/"src"/"bip_eos"/"cli"
fw=cli/"framework"

for n,t in FRAMEWORK.items():
    write(fw/n,t)

write(cli/"ueos.py",ROUTER)
write(cli/"__init__.py",'"""UEOS CLI"""\n')

for s in SYSTEMS:
    d=cli/s
    write(d/"__init__.py",f'"""{s.title()} CLI."""\n')
    write(d/"commands.py",f'"""{s.title()} commands."""\n')

print("UEOS CLI bootstrap complete.")
