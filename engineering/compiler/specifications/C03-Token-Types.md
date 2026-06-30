# C03 – Token Types

**Module:** EOS Compiler Front-End

**Status:** Draft

---

# Purpose

Define the canonical token types produced by the Lexer.
Tokens are the fundamental units consumed by the Parser.

---

# Token Structure

```python
Token(
    type,
    value,
    span,
)
```

---

# Identifier Tokens

- IDENTIFIER
- KEYWORD

---

# Literal Tokens

- STRING
- INTEGER
- FLOAT
- BOOLEAN
- NULL

---

# Delimiters

- LPAREN
- RPAREN
- LBRACE
- RBRACE
- LBRACKET
- RBRACKET

---

# Punctuation

- COMMA
- COLON
- SEMICOLON
- DOT

---

# Operators

- EQUALS
- ARROW

---

# Layout

- NEWLINE
- INDENT
- DEDENT

---

# Special

- EOF
- ERROR

---

# Responsibilities

- Provide a stable token vocabulary
- Remain independent of parsing
- Support deterministic compilation

---

# Non-Responsibilities

Token Types SHALL NOT:

- Scan files
- Read characters
- Parse syntax
- Build AST nodes

---

# Processing Pipeline

Characters

↓

Lexer

↓

Token Stream

↓

Parser

---

# Design Principles

- Immutable
- Strongly typed
- Language agnostic
- Extensible

---

# Future Enhancements

- Plugin-defined token types
- Compiler directives
- Engineering annotations

---

# Success Criteria

Every lexical element recognized by the Lexer maps to exactly one
well-defined Token Type.
