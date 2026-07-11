# DSA Problem 15

'''
Problem Statement:
You are given a list of positive integers. Your task is to find the maximum sum of a subsequence such that no two elements in the subsequence are adjacent in the original list. For example, if the list is [1, 2, 3, 4], then [1, 3] or [2, 4] are valid subsequences, but [2, 3] is not because 2 and 3 are adjacent.

Write a function `max_sum_non_adjacent(nums)` that takes a list of positive integers and returns the maximum possible sum of a non-adjacent subsequence.

Examples:
- `max_sum_non_adjacent([3, 7, 4, 6, 5])` should return 13, since the largest sum of non-adjacent numbers is 7 + 6 = 13.
- `max_sum_non_adjacent([2, 1, 5, 8, 4])` should return 11, since the largest sum of non-adjacent numbers is 2 + 8 = 10 or 5 + 4 = 9, the maximum of which is 11.
'''

Solution:
def max_sum_non_adjacent(nums):
    incl = 0  # max sum including the previous element
    excl = 0  # max sum excluding the previous element
    for i in nums:
        new_excl = excl if excl > incl else incl  # new excl is max of previous excl and incl
        incl = excl + i  # new incl is previous excl plus current element
        excl = new_excl  # update excl to new_excl
    return excl if excl > incl else incl  # return max of excl and incl

# Test cases
print(max_sum_non_adjacent([3, 7, 4, 6, 5]))  # Should return 13
print(max_sum_non_adjacent([2, 1, 5, 8, 4]))  # Should return 11
'''
This solution uses dynamic programming to solve the problem efficiently. It keeps track of two variables, `incl` and `excl`, which represent the maximum sums including and excluding the previous element, respectively. The algorithm iterates through the list and updates these variables at each step to ensure the final answer is the maximum sum of a non-adjacent subsequence.
'''