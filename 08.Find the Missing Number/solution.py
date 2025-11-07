def find_missing_number(arr):
    n = len(arr) + 1  
    total_sum = n * (n + 1)  // 2
    arr_sum = sum(arr) 
    missing_number = total_sum - arr_sum  
    return missing_number

