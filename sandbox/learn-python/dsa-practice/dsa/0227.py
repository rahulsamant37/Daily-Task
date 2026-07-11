# DSA Problem 227

'''
Problem Statement:
You are given a list of positive integers `nums` and a positive integer `k`. Your task is to find the maximum sum of any contiguous subarray of size `k` in `nums`. If `k` is larger than the length of `nums`, return -1 as it's not possible to create a subarray of that size.

For example, if `nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]` and `k = 4`, the function should return the maximum sum of all possible subarrays of size 4, which is 39 (from the subarray [10, 23, 3, 1]).
'''

Solution:
```python
def max_sum_subarray(nums, k):
    if k > len(nums):
        return -1
    max_sum = 0
    # Calculate the sum of the first subarray of size k
    for i in range(k):
        max_sum += nums[i]
    temp_sum = max_sum
    # Use sliding window to find the maximum sum of any subarray of size k
    for i in range(k, len(nums)):
        temp_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, temp_sum)
    return max_sum

# Example usage
nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(max_sum_subarray(nums, k))  # Output: 39
```

This Python code defines a function `max_sum_subarray` which takes a list of positive integers `nums` and a positive integer `k` as input, and returns the maximum sum of any contiguous subarray of size `k` in `nums`. It employs a sliding window technique to efficiently compute the maximum sum without recalculating the sum of overlapping parts of the subarrays. If `k` exceeds the length of `nums`, the function returns -1, indicating the impossibility of the requested operation.