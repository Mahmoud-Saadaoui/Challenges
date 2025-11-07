def remove_duplicates(array):
    unique = []
    for el in array:
        if el not in unique:
            unique.append(el)
    return unique

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(remove_duplicates([1, 1, 1, 1, 1]))        # Output: [1]
print(remove_duplicates([]))                       # Output: [] 
print(remove_duplicates([1, 2, 3, 4, 5, True, 1, 'hello', 2, 3, 'hello', True]))
