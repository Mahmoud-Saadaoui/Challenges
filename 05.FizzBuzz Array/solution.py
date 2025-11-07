def fizz_buzz_array(array):
    for i in range(len(array)):
        if array[i] % 3 == 0 and array[i] % 5 == 0:
            array[i] = "FizzBuzz"
        elif array[i] % 3 == 0:
            array[i] = "Fizz"
        elif array[i] % 5 == 0:
            array[i] = "Buzz"
    return array

print(fizz_buzz_array([1, 2, 3, 4, 5, 15, 17]))