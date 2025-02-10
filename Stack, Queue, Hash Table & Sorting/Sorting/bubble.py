# Big o time : worst O(n2) best O(n)
# space : O(1) no need of extra space

def bubble_sort(arr):
    print("1 is worst")
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

def bubble_sort(arr):
    print("2 average")
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubble_sort(arr):
    print("3 is best")
    print('big o of 3 are same')
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    
arr = [7,3,1, 2,6, 5, 4]

print(bubble_sort(arr))