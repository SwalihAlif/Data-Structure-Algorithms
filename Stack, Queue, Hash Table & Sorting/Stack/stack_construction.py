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
            print("Stack is empty")
            return
        
        temp = self.top
        print("Top")
        while temp is not None:
            print(temp.value)
            if temp.next:
                print("↓") 
            temp = temp.next
        print("Bottom")

my_stack = Stack(4)
my_stack.print_stack()

    