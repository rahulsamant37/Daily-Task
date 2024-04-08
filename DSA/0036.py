# DSA Problem 36

'''
Problem Statement:
Given a list of integers `nums`, write a function `max_subarray_sum` that finds the contiguous subarray (containing at least one number) which has the largest sum and returns its sum. Additionally, provide the start and end indices of this subarray in the original list. If there are multiple subarrays with the same maximum sum, return the indices of any one of them.

For example, if `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`, the function should return the sum 6 and the indices (3, 6), as the subarray [4, -1, 2, 1] has the largest sum.

Constraints:
- The list `nums` will contain between 1 and 10^4 elements.
- Each element in `nums` will be between -10^4 and 10^4.
'''

Solution:
```python
def max_subarray_sum(nums):
    max_sum = curr_sum = nums[0]
    start = end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        if curr_sum < 0:
            curr_sum = nums[i]
            temp_start = i
        else:
            curr_sum += nums[i]
        
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i
    
    return max_sum, (start, end)

# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))  # Output: (6, (3, 6))
```

This solution implements a variation of Kadane's algorithm to find the maximum subarray sum along with its start and end indices. The time complexity of this solution is O(n), where n is the length of the list `nums`.