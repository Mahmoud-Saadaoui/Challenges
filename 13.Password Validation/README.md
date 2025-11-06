# Problem: Password Validation

## Instructions
Write a function called validatePassword that takes in a string and validates it based on the following criteria:
1.	The password must be at least 8 characters long.
2.	The password must contain at least one uppercase letter.
3.	The password must contain at least one lowercase letter.
4.	The password must contain at least one digit.
The function should return true if the password is valid according to the criteria, and false otherwise.

## Examples
```
validatePassword('Abc12345'); // should return true
validatePassword('password123'); // should return false (no uppercase letter)
validatePassword('Pass'); // should return false (length less than 8 characters)
validatePassword('HelloWorld'); // should return false (no digit)

```

## Constraints
•	The input password can contain any combination of letters and digits.
•	The input password can contain both uppercase and lowercase letters.