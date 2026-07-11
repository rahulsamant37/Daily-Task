# DSA Problem 316

'''
Problem Statement:
You are given a list of integers, `nums`, and an integer `k`. Your task is to find out if there are two distinct indices `i` and `j` in the list such that `nums[i] = nums[j]` and the absolute difference between `i` and `j` is at most `k`. Design a function `containsNearbyDuplicate` that returns `True` if such indices exist and `False` otherwise.

Example:
Input: nums = [1,2,3,1], k = 3
Output: True
Explanation: nums[0] == nums[3] and the absolute difference between 0 and 3 is 3, which is at most k (3).

Input: nums = [1,0,1,1], k = 1
Output: True
Explanation: nums[2] == nums[3] and the absolute difference between 2 and 3 is 1, which is at most k (1).

Input: nums = [1,2,3,1,2,3], k = 2
Output: False
Explanation: There are duplicates, but the absolute difference between the indices of duplicates is greater than 2.
'''

Solution:
def containsNearbyDuplicate(nums, k):
    index_map = {}
    for i, num in enumerate(nums):
        if num in index_map and i - index_map[num] <= k:
            return True
        index_map[num] = i
    return False

# Test the function
print(containsNearbyDuplicate([1,2,3,1], 3))  # True
print(containsNearbyDuplicate([1,0,1,1], 1))  # True
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))  # False
'''

This DSA problem involves using a dictionary to track the last seen index of each number in the list. The solution checks if the current number has been seen before and if the difference between the current index and the stored index is less than or equal to `k`.