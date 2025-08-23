# DSA Problem 250

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum sum of a subsequence from `nums` such that the sum is divisible by `k`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, if nums = [1, 2, 3, 4] and k = 3, then the subsequence [1, 2, 3] has a sum of 6, which is divisible by 3. Note that the subsequence [1, 3] also has a sum divisible by 3, but its sum is smaller.

Return the maximum sum of a subsequence that meets the criteria. If no such subsequence exists, return 0.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
- 1 <= k <= 100
'''

Solution:
```python
def max_subsequence_sum(nums, k):
    dp = [0] + [-float('inf')] * k
    for num in nums:
        new_dp = dp[:]
        for i in range(k):
            if dp[i] >= 0:
                new_dp[(i + num) % k] = max(new_dp[(i + num) % k], dp[i] + num)
        dp = new_dp
    return dp[0] if dp[0] >= 0 else 0

# Example check (the function should return the correct output for these inputs)
print(max_subsequence_sum([1, 2, 3, 4], 3))  # Output: 6
print(max_subsequence_sum([5, 3, 9], 4))     # Output: 12
```

This solution uses dynamic programming to efficiently compute the maximum sum of a subsequence that is divisible by `k`. The `dp` array is used to keep track of the maximum sums that can be obtained for each possible remainder when divided by `k`.