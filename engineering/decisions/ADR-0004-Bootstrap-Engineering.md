# ADR-0004 Bootstrap Engineering

## Status

Accepted

## Decision

EOS bootstrap scripts shall generate repository artifacts using explicit
file maps instead of embedded executable source blocks.

## Consequences

- Deterministic output
- Easier maintenance
- Easier review
- Fewer quoting/escaping errors
- Consistent engineering pattern
