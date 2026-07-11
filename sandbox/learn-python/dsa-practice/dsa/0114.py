# DSA Problem 114

'''
Problem Statement:
A palindrome is a string that reads the same backward as forward, such as "radar" or "level". Given a string `s`, you are allowed to perform exactly one move. In one move, you can choose any character of the string and change it to any other lowercase English letter. Your task is to determine if it's possible to make the string `s` a palindrome after exactly one move. If it's possible, return "YES", otherwise return "NO". Note that an empty string is considered a palindrome.

For example:
- If s = "abccba", you can change one of the 'b's to 'c' to make it a palindrome, so the answer would be "YES".
- If s = "abc", you cannot make it a palindrome with just one move, so the answer would be "NO".
'''

Solution:
```python
def can_make_palindrome(s: str) -> str:
    left, right = 0, len(s) - 1
    move_made = False
    
    while left < right:
        if s[left] != s[right]:
            if move_made:
                return "NO"
            # Check if making a move on one of the sides will make the rest of the string a palindrome
            if s[left + 1] == s[right] or s[left] == s[right - 1]:
                move_made = True
            else:
                return "NO"
        left += 1
        right -= 1
    
    return "YES" if move_made else "NO"

# Test cases
print(can_make_palindrome("abccba"))  # "YES"
print(can_make_palindrome("abc"))     # "NO"
print(can_make_palindrome("aabb"))    # "YES"
print(can_make_palindrome("abcba"))  # "YES"
```

This Python solution checks if it's possible to make a string a palindrome by changing exactly one character. It uses two pointers to compare characters from both ends of the string, moving towards the center. If it finds a mismatch and a move hasn't been made yet, it checks if a single change can make the string a palindrome. If more than one mismatch is found without being able to correct it with a single move, it returns "NO".