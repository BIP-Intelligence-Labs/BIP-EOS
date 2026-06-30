"""
bootstrap_c03_report.py

Generates:
reports/compiler_c03_report.md
"""

from pathlib import Path
from datetime import datetime

ROOT = Path.cwd()

REPORT = ROOT / "reports" / "compiler_c03_report.md"
REPORT.parent.mkdir(parents=True, exist_ok=True)

CHECKS = [
    "src/bip_eos/compiler/token_type.py",
    "src/bip_eos/compiler/token.py",
    "src/bip_eos/compiler/keywords.py",
    "tests/unit/test_token_type.py",
    "tests/unit/test_token.py",
    "bootstrap/compiler/c03/verify_c03.py",
    "engineering/compiler/specifications/C03-Token-System.md",
]

status = []
passed = 0

for rel in CHECKS:
    ok = (ROOT / rel).exists()
    status.append((rel, ok))
    if ok:
        passed += 1

lines = [
    "# Compiler C03 Engineering Report",
    "",
    f"Generated: {datetime.now().isoformat(timespec='seconds')}",
    "",
    "## Phase",
    "",
    "- C03 — Token System",
    "",
    "## Verification",
    "",
]

for rel, ok in status:
    lines.append(f"- [{'x' if ok else ' '}] {rel}")

lines += [
    "",
    f"**Result:** {passed}/{len(CHECKS)} artifacts present.",
    "",
    "## Deliverables",
    "",
    "- TokenType",
    "- Token",
    "- Keyword Registry",
    "- Token Unit Tests",
    "- TokenType Unit Tests",
    "- Verification Script",
    "- Engineering Specification",
    "",
    "## Next Phase",
    "",
    "**C04 — Lexer**",
    "",
    "Build a production lexer that converts characters into immutable Token objects.",
]

REPORT.write_text("\n".join(lines), encoding="utf-8")

print("=" * 60)
print("BIP EOS")
print("=" * 60)
print("Engineering Report Generated")
print(REPORT)
