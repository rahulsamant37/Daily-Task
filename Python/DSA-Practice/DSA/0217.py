# DSA Problem 217

'''
Problem Statement:
You are given a list of positive integers. Your task is to find the length of the longest subsequence where each element is a divisor of its successor. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, for the list [2, 3, 6, 8, 12], one such subsequence could be [2, 6, 12] since 2 divides 6 and 6 divides 12.

Write a function `longest_divisible_subsequence` that takes a list of integers as input and returns the length of the longest divisible subsequence.

Constraints:
- 1 <= len(nums) <= 1000
- 1 <= nums[i] <= 10^5
'''

Solution:
```python
def longest_divisible_subsequence(nums):
    nums.sort()
    dp = [1] * len(nums)
    
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)

# Example check:
# The longest divisible subsequence could be [2, 6, 12] or [2, 4, 8] or [3, 6, 12], etc.
print(longest_divisible_subsequence([2, 3, 6, 8, 12]))  # Output: 3
```

This solution sorts the input list and then uses dynamic programming to find the longest subsequence where each element is a divisor of its successor. The `dp` array keeps track of the longest divisible subsequence length ending at each index.