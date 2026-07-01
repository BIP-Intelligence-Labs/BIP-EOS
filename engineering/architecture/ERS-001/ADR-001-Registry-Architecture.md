# ADR-001 — ERS-001 Registry Architecture

## Status
Accepted

## Decision

ERS-001 SHALL be implemented as an orchestration engine with dedicated
constitutional services.

RegistryEngine
    ├── IdentityResolver
    ├── RegistryStore
    ├── RegistryValidator
    ├── RegistrySerializer
    └── RegistryIndex

## Rationale

- Single Responsibility Principle
- Stable constitutional identities
- Storage independence
- Extensible architecture
- Reusable engineering services
