# C02 – Scanner

**Module:** EOS Compiler Front-End

**Status:** Draft

---

# Purpose

The Scanner is the first executable phase of the EOS Compiler.

Its responsibility is to discover engineering source files and produce
normalized `SourceFile` objects for downstream compiler phases.

---

# Inputs

- Repository Root
- Directory
- Single Engineering File

---

# Outputs

```python
Iterable[SourceFile]
```

Each SourceFile contains:

- Path
- File Name
- Extension
- UTF-8 Text
- File Size

---

# Supported Extensions

- .md
- .adr
- .yaml
- .yml
- .json
- .bip

Additional extensions may be registered by plugins.

---

# Responsibilities

- Traverse directories
- Discover engineering artifacts
- Ignore unsupported files
- Normalize UTF-8 encoding
- Preserve source paths
- Produce immutable SourceFile objects

---

# Non-Responsibilities

The Scanner SHALL NOT:

- Tokenize
- Parse
- Validate
- Interpret semantics
- Build an AST

These belong to later compiler phases.

---

# Processing Pipeline

Repository

↓

Scanner

↓

SourceFile[]

↓

Lexer

---

# Design Principles

- Deterministic
- Streaming-friendly
- Platform independent
- Stateless
- Read-only

---

# Future Enhancements

- .gitignore awareness
- compilerignore support
- Incremental scanning
- Parallel directory traversal
- Plugin discovery

---

# Dependencies

- pathlib
- SourceFile
- Position
- Span

---

# Success Criteria

The Scanner successfully discovers all supported engineering artifacts
and returns a complete collection of SourceFile objects without modifying
repository contents.
