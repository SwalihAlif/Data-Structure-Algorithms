class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        print(None, end=' <-> ')
        while temp is not None:
            print(temp.value, end= ' <-> ')
            temp = temp.next
        print(None)
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
        
    5
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else: 
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value
    2
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    3   
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp.value
    6
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
                
        return temp
        
    5
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        
    4
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
            
        new_node = Node(value)
        before = self.get(index -1)
        after = before.next
        
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1
        return True
        
    4
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
            
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        
        temp.next = None
        temp.prev = None
        self.length -= 1
        return True
    
            
        

my_dll = DoublyLL(5)
my_dll.append(5)
my_dll.append(24)
my_dll.append(7)
my_dll.append(9)
my_dll.print_list()
print(my_dll.pop())
my_dll.print_list()
my_dll.prepend(10)
my_dll.print_list()
print(my_dll.pop_first())
my_dll.print_list()
print(my_dll.get(2))
my_dll.set_value(3, 11)
my_dll.print_list()
my_dll.insert(0, 100)
my_dll.print_list()
my_dll.insert(2, 200)
my_dll.print_list()
my_dll.insert(6, 300)
my_dll.print_list()
my_dll.remove(1)
my_dll.print_list()