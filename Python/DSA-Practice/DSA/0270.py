# DSA Problem 270

'''
Problem Statement:
You are given a list of integers, `nums`, and an integer `k`. Your task is to find the maximum number of non-overlapping subarrays whose sums are each equal to `k`. A subarray is defined as a contiguous part of the array.

For example, if nums = [1, -1, 2, 2, -1, 3], k = 3, the answer would be 2, because there are two non-overlapping subarrays [1, -1, 2] and [2, -1, 3] whose sums are equal to 3.

Constraints:
- 1 <= nums.length <= 1e5
- -1000 <= nums[i] <= 1000
- -1e7 <= k <= 1e7
'''

Solution:
```python
def maxNonOverlapping(nums, k):
    sum_to_index = {0: -1}
    current_sum = 0
    count = 0
    last_valid_index = -1
    
    for i, num in enumerate(nums):
        current_sum += num
        if (current_sum - k) in sum_to_index and sum_to_index[current_sum - k] >= last_valid_index:
            count += 1
            last_valid_index = i
            # Reset current_sum and sum_to_index to avoid counting overlapping subarrays
            current_sum = 0
            sum_to_index = {0: i}
        else:
            sum_to_index[current_sum] = i
    
    return count

# Example check (the function can be tested with the provided example)
nums = [1, -1, 2, 2, -1, 3]
k = 3
print(maxNonOverlapping(nums, k))  # Expected output: 2
```

This Python function `maxNonOverlapping` solves the problem by using a dictionary to keep track of the sums of subarrays and their indices. It iterates through the list `nums`, accumulating the sum of elements and checking if there exists a subarray that sums up to `k`. Once such a subarray is found, it counts it and resets the sum and index dictionary to ensure subarrays are non-overlapping.