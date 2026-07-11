# DSA Problem 344

'''
Problem Statement:
You are given a list of positive integers `nums` and an integer `k`. Your task is to find the smallest length of a contiguous subarray of `nums` such that the sum of its elements is greater than or equal to `k`. If there is no such subarray, return 0.

For example, given `nums = [2, 3, 1, 2, 4, 3]` and `k = 7`, the subarray [4, 3] has the smallest length (2) and its sum is greater than or equal to `k`.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
- 1 <= k <= 10^9
'''

Solution:
```python
def min_subarray_length(nums, k):
    n = len(nums)
    min_length = float('inf')
    current_sum = 0
    start = 0
    
    for end in range(n):
        current_sum += nums[end]
        
        while current_sum >= k:
            min_length = min(min_length, end - start + 1)
            current_sum -= nums[start]
            start += 1
    
    return min_length if min_length != float('inf') else 0

# Example usage
nums = [2, 3, 1, 2, 4, 3]
k = 7
print(min_subarray_length(nums, k))  # Output: 2
```

This solution uses a sliding window approach to find the smallest subarray length efficiently. It iterates through the list while maintaining a running sum and adjusts the window size to ensure the sum is at least `k`.