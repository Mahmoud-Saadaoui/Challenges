def validate_email(email):
    if email.find('@') == -1 or email.find('.') == -1:
        return False
    
    if email.find('@') < 3:
        return False

    after_at = email.split('@')[1]
    if after_at.count('.') != 1:
        return False
    if after_at.find('.') < 2:
        return False
    
    dot_index = after_at.find('.')
    if len(after_at[dot_index:]) < 3:
        return False
    
    return True

# email = "userexample.com"
print(validate_email("us.er@example.cn")) 