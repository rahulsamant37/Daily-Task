# DSA Problem 273

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum sum of a non-empty subsequence of `nums` such that the sum of the elements in the subsequence is divisible by `k`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, given `nums = [5, 9, 13, 17, 21]` and `k = 3`, the maximum sum of a subsequence that meets the condition is 55 (sum of [5, 17, 21]).

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 100
'''

Solution:
```python
def max_sum_divisible_by_k(nums, k):
    dp = [0] + [float('-inf')] * (k - 1)
    for num in nums:
        for i in range(k):
            if dp[i] != float('-inf'):
                dp[(i + num) % k] = max(dp[(i + num) % k], dp[i] + num)
    return dp[0]

# Example check (You can use this to test your solution)
nums = [5, 9, 13, 17, 21]
k = 3
print(max_sum_divisible_by_k(nums, k))  # Expected output: 55
```

Explanation:
This solution uses dynamic programming to track the maximum sum of subsequences for each possible remainder when divided by `k`. For each number in the input list, it updates the DP array to reflect the maximum sums achievable by including the current number in the subsequences that end with each possible remainder. The final answer is found in the first element of the DP array, representing the maximum sum with a remainder of 0 (i.e., divisible by `k`).