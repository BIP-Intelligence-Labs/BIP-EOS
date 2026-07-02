class EventBusEngine:
    def publish(self, event):
        raise NotImplementedError

    def subscribe(self, topic, handler):
        raise NotImplementedError
