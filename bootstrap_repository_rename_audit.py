"""
Repository Rename Readiness Audit

Checks for references to the current repository folder name ("genesis")
before renaming:

C:\Project\BIP-Intelligence-Labs\genesis
            ↓
C:\Project\BIP-Intelligence-Labs\BIP-EOS

The script is read-only. It does not rename anything.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
OLD_NAME = "genesis"

IGNORE_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "build",
    "dist",
    "node_modules",
}

EXTENSIONS = {
    ".py",".md",".txt",".toml",".yaml",".yml",".json",
    ".ini",".cfg",".ps1",".bat",".cmd",".sh",".xml",
    ".code-workspace",".sln",".csproj",".gitignore"
}

print("="*70)
print("BIP EOS Repository Rename Readiness Audit")
print("="*70)

hits = []

# VS Code / IDE files
for pattern in ("*.code-workspace", ".vscode/*", ".idea/*"):
    pass

for p in ROOT.rglob("*"):
    rel = p.relative_to(ROOT)

    if any(part in IGNORE_DIRS for part in rel.parts):
        continue

    if p.is_file():
        # Check filenames
        if OLD_NAME.lower() in p.name.lower():
            hits.append((str(rel), "filename"))

        # Check text files
        if p.suffix.lower() in EXTENSIONS or p.name.startswith("."):
            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            if str(ROOT) in text:
                hits.append((str(rel), "absolute repository path"))

            if OLD_NAME in text:
                hits.append((str(rel), 'contains "genesis"'))

print()

if not hits:
    print("PASS")
    print()
    print("No repository-path references were found.")
    print()
    print("Repository appears safe to rename.")
    print()
    print("Suggested:")
    print(r"Rename:")
    print(r"C:\Project\BIP-Intelligence-Labs\genesis")
    print(r"to")
    print(r"C:\Project\BIP-Intelligence-Labs\BIP-EOS")
else:
    print(f"Found {len(hits)} possible references:\n")
    for file, reason in sorted(hits):
        print(f"[CHECK] {file}")
        print(f"        {reason}")
    print("\nReview these before renaming.")

print("="*70)
