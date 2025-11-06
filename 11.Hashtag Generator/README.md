# Problem: Hashtag Generator

## Instructions
Write a function called generateHashtag that takes a string as input and returns a hashtag-generated string according to the rules below. If the generated hashtag string is longer than 140 characters or the input/result is an empty string, the function should return false.

## Examples
```
generateHashtag("JavaScript is awesome"); // "#JavaScriptIsAwesome"
generateHashtag("hello world"); // "#HelloWorld"
generateHashtag("This is a very very very very very very very very very very very very very very long input that should result in a false hashtag because it exceeds the character limit of 140"); // false
generateHashtag(""); // false

```

## Constraints
•	Return false if the input string is empty or contains only whitespace characters.
•	Return false if the generated hashtag string is longer than 140 characters.
•	Every word in the hashtag should start with a capital letter.
•	The input string may contain leading/trailing whitespace characters.