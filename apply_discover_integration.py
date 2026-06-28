"""
apply_discover_integration.py

Applies the Bootstrap Discover integration automatically.
"""

from pathlib import Path

cli = Path("bootstrap/cli")
commands = cli / "commands.py"
bootstrap = cli / "bootstrap.py"

# Patch commands.py
text = commands.read_text(encoding="utf-8")

if "from .discover import DiscoverCommand" not in text:
    text = text.replace(
        "from .new import NewCommand",
        "from .new import NewCommand\nfrom .discover import DiscoverCommand",
    )

if "def discover(url: str)" not in text:
    marker = 'print("new_plugin(name)")'
    addition = (
        "\n    @staticmethod\n"
        "    def discover(url: str) -> None:\n"
        '        """Run the Universal Discovery Engine."""\n'
        "        DiscoverCommand().run(url)\n\n"
    )
    text = text.replace(marker, addition + marker)

commands.write_text(text, encoding="utf-8")
print("✓ Patched commands.py")

# Patch bootstrap.py
text = bootstrap.read_text(encoding="utf-8")

if 'sub.add_parser("discover")' not in text:
    text = text.replace(
        'sub.add_parser("root")',
        'sub.add_parser("root")\n\n    discover = sub.add_parser("discover")\n    discover.add_argument("url")'
    )

if 'case "discover":' not in text:
    text = text.replace(
        'case "root":',
        'case "discover":\n            Commands.discover(args.url)\n\n        case "root":'
    )

bootstrap.write_text(text, encoding="utf-8")
print("✓ Patched bootstrap.py")

print("\n🚀 Discover integration complete.")
