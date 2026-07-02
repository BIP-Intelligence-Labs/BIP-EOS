"""
M-006.7.1 — AI Kernel
UEOS AI Runtime Foundation

This module defines the public interface for the UEOS AI Kernel.
Provider implementations will be added separately.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(slots=True)
class AIRequest:
    prompt: str
    context: Optional[Dict[str, Any]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class AIResponse:
    content: str
    provider: str
    model: str
    tokens_input: int = 0
    tokens_output: int = 0
    latency_ms: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)


class AIProvider(ABC):
    """Abstract interface implemented by every AI provider."""

    name: str = "provider"

    @abstractmethod
    def ask(self, request: AIRequest) -> AIResponse:
        raise NotImplementedError

    @abstractmethod
    def health(self) -> bool:
        raise NotImplementedError


class AIKernel:
    """
    UEOS AI Kernel.

    Central entry point for every AI request.
    """

    def __init__(self) -> None:
        self._providers: Dict[str, AIProvider] = {}
        self._default_provider: Optional[str] = None

    def register_provider(self, provider: AIProvider, default: bool = False) -> None:
        self._providers[provider.name] = provider
        if default or self._default_provider is None:
            self._default_provider = provider.name

    def providers(self) -> List[str]:
        return sorted(self._providers.keys())

    def health(self) -> Dict[str, bool]:
        return {name: provider.health() for name, provider in self._providers.items()}

    def ask(
        self,
        prompt: str,
        *,
        context: Optional[Dict[str, Any]] = None,
        provider: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> AIResponse:
        if not self._providers:
            raise RuntimeError("No AI providers registered.")

        provider_name = provider or self._default_provider
        if provider_name is None or provider_name not in self._providers:
            raise RuntimeError(f"Unknown AI provider: {provider_name}")

        request = AIRequest(
            prompt=prompt,
            context=context,
            metadata=metadata or {},
        )

        return self._providers[provider_name].ask(request)


class MockProvider(AIProvider):
    """Simple provider used for testing the kernel."""

    name = "mock"

    def ask(self, request: AIRequest) -> AIResponse:
        return AIResponse(
            content=f"[MOCK] {request.prompt}",
            provider=self.name,
            model="mock-1",
        )

    def health(self) -> bool:
        return True


if __name__ == "__main__":
    kernel = AIKernel()
    kernel.register_provider(MockProvider(), default=True)

    response = kernel.ask(
        "Generate an ADR for the Graph Engine.",
        context={"repository": "genesis"},
    )

    print("=" * 60)
    print("UEOS AI Kernel")
    print("=" * 60)
    print("Providers :", kernel.providers())
    print("Response  :", response.content)
