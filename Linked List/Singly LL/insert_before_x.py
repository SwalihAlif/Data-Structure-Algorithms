class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=' -> ')
            temp = temp.next
        print(None)
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def insert_before(self, x, value):
        if self.length == 0:
            print("The list is empty")
            return
    
        if self.head.value == x:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return
        temp = self.head
        prev = None
        while temp and temp.value != x:
            prev = temp
            temp = temp.next
        if not temp:
            print('No such value in list')
            return
        new_node = Node(value)
        prev.next = new_node
        new_node.next = temp
        self.length += 1
        return
        
        
    
my_ll = LinkedList(1)
my_ll.append(2)
my_ll.append(3)
my_ll.append(4)
my_ll.append(5)
my_ll.print_list()
my_ll.insert_before(3, 7)
my_ll.print_list()