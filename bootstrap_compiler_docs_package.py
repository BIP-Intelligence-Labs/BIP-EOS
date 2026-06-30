
"""
bootstrap_compiler_docs_package.py

Creates the canonical BIP EOS compiler documentation bootstrap package:

bootstrap/
└── compiler/
    └── docs/
        ├── engine.py
        ├── bootstrap_all.py
        ├── c01_source_files.py
        ├── c02_scanner.py
        ├── c03_token_types.py
        ├── c04_lexer.py
        ├── c05_parser.py
        ├── c06_ast.py
        ├── c07_engineering_model.py
        ├── c08_validator.py
        ├── c09_emitters.py
        └── c10_runtime.py
"""

from pathlib import Path
from textwrap import dedent

ROOT = Path.cwd()
DOCS = ROOT / "bootstrap" / "compiler" / "docs"
DOCS.mkdir(parents=True, exist_ok=True)

(DOCS / "__init__.py").write_text(
    '"""BIP EOS Compiler Documentation Bootstrap."""\n',
    encoding="utf-8",
)

engine = dedent("""
from pathlib import Path

class SpecificationGenerator:

    def __init__(self, specification, title, content):
        self.specification = specification
        self.title = title
        self.content = content

    @property
    def target(self):
        return (
            Path.cwd()
            / "engineering"
            / "compiler"
            / "specifications"
            / f"{self.specification}.md"
        )

    def generate(self, overwrite=False):
        print("=" * 60)
        print("BIP EOS Bootstrap")
        print("=" * 60)
        print(f"Specification : {self.title}")
        print()

        self.target.parent.mkdir(parents=True, exist_ok=True)

        if self.target.exists() and not overwrite:
            print("Status        : Already Exists")
        else:
            self.target.write_text(self.content.strip() + "\\n", encoding="utf-8")
            print("Status        : Created")

        print(f"Location      : {self.target}")
""").strip() + "\n"

(DOCS / "engine.py").write_text(engine, encoding="utf-8")

phases = [
    ("c01_source_files.py","C01-Source-Files","C01 – Source Files"),
    ("c02_scanner.py","C02-Scanner","C02 – Scanner"),
    ("c03_token_types.py","C03-Token-Types","C03 – Token Types"),
    ("c04_lexer.py","C04-Lexer","C04 – Lexer"),
    ("c05_parser.py","C05-Parser","C05 – Parser"),
    ("c06_ast.py","C06-AST","C06 – AST"),
    ("c07_engineering_model.py","C07-Engineering-Model","C07 – Engineering Model"),
    ("c08_validator.py","C08-Validator","C08 – Validator"),
    ("c09_emitters.py","C09-Emitters","C09 – Emitters"),
    ("c10_runtime.py","C10-Runtime","C10 – Runtime"),
]

template = """from textwrap import dedent
from engine import SpecificationGenerator

CONTENT = dedent(\"\"\"
# {title}

**Module:** EOS Compiler

**Status:** Engineering Specification

## Purpose

TODO: Complete specification.
\"\"\")

SpecificationGenerator(
    specification="{spec}",
    title="{title}",
    content=CONTENT,
).generate()
"""

for filename, spec, title in phases:
    (DOCS / filename).write_text(
        template.format(spec=spec, title=title),
        encoding="utf-8",
    )

bootstrap_all = dedent("""
import runpy
from pathlib import Path

HERE = Path(__file__).parent

for script in sorted(HERE.glob("c*.py")):
    print("\\n" + "=" * 72)
    print(f"Running {script.name}")
    print("=" * 72)
    runpy.run_path(str(script))
""").strip() + "\n"

(DOCS / "bootstrap_all.py").write_text(bootstrap_all, encoding="utf-8")

print("=" * 60)
print("BIP EOS")
print("=" * 60)
print("Created:")
print(DOCS)
