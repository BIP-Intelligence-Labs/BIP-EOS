"""
normalize_cli_facades.py
"""

from pathlib import Path

ROOT = Path.cwd()
CLI = ROOT / "src" / "bip_eos" / "cli"

TARGETS = ["graph","runtime","registry","compiler"]

INIT='"""Package."""\n'

for name in TARGETS:
    pkg=CLI/name
    pkg.mkdir(exist_ok=True)

    for sub in ("services","models"):
        d=pkg/sub
        d.mkdir(exist_ok=True)
        i=d/"__init__.py"
        if not i.exists():
            i.write_text(INIT,encoding="utf-8")

    i=pkg/"__init__.py"
    if not i.exists():
        i.write_text(INIT,encoding="utf-8")

    e=pkg/"engine.py"
    if not e.exists():
        e.write_text(
            '"""\\n{} subsystem engine.\\n"""\\n\\ndef main() -> int:\\n    print("{} subsystem started.")\\n    return 0\\n'.format(name.capitalize(),name.capitalize()).replace('\\n','\n'),
            encoding="utf-8"
        )

    facade=CLI/f"{name}.py"
    content=('"""\nCLI facade for the {0} subsystem.\n"""\n\n'
             'from bip_eos.cli.{0}.engine import main\n\n'
             'if __name__ == "__main__":\n'
             '    raise SystemExit(main())\n').format(name)

    if facade.exists():
        try:
            existing=facade.read_text(encoding="utf-8")
        except Exception:
            existing=""
        if len(existing.splitlines())<40:
            facade.write_text(content,encoding="utf-8")
            print("Updated:",facade.relative_to(ROOT))
        else:
            print("Skipped:",facade.relative_to(ROOT))
    else:
        facade.write_text(content,encoding="utf-8")
        print("Created:",facade.relative_to(ROOT))

print("Done.")
