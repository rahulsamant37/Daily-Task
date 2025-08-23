# DSA Problem 149

'''
Problem Statement:
Given a list of positive integers, rotate the list to the right by k steps, where k is a non-negative integer. You are to do this in-place without allocating extra space for another list. After the rotation, return the modified list.

Example:
Input: nums = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]
Explanation: The rotated array is [4, 5, 1, 2, 3] which is the input array rotated to the right by 2 steps.
'''

Solution:
def rotate(nums, k):
    """
    Rotates the list nums to the right by k steps.
    """
    n = len(nums)
    k = k % n  # In case k is larger than the length of the list
    reverse(nums, 0, n - 1)  # Reverse the entire list
    reverse(nums, 0, k - 1)  # Reverse the first k elements
    reverse(nums, k, n - 1)  # Reverse the rest of the list

def reverse(nums, start, end):
    """
    Helper function to reverse elements in the list from start to end indices.
    """
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

# Example usage
nums = [1, 2, 3, 4, 5]
k = 2
rotate(nums, k)
print(nums)  # Output should be [4, 5, 1, 2, 3]