# DSA Problem 213

'''
Problem Statement:
You are given a list of positive integers. Your task is to find the maximum sum of non-adjacent elements in the list. For example, if the list is [3, 2, 7, 10], one possible maximum sum of non-adjacent elements is 13 (3 + 10), as picking both 7 and 10 would violate the non-adjacency condition. Note that if the list contains only one element, that element is considered the maximum sum.

Write a function `max_non_adjacent_sum(nums)` that takes in a list of integers and returns the maximum sum of non-adjacent elements.

Example:
- max_non_adjacent_sum([3, 2, 7, 10]) should return 13.
- max_non_adjacent_sum([3, 2, 5, 10, 7]) should return 15.
'''

Solution:
```python
def max_non_adjacent_sum(nums):
    """
    Returns the maximum sum of non-adjacent elements in the list.
    """
    if not nums:
        return 0
    elif len(nums) <= 2:
        return max(nums + [0])
    
    dp = [0] * len(nums)
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]

# Check function to verify the correctness of the solution
def check_solution():
    assert max_non_adjacent_sum([3, 2, 7, 10]) == 13, "Test case 1 failed"
    assert max_non_adjacent_sum([3, 2, 5, 10, 7]) == 15, "Test case 2 failed"
    assert max_non_adjacent_sum([5]) == 5, "Test case 3 failed"
    assert max_non_adjacent_sum([]) == 0, "Test case 4 failed"
    assert max_non_adjacent_sum([5, 5, 10, 100, 10, 5]) == 110, "Test case 5 failed"
    print("All test cases passed!")

check_solution()
```

This Python code snippet defines a function that calculates the maximum sum of non-adjacent elements in a list, following the problem statement and solution format provided.