class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1
    def dequeue(self):
        if self.front is None:
            return None
        if self.front.next is None:
            poped = self.front.value
            self.front = self.front.next
            self.length -= 1
            if self.front is None:
                self.rear = None
            return poped
        current = self.front
        self.front = current.next
        current.next = None
        self.length -= 1
        return current.value
    def print_queue(self):
        if self.front is None:
            return
        current = self.front
        print("Front", end=" ")
        while current:
            print(current.value, end=" <- ")
            current = current.next
        print("Rear")
        
        
que = Queue()
que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
que.enqueue(40)
que.print_queue()
if que.front:
    print("Front: ", que.front.value)
    print("Rear: ", que.rear.value)
print("Length: ", que.length)
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()
que.print_queue()
if que.front:
    print("Front: ", que.front.value)
    print("Rear: ", que.rear.value)
else:
    print("Everything is poped!")
print("Length: ", que.length)
    