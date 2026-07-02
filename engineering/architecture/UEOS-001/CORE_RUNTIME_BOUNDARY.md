# CORE / RUNTIME BOUNDARY

## ueos.core (Platform Infrastructure)

- kernel
- configuration
- dependency_injection
- event_bus
- lifecycle
- platform
- service_registry

## ueos.runtime (Runtime Services)

- diagnostics
- health
- logging
- plugins
- registry
- scheduler
- security
- service_host
- telemetry
- version

## Dependency Rule

Allowed:
runtime --> core

Forbidden:
core --> runtime
