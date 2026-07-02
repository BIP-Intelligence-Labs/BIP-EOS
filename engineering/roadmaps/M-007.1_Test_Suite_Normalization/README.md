# M-007.1 Test Suite Normalization

Objectives

- Exclude roadmap tests from the default pytest run.
- Exclude migration scaffold tests.
- Use package imports in kernel tests.
- Keep only production tests in the default collection.

Kernel import example

Replace:

    from runtime_state_machine import RuntimeState

With:

    from ueos.core.kernel.runtime_state_machine import RuntimeState
