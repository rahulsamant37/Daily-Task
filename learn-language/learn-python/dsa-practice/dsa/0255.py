# DSA Problem 255

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, return the maximum sum of any non-empty subsequence of `nums` such that for every two consecutive integers in the subsequence, `nums[i]` and `nums[j]`, where `i < j`, the condition `j - i <= k` must be satisfied. If there is no such subsequence, return 0.

A subsequence of an array is a new array generated from the original array with some elements (can be none) deleted without changing the relative order of the remaining elements.

Example 1:
Input: nums = [10,2,-2,-20,10], k = 5
Output: 18
Explanation: The optimal subsequence is [10, 2, -2, 10] which has a sum of 18.

Example 2:
Input: nums = [4,2,1], k = 2
Output: 7
Explanation: The optimal subsequence is [4, 2, 1] which has a sum of 7.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
'''

Solution:
```python
from collections import deque

def maxSubsequenceSum(nums, k):
    dp = [0] * len(nums)
    max_sum = 0
    dq = deque()
    
    for i in range(len(nums)):
        # Remove elements out of the window
        if dq and dq[0] < i - k:
            dq.popleft()
        
        dp[i] = nums[i]
        if dq:
            dp[i] += dp[dq[0]]
            dp[i] = max(dp[i], nums[i])
        
        # Maintain deque in decreasing order
        while dq and dp[i] >= dp[dq[-1]]:
            dq.pop()
        
        dq.append(i)
        max_sum = max(max_sum, dp[i])
    
    return max_sum

# Example usage:
nums = [10,2,-2,-20,10]
k = 5
print(maxSubsequenceSum(nums, k))  # Output: 18
```

This solution uses dynamic programming combined with a deque to efficiently find the maximum sum of a subsequence under the given constraints. It ensures that only the most promising subsequence sums are kept in the deque, allowing for linear time complexity relative to the size of the input array.