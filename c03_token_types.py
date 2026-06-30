"""
bootstrap/compiler/docs/c03_token_types.py

Generates:
engineering/compiler/specifications/C03-Token-Types.md
"""

from pathlib import Path
from textwrap import dedent

ROOT = Path.cwd()
TARGET = ROOT / "engineering" / "compiler" / "specifications" / "C03-Token-Types.md"

CONTENT = dedent("""
# C03 – Token Types

**Module:** EOS Compiler Front-End

**Status:** Engineering Specification

---

## Purpose

Token Types define the canonical vocabulary emitted by the Lexer and
consumed by the Parser.

---

## Token Structure

```python
Token(
    type,
    value,
    span,
)
```

---

## Categories

### Identifiers
- IDENTIFIER
- KEYWORD

### Literals
- STRING
- INTEGER
- FLOAT
- BOOLEAN
- NULL

### Delimiters
- LPAREN
- RPAREN
- LBRACE
- RBRACE
- LBRACKET
- RBRACKET

### Punctuation
- COMMA
- COLON
- SEMICOLON
- DOT

### Operators
- EQUALS
- ARROW

### Layout
- NEWLINE
- INDENT
- DEDENT

### Special
- EOF
- ERROR

---

## Responsibilities

- Define compiler token vocabulary
- Remain parser-independent
- Support deterministic compilation

---

## Non-Responsibilities

- Scan files
- Parse syntax
- Build AST nodes

---

## Pipeline

Characters

↓

Lexer

↓

Token Stream

↓

Parser

---

## Success Criteria

Every lexical element maps to one and only one Token Type.
""").strip() + "\n"

print("=" * 60)
print("BIP EOS Bootstrap")
print("=" * 60)
print("Engineering Specification")
print("Specification : C03 Token Types")
print()

TARGET.parent.mkdir(parents=True, exist_ok=True)

if TARGET.exists():
    print("Status        : Already Exists")
else:
    TARGET.write_text(CONTENT, encoding="utf-8")
    print("Status        : Created")

print(f"Location      : {TARGET}")
