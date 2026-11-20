from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def __iter__(self):
        while len(self.stack) != 0:
            yield self.dequeue()

    def enqueue(self, value):
        self.stack.append(value)

    def dequeue(self):
        if len(self.stack) != 0:
            return self.stack.pop()

stack = Stack()
stack.enqueue(1)
stack.enqueue(2)
stack.enqueue(3)

for num in stack:
    print(num)
