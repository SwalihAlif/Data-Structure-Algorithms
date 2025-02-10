# best, worst, average is O(n2)
# space O(1)
# Advantages---------------------:
# Simple to implement.
# Performs well on small datasets.
# Disadvantages--------------------:
# Inefficient for large datasets due to O(n²) time complexity.
# Doesn't adapt to already sorted arrays.

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
                
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
    
arr = [7,3,1, 2,6, 5, 4]

print(selection_sort(arr))