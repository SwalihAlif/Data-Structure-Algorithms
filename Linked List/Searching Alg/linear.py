def linear_search(arr, target):

    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


arr = [7, 3, 2, 8, 9]
key = 90

result = linear_search(arr, key)
if result != -1:
    print(f"the element is found at {result}")
else:
    print('the element is not found')