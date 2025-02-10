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
    
    def sort(self):
        if not self.head or not self.head.next:
            return
        
        end = None
        while end != self.head:
            temp = self.head
            while temp.next != end:
                if temp.value > temp.next.value:
                    temp.value, temp.next.value = temp.next.value, temp.value
                temp = temp.next
            end = temp

    def remove_duplicates(self):
        temp = self.head
        while temp.next:
            if temp.value == temp.next.value:
                temp.next = temp.next.next
                self.length -= 1
            else:
                temp = temp.next

    
my_ll = LinkedList(2)
my_ll.append(4)
my_ll.append(1)
my_ll.append(5)
my_ll.append(1)
my_ll.append(5)
my_ll.append(3)
my_ll.print_list()
my_ll.sort()
my_ll.print_list()
my_ll.remove_duplicates()
my_ll.print_list()