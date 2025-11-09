def hashtag_generator(text):
    if not text or len(text) > 140:
        return False

    arr = [word.capitalize() for word in text.split()]
    return '#' + ''.join(arr)

# Example usage:
print(hashtag_generator("hello world"))  # Output: #HelloWorld
print(hashtag_generator(""))  # Output: False
print(hashtag_generator("a" * 141))  # Output: False    
print(hashtag_generator("this is a test"))  # Output: #ThisIsATest