# DSA Problem 301

'''
Problem Statement:
Given a list of integers, find the maximum sum of non-adjacent elements. In other words, you cannot include two adjacent numbers in the sum. For example, given the list [3, 2, 7, 10], the function should return 13, as the optimal choice is to take 3 and 10.

Constraints:
- The length of the list will be between 1 and 1000.
- The elements in the list will be between -1000 and 1000.
'''

Solution:
```python
def max_sum_non_adjacent(nums):
    if not nums:
        return 0

    if len(nums) <= 2:
        return max(nums)

    dp = [0] * len(nums)
    dp[0] = max(0, nums[0])  # If the first number is negative, we ignore it.
    dp[1] = max(dp[0], nums[1])  # Choose the larger of the first two numbers.

    for i in range(2, len(nums)):
        # Either take the current number and the maximum sum two steps back,
        # or skip the current number and take the maximum sum from the previous step.
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])

    return dp[-1]

# Check function to verify the solution with provided data points
def check_solution():
    assert max_sum_non_adjacent([2, 4, 6, 2, 5]) == 13
    assert max_sum_non_adjacent([5, 1, 1, 5]) == 10
    assert max_sum_non_adjacent([-1, -2, -3, -1]) == 0
    print("All test cases passed!")

check_solution()
```

This Python solution uses dynamic programming to efficiently solve the problem of finding the maximum sum of non-adjacent elements in a list.