class ContainerEngine:
    def register(self, name, service):
        raise NotImplementedError

    def resolve(self, name):
        raise NotImplementedError
