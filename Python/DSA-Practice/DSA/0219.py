# DSA Problem 219

'''
Problem Statement:
You are given a list of integers `nums`. Your task is to find the maximum number of non-overlapping subarrays whose sum is exactly equal to a given value `target`. Each subarray must consist of consecutive elements from the original list.

For example, given `nums = [1, 2, 3, 4, 5, 6]` and `target = 9`, the subarrays `[1, 2, 3]` and `[4, 5]` both sum to `9`, but since they overlap, you can only count one of them. The maximum number of non-overlapping subarrays that sum up to `9` is `1` in this case.
'''

Solution:
```python
def maxNonOverlappingSubarrays(nums, target):
    sum_indices = {0: -1}
    current_sum = 0
    count = 0
    last_end = -1
    
    for i, num in enumerate(nums):
        current_sum += num
        if (current_sum - target) in sum_indices and sum_indices[current_sum - target] >= last_end:
            count += 1
            last_end = i
        sum_indices[current_sum] = i
    
    return count

# Example check
print(maxNonOverlappingSubarrays([1, 2, 3, 4, 5, 6], 9))  # Output: 1
```

This Python function `maxNonOverlappingSubarrays` computes the maximum number of non-overlapping subarrays in `nums` whose sum equals `target`. It uses a dictionary `sum_indices` to track the first occurrence of each cumulative sum to efficiently find subarrays with the desired sum.