# DSA Problem 128

'''
Problem Statement:
You are given a list of integers and a positive integer k. Your task is to find the longest contiguous subarray such that the sum of the elements in the subarray is divisible by k. If there are multiple subarrays of the same maximum length, return the one that appears first.

For example, given the list [5, 2, 6, 1, 4, 3] and k = 3, the longest subarray where the sum is divisible by 3 is [5, 2, 6, 1], since 5 + 2 + 6 + 1 = 14, which is divisible by 3. Note that [1, 4, 3] also sums to 8, which is divisible by 3, but it is not the longest.
'''

Solution:
```python
def longest_divisible_subarray(nums, k):
    sum_indices = {0: -1}
    current_sum = 0
    max_length = 0
    start_index = 0
    
    for index, num in enumerate(nums):
        current_sum += num
        mod_sum = current_sum % k
        
        if mod_sum not in sum_indices:
            sum_indices[mod_sum] = index
        else:
            subarray_length = index - sum_indices[mod_sum]
            if subarray_length > max_length:
                max_length = subarray_length
                start_index = sum_indices[mod_sum] + 1
                
    return nums[start_index:start_index + max_length]

# Test the function
nums = [5, 2, 6, 1, 4, 3]
k = 3
print(longest_divisible_subarray(nums, k))  # Output should be [5, 2, 6, 1]
```

This Python solution defines a function `longest_divisible_subarray` that takes a list of integers `nums` and a positive integer `k`, then returns the longest subarray where the sum of elements is divisible by `k`. It uses a dictionary to track the earliest occurrence of each remainder (`mod_sum`) when summing the elements of the array. This allows the function to efficiently find the longest subarray that meets the criteria.