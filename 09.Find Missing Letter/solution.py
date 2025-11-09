def find_missing_letter(arr):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(arr) == 0:
        return ""
    alpha_list = list(alpha)
    first_index = alpha_list.index(arr[0])
    last_index = alpha_list.index(arr[-1]) + 1
    my_slice = alpha_list[first_index:last_index]
    for letter in my_slice:
        if letter not in arr:
            return letter

# Example usage:
print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))
print(find_missing_letter(['O', 'Q', 'R', 'S']))
print(find_missing_letter(['t', 'u', 'v', 'w', 'x', 'z']))  

