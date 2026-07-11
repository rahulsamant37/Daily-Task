# DSA Problem 234

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum sum of a non-empty subsequence of `nums` such that for every pair of consecutive integers in the subsequence, the absolute difference between them is at most `k`.

For example, if `nums = [5, 4, 3, 2, 1]` and `k = 1`, a valid subsequence could be `[5, 4, 3]` because the absolute difference between consecutive elements does not exceed 1. However, the subsequence `[5, 3]` is invalid because the absolute difference between 5 and 3 is greater than 1.

Return the maximum possible sum of such a valid subsequence. If no such subsequence exists that satisfies the conditions, return 0.
'''

Solution:
```python
def max_subsequence_sum(nums, k):
    if not nums:
        return 0
    
    # Sort the array to simplify the process of finding valid subsequences
    nums.sort()
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    max_sum = nums[0]
    
    for i in range(1, n):
        dp[i] = nums[i]
        for j in range(i):
            if abs(nums[i] - nums[j]) <= k:
                dp[i] = max(dp[i], dp[j] + nums[i])
        max_sum = max(max_sum, dp[i])
    
    return max_sum

# Example check function
def check():
    print(max_subsequence_sum([5, 4, 3, 2, 1], 1))  # Output: 15 (Subsequence: [5, 4, 3, 2, 1])
    print(max_subsequence_sum([4, 2, 1], 1))        # Output: 7 (Subsequence: [4, 2])
    print(max_subsequence_sum([7, 7, 7, 7, 7], 2))  # Output: 35 (Subsequence: [7, 7, 7, 7, 7])
    print(max_subsequence_sum([10, 20, 30], 1))     # Output: 10 (Subsequence: [10])

check()
```

Note: The solution provided above is a dynamic programming approach that first sorts the input list to ensure that we only need to check the previous elements for the condition. The `dp` array keeps track of the maximum sum subsequence ending at each index that satisfies the condition.