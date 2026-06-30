"""
bootstrap_sprint_04.py

Generates engineering/sprints/SPRINT_04.md
"""

from pathlib import Path

ROOT = Path.cwd()
TARGET = ROOT / "engineering" / "sprints" / "SPRINT_04.md"

DOCUMENT = """# Sprint 04 — Lexer & Parser

**Status:** Planned

## Objective

Implement the lexical analysis and parsing stages of the BIP EOS Compiler,
transforming engineering source files into a validated Abstract Syntax Tree (AST).

---

## Planned Deliverables

### Lexer

- Implement Token class
- Implement TokenType enumeration
- Implement keyword definitions
- Implement lexical analysis
- Produce deterministic token streams
- Report lexical diagnostics

### Parser

- Implement parser framework
- Parse token streams
- Construct AST nodes
- Recover from syntax errors
- Produce parser diagnostics

### Abstract Syntax Tree

- Define AST node hierarchy
- Implement root document node
- Implement statement nodes
- Implement expression nodes
- Preserve source spans

### Diagnostics

- Lexical error reporting
- Syntax error reporting
- Source position tracking
- Human-readable compiler messages

### Testing

- Lexer unit tests
- Parser unit tests
- AST construction tests
- Error recovery tests

---

## Engineering Goals

- Deterministic compilation
- Immutable compiler structures
- Full source traceability
- Comprehensive diagnostics
- Test-first implementation

---

## Success Criteria

- Source files tokenize successfully
- Token stream parses successfully
- AST generated for valid input
- Invalid input produces deterministic diagnostics
- Unit tests pass

---

## Expected Outcome

Sprint 04 completes the lexical and syntactic front-end of the BIP EOS Compiler,
providing the foundation for semantic analysis, validation, and code generation
in subsequent sprints.
"""

TARGET.parent.mkdir(parents=True, exist_ok=True)
TARGET.write_text(DOCUMENT, encoding="utf-8")

print("=" * 60)
print("BIP EOS Bootstrap")
print("=" * 60)
print("Generated:")
print(TARGET)
