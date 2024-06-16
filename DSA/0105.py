# DSA Problem 105

'''
Problem Statement:
A palindrome is a string that reads the same forward and backward. Given a string `s`, determine if it can be rearranged to form a palindrome. If it can, return `True`; otherwise, return `False`. Note that you can rearrange the characters in any order, but all characters in `s` must be used exactly once.

Example 1:
Input: s = "carrace"
Output: True
Explanation: The string "carrace" can be rearranged to form the palindrome "racecar".

Example 2:
Input: s = "daily"
Output: False
Explanation: The string "daily" cannot be rearranged to form a palindrome.
'''

Solution:
```python
def can_form_palindrome(s: str) -> bool:
    from collections import Counter
    
    char_count = Counter(s)
    odd_counts = sum(1 for count in char_count.values() if count % 2 != 0)
    
    # For a string to be rearranged into a palindrome, at most one character can have an odd count
    return odd_counts <= 1

# Example check function
def check_solution():
    test_cases = [("carrace", True), ("daily", False), ("aabbcc", True), ("abc", False)]
    for s, expected in test_cases:
        assert can_form_palindrome(s) == expected, f"Failed for input: {s}"
    print("All test cases passed!")

check_solution()
```
This Python solution checks if the given string can be rearranged to form a palindrome by counting the occurrences of each character and ensuring that at most one character has an odd count.