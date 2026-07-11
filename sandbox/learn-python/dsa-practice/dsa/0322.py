# DSA Problem 322

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, find the maximum sum of a non-empty subsequence of `nums` such that the sum is divisible by `k`. If no such subsequence exists, return -1.

A subsequence of an array is a new array generated from the original array with some elements (can be none) deleted without changing the relative order of the remaining elements.
'''

Solution:
```python
from typing import List
from functools import lru_cache

def max_subsequence_sum_divisible_by_k(nums: List[int], k: int) -> int:
    n = len(nums)
    
    @lru_cache(None)
    def dp(index, current_sum):
        if index == n:
            if current_sum % k == 0 and current_sum != 0:
                return current_sum
            else:
                return float('-inf')
        # Option 1: Include the current number in the subsequence
        include = dp(index + 1, current_sum + nums[index]) + nums[index]
        # Option 2: Exclude the current number from the subsequence
        exclude = dp(index + 1, current_sum)
        
        return max(include, exclude)
    
    result = dp(0, 0)
    return result if result != float('-inf') else -1

# Example check function
def check_solution():
    assert max_subsequence_sum_divisible_by_k([5, 9, 9, 4], 4) == 8, "Test case 1 failed"
    assert max_subsequence_sum_divisible_by_k([3, 1, 6, 10, 11], 4) == 18, "Test case 2 failed"
    assert max_subsequence_sum_divisible_by_k([2, 3, 5], 13) == -1, "Test case 3 failed"
    print("All test cases passed!")

check_solution()
```

This Python solution uses dynamic programming with memoization to efficiently find the maximum sum of a subsequence divisible by `k`. The `dp` function is a recursive function that uses memoization to store intermediate results and avoid redundant calculations. The `check_solution` function is used to validate the correctness of the solution with given test cases.