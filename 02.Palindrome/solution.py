def is_palindrome(string):
    if string == "":
        return True

    if " " in string:
        string = string.replace(" ", "")

    reverse = string[::-1]
    if string == reverse:
        return True
    else:
        return False


print(is_palindrome("hello")) 
print('***********************************************') 
print(is_palindrome("racecar"))
print('***********************************************') 
print(is_palindrome("madam"))
print('***********************************************')
print(is_palindrome(""))
print('***********************************************')
print(is_palindrome("mad am")) 