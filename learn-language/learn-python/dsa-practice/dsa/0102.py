# DSA Problem 102

'''
Problem Statement:
A group of students are participating in a coding competition where they are given a list of numbers. They need to find the maximum sum they can get by adding up the numbers under the following conditions:
1. They can pick any number from the list.
2. After picking a number, they cannot pick the number immediately before or after it.
3. The list can contain both positive and negative numbers.

Write a function `max_sum_skip_adjacent(nums)` that takes a list of integers `nums` and returns the maximum sum possible under the given conditions.

Example:
- max_sum_skip_adjacent([3, 7, 4, 6, 5]) should return 13, because picking 7 and 6 gives the maximum sum.
- max_sum_skip_adjacent([-2, 1, 3, -4, 5]) should return 8, because picking 1 and 5 gives the maximum sum.
'''

Solution:
def max_sum_skip_adjacent(nums):
    if not nums:
        return 0
    elif len(nums) <= 2:
        return max(nums)
    
    dp = [0]*len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]

# Test cases
print(max_sum_skip_adjacent([3, 7, 4, 6, 5]))  # Should return 13
print(max_sum_skip_adjacent([-2, 1, 3, -4, 5]))  # Should return 8
print(max_sum_skip_adjacent([5, 5, 10, 100, 10, 5]))  # Additional case, should return 110