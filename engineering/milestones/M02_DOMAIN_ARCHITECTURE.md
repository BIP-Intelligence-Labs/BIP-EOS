# M02 - Domain Architecture

Status: COMPLETE

## Objective

Establish a domain-driven architecture for the Builder Intelligence Platform.

## Completed

- Domain-driven package structure
- Lead domain
- Builder domain
- Community domain
- Inventory domain
- Questionnaire domain
- Recommendation domain
- Report domain
- Appointment domain

## Architecture

```
builders/
├── lead/
├── builder/
├── community/
├── inventory/
├── questionnaire/
├── recommendation/
├── report/
└── appointment/
```

## Design Principles

- Business capabilities own their models, services, repositories and APIs.
- New development belongs in `src/bip_eos/`.
- `src/genesis/` is read-only except for migration fixes.
- Cross-cutting concerns belong in `core/`, `config/`, or `shared/`.

## Exit Criteria

- [x] Domain structure created
- [x] Stub modules created
- [x] Governance documented
- [x] Configuration package established

## Next Milestone

M03 - Data Layer

Deliverables:
- Supabase client
- Database configuration
- Repository implementations
- Initial domain models
