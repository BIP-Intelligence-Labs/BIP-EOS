"""Genesis EEOS Exception Framework."""

class GenesisError(Exception):
    """Base exception for all Genesis errors."""


class EngineError(GenesisError):
    """Raised for engine-related failures."""


class RepositoryError(EngineError):
    """Raised for repository engine failures."""


class ValidationError(GenesisError):
    """Raised when validation fails."""


class ConfigurationError(GenesisError):
    """Raised for configuration errors."""
