"""
bootstrap_c03.py

BIP EOS Compiler
C03 — Token System Bootstrap

Generates the C03 compiler artifacts if they do not exist and verifies
the resulting repository layout.
"""

from pathlib import Path
import subprocess
import sys

ROOT = Path.cwd()

FILES = [
    "src/bip_eos/compiler/token_type.py",
    "src/bip_eos/compiler/token.py",
    "src/bip_eos/compiler/keywords.py",
    "tests/unit/test_token_type.py",
    "tests/unit/test_token.py",
]

SPEC = "engineering/compiler/specifications/C03-Token-System.md"
VERIFY = "bootstrap/compiler/c03/verify_c03.py"


def touch(path: Path, text: str = "") -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return "SKIP"
    path.write_text(text, encoding="utf-8")
    return "CREATE"


def main() -> int:
    print("=" * 60)
    print("BIP EOS")
    print("Compiler Bootstrap")
    print("=" * 60)
    print("Phase : C03")
    print("Title : Token System")
    print()

    created = 0

    spec = ROOT / SPEC
    status = touch(
        spec,
        "# C03 — Token System\n\n"
        "Canonical engineering specification for the compiler token system.\n",
    )
    print(f"[{status}] {SPEC}")
    created += status == "CREATE"

    for rel in FILES:
        status = touch(ROOT / rel)
        print(f"[{status}] {rel}")
        created += status == "CREATE"

    verify = ROOT / VERIFY
    if verify.exists():
        print("\nRunning verification...\n")
        result = subprocess.run([sys.executable, str(verify)])
        if result.returncode:
            print("\nVerification FAILED.")
            return result.returncode
    else:
        print(f"[WARN] Verification script not found: {VERIFY}")

    print("\n" + "-" * 60)
    print(f"Files created : {created}")
    print("Status        : SUCCESS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
