# DSA Problem 205

'''
Problem Statement:
You are given a list of positive integers and a target integer. Your task is to find the length of the smallest contiguous subarray whose sum is greater than or equal to the target. If no such subarray exists, return 0.

Example:
Input: nums = [2, 3, 1, 2, 4, 3], target = 7
Output: 2
Explanation: The subarray [4, 3] has the smallest length and its sum is 7 which is equal to the target.
'''

Solution:
def min_subarray_len_for_sum(nums, target):
    """
    Finds the length of the smallest contiguous subarray with a sum greater than or equal to the target.
    """
    n = len(nums)
    min_length = float('inf')
    left = 0
    current_sum = 0
    
    for right in range(n):
        current_sum += nums[right]
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
            
    return min_length if min_length != float('inf') else 0

# Example check
nums = [2, 3, 1, 2, 4, 3]
target = 7
print(min_subarray_len_for_sum(nums, target))  # Output should be 2

This Python solution efficiently finds the smallest subarray length with a sum greater than or equal to the target using a sliding window approach, ensuring optimal performance even for large lists.