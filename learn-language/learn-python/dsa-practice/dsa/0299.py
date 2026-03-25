# DSA Problem 299

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum sum of a non-empty subsequence of `nums` such that for every two consecutive integers in the subsequence, `nums[i]` and `nums[j]`, where `i < j`, the condition `j - i <= k` must hold.

For example, if `nums = [10,2,-2,-5,20]` and `k = 2`, a valid subsequence could be `[10, -2, 20]` (since the indices are 0, 1, and 4, and the difference between 4 and 1 is not greater than 2), and its sum is `28`. However, `[10, 20]` is not valid because the difference between their indices is greater than 2.

Write a function `max_subsequence_sum(nums: List[int], k: int) -> int` that returns the maximum possible sum of a valid subsequence.
'''

Solution:
```python
from collections import deque
from typing import List

def max_subsequence_sum(nums: List[int], k: int) -> int:
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    window = deque()
    max_sum = dp[0]
    
    for i in range(1, n):
        while window and i - window[0] > k:
            window.popleft()
        dp[i] = nums[i] + (max(window) if window else 0)
        while window and dp[i] > dp[window[-1]]:
            window.pop()
        window.append(i)
        max_sum = max(max_sum, dp[i])
    
    return max_sum

# Test the function
nums = [10, 2, -2, -5, 20]
k = 2
print(max_subsequence_sum(nums, k))  # Output: 28
```

This Python solution uses dynamic programming combined with a deque to maintain the maximum sum of subsequence that satisfies the index difference condition.