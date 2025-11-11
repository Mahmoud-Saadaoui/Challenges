# Problem: Password Validation

def validatePassword(password):
    # Condition 1: must be at least 8 characters long
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    # Loop through each character
    for ch in password:
        # Check for uppercase letter
        if 'A' <= ch <= 'Z':
            has_upper = True
        # Check for lowercase letter
        elif 'a' <= ch <= 'z':
            has_lower = True
        # Check for digit
        elif '0' <= ch <= '9':
            has_digit = True

    # Final validation
    if has_upper and has_lower and has_digit:
        return True
    else:
        return False


# ==========================
# 🧪 Example Tests
# ==========================
print(validatePassword("Abc12345"))     # ✅ True
print(validatePassword("password123"))  # ❌ False (no uppercase)
print(validatePassword("Pass"))         # ❌ False (too short)
print(validatePassword("HelloWorld"))   # ❌ False (no digit)
print(validatePassword("A1b2c3d4"))     # ✅ True
