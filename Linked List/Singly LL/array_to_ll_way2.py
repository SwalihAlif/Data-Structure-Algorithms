class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def array_to_ll(arr):
    if not arr:
        return None

    head = tail = None
    for elem in arr:
        new_node = Node(elem)
        if head is None:
            head = tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

def print_list(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print(None)

arr = [1, 2, 3, 4, 5]
arr_ll = array_to_ll(arr)
print_list(arr_ll)