# BIP EOS Development Rules

## Repository Rules

1. All NEW development goes into `src/bip_eos/`.
2. `src/genesis/` is READ-ONLY.
3. Changes to `src/genesis/` are allowed only for migration fixes, critical bug fixes, and compatibility shims.

## Production
- src/
- docs/
- tests/

## Developer Tooling
- bootstrap/
- engineering/
- tools/

## Runtime Assets
- logs/
- registry/
- reports/
- plugins/

## CLI Vision

bip bootstrap
bip doctor
bip audit
bip docs
bip migrate
bip registry
bip plugins
