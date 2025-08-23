# DSA Problem 221

'''
Problem Statement:
A palindrome is a string that reads the same backward as forward, such as "madam" or "racecar". Given a string `s`, find the length of the longest palindromic substring in `s`. For example, given the string "babad", the longest palindromic substring is "bab" or "aba", so the function should return 3. If the input string is "cbbd", then the function should return 2, as the longest palindromic substring could be "bb".
'''

Solution:
```python
def longest_palindromic_substring(s: str) -> int:
    def expand_around_center(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    if len(s) == 0:
        return 0

    start, end = 0, 0
    for i in range(len(s)):
        len1 = expand_around_center(i, i)  # Odd length palindromes
        len2 = expand_around_center(i, i + 1)  # Even length palindromes
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return end - start + 1

# Example usage
print(longest_palindromic_substring("babad"))  # Output: 3
print(longest_palindromic_substring("cbbd"))   # Output: 2
```

This solution implements a method to find the longest palindromic substring in a given string. It uses a helper function `expand_around_center` to expand around a center (or centers for even-length palindromes) and check for the longest palindrome. This approach is efficient for finding the longest palindromic substring without needing to generate all possible substrings and check each one for being a palindrome.