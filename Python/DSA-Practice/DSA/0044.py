# DSA Problem 44

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum possible sum of a subsequence of `nums` such that no two elements in the subsequence are adjacent in the original list, and the sum of the subsequence does not exceed `k`.

For example, given `nums = [3, 7, 4, 6, 5]` and `k = 12`, you could choose the subsequence `[7, 5]` with a sum of `12`, which is the maximum sum not exceeding `k`.

Write a function `maxSubsequenceSum(nums, k)` that returns the maximum sum of such a subsequence.

Constraints:
- 1 <= len(nums) <= 10^5
- 1 <= nums[i] <= 10^4
- 1 <= k <= 10^9
'''

Solution:
```python
def maxSubsequenceSum(nums, k):
    if not nums:
        return 0
    
    dp = [0] * len(nums)
    dp[0] = min(nums[0], k)
    
    for i in range(1, len(nums)):
        take = nums[i] + (dp[i-2] if i > 1 else 0)
        not_take = dp[i-1]
        dp[i] = min(max(take, not_take), k)
    
    return dp[-1]

# Example check (this part is not part of the solution code)
print(maxSubsequenceSum([3, 7, 4, 6, 5], 12))  # Expected output: 12
print(maxSubsequenceSum([5, 5, 5, 5], 10))  # Expected output: 10
```

This solution uses dynamic programming to calculate the maximum sum of a valid subsequence that does not exceed `k`. The `dp` array is used to store the maximum sum possible up to each index, considering the constraint that no two elements can be adjacent.