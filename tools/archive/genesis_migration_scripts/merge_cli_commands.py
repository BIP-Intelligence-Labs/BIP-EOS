"""
merge_cli_commands.py

Safely merge the new CLI infrastructure with the existing UEOS CLI.
Run from the repository root:

    python merge_cli_commands.py
"""

from pathlib import Path
import shutil
from datetime import datetime

ROOT = Path.cwd()
CLI = ROOT / "src" / "bip_eos" / "cli"
COMMANDS = CLI / "commands"

BACKUP = ROOT / ".backup" / datetime.now().strftime("%Y%m%d_%H%M%S")
BACKUP.mkdir(parents=True, exist_ok=True)

print("=" * 70)
print("UEOS CLI MERGE")
print("=" * 70)

for filename in ("command.py", "dispatcher.py", "shell.py"):
    src = CLI / filename
    if src.exists():
        shutil.copy2(src, BACKUP / filename)
        print(f"BACKUP : {filename}")

COMMANDS.mkdir(parents=True, exist_ok=True)

stubs = {
    "help.py": '''from ..command import Command

class HelpCommand(Command):
    name="help"
    description="Show available commands."
    aliases=["?"]

    def execute(self,args:list[str])->int:
        print("Use: doctor runtime graph registry compiler install ai")
        return 0
''',
    "version.py": '''from ..command import Command

class VersionCommand(Command):
    name="version"
    description="Display UEOS version."
    aliases=["ver"]

    def execute(self,args:list[str])->int:
        print("UEOS 0.1.0 Genesis")
        return 0
''',
    "exit.py": '''from ..command import Command

class ExitCommand(Command):
    name="exit"
    description="Exit UEOS."
    aliases=["quit"]

    def execute(self,args:list[str])->int:
        raise SystemExit(0)
'''
}

for filename, content in stubs.items():
    target = COMMANDS / filename
    if target.exists():
        print(f"KEEP   : commands/{filename}")
    else:
        target.write_text(content, encoding="utf-8")
        print(f"CREATE : commands/{filename}")

print("\nPreserved command modules:")
for py in sorted(COMMANDS.glob("*.py")):
    if py.name not in stubs:
        print("  ✓", py.name)

print("\nNext:")
print("1. Merge command.py")
print("2. Merge dispatcher.py")
print("3. Merge shell.py")
print("4. Register existing commands in the dispatcher")

print("\nDone.")
