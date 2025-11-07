def count_vowels(string):
    count = 0
    vowels = "aeiouAEIOU"
    for s in string:
        if s in vowels:
            count += 1
    return count

# Example usage:
print(count_vowels("Hello World"))  # Output: 3
print(count_vowels("Python"))       # Output: 1
print(count_vowels("why"))        # Output: 0
print(count_vowels("mississippi"))            # Output: 4
