# DSA Problem 5

'''
Problem Statement:
You are given a list of non-negative integers, `nums`, and an integer `k`. Your task is to find the length of the shortest, non-empty, contiguous subarray of `nums` with a sum of at least `k`. If there isn't one, return 0.

For example, given nums = [2,3,1,2,4,3] and k = 7, the answer is 2, because the subarray [4,3] is the shortest with a sum >= 7.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
- 1 <= k <= 10^9
'''

Solution:
```python
from collections import deque

def shortest_subarray(nums, k):
    """
    Finds the length of the shortest, non-empty, contiguous subarray of nums with a sum of at least k.
    """
    n = len(nums)
    shortest = n + 1  # Initialize with a value greater than the max possible length of subarray
    deque_sum = deque()  # Will store indices of nums elements
    current_sum = 0

    for i in range(n):
        current_sum += nums[i]
        if current_sum >= k:
            shortest = min(shortest, i + 1)
        while deque_sum and current_sum - nums[deque_sum[0]] >= k:
            current_sum -= nums[deque_sum.popleft()]
        while deque_sum and nums[deque_sum[-1]] >= nums[i]:
            deque_sum.pop()
        deque_sum.append(i)

    return shortest if shortest <= n else 0

# Example check:
print(shortest_subarray([2,3,1,2,4,3], 7))  # Expected output: 2
```

This solution uses a sliding window technique to find the shortest subarray with a sum of at least `k`. It employs a deque to maintain the indices of elements in the current window, optimizing the search for the subarray.