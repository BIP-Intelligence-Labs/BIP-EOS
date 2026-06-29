
# Bootstrap Development Standards

## Repository Generation

Use explicit file maps.

```python
FILES = {
    "README.md": "...",
    "version.py": "...",
}
```

Use explicit directory maps.

```python
DIRECTORIES = [
    "compiler/frontend",
]
```

Bootstrap scripts shall be deterministic, idempotent, and safe to run
multiple times.
