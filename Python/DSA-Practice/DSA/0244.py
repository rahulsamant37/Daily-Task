# DSA Problem 244

'''
Problem Statement:
You are given a list of positive integers, `nums`, and an integer `k`. Your task is to find the maximum sum of a non-empty subsequence of `nums` such that for every pair of consecutive integers in the subsequence, the absolute difference between them is at most `k`. If there is no such subsequence, return 0.

A subsequence of an array is a new array generated from the original array with some elements (can be none) deleted without changing the relative order of the remaining elements.

For example, `[2,4,6]` is a subsequence of `[1,2,3,4,5,6]`, but `[2,6,4]` is not.
'''

Solution:
```python
from heapq import heappush, heappop

def maxSubsequenceSum(nums, k):
    nums.sort()
    dp = {}
    
    def dfs(index, prev):
        if index == len(nums):
            return 0
        if (index, prev) in dp:
            return dp[(index, prev)]
        
        # Option 1: Skip the current number
        take = 0
        if prev == -1 or abs(nums[index] - nums[prev]) <= k:
            # Option 2: Take the current number
            take = nums[index] + dfs(index + 1, index)
        
        skip = dfs(index + 1, prev)
        dp[(index, prev)] = max(take, skip)
        return dp[(index, prev)]
    
    return dfs(0, -1)

# Example check function (not part of the solution)
def check():
    assert maxSubsequenceSum([2,6,5,3], 1) == 7  # [3,5] is the subsequence with the maximum sum.
    assert maxSubsequenceSum([10,5,-2], 3) == 10  # [10] is the only subsequence.
    print("All tests passed!")

check()
```

This Python solution utilizes dynamic programming with memoization to efficiently solve the problem. The `dfs` function is a recursive function that explores all possible subsequences starting from the given index and considering the last number included in the subsequence (tracked by `prev`). The `dp` dictionary is used to store the results of subproblems to avoid redundant calculations.