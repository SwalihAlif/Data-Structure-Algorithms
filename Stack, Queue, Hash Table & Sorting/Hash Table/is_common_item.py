
# O(n2)
# def is_common_item(list1, list2):
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 return True
            
#     return False

# O(n)
def is_common_item(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True
    return False

list1 = [1, 2, 3]
list2 = [7, 2, 5]

print(is_common_item(list1, list2))