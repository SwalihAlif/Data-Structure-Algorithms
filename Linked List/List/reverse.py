

# def reverse_list(lst):
#     left, right = 0, len(lst)-1
#     while left < right:
#         lst[left], lst[right] = lst[right], lst[left]
#         left += 1
#         right -= 1
#     return lst

# my_list = [10, 20, 30, 40, 50]
# print(reverse_list(my_list))







# def reverse_list(lst):
#     print('befor', lst)
#     return lst[::-1]

# my_list = [10, 20, 30, 40, 50]
# print(reverse_list(my_list))








# def unique_elements(arr):
#     unique = []
#     for element in arr:
#         if element not in unique:
#             unique.append(element)
#     return unique

# for_remove_dups = [1, 2, 2, 3, 4, 4, 5]
# result = unique_elements(for_remove_dups)
# print(result)







# def find_duplicates(arr):
#     occurance = {}
#     duplicates = []

#     for elem in arr:
#         if elem in occurance:
#             occurance[elem] += 1
#         else:
#             occurance[elem] = 1
    
#     for elem, count in occurance.items():
#         if count > 1:
#             duplicates.append(elem)
    
#     return duplicates

# arr = [1, 2, 2, 3, 4, 4, 5, 5]
# result = find_duplicates(arr)
# print(result)










def second_largest(arr):

    largest, second = float('-inf'), float('-inf')

    for elem in arr:
        if elem > largest:
            second = largest
            largest = elem
        elif elem > second and elem != largest:
            second = elem

    return second
    
arr = [10, 2, 3, 4, 5, 8]
print(second_largest(arr))