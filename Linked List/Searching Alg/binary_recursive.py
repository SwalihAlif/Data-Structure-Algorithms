def binary_recursive(arr, target, low, high):
    
    if low > high:
        return - 1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
        
    if arr[mid] > target:
        return binary_recursive(arr, target, low, mid - 1)
        
    else:
        return binary_recursive(arr, target, mid +1, high)
    
    
arr = [1, 2, 3, 4, 5]
ta = 4
low = 0
high = len(arr)-1

result = binary_recursive(arr, ta, low, high)

if result != -1:
    print(f"The element is in index: {result}")
else:
    print("Not found")