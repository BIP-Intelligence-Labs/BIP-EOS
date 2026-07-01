from pathlib import Path

content = """[project]
name = "ueos"
version = "0.1.0"
description = "Universal Engineering Operating System"
requires-python = ">=3.11"

[project.scripts]
ueos = "bip_eos.cli.ueos:main"
bip = "bip_eos.cli.ueos:main"

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
"""

path = Path("pyproject.toml")

if path.exists():
    backup = Path("pyproject.toml.bak")
    backup.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"[BACKUP ] {backup}")

path.write_text(content, encoding="utf-8")

print("[UPDATE ] pyproject.toml")
print("Done.")
