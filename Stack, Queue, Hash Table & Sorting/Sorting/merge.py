def merge(arr1, arr2):
    combined = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            combined.append(arr1[i])
            i += 1
        else:
            combined.append(arr2[j])
            j += 1
    while i < len(arr1):
        combined.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        combined.append(arr2[j])
        j += 1
        
    return combined
    
def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    
    return merge(left, right)
    
original_list = [38, 23, 98, 12, 8, 43, 88]
sorted_list = merge_sort(original_list)
print("Original List: ", original_list) 
print("\nSorted List: ", sorted_list)
        