
"""
bootstrap_bootstrap_framework.py
Creates the canonical Bootstrap Engineering Framework.
"""
from pathlib import Path

ROOT = Path.cwd()

dirs = [
"bootstrap/common",
"bootstrap/compiler/common","bootstrap/compiler/templates",
"bootstrap/compiler/c01","bootstrap/compiler/c02","bootstrap/compiler/c03","bootstrap/compiler/c04","bootstrap/compiler/c05","bootstrap/compiler/c06","bootstrap/compiler/c07","bootstrap/compiler/c08","bootstrap/compiler/c09","bootstrap/compiler/c10",
"bootstrap/academy/common","bootstrap/academy/templates",
"bootstrap/engineering/common","bootstrap/engineering/templates",
"bootstrap/repository/common","bootstrap/repository/templates",
"bootstrap/plugins","bootstrap/reports"
]

files = {
"bootstrap/__init__.py": '"""BIP EOS Bootstrap Framework."""\n',
"bootstrap/__main__.py": 'from .bootstrap import main\n\nif __name__=="__main__":\n    main()\n',
"bootstrap/bootstrap.py": 'def main():\n    print("BIP EOS Bootstrap Framework")\n',
"bootstrap/common/console.py": '"""Console."""\n',
"bootstrap/common/filesystem.py": '"""Filesystem."""\n',
"bootstrap/common/generator.py": '"""Generator."""\n',
"bootstrap/common/manifest.py": '"""Manifest."""\n',
"bootstrap/common/report.py": '"""Report."""\n',
"bootstrap/common/template_engine.py": '"""Templates."""\n',
"bootstrap/common/verification.py": '"""Verification."""\n',
"bootstrap/common/renderer.py": '"""Renderer."""\n',
"bootstrap/common/registry.py": '"""Registry."""\n',
"bootstrap/common/utils.py": '"""Utils."""\n',
"bootstrap/compiler/bootstrap.py": '"""Compiler Bootstrap."""\n',
"bootstrap/compiler/common/compiler_generator.py": '"""Compiler Generator."""\n',
"bootstrap/compiler/common/compiler_manifest.py": '"""Compiler Manifest."""\n',
"bootstrap/compiler/common/compiler_report.py": '"""Compiler Report."""\n',
"bootstrap/compiler/common/compiler_verification.py": '"""Compiler Verification."""\n',
"bootstrap/compiler/templates/token.py.j2": "# token\n",
"bootstrap/compiler/templates/token_type.py.j2": "# token type\n",
"bootstrap/compiler/templates/keywords.py.j2": "# keywords\n",
"bootstrap/compiler/templates/specification.md.j2": "# specification\n",
"bootstrap/compiler/templates/report.md.j2": "# report\n",
"bootstrap/compiler/templates/test.py.j2": "# test\n",
"bootstrap/academy/bootstrap.py": '"""Academy Bootstrap."""\n',
"bootstrap/engineering/bootstrap.py": '"""Engineering Bootstrap."""\n',
"bootstrap/repository/bootstrap.py": '"""Repository Bootstrap."""\n',
"bootstrap/plugins/compiler.py": '"""Compiler plugin."""\n',
"bootstrap/plugins/academy.py": '"""Academy plugin."""\n',
"bootstrap/plugins/engineering.py": '"""Engineering plugin."""\n',
"bootstrap/plugins/repository.py": '"""Repository plugin."""\n',
}

for d in dirs:
    (ROOT/d).mkdir(parents=True, exist_ok=True)
for rel, content in files.items():
    p=ROOT/rel
    p.parent.mkdir(parents=True, exist_ok=True)
    if not p.exists():
        p.write_text(content, encoding="utf-8")
print("Bootstrap framework created.")
