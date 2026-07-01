# ADR-0010 — Graph Kernel Extraction

**Status:** Accepted

**Date:** 2026-07-01

---

# Context

The UEOS repository originally implemented generic graph functionality
inside the `engineering_graph` package. As the platform evolved, new
domains (AI, Logistics, Security, Knowledge, Supply Chain, and Real
Estate) were identified that also require graph capabilities.

Continuing to couple the graph engine to the Engineering Graph would
create unnecessary duplication and limit reuse.

---

# Decision

Extract the generic graph implementation into a reusable framework:

```text
src/bip_eos/graph/
```

The framework contains generic graph primitives including:

- Graph Kernel
- Node
- Edge
- Query Engine
- Traversal
- Serialization

The `engineering_graph` package becomes a domain-specific layer built
on top of the Graph Framework.

---

# Compatibility Strategy

To avoid breaking existing imports, compatibility wrappers remain in:

```text
src/bip_eos/engineering_graph/
```

Each wrapper re-exports the implementation from the Graph Framework.

Example:

```python
from bip_eos.graph.kernel.graph import *
```

The wrappers are temporary and will be removed after all internal
imports migrate to the new package structure.

---

# Target Architecture

```text
Graph Framework
│
├── kernel
├── node
├── edge
├── query
├── traversal
├── serialization
├── projection
├── persistence
├── validation
└── services
        │
        ▼
Engineering Graph
        │
        ▼
Future Domain Graphs
    • Knowledge Graph
    • AI Memory Graph
    • Logistics Graph
    • Supply Chain Graph
    • Security Graph
    • Enterprise Graph
    • Real Estate Graph
```

---

# Consequences

## Benefits

- Reusable graph infrastructure
- Clear separation of framework and domain logic
- Backward-compatible migration
- Simplified maintenance
- Foundation for future graph-based subsystems

## Trade-offs

- Temporary compatibility wrappers increase maintenance slightly.
- Imports must be migrated incrementally.
- A future cleanup sprint is required to remove wrappers.

---

# Migration Plan

Phase 1
- Extract Graph Framework
- Add compatibility wrappers

Phase 2
- Update repository imports
- Validate with regression tests

Phase 3
- Remove compatibility wrappers
- Freeze Graph API

---

# Validation

Repository Certification: PASS

Regression Test Suite:

- Compiler: PASS
- Engineering Graph: PASS
- Package Manager: PASS

Total Passing Tests: 58

---

# Decision Summary

The Graph Framework is the canonical implementation for all graph
capabilities within UEOS.

`engineering_graph` remains as a domain-specific specialization until
all code has migrated to the new framework.
