from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def __iter__(self):
        while len(self.queue) != 0:
            yield self.dequeue()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) != 0:
            return self.queue.pop()

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

for num in queue:
    print(num)
