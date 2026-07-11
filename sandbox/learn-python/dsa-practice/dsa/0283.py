# DSA Problem 283

'''
Problem Statement:
You are given a list of positive integers and a target sum. Your task is to find the length of the shortest contiguous subarray (if any) in the list that sums up to the target sum. If there is no such subarray, return -1.

For example, given the list [1, 4, 20, 3, 10, 5] and the target sum 33, the shortest subarray with the target sum is [20, 3, 10], so the function should return 3.

Input:
- A list of positive integers, nums (1 <= len(nums) <= 10^5)
- An integer, target (1 <= target <= 10^9)

Output:
- An integer representing the length of the shortest contiguous subarray that sums up to the target, or -1 if no such subarray exists.
'''

Solution:
```python
def shortest_subarray_with_sum(nums, target):
    n = len(nums)
    min_length = float('inf')
    current_sum = 0
    start = 0
    
    for end in range(n):
        current_sum += nums[end]
        
        while current_sum >= target:
            if current_sum == target:
                min_length = min(min_length, end - start + 1)
            current_sum -= nums[start]
            start += 1
    
    return min_length if min_length != float('inf') else -1

# Example check (the following lines are not part of the solution)
nums = [1, 4, 20, 3, 10, 5]
target = 33
print(shortest_subarray_with_sum(nums, target))  # Output should be 3
```

This Python function `shortest_subarray_with_sum` efficiently finds the length of the shortest contiguous subarray that sums up to the target sum by using a sliding window approach.