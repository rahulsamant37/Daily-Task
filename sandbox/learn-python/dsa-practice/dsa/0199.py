# DSA Problem 199

'''
Problem Statement:
Given a list of integers, find the longest subsequence such that the absolute difference between any two adjacent elements in the subsequence is at most 1. The subsequence does not need to be contiguous, and the order of elements in the subsequence should match their order in the original list.

For example, given the list [4, 3, 5, 4, 3, 6], one such subsequence could be [4, 3, 4, 3] since the absolute difference between any two adjacent elements is at most 1.

Write a function `longest_subsequence` that takes a list of integers and returns the length of the longest such subsequence.

Constraints:
- The length of the list will be between 1 and 1000.
- Each integer in the list will be between 1 and 1000.
'''

Solution:
```python
def longest_subsequence(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if abs(nums[i] - nums[j]) <= 1:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Test the function
print(longest_subsequence([4, 3, 5, 4, 3, 6]))  # Expected output: 4
print(longest_subsequence([1, 3, 5, 7]))       # Expected output: 1
```

This Python solution uses dynamic programming to find the length of the longest subsequence where the absolute difference between any two adjacent elements is at most 1. It iterates through the list, comparing each element with the previous ones to update the length of the longest subsequence ending at each index.