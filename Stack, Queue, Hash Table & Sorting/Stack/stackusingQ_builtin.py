from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()  # Main queue
        self.queue2 = deque()  # Temporary queue

    def push(self, x):
        """Push element onto stack"""
        self.queue1.append(x)

    def pop(self):
        """Remove and return the top element"""
        if self.empty():
            return None
        # Move elements except last to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        top_element = self.queue1.popleft()  # Last element (stack top)
        # Swap queues
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element

    def top(self):
        """Return the top element without removing it"""
        if self.empty():
            return None
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        top_element = self.queue1[0]  # Get last element
        self.queue2.append(self.queue1.popleft())  # Move it to queue2
        # Swap queues
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element

    def empty(self):
        """Check if stack is empty"""
        return len(self.queue1) == 0

# Example Usage:
stack = StackUsingQueues()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.top())  # Output: 30
print(stack.pop())  # Output: 30
print(stack.pop())  # Output: 20
print(stack.empty())  # Output: False
print(stack.pop())  # Output: 10
print(stack.empty())  # Output: True
