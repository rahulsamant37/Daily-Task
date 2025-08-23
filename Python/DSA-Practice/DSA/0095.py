# DSA Problem 95

'''
Problem Statement:
A sequence of integers `nums` and an integer `k` are given. Your task is to find the maximum number of consecutive 1's in the array if you may flip at most `k` 0's to 1's.

For example, if `nums = [1,1,0,0,1,1,1,0,1]` and `k = 2`, the answer would be 6, as we can flip the two zeros to ones, making the longest subarray of ones [1,1,0,0,1,1,1,1,1].
'''

Solution:
```python
def longest_ones(nums, k):
    left, right = 0, 0
    zeros_count = 0
    max_length = 0
    
    while right < len(nums):
        if nums[right] == 0:
            zeros_count += 1
        
        while zeros_count > k:
            if nums[left] == 0:
                zeros_count -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
        right += 1
    
    return max_length

# Example check (the function can be tested with the following lines)
nums = [1,1,0,0,1,1,1,0,1]
k = 2
print(longest_ones(nums, k))  # Expected output: 6
```

This Python function implements a sliding window approach to efficiently find the longest subarray with at most `k` zeros, by flipping them to ones, maximizing the number of consecutive ones.