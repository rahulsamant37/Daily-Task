# DSA Problem 323

'''
Problem Statement:
A palindrome is a word, phrase, or sequence that reads the same backward as forward. Given a string `s` consisting of lowercase English letters, return the length of the longest palindrome that can be constructed by choosing some characters from `s`. Characters can be used multiple times, but only an even number of times if they are not unique.

For example, given the string "abccccdd", the longest palindrome that can be built from these letters is "dccaccd", whose length is 7.

Constraints:
- 1 <= s.length <= 2000
- s consists of lowercase English letters only.
'''

Solution:
```python
from collections import Counter

def longest_palindrome(s: str) -> int:
    """
    Calculates the length of the longest palindrome that can be constructed from the given string.
    """
    char_counts = Counter(s)
    length = 0
    odd_used = False
    for count in char_counts.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            if not odd_used:
                length += 1
                odd_used = True
    return length

# Check function to verify the solution with provided data points
def check_solution():
    assert longest_palindrome("abccccdd") == 7, "Test case 1 failed"
    assert longest_palindrome("a") == 1, "Test case 2 failed"
    assert longest_palindrome("aaabbbb") == 7, "Test case 3 failed"
    assert longest_palindrome("abc") == 1, "Test case 4 failed"
    print("All test cases passed!")

check_solution()
```

This Python solution introduces a problem related to constructing the longest palindrome from a given string, which is a common yet interesting problem in algorithmic challenges. The solution makes use of the `Counter` class from the `collections` module to efficiently count character occurrences and then calculates the maximum possible length of a palindrome based on these counts.