class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class Singly:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print(None)
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    def insert(self, position, value):
        if position < 0 or position > self.length:
            return False
        if position == 0:
            self.prepend(value)
            return True
        if position == self.length:
            self.append(value)
            return True
        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node = Node(value)
        new_node.next = current.next
        current = new_node
        if current.next is None:
            self.tail = new_node
        self.length += 1
        
def detect_linked_list_type(head):
    if head is None:
        return "Empty List"
    #checking for circularity
    is_circular = False
    slow = head
    fast = head
    while fast and getattr(fast, 'next', None):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            is_circular = True
            break
    #check if it's doubly
    is_doubly = True
    has_prev = hasattr(head, 'prev')
    if not has_prev:
        is_doubly = False
    else:
        current = head
        while current and current.next:
            if current.next.prev != current:
                is_doubly = False
                break
            current = current.next
    if is_doubly and is_circular:
        return "Doubly circular"
    elif is_circular:
        return "Circular"
    elif is_doubly:
        return "Doubly"
    else:
        return "Singly"


sll = Singly()
sll.append(40)
sll.append(50)
sll.append(60)
sll.append(70)
sll.append(80)
sll.print_list()
print("Head: ", sll.head.value)
print("Tail: ", sll.tail.value)
print("Length: ", sll.length)
sll.prepend(30)
sll.prepend(20)
sll.prepend(10)
sll.print_list()
print("Head: ", sll.head.value)
print("Tail: ", sll.tail.value)
print("Length: ", sll.length)
sll.insert(8, 90)
sll.print_list()
print("Head: ", sll.head.value)
print("Tail: ", sll.tail.value)
print("Length: ", sll.length)
result = detect_linked_list_type(sll.head)
print(result)