# DSA Problem 154

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, write a function `find_max_subarray` that returns the maximum sum of any contiguous subarray of size exactly `k`. If the list is empty or the size of `k` is invalid, return 0. The function should run in O(n) time complexity, where n is the length of the list.

Example:
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
The function should return 39, as the subarray [10, 23, 3, 1] has the maximum sum of 37.
'''

Solution:
def find_max_subarray(nums, k):
    if not nums or k <= 0 or k > len(nums):
        return 0
    
    max_sum = float('-inf')
    window_sum = 0
    start = 0
    
    for end in range(len(nums)):
        window_sum += nums[end]  # Add the next element to the window
        
        # Slide the window if we've hit the size k
        if end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[start]  # Subtract the element going out
            start += 1  # Slide the window ahead
    
    return max_sum

# Example check
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(find_max_subarray(nums, k))  # Expected output: 39
'''
This problem involves finding the maximum sum of any contiguous subarray of a given size, using a sliding window algorithm to achieve the optimal O(n) time complexity.