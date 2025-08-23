# DSA Problem 203

'''
Problem Statement:
Given a list of integers, find the smallest positive integer that does not appear in the list. You are required to implement this in O(n) time complexity and O(1) space complexity, excluding the input storage. You cannot use extra space for a separate list or array, and you cannot sort the input list.

For example:
- If the input list is [1, 2, 0], the function should return 3.
- For an input list of [3, 4, -1, 1], the function should return 2.
- If the input is [7, 8, 9, 11, 12], the function should return 1.
'''

Solution:
def findMissingPositive(nums):
    n = len(nums)
    if 1 not in nums:
        return 1
    if n == 1:
        return 2

    # Replace negative numbers, zeros, and numbers larger than n by 1
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1

    # Use index as a hash; mark an index corresponding to each positive number as visited
    for i in range(n):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])

    # The first place where there is no negative number is the missing number
    for i in range(n):
        if nums[i] > 0:
            return i + 1

    # If all numbers from 1 to n are present, then the missing number is n+1
    return n + 1

# Example check function (not part of the solution, for verification only)
def check_solution():
    assert findMissingPositive([1, 2, 0]) == 3
    assert findMissingPositive([3, 4, -1, 1]) == 2
    assert findMissingPositive([7, 8, 9, 11, 12]) == 1
    print("All tests passed!")

check_solution()