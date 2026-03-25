# DSA Problem 39

'''
Problem Statement:
You are given a string `s` consisting of lowercase English letters. Your task is to determine if the string `s` can be rearranged so that no two adjacent characters are the same. If it is possible to rearrange the string in such a way, return `True`; otherwise, return `False`.

For example, given the string "aabbcc", you can rearrange it to "abcabc" where no two adjacent characters are the same, so the function should return `True`. However, for the string "aaabc", it is not possible to rearrange the string so that no two adjacent characters are the same, so the function should return `False`.

Constraints:
- 1 <= s.length <= 10^5
- s` consists only of lowercase English letters.
'''

Solution:
```python
from collections import Counter

def can_rearrange(s: str) -> bool:
    """
    Determines if the string can be rearranged so that no two adjacent characters are the same.
    """
    # Count the frequency of each character in the string
    char_count = Counter(s)
    max_count = max(char_count.values())
    
    # If the most frequent character is more than half the length of the string, rearrangement is impossible
    if max_count > (len(s) + 1) // 2:
        return False
    
    return True

# Check function to verify the correctness of the solution
def check_solution():
    test_cases = [("aabbcc", True), ("aaabc", False), ("aaab", False), ("abc", True)]
    for s, expected in test_cases:
        assert can_rearrange(s) == expected, f"Failed on {s}"
    print("All test cases passed.")

check_solution()
```

This solution leverages the fact that if any character's frequency is more than half the length of the string (considering the integer division for odd-length strings), then it's impossible to rearrange the string such that no two adjacent characters are the same.