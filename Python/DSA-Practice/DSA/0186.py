# DSA Problem 186

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to determine if there are two distinct indices `i` and `j` in the list such that `nums[i] = nums[j]` and the absolute difference between `i` and `j` is at most `k`.

For example, given the list `[1, 2, 3, 1]` and `k = 3`, the function should return `True` because the value `1` appears at indices `0` and `3`, and the absolute difference between these indices is `3`, which is equal to `k`.

Write a function `has_close_duplicates` that takes a list of integers and an integer `k`, and returns `True` if such a pair of indices exists, and `False` otherwise.
'''

Solution:
```python
def has_close_duplicates(nums, k):
    """
    Determines if there are two distinct indices i and j in the list such that
    nums[i] = nums[j] and the absolute difference between i and j is at most k.
    """
    index_map = {}
    for i, num in enumerate(nums):
        if num in index_map and i - index_map[num] <= k:
            return True
        index_map[num] = i
    return False

# Check function to verify the correctness of the solution
def check_solution():
    assert has_close_duplicates([1, 2, 3, 1], 3) == True, "Test case 1 failed"
    assert has_close_duplicates([1, 0, 1, 1], 1) == True, "Test case 2 failed"
    assert has_close_duplicates([1, 2, 3, 1, 2, 3], 2) == False, "Test case 3 failed"
    print("All test cases passed!")

check_solution()
```
This solution uses a dictionary to keep track of the indices of the numbers we have seen so far, allowing us to efficiently check if a duplicate has been found within the required index distance.