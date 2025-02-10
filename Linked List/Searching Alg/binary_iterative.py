def binary_iterative(arr, target):
    low, high = 0, len(arr) -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

sorted_numbers = [1, 3, 5, 7, 9, 11, 13]
key = 7

result = binary_iterative(sorted_numbers, key)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
