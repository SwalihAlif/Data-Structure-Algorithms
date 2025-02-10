class Node:
    """Node class for Stack"""
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """Stack implementation using a linked list"""
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, value):
        """Push element onto stack"""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self):
        """Pop and return the top element"""
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        self.length -= 1
        return temp.value

    def peek(self):
        """Return the top element without removing it"""
        if self.top is None:
            return None
        return self.top.value

    def is_empty(self):
        """Check if the stack is empty"""
        return self.top is None

    def size(self):
        """Return the size of the stack"""
        return self.length


class QueueUsingStacks:
    """Queue implementation using two stacks"""
    def __init__(self):
        self.stack1 = Stack()  # Main stack for enqueue
        self.stack2 = Stack()  # Temporary stack for dequeue

    def enqueue(self, value):
        """Enqueue element into the queue"""
        self.stack1.push(value)

    def dequeue(self):
        """Dequeue the front element"""
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()  # Pop from stack2 (FIFO order)

    def peek(self):
        """Return the front element without removing it"""
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.peek()  # Peek from stack2

    def is_empty(self):
        """Check if the queue is empty"""
        return self.stack1.is_empty() and self.stack2.is_empty()


# Example Usage:
queue = QueueUsingStacks()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.peek())  # Output: 10
print(queue.dequeue())  # Output: 10
print(queue.dequeue())  # Output: 20
print(queue.is_empty())  # Output: False
print(queue.dequeue())  # Output: 30
print(queue.is_empty())  # Output: True


# Time Complexity
# Enqueue: O(1) → Direct push to stack1.
# Dequeue: O(N) → Moves all elements to stack2 only when empty.
# Peek: O(N) → Similar to dequeue, but does not remove the element.
# Empty: O(1)