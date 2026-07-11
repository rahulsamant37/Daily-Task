# DSA Problem 53

'''
Problem Statement:
You are given a string `s` consisting of lowercase English letters. You need to calculate the number of substrings that contain exactly `k` distinct characters. For example, in the string "abcabc", there are 10 substrings that contain exactly 3 distinct characters ("abc", "bca", "cab", "abc", "bca", "cab", "abc", "bca", "cab", "abc").

Write a function `count_substrings_with_k_distinct_chars(s: str, k: int) -> int:` that takes a string `s` and an integer `k`, and returns the number of substrings that have exactly `k` distinct characters.
'''

Solution:
```python
from collections import defaultdict

def count_substrings_with_k_distinct_chars(s: str, k: int) -> int:
    def at_most_k_distinct(k: int) -> int:
        count = defaultdict(int)
        start = 0
        res = 0
        for end in range(len(s)):
            if count[s[end]] == 0:
                k -= 1
            count[s[end]] += 1
            
            while k < 0:
                count[s[start]] -= 1
                if count[s[start]] == 0:
                    k += 1
                start += 1
            
            res += end - start + 1
        return res

    return at_most_k_distinct(k) - at_most_k_distinct(k-1)

# Example usage
print(count_substrings_with_k_distinct_chars("abcabc", 3))  # Output: 10
```

This solution calculates the number of substrings with at most `k` distinct characters and subtracts the number with at most `k-1` distinct characters to get the exact count for `k`. It uses a sliding window approach to efficiently find the substrings.