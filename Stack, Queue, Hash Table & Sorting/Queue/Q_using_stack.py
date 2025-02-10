class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.top = new_node
            self.height = 1
        else:
            self.top = None
            self.height = 0
        
    def push(self, value):
        new_node = Node(value)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top  
        if self.height == 1:
            self.top = None
        else:
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp.value
        
    def peek(self):
        return self.top
        
    def is_empty(self):
        return self.height == 0
        
    def size(self):
        return self.height
    
    def print_stack(self):
        temp = self.top
        print('Top')
        while temp is not None:
            print(temp.value)
            if temp.next:
                print('↓')
            temp = temp.next
        print('Bottom')
        
class Queue_using_stacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        
    def enqueue(self, value):
        self.stack1.push(value)
        
    def dequeue(self):
        if self.stack1.is_empty():
            return None
        while self.stack1.size() > 1:
            self.stack2.push(self.stack1.pop())
            
        first_element = self.stack1.pop()
        
        self.stack1,self.stack2 = self.stack2,self.stack1,
        return first_element
        
    def is_empty(self):
        return self.stack1.is_empty()
        
        
    def print_queue(self):
        if self.stack1.is_empty():
            print('Stack is empty')
            return
        temp_stack = Stack()
        temp = self.stack1.top
        print('front')
        while temp:
            temp_stack.push(temp.value)
            temp = temp.next
            
            while not temp_stack.is_empty():
                print('↓')
                print(temp_stack.pop())
        print('rear')
        
        
ms = Stack()
ms.push(1)
ms.push(2)
ms.push(3)
ms.push(4)
ms.print_stack()
ms.pop()
ms.print_stack()

mqs = Queue_using_stacks()
mqs.enqueue(1)
mqs.enqueue(2)
mqs.enqueue(3)
mqs.enqueue(4)
mqs.print_queue()
print('deleted', mqs.dequeue())