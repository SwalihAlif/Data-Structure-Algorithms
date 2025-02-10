class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    """Queue implementation using a linked list"""
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, value):
        """Add an element to the queue"""
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1

    def dequeue(self):
        """Remove and return the front element of the queue"""
        if self.front is None:
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.length -= 1
        return temp.value

    def is_empty(self):
        """Check if the queue is empty"""
        return self.front is None

    def size(self):
        """Return the size of the queue"""
        return self.length

class StackUsingQueues:
    """Stack implementation using two queues with linked lists"""
    def __init__(self):
        self.queue1 = Queue()  # Main queue
        self.queue2 = Queue()  # Temporary queue

    def push(self, value):
        """Push element onto stack"""
        self.queue1.enqueue(value)

    def pop(self):
        """Remove and return the top element"""
        if self.queue1.is_empty():
            return None

        # Move all elements except the last one to queue2
        while self.queue1.size() > 1:
            self.queue2.enqueue(self.queue1.dequeue())

        top_element = self.queue1.dequeue()  # Last element (top of stack)

        # Swap queues
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element

    def top(self):
        """Return the top element without removing it"""
        if self.queue1.is_empty():
            return None
        
        while self.queue1.size() > 1:
            self.queue2.enqueue(self.queue1.dequeue())

        top_element = self.queue1.front.value  # Get last element

        self.queue2.enqueue(self.queue1.dequeue())  # Move it to queue2

        # Swap queues
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element

    def is_empty(self):
        """Check if the stack is empty"""
        return self.queue1.is_empty()

# Example Usage:
stack = StackUsingQueues()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.top())  # Output: 30
print(stack.pop())  # Output: 30
print(stack.pop())  # Output: 20
print(stack.is_empty())  # Output: False
print(stack.pop())  # Output: 10
print(stack.is_empty())  # Output: True



# Stack using Queues (Implemented with Linked List)
# Instead of using Python’s built-in deque, we'll implement queues using a linked list, and then use two queues to simulate a stack.

# Approach:
# Queue implementation using a Linked List
# Stack using two Queues:
# push(x) → Enqueue to queue1.
# pop() → Move all elements except the last one to queue2, remove the last element, then swap queues.
# top() → Same as pop(), but return the last element instead of removing it.
# empty() → Check if queue1 is empty.
# Implementation
# python
# Copy
# Edit


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    """Queue implementation using a linked list"""
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, value):
        """Add an element to the queue"""
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1

    def dequeue(self):
        """Remove and return the front element of the queue"""
        if self.front is None:
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.length -= 1
        return temp.value

    def is_empty(self):
        """Check if the queue is empty"""
        return self.front is None

    def size(self):
        """Return the size of the queue"""
        return self.length

class StackUsingQueues:
    """Stack implementation using two queues with linked lists"""
    def __init__(self):
        self.queue1 = Queue()  # Main queue
        self.queue2 = Queue()  # Temporary queue

    def push(self, value):
        """Push element onto stack"""
        self.queue1.enqueue(value)

    def pop(self):
        """Remove and return the top element"""
        if self.queue1.is_empty():
            return None

        # Move all elements except the last one to queue2
        while self.queue1.size() > 1:
            self.queue2.enqueue(self.queue1.dequeue())

        top_element = self.queue1.dequeue()  # Last element (top of stack)

        # Swap queues
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element

    def top(self):
        """Return the top element without removing it"""
        if self.queue1.is_empty():
            return None
        
        while self.queue1.size() > 1:
            self.queue2.enqueue(self.queue1.dequeue())

        top_element = self.queue1.front.value  # Get last element

        self.queue2.enqueue(self.queue1.dequeue())  # Move it to queue2

        # Swap queues
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element

    def is_empty(self):
        """Check if the stack is empty"""
        return self.queue1.is_empty()

# Example Usage:
stack = StackUsingQueues()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.top())  # Output: 30
print(stack.pop())  # Output: 30
print(stack.pop())  # Output: 20
print(stack.is_empty())  # Output: False
print(stack.pop())  # Output: 10
print(stack.is_empty())  # Output: True


# Time Complexity
# Push: O(1) (direct enqueue)
# Pop: O(N) (moving elements to another queue)
# Top: O(N) (similar to pop but element is reinserted)
# Empty: O(1)