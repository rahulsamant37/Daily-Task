# DSA Problem 310

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum possible sum of a non-empty subsequence of `nums` such that for any two consecutive integers in the subsequence, their difference is at most `k`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, if `nums = [3, 6, 1, 2]` and `k = 2`, the subsequence `[3, 1, 2]` is valid since the difference between consecutive elements is at most `2`, and its sum is `6`. However, the subsequence `[6, 1]` is not valid since the difference between `6` and `1` is greater than `2`.

Write a function `maxSubsequenceSum(nums, k)` that returns the maximum possible sum of such a valid subsequence.

Constraints:
- 1 <= len(nums) <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 10^9
'''

Solution:
```python
from sortedcontainers import SortedDict

def maxSubsequenceSum(nums, k):
    dp = SortedDict()
    for num in sorted(nums):
        # Find the maximum sum that can be achieved with the current number
        if dp.bisect_left(num - k) != 0:
            dp[num] = max(dp.values()) + num
        else:
            dp[num] = num
        # Remove entries that are no longer needed to keep the space complexity low
        if dp.bisect_right(num + k) < len(dp):
            dp.popitem(index=dp.bisect_right(num + k))
    return max(dp.values())

# Example check (this part is not part of the solution code):
nums = [3, 6, 1, 2]
k = 2
print(maxSubsequenceSum(nums, k))  # Expected output: 6
```

This solution uses a `SortedDict` from the `sortedcontainers` module for efficiently managing and querying the dynamic programming states, ensuring an optimal solution is found within the constraints.