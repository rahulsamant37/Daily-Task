# DSA Problem 296

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, find the maximum sum of any contiguous subarray of size exactly `k`. If the list is empty or the size of `k` is not valid, return 0.

For example, given nums = [2, 1, 5, 1, 3, 2] and k = 3, the output should be 9, since the subarray with the largest sum is [5, 1, 3].
'''

Solution:
```python
def max_sum_subarray(nums, k):
    if not nums or k <= 0 or k > len(nums):
        return 0
    
    max_sum = current_sum = sum(nums[:k])
    
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, current_sum)
        
    return max_sum

# Example usage
nums = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(nums, k))  # Output: 9
```

This code defines a function `max_sum_subarray` that calculates the maximum sum of any contiguous subarray of size `k` within the input list `nums`. It uses a sliding window approach to efficiently find the solution without recalculating the sum of each subarray from scratch.