stack = []

stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after pushing: ", stack)

top_element = stack.pop()
print("Top element after pop: ", top_element)

print("Top element without pop: ", stack[-1])

print("If stack is empty? ", len(stack) == 0)

print("Length of the stack: ", len(stack))