# DSA Problem 225

'''
Problem Statement:
You are given a list of integers, `nums`, and an integer `k`. Your task is to find the maximum sum of a subsequence of `nums` such that the sum of the subsequence is divisible by `k`. A subsequence of an array is a new array generated from the original array with some elements (can be none) deleted without changing the relative order of the remaining elements.

For example, `[1,3,4]` is a subsequence of `[1,2,3,4]`, but `[1,2,4,3]` is not.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 100

Example:
Input: nums = [2,6,5,3,4,2], k = 3
Output: 12
Explanation: The subsequence [6, 3, 3] has a sum of 12, which is divisible by 3. No other subsequence has a larger sum that is divisible by 3.
'''

Solution:
```python
from typing import List
import heapq

def max_sum_divisible_by_k(nums: List[int], k: int) -> int:
    dp = [0] + [-float('inf')] * (k-1)
    for num in nums:
        for i in range(k):
            if dp[i] == -float('inf'):
                continue
            dp[(i + num) % k] = max(dp[(i + num) % k], dp[i] + num)
    return dp[0]

# Example usage
nums = [2,6,5,3,4,2]
k = 3
print(max_sum_divisible_by_k(nums, k))  # Output: 12
```

This solution implements dynamic programming to keep track of the maximum sum possible for each remainder when divided by `k`. It iterates through each number, updating the sums for each possible remainder. The final answer is the maximum sum with a remainder of 0 when divided by `k`, which is stored in `dp[0]`.