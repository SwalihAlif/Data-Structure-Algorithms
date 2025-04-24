def linear_search(arr, target):
    indices = []

    for index in range(len(arr)):
        if arr[index] == target:
            indices.append(index)
    return indices

arr = [1, 8, 9, 1, 5, 2]
key = 10

result = linear_search(arr, key)
if result:
    print(f"the elements are found at indices {result}")
else:
    print('not found')