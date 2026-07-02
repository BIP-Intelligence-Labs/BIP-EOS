class Kernel:
    """UEOS kernel."""

    def boot(self):
        raise NotImplementedError

    def shutdown(self):
        raise NotImplementedError
