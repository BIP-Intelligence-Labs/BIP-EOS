# Compiler Frontend

## Overview

The UEOS Compiler Frontend converts source code into structured program
representations that can be analyzed and processed by later compiler stages.

The frontend performs:

- Lexical analysis
- Parsing
- AST generation
- Semantic analysis
- Diagnostics

---

# Workflow

```
Source Code
    ↓
Lexer
    ↓
Tokens
    ↓
Parser
    ↓
AST
    ↓
Semantic Analysis
    ↓
Diagnostics
```

---

# CLI Commands

## Compile

```text
ueos compile <source>
```

Compile a source file.

## Lex

```text
ueos lex <source>
```

Display generated tokens.

## Parse

```text
ueos parse <source>
```

Display the parsed syntax tree.

## Diagnostics

```text
ueos diagnostics <source>
```

Display compiler diagnostics.

---

# Components

- Token
- TokenType
- Lexer
- Parser
- AST
- Symbol Table
- Semantic Analyzer
- Diagnostics

---

# Example

```text
ueos lex hello.ue
ueos parse hello.ue
ueos compile hello.ue
```

---

# Future Enhancements

- Optimizer
- Intermediate Representation (IR)
- Code Generation
- LLVM backend
- Native executable generation
- Language Server Protocol (LSP)
- Incremental compilation

---

For engineering details, refer to the Engineering Documentation for
Atlas M-006.6.
