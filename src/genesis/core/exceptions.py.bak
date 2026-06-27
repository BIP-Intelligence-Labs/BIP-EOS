
\"\"\"Genesis Core Exceptions\"\"\"

class GenesisError(Exception):
    \"\"\"Base exception for all Genesis errors.\"\"\"

class ConfigurationError(GenesisError):
    pass

class ContextError(GenesisError):
    pass

class ManifestError(GenesisError):
    pass

class FilesystemError(GenesisError):
    pass

class ValidationError(GenesisError):
    pass

class VerificationError(GenesisError):
    pass

class TemplateError(GenesisError):
    pass

class EngineError(GenesisError):
    pass

class BuildError(GenesisError):
    pass

class CLIError(GenesisError):
    pass

EXCEPTION_REGISTRY = {
    "configuration": ConfigurationError,
    "context": ContextError,
    "manifest": ManifestError,
    "filesystem": FilesystemError,
    "validation": ValidationError,
    "verification": VerificationError,
    "template": TemplateError,
    "engine": EngineError,
    "build": BuildError,
    "cli": CLIError,
}
