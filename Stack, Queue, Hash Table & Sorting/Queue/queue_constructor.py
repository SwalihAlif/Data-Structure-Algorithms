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
        temp = self.first
        print("First -> ", end='')
        while temp is not None:
            print(temp.value, end='')
            if temp.next:
                print(" → ", end='')
            temp = temp.next
        print(" -> Last")

my_queue = Queue(5)
my_queue.print_queue()