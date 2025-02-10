dict1 = {
    'value': 11
}

dict2 = dict1

print("Before value is updated")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("dict1 points to", id(dict1))
print("dict2 points to", id(dict2))

dict2['value'] = 22

print("After updating the value of dict2")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("dict1 points to", id(dict1))
print("dict2 points to", id(dict2))