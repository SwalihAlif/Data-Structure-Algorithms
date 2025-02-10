class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        if self.length == 0:
            print("Queue is empty.")
            return
        temp = self.first
        print("First -> ", end='')
        while temp is not None:
            print(temp.value, end='')
            if temp.next:
                print(" → ", end='')
            temp = temp.next
        print(" -> Last")


    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp.value
    
my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()        
my_queue.dequeue()
my_queue.print_queue()
my_queue.dequeue()
my_queue.print_queue()        
my_queue.dequeue()
my_queue.print_queue()
            

