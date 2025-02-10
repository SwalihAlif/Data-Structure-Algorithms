def count_occurrences(s):
    occurrence_dict = {}
    for char in s:
        if char in occurrence_dict:
            occurrence_dict[char] += 1
        else:
            occurrence_dict[char] = 1
    return occurrence_dict

# Example usage
string = "hello"
result = count_occurrences(string)
print(result)  
