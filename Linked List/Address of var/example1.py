num1 = 11
num2 = num1
num3 = 11

print("Before updating the value of num2")
print(f"num1: {num1}")
print(f"num2: {num2}")

print("address of num1 is:", id(num1))
print("address of num2 is", id(num2))
print("num3 points to", id(num3))


num2 = 22

print("After updating the value of num2")

print('num1 points to', id(num1))
print('num2 points to', id(num2))