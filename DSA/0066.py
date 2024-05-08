# DSA Problem 66

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to determine if there are two distinct indices `i` and `j` in the array such that `nums[i] = nums[j]` and the absolute difference between `i` and `j` is at most `k`. In other words, you need to find if there are any duplicate numbers within a `k` distance from each other in the array.

For example, for the array [1, 2, 3, 1] and `k = 3`, the answer would be `True` since the number 1 appears twice and the distance between the two appearances is 3, which is equal to `k`.

Constraints:
- The array `nums` will have between 1 and 10^5 elements.
- Each element in `nums` will be an integer between -10^5 and 10^5.
- `k` will be a non-negative integer less than the length of `nums`.
'''

Solution:
```python
def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    # Dictionary to store the last index of each number encountered
    index_map = {}
    
    for i, num in enumerate(nums):
        if num in index_map and i - index_map[num] <= k:
            return True
        index_map[num] = i
    
    return False

# Example check function
def check_solution():
    assert containsNearbyDuplicate([1,2,3,1], 3) == True, "Example 1 failed"
    assert containsNearbyDuplicate([1,0,1,1], 1) == True, "Example 2 failed"
    assert containsNearbyDuplicate([1,2,3,1,2,3], 2) == False, "Example 3 failed"
    print("All examples passed")

check_solution()
```

This Python solution efficiently checks for the presence of duplicates within the specified `k` distance by leveraging a dictionary to track the last seen index of each number. This solution is optimal with a time complexity of O(n), where `n` is the length of the input list `nums`.