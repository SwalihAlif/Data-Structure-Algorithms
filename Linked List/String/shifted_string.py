#write a function to replace each alphabet in the given string with another alphabet occuring at the n-th position from each of them

def shift_alphabets(string, n):
    result = []
    for char in string:
        if char.isalpha():
            shifted_index = (ord(char) - ord('a') + n) % 26
            shifted_char = chr(ord('a') + shifted_index)
            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)
    
original_string = 'swalihs'
shift_by = 3
shifted_string = shift_alphabets(original_string, shift_by)
print(f"Original string: {original_string}")
print(f"Shifted string: {shifted_string}")