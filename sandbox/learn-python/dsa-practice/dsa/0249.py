# DSA Problem 249

'''
Problem Statement:
A palindrome is a string that reads the same backward as forward, e.g., "madam". Given a string `s`, you are to find the length of the longest palindromic substring in `s`. Additionally, if there are multiple palindromic substrings of the same maximum length, return the one that appears first.

For example, if `s = "babad"`, the function should return "bab" because "bab" is a palindrome and its length is 3. Note that "aba" is also a valid answer.
'''

Solution:
```python
def longest_palindromic_substring(s: str) -> str:
    if len(s) == 0:
        return ""
    
    start = 0
    max_length = 1
    
    def expand_around_center(left: int, right: int) -> int:
        nonlocal start
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if right - left - 1 > max_length:
            start = left + 1
        return right - left - 1
    
    for i in range(len(s)):
        # Odd length palindromes
        len1 = expand_around_center(i, i)
        # Even length palindromes
        len2 = expand_around_center(i, i + 1)
        max_length = max(len1, len2, max_length)
        
    return s[start:start + max_length]

# Example usage
print(longest_palindromic_substring("babad"))  # Output could be "bab" or "aba"
```

This solution uses a dynamic programming approach to find the longest palindromic substring. It expands around the center for each character (and the gap between every two characters) to find the longest palindrome centered there, and keeps track of the longest palindrome found so far.