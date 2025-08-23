# DSA Problem 264

'''
Problem Statement:
A palindrome is a string that reads the same forward and backward. Given a string `s` consisting of lowercase English letters, determine the length of the longest palindromic substring in `s`. A substring is a contiguous sequence of characters within the string. 

For example, given the string "babad", the longest palindromic substring can be either "bab" or "aba", which have a length of 3. If the input string is "cbbd", the longest palindromic substring is "bb" with a length of 2.

Write a function `longest_palindrome_length(s)` that returns the length of the longest palindromic substring in the given string `s`.

Example:
- `longest_palindrome_length("babad")` returns `3`
- `longest_palindrome_length("cbbd")` returns `2`
- `longest_palindrome_length("a")` returns `1`
- `longest_palindrome_length("")` returns `0`
'''

Solution:
```python
def longest_palindrome_length(s: str) -> int:
    if not s:
        return 0
    
    start = 0
    end = 0
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    return end - start + 1

def expand_around_center(s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

# Test cases
print(longest_palindrome_length("babad"))  # Output: 3
print(longest_palindrome_length("cbbd"))   # Output: 2
print(longest_palindrome_length("a"))      # Output: 1
print(longest_palindrome_length(""))       # Output: 0
```

This solution finds the longest palindromic substring by expanding around each character (and the space between each pair of characters) to check for palindromes centered at that point. It returns the length of the longest palindrome found.