def array_intersection(list_one, list_two):
    intersection = []
    for item in list_one:
        if item in list_two:
            intersection.append(item)
    return intersection

# Example usage:
print(array_intersection([1, 2, 3, 4], [3, 4, 5, 6]))  
print(array_intersection([1, 2, 3, 4, 5], [1, 3, 5, 7, 9]))
print(array_intersection([1, 1, 1, 1, 1], [2, 2, 2, 2, 2]))
print(array_intersection([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))