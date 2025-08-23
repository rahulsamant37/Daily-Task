# DSA Problem 194

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum sum of a non-empty subsequence of `nums` such that for every pair of consecutive elements in the subsequence, the absolute difference between them is at most `k`.

For example, if `nums = [4, 2, 5, 9]` and `k = 3`, a valid subsequence could be `[4, 2, 5]` because the absolute differences (|4-2|=2 and |2-5|=3) are both at most `k`. However, `[9, 4]` is not valid as the absolute difference (|9-4|=5) is greater than `k`.

Return the maximum possible sum of such a subsequence. If no such subsequence exists, return 0.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
- 1 <= k <= 10^4
'''

Solution:
```python
from sortedcontainers import SortedList

def maxSumSubsequence(nums, k):
    dp = {}
    sorted_nums = SortedList()
    max_sum = 0
    
    for num in nums:
        if num not in dp:
            dp[num] = num
        
        # Find the range of valid predecessors
        valid_predecessors = sorted_nums.irange(max(num - k, sorted_nums[0]), min(num + k, sorted_nums[-1]))
        
        for pred in valid_predecessors:
            dp[num] = max(dp[num], dp[pred] + num)
        
        sorted_nums.add(num)
        max_sum = max(max_sum, dp[num])
    
    return max_sum

# Example check (this part is not part of the solution code, just for verification)
nums = [4, 2, 5, 9]
k = 3
print(maxSumSubsequence(nums, k))  # Expected output: 11
```

Explanation:
This solution uses dynamic programming combined with a `SortedList` from the `sortedcontainers` package to efficiently find the maximum sum of a valid subsequence. The `dp` dictionary tracks the maximum sum achievable ending at each number. We iterate through the numbers, updating the maximum sum possible for each, considering only those predecessors that satisfy the absolute difference constraint `k`. The `SortedList` helps in efficiently querying the range of valid predecessors for each number.