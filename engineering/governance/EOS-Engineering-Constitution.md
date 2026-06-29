# EOS Engineering Constitution

## Article XII — Bootstrap Engineering

### Principle

Bootstrap scripts shall generate repository artifacts from explicit file
maps rather than embedded executable source blocks.

### Requirements

Bootstrap scripts shall:

- Use explicit `FILES` maps.
- Use explicit `DIRECTORIES` maps.
- Be deterministic.
- Be idempotent.
- Never overwrite existing engineering artifacts unless explicitly requested.
- Produce consistent execution logs.

Bootstrap scripts shall not:

- Generate executable Python through nested executable source blocks.
- Depend on fragile string concatenation.

### Engineering Philosophy

Engineering infrastructure is production software.
