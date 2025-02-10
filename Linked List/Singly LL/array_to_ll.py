class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def array_to_ll(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for elem in arr[1:]:
        current.next = Node(elem)
        current = current.next
    return head
def print_list(head):
    current = head
    while current is not None:
        print(current.value, end=' -> ')
        current = current.next
    print(None)

arr = [1, 2, 3, 4, 5]
to_ll = array_to_ll(arr)
print_list(to_ll)
    