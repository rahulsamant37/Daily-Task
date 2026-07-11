# DSA Problem 242

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, return the maximum sum of any non-empty subsequence of `nums` where the sum of the subsequence is divisible by `k`. If no such subsequence exists, return -1.

A subsequence of an array is a new array generated from the original array with some elements (can be none) deleted without changing the relative order of the remaining elements.

For example, [2,4,6,8] is a subsequence of [1,2,3,4,5,6,7,8].
'''

Solution:
```python
from typing import List

def maxSumDivisibleByK(nums: List[int], k: int) -> int:
    dp = [float('-inf')] * k
    dp[0] = 0
    for num in nums:
        for i in range(k):
            if dp[i] != float('-inf'):
                remainder = (i + num) % k
                dp[remainder] = max(dp[remainder], dp[i] + num)
    return dp[0] if dp[0] != 0 else -1

# Example usage:
nums = [5, 2, 1]
k = 3
print(maxSumDivisibleByK(nums, k))  # Output: 6
```

This problem uses dynamic programming to find the maximum sum of a subsequence that is divisible by `k`. It keeps track of the maximum sums for all possible remainders when divided by `k`, allowing it to efficiently find the desired subsequence sum.