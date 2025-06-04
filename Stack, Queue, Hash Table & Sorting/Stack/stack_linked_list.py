class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
        self.height = 0
        
    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    def pop(self):
        if self.top is None:
            return None
        if self.top.next is None:
            poped = self.top.value
            self.top = None
            self.height -= 1
            return poped
        current = self.top
        self.top = self.top.next
        self.height -= 1
        return current.value
        
    def print_stack(self):
        if self.top is None:
            return 
        current = self.top
        print("(Top)")
        while current:
            print(current.value)
            if current.next:
                print("↓")
            current = current.next
        print("(Bottom)")
        
stk = Stack()
stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)
stk.print_stack()
stk.pop()
stk.pop()
stk.pop()
stk.pop()
stk.pop()
stk.print_stack()