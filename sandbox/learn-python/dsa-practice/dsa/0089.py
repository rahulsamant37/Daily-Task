# DSA Problem 89

'''
Problem Statement:
You are given a list of integers and a positive integer k. Your task is to find the maximum sum of a contiguous subarray of length exactly k. The list will contain at least one element and at most 10^5 elements. Each element in the list will be an integer between -10^3 and 10^3.

For example, if the list is [1, 4, 2, 10, 23, 3, 1, 0, 20] and k is 4, the maximum sum of a subarray of length 4 is 39 (10 + 23 + 3 + 1).

Write a function `max_subarray_sum(nums, k)` that returns the maximum sum of any contiguous subarray of length k.
'''

Solution:
```python
def max_subarray_sum(nums, k):
    # Initialize the maximum sum to be the smallest possible integer
    max_sum = float('-inf')
    # Calculate the sum of the first subarray of length k
    current_sum = sum(nums[:k])
    max_sum = max(max_sum, current_sum)
    
    # Slide the window across the list
    for i in range(len(nums) - k):
        # Subtract the element that is left behind and add the new element
        current_sum = current_sum - nums[i] + nums[i + k]
        # Update the maximum sum if needed
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage:
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(max_subarray_sum(nums, k))  # Output: 39
```

This solution uses a sliding window approach to efficiently calculate the sums of all possible subarrays of length k and determine the maximum sum among them. The time complexity is O(n), where n is the length of the list `nums`.