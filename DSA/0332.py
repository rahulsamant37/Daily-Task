# DSA Problem 332

'''
Problem Statement:
Given a list of integers, find the smallest positive integer that does not appear in the list. The list may contain duplicates and negative numbers, but you should only consider positive integers for finding the missing number.

For example, given the list [3, 4, -1, 1], the smallest missing positive integer is 2. If the list is [1, 2, 0], the smallest missing positive integer is 3.
'''

Solution:
def find_smallest_missing_positive(nums):
    """
    Finds the smallest missing positive integer from a list of integers.
    """
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap nums[i] with the number at its target position
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    
    # Find the first index i such that nums[i] != i + 1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1

# Test the function
print(find_smallest_missing_positive([3, 4, -1, 1]))  # Output: 2
print(find_smallest_missing_positive([1, 2, 0]))  # Output: 3