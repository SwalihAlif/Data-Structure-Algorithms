def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp
    
def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index # return swap index, not the value in the index


my_list = [4, 6, 1, 7, 3, 2, 5]
print(my_list)
print(pivot(my_list, 0, 6))
print(my_list)