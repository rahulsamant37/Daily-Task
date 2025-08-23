# DSA Problem 314

'''
Problem Statement:
You are given a list of positive integers, `nums`, and an integer `k`. Your task is to find the maximum sum of any subsequence of `nums` where the sum is divisible by `k`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. If no such subsequence exists, return 0.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 100

Examples:
1. Given nums = [4, 5, 1, 3, 2] and k = 3, the output should be 9 since the subsequence [4, 5] sums up to 9 which is divisible by 3.
2. Given nums = [1, 2, 3, 4] and k = 5, the output should be 5 since the subsequence [1, 4] sums up to 5 which is divisible by 5.
'''

Solution:
```python
def max_subsequence_sum_divisible_by_k(nums, k):
    dp = [0] + [-float("inf")] * (k - 1)
    for num in nums:
        new_dp = dp[:]
        for i in range(k):
            new_dp[(i + num) % k] = max(new_dp[(i + num) % k], dp[i] + num)
        dp = new_dp
    return dp[0] if dp[0] > 0 else 0

# Example check function
def check_solution():
    assert max_subsequence_sum_divisible_by_k([4, 5, 1, 3, 2], 3) == 9
    assert max_subsequence_sum_divisible_by_k([1, 2, 3, 4], 5) == 5
    assert max_subsequence_sum_divisible_by_k([2, 4, 6, 8], 7) == 14
    assert max_subsequence_sum_divisible_by_k([1, 2, 3], 9) == 0
    print("All test cases passed.")

check_solution()
```

This Python solution uses dynamic programming to find the maximum sum of a subsequence that is divisible by `k`. The `dp` array keeps track of the maximum sums that leave a remainder of `i` when divided by `k`. The function iterates over each number in `nums`, and for each number, it updates the `dp` array to reflect the best possible sums that can be achieved with the new number added to existing subsequences. Finally, `dp[0]` contains the maximum sum of a subsequence that is divisible by `k`.