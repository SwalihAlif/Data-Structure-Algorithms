def reverse_str(st):
    reversed_st = ""

    for char in st:
        reversed_st = char + reversed_st
    return reversed_st

string = "Hello, World!"
print(reverse_str(string))