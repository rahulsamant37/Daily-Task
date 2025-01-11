# DSA Problem 308

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, determine if there exists a pair of distinct indices `i` and `j` such that `nums[i] = nums[j]` and the absolute difference between `i` and `j` is at most `k`.

For example, given `nums = [1, 2, 3, 1]` and `k = 3`, the function should return `True` since the number 1 appears at indices 0 and 3, and the absolute difference between these indices is 3, which is less than or equal to `k`.

However, for the same list `nums = [1, 2, 3, 1]` but with `k = 2`, the function should return `False` as the absolute difference between the indices is greater than `k`.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^5
'''

Solution:
```python
def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    seen = {}
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False

# Test the solution
print(containsNearbyDuplicate([1,2,3,1], 3))  # Expected output: True
print(containsNearbyDuplicate([1,0,1,1], 1))  # Expected output: True
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))  # Expected output: False
```

This Python solution uses a dictionary to track the last seen index of each element within `nums`. As it iterates through the list, it checks if the current number has been seen before and if the difference between the current index and the last seen index is less than or equal to `k`. If so, it returns `True`. If no such pair is found, it returns `False` after completing the iteration.