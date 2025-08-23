# DSA Problem 116

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find out if there are two distinct indices `i` and `j` in the array such that `nums[i]` is equal to `nums[j]` and the absolute difference between `i` and `j` is at most `k`.

For example, given the array [1, 2, 3, 1] and `k = 3`, the function should return `True` because there are two `1`s and the indices of these `1`s differ by at most `3`. However, for the same array with `k = 2`, the function should return `False` because the indices of the two `1`s differ by `3`, which is greater than `k`.

Write a function `containsNearbyDuplicate(nums, k)` to solve the given problem.

Constraints:
1. 1 <= len(nums) <= 10^5
2. -2^31 <= nums[i] <= 2^31 - 1
3. 0 <= k <= 10^5
'''

Solution:
```python
def containsNearbyDuplicate(nums, k):
    num_dict = {}
    for i, num in enumerate(nums):
        if num in num_dict and i - num_dict[num] <= k:
            return True
        num_dict[num] = i
    return False

# Example check function
def check_solution():
    assert containsNearbyDuplicate([1, 2, 3, 1], 3) == True, "Test case 1 failed"
    assert containsNearbyDuplicate([1, 0, 1, 1], 1) == True, "Test case 2 failed"
    assert containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False, "Test case 3 failed"
    print("All test cases passed!")

check_solution()
```

This Python code snippet defines a function `containsNearbyDuplicate` that takes a list of integers and an integer `k` as input and returns `True` if there are duplicates in the list within `k` distance, and `False` otherwise. It also includes a check function to verify the correctness of the solution with some test cases.