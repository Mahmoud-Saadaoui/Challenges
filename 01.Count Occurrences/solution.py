#----------------------------
# Count Occurrences Problem
#-----------------------------

def count_occurences(string, character):
    count = 0
    for i in string:
        if i == character:
            count += 1
    return count

# Test cases
print(count_occurences("hello world", "o"))
print('#' * 50)
print(count_occurences("banana", "a"))
print('#' * 50)
print(count_occurences("hello", "z"))