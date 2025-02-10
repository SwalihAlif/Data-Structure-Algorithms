class Node:
    def __init__(self, value):
        self.value =value
        self.next = None
        
def arr_to_ll_recursion(arr, index=0):
    if index >= len(arr):
        return None
    node = Node(arr[index])
    node.next = arr_to_ll_recursion(arr, index + 1)
    return node
    
arr = [1, 9, 2, 8, 9, 10]
head_of_ll = arr_to_ll_recursion(arr)

current = head_of_ll
while current is not None:
    print(current.value, end=" -> ")
    current = current.next
print(None)
