class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def print_stack(self):
        if self.length == 0:
            print("The stack is empty.")
            return
        temp = self.top
        print("Top")
        while temp is not None:
            print(temp.value)
            if temp.next:
                print("↓")
            temp = temp.next
        print("Bottom")

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1 
        

my_stack = Stack(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)
my_stack.push(0)
my_stack.print_stack()