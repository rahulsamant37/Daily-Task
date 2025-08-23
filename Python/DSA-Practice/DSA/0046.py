# DSA Problem 46

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, return the maximum sum of any contiguous subarray of the list that is divisible by `k`. If no such subarray exists, return 0.

For example, if nums = [4, 2, 2, 8, 2, 6, 1] and k = 4, the maximum sum of a subarray divisible by 4 is 12 (subarray [2, 2, 8]).
'''

Solution:
```python
def max_sum_subarray_divisible_k(nums, k):
    prefix_sum = 0
    max_sum = 0
    # Dictionary to store (prefix_sum % k, index). Initialize with (0, -1) to handle cases where the subarray starts from index 0.
    sum_modulo = {0: -1}
    
    for i, num in enumerate(nums):
        prefix_sum += num
        mod = prefix_sum % k
        
        if mod not in sum_modulo:
            sum_modulo[mod] = i
        else:
            # If the same mod was found earlier, it means the subarray [sum_modulo[mod]+1, i] is divisible by k.
            # Calculate the sum of this subarray and update max_sum if this sum is greater.
            subarray_sum = prefix_sum - nums[sum_modulo[mod]]
            max_sum = max(max_sum, subarray_sum)
    
    return max_sum

# Test the function
nums = [4, 2, 2, 8, 2, 6, 1]
k = 4
print(max_sum_subarray_divisible_k(nums, k))  # Expected output: 12
```

Note: The provided solution assumes there's no subarray with a negative sum that would falsely maximize the result due to the modulo operation. In more complex scenarios, additional handling might be required to ensure the correct subarray is selected.