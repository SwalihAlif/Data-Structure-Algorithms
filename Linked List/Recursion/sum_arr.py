def sum_arr(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_arr(arr[1:])

my_arr = [1, 2, 3, 4, 5]
print(sum_arr(my_arr))


def product_of_array(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * product_of_array(arr[1:])

my_arr = [1, 2, 3, 4, 5]
print(product_of_array(my_arr))

