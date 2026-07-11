# DSA Problem 155

'''
Problem Statement:
You are given an array of integers and an integer k. Your task is to find the maximum for each and every contiguous subarray of size k.

For example, if the array is [1, 3, -1, -3, 5, 3, 6, 7] and k is 3, the maximum values for each contiguous subarray of size 3 are [3, 3, 5, 5, 6, 7].

Write a function `max_in_subarrays(nums, k)` that returns a list containing the maximum value of each subarray of size k.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
'''

Solution:
```python
from collections import deque

def max_in_subarrays(nums, k):
    if not nums:
        return []
    
    # Initialize deque and result list
    deq = deque()
    result = []
    
    for i in range(len(nums)):
        # Remove elements out of the current window from the front
        if deq and deq[0] == i - k:
            deq.popleft()
        
        # Remove elements smaller than the current element from the back
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        
        deq.append(i)
        
        # Start adding max to the result list for the first subarray
        if i >= k - 1:
            result.append(nums[deq[0]])
    
    return result

# Test the function
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_in_subarrays(nums, k))  # Output: [3, 3, 5, 5, 6, 7]
```

This Python solution makes use of a deque to keep track of the indices of the elements that are candidates for the maximum value in the current window of size k. It ensures that the deque is always in a state where its front holds the maximum value for the current window.