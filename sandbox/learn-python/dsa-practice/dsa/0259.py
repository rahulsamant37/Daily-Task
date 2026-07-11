# DSA Problem 259

'''
Problem Statement:
Given a list of positive integers, find the smallest integer that is evenly divisible by all the integers in the list. If no such integer exists within the range of 1 to 1,000,000, return -1. The list will contain at most 15 integers, and each integer in the list will be between 1 and 100, inclusive.

For example, given the list [2, 3, 5], the smallest number that is evenly divisible by 2, 3, and 5 is 30. If the list is [4, 6, 5], the smallest such number is 60.
'''

Solution:
def smallest_divisible_number(nums):
    from math import gcd
    from functools import reduce

    lcm = lambda x, y: x * y // gcd(x, y)
    result = reduce(lcm, nums, 1)
    
    return result if result <= 1000000 else -1

# Example check function
def check_solution():
    assert smallest_divisible_number([2, 3, 5]) == 30
    assert smallest_divisible_number([4, 6, 5]) == 60
    assert smallest_divisible_number([100, 50, 25]) == 100
    assert smallest_divisible_number([101, 202]) == -1  # Since the result would be greater than 1,000,000
    print("All tests passed!")

check_solution()