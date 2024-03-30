# DSA Problem 27

'''
Problem Statement:
You are given a string `s` consisting of lowercase English letters. You are tasked with splitting this string into the maximum number of substrings such that each substring contains exactly one unique character. For example, the string "aababc" can be split into ["aa", "b", "a", "b", "c"]. Your job is to return the maximum number of substrings you can obtain under these conditions.

Note:
- The original string does not necessarily contain all 26 letters.
- Empty substrings are not counted.
'''

Solution:
```python
def max_unique_substrings(s: str) -> int:
    """
    Splits the string into the maximum number of substrings such that each substring contains exactly one unique character.
    """
    if not s:
        return 0
    
    count = 0
    prev_char = s[0]
    for char in s[1:]:
        if char != prev_char:
            count += 1
            prev_char = char
    # Count the last substring
    count += 1
    
    return count

# Check function to verify the correctness of the solution
def check_solution():
    assert max_unique_substrings("aababc") == 5, "Test case 1 failed"
    assert max_unique_substrings("aaaaa") == 1, "Test case 2 failed"
    assert max_unique_substrings("abcdef") == 6, "Test case 3 failed"
    assert max_unique_substrings("a") == 1, "Test case 4 failed"
    assert max_unique_substrings("ababab") == 6, "Test case 5 failed"
    print("All test cases passed!")

check_solution()
```

This Python solution defines a function `max_unique_substrings` that calculates the maximum number of substrings that can be formed from the given string `s` under the given conditions. The check function `check_solution` is used to validate the solution against several test cases.