# DSA Problem 331

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, return the maximum sum of any subsequence of `nums` such that the sum is divisible by `k`. A subsequence is obtained by deleting some number of elements (can be zero) from the original list, leaving the remaining elements in their original order.

For example, if `nums = [3, 1, 4, 2]` and `k = 3`, the possible subsequences include [3], [1, 2], [3, 1, 4, 2], etc. The sum of the subsequence [3, 1, 2] is 6, which is divisible by 3 and is the maximum sum possible.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
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

# Example check (the function to test the solution)
def check_solution():
    assert max_sum_divisible_by_k([3, 1, 4, 2], 3) == 6, "Test case 1 failed"
    assert max_sum_divisible_by_k([1, 2, 3, 4], 5) == 10, "Test case 2 failed"
    assert max_sum_divisible_by_k([5, 9, 10, 12], 4) == 24, "Test case 3 failed"
    print("All test cases passed!")

check_solution()
```

This Python code provides a solution to the problem of finding the maximum sum of any subsequence of a list of integers that is divisible by a given integer `k`. The solution utilizes dynamic programming to efficiently calculate the maximum sum for subsequences with sums divisible by `k` as it iterates through the list of numbers.