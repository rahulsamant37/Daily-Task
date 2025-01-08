# DSA Problem 305

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. The task is to rotate the list `nums` to the right by `k` steps, where `k` is non-negative. The rotation should be done in-place, meaning you should not allocate extra space for another list. Additionally, you must achieve this in O(1) extra space and O(n) runtime complexity.

For example, if the list is [1, 2, 3, 4, 5] and `k` is 2, the list should be rotated to [4, 5, 1, 2, 3].

Write a function `rotate_list(nums, k)` that modifies the input list in-place.
'''

Solution:
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start, end = start + 1, end - 1

def rotate_list(nums, k):
    n = len(nums)
    k = k % n  # In case the steps are greater than the length of the list
    reverse(nums, 0, n - 1)  # Reverse the entire list
    reverse(nums, 0, k - 1)  # Reverse the first part
    reverse(nums, k, n - 1)  # Reverse the second part

# Example usage
nums = [1, 2, 3, 4, 5]
k = 2
rotate_list(nums, k)
# nums should now be [4, 5, 1, 2, 3]
print(nums)

# The function modifies the list in-place to achieve the rotation, adhering to the O(1) extra space and O(n) runtime complexity constraints.