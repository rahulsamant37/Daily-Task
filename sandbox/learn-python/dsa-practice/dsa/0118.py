# DSA Problem 118

'''
Problem Statement:
A palindrome is a string that reads the same backward as forward, such as "madam" or "racecar". Given a string `s` consisting of lowercase English letters, find the length of the longest palindromic substring in `s`. For example, in the string "babad", the longest palindromic substring could be "bab" or "aba", both of which have a length of 3.

Your task is to write a function `longest_palindromic_substring` that takes a string `s` as input and returns the length of the longest palindromic substring in `s`.

Constraints:
- The input string length is between 1 and 1000.

Example:
Input: s = "babad"
Output: 3
Explanation: "bab" and "aba" are both valid palindromic substrings with the longest length of 3.
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
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return end - start + 1

# Example check (You can remove or comment this part before submitting your solution)
print(longest_palindromic_substring("babad"))  # Expected output: 3
```

This Python solution defines a function `longest_palindromic_substring` that computes the length of the longest palindromic substring within the given string `s`. The solution uses a helper function `expand_around_center` to find the longest palindrome by expanding around its center, considering both odd and even length palindromes.