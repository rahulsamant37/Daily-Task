# DSA Problem 83

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to return the length of the longest subarray where the difference between the maximum and minimum values in that subarray is less than or equal to `k`. If no such subarray exists, return 0.

For example, if nums = [4, 2, 2, 4, 2] and k = 1, then the longest subarray where the difference between the maximum and minimum values is less than or equal to 1 is [2, 2, 2], hence the function should return 3.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
- 0 <= k <= 10^4
'''

Solution:
```python
from collections import deque

def longest_subarray(nums, k):
    max_q = deque()
    min_q = deque()
    start = 0
    max_length = 0
    
    for end in range(len(nums)):
        # Maintain max_q
        while max_q and nums[end] > nums[max_q[-1]]:
            max_q.pop()
        max_q.append(end)
        
        # Maintain min_q
        while min_q and nums[end] < nums[min_q[-1]]:
            min_q.pop()
        min_q.append(end)
        
        # Shrink the window if the condition is not met
        while nums[max_q[0]] - nums[min_q[0]] > k:
            if max_q[0] == start:
                max_q.popleft()
            if min_q[0] == start:
                min_q.popleft()
            start += 1
        
        # Update the maximum length
        max_length = max(max_length, end - start + 1)
    
    return max_length

# Example check (You can remove or comment out this part before submitting your solution)
nums = [4, 2, 2, 4, 2]
k = 1
print(longest_subarray(nums, k))  # Expected output: 3
```

This Python function implements a sliding window approach to find the longest subarray meeting the specified criteria. It uses two deques to maintain the indices of the maximum and minimum values within the current window of the array.