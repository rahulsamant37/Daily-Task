# DSA Problem 340

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum possible sum of a non-empty subsequence of the list where the sum of the subsequence elements is divisible by `k`. If no such subsequence exists, return -1.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example:
- If nums = [5, 9, 14], k = 6, the answer is 15 because the subsequence [9, 14] has a sum of 23, which is not divisible by 6, but the subsequence [9] has a sum of 9 which is divisible by 6.
- If nums = [-1, 2, -4, 5], k = 3, the answer is 4 because the subsequence [2, -4, 5] has a sum of 3, which is divisible by 3.
'''

Solution:
```python
from typing import List

def max_subsequence_sum(nums: List[int], k: int) -> int:
    """
    Finds the maximum possible sum of a subsequence of nums where the sum is divisible by k.
    """
    n = len(nums)
    dp = [[-float('inf')] * k for _ in range(n+1)]
    dp[0][0] = 0  # Base case: sum 0 with 0 elements is possible with sum 0
    
    for i in range(1, n+1):
        for j in range(k):
            dp[i][j] = dp[i-1][j]  # Carry forward the previous state
            new_sum = (dp[i-1][j] + nums[i-1]) % k
            dp[i][new_sum] = max(dp[i][new_sum], dp[i-1][j] + nums[i-1])
    
    return dp[n][0] if dp[n][0] != 0 else -1

# Example check function
def check_solution():
    assert max_subsequence_sum([5, 9, 14], 6) == 9
    assert max_subsequence_sum([-1, 2, -4, 5], 3) == 4
    assert max_subsequence_sum([1, 2, 3], 5) == -1  # No subsequence sum divisible by 5
    print("All tests passed!")

check_solution()
```

This solution uses dynamic programming to keep track of the maximum subsequence sum that gives a certain remainder when divided by `k`. It iterates through each number in the list and updates the DP table accordingly. The final answer is found in `dp[n][0]`, if there's a subsequence whose sum is divisible by `k`.