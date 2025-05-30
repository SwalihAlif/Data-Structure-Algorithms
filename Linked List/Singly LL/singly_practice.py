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

    def pop(self):
        if self.length == 0: 
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None 
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    def insert_after(self, prev_node_value, value):
        current = self.head
        while current and current.value != prev_node_value:
            current = current.next
            
            if current is None:
                print("Cant find prev node")
                return None
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node
        return True
    def insert_before_node(self, target_value, value):
        if self.head is None:
            return None
        new_node = Node(value)
        if self.head.value == target_value:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return True
        
        prev = self.head
        while prev.next and prev.next.value != target_value:
            prev = prev.next
        if not prev.next:
            print("Couldn't find")
            return None
        
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True







my_ll = LinkedList(5)
my_ll.append(6)
my_ll.append(7)
my_ll.append(8)
my_ll.append(9)
my_ll.print_list()
my_ll.pop()
my_ll.print_list()
my_ll.pop()
my_ll.print_list()
my_ll.prepend(4)
my_ll.print_list()
my_ll.prepend(3)
my_ll.print_list()
my_ll.insert(2, 69)
my_ll.print_list()
my_ll.insert_before_node(5, 70)
my_ll.print_list()

