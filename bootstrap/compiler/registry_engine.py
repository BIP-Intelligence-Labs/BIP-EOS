""Engineering Registry Engine.""

from registry.registry import EngineeringRegistry

class RegistryEngine:

    def build(self, repository):
        registry = EngineeringRegistry()
        for document in repository.documents:
            registry.documents[str(document.relative_path)] = document
        return registry
