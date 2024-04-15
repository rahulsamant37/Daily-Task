# DSA Problem 43

'''
Problem Statement:
You are given a list of integers. Your task is to find the longest subsequence of the list such that the absolute difference between any two adjacent elements in the subsequence is at most 1. A subsequence is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

For example, given the list [4, 2, 1, 3, 5], one such subsequence could be [2, 1, 2] or [1, 2, 3]. Note that [1, 3] is not a valid subsequence as the difference between 1 and 3 is greater than 1. You need to return the length of the longest such subsequence.

Constraints:
- The list can contain between 1 and 1000 integers.
- Each integer in the list will be between 1 and 10000.
'''

Solution:
```python
def longest_adjacent_subsequence(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    max_length = 1
    
    for i in range(len(nums)):
        for j in range(i):
            if abs(nums[i] - nums[j]) <= 1:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])
    
    return max_length

# Example usage
nums = [4, 2, 1, 3, 5]
print(longest_adjacent_subsequence(nums))  # Output: 4
```

Explanation:
This solution uses dynamic programming to keep track of the longest subsequence found so far that can end with the current element. For each element in the list, it checks all previous elements to see if they can be part of a valid subsequence ending at the current element. If so, it updates the length of the subsequence that ends with the current element. The maximum value in the `dp` array at the end of the iteration gives the length of the longest subsequence as required.