# DSA Problem 297

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to determine if there are two distinct indices `i` and `j` in the list such that `nums[i] = nums[j]` and the absolute difference between `i` and `j` is less than or equal to `k`. 

For example, if the list is [1, 2, 3, 1] and `k` is 3, the function should return `True` because the number 1 appears at both index 0 and index 3, and the absolute difference between these indices is 3, which is equal to `k`. If the list is [1, 2, 3, 1, 2, 3] and `k` is 2, the function should return `False` as no two identical elements are within `k` distance of each other.

Write a function `is_within_k_distance(nums, k)` that takes in a list of integers `nums` and an integer `k`, and returns `True` if the condition is met, otherwise `False`.
'''

Solution:
def is_within_k_distance(nums, k):
    num_dict = {}
    for i, num in enumerate(nums):
        if num in num_dict and i - num_dict[num] <= k:
            return True
        num_dict[num] = i
    return False

# Example check function to test your solution
def check_solution():
    assert is_within_k_distance([1, 2, 3, 1], 3) == True, "Example 1 failed"
    assert is_within_k_distance([1, 2, 3, 1, 2, 3], 2) == False, "Example 2 failed"
    assert is_within_k_distance([1, 0, 1, 1], 1) == True, "Example 3 failed"
    print("All test cases passed!")

check_solution()
