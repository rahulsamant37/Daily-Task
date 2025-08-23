# DSA Problem 106

'''
Problem Statement:
You are given a list of integers `nums` and a positive integer `k`. Your task is to find the maximum sum of a non-empty subsequence of `nums` such that for every pair of consecutive integers in the subsequence, their absolute difference is at most `k`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, if `nums = [4,6,1,2]` and `k = 2`, one possible subsequence could be `[4,6]` or `[1,2]` because the absolute difference between consecutive elements is at most `2`. However, `[4,1]` is not a valid subsequence for this problem because the absolute difference between `4` and `1` is greater than `2`.

Constraints:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= 10^4

Return the maximum possible sum of any valid subsequence.

Example:
Input: nums = [4,6,1,2], k = 2
Output: 10
Explanation: The optimal subsequence is [4,6] or [6,4], which gives a sum of 10.
'''

Solution:
```python
from sortedcontainers import SortedList

def maxSubsequenceSum(nums, k):
    nums.sort()
    dp = SortedList()
    max_sum = -float('inf')
    for num in nums:
        left = num - k
        right = num + k
        index = dp.bisect_left(left)
        if index != len(dp) and dp[index] <= right:
            current_max = dp[index] + num
            dp.add(current_max)
            max_sum = max(max_sum, current_max)
        else:
            dp.add(num)
            max_sum = max(max_sum, num)
    return max_sum

# Example usage
nums = [4,6,1,2]
k = 2
print(maxSubsequenceSum(nums, k))  # Output should be 10
```

Note: This solution assumes the `SortedList` from `sortedcontainers` is available, which is not a built-in Python library and would need to be installed separately. The function `maxSubsequenceSum` finds the maximum sum of a valid subsequence as per the problem's constraints and requirements.