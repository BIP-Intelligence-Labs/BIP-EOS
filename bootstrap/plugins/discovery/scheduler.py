from collections import deque
class DiscoveryScheduler:
    def __init__(self):
        self.q=deque()
    def enqueue(self,url):
        self.q.append(type("Job",(),{"url":url})())
    def dequeue(self):
        return self.q.popleft() if self.q else None
