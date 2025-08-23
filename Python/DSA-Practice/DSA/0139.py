# DSA Problem 139

'''
Problem Statement:
You are given a list of positive integers and a positive integer k. Your task is to find the length of the longest subsequence of the list such that the sum of the subsequence is divisible by k. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, given the list [3, 1, 2, 4, 5] and k = 3, the longest subsequence with a sum divisible by 3 is [1, 2, 4], which has a sum of 7 and a length of 3.

Write a function `longest_divisible_subsequence(nums, k)` that returns the length of the longest such subsequence.
'''

Solution:
```python
from collections import defaultdict

def longest_divisible_subsequence(nums, k):
    # Initialize a dictionary to keep track of the minimum length for each remainder
    dp = defaultdict(lambda: float('inf'))
    dp[0] = 0
    current_sum = 0
    max_length = 0
    
    for num in nums:
        current_sum += num
        for remainder in list(dp.keys()):
            new_sum = current_sum - (dp[remainder] * k)
            if new_sum % k == remainder:
                dp[new_sum % k] = min(dp[remainder] + 1, dp[new_sum % k])
                max_length = max(max_length, dp[new_sum % k])
    
    return max_length

# Test the function with an example
nums = [3, 1, 2, 4, 5]
k = 3
print(longest_divisible_subsequence(nums, k))  # Expected output: 3
```

Note: The given solution uses a dynamic programming approach with a twist, where it tracks the minimum length of subsequences for each possible remainder when divided by k. The complexity of this problem makes it a bit challenging, and the provided solution attempts to find a feasible solution that might not be the most optimal in all cases.