# DSA Problem 330

'''
Problem Statement:
You are given a list of integers and a positive integer k. Your task is to find the length of the longest subarray where the absolute difference between any two elements is less than or equal to k. If no such subarray exists, return 0.

For example, given the list [1, 2, 3, 4, 5] and k = 2, the longest subarray would be [1, 2, 3] or [2, 3, 4] or [3, 4, 5], as the absolute difference between any two elements in these subarrays is at most 2.

Input:
- A list of integers, nums (1 <= len(nums) <= 10^5)
- An integer k (0 <= k <= 10^6)

Output:
- Return the length of the longest subarray meeting the criteria.
'''

Solution:
```python
def longest_subarray(nums, k):
    from sortedcontainers import SortedList
    
    sl = SortedList()
    left = 0
    max_len = 0
    
    for right in range(len(nums)):
        sl.add(nums[right])
        
        # Ensure the difference between the max and min in the window is <= k
        while sl[-1] - sl[0] > k:
            sl.remove(nums[left])
            left += 1
        
        # Update the maximum length of a valid subarray
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Example check (This part is not part of the problem and solution)
print(longest_subarray([1, 2, 3, 4, 5], 2))  # Expected output: 3
```

Note: This solution uses the `SortedList` from the `sortedcontainers` package for efficient insertion and removal operations while maintaining a sorted order, which is crucial for quickly finding the minimum and maximum elements within the current window. To use this code, make sure to install the `sortedcontainers` package (`pip install sortedcontainers`).