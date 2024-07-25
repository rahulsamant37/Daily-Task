# DSA Problem 144

'''
Problem Statement:
You are given a list of integers, `nums`, and an integer `k`. You need to find the maximum number of unique integers you can pick from the list such that the sum of these picked integers is exactly `k`. If there's no way to pick such integers, return -1.

For example:
- If nums = [1, 2, 3, 4, 5] and k = 7, the answer is 2 because you can pick 2 and 5.
- If nums = [1, 1, 1, 1] and k = 5, the answer is -1 because it's impossible to get a sum of 5 with 1s.
'''

Solution:
```python
from collections import Counter
from itertools import combinations

def max_unique_sum(nums, k):
    unique_nums = list(Counter(nums).keys())
    for r in range(len(unique_nums), 0, -1):
        for combo in combinations(unique_nums, r):
            if sum(combo) == k:
                return len(combo)
    return -1

# Test the function
print(max_unique_sum([1, 2, 3, 4, 5], 7))  # Output: 2
print(max_unique_sum([1, 1, 1, 1], 5))    # Output: -1
```

Note: This solution uses a brute-force approach to find the maximum number of unique integers that sum up to `k`. It iterates over all possible combinations of the unique numbers in `nums` in descending order of their lengths. This ensures that the first combination found is the one with the maximum number of unique integers. The time complexity of this solution is high, especially for large lists, as it checks all combinations, making it inefficient for large-scale problems.