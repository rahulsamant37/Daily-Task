# DSA Problem 131

'''
Problem Statement:
You are given a list of integers `nums`. Your task is to rotate the list to the right by `k` steps, where `k` is a non-negative integer. A single rotation means taking the last element of the list and moving it to the front, while shifting all other elements one position to the right. After performing the rotations, return the modified list.

For example, if `nums = [1, 2, 3, 4, 5]` and `k = 2`, after the first rotation, the list becomes `[5, 1, 2, 3, 4]`, and after the second rotation, it becomes `[4, 5, 1, 2, 3]`. Therefore, the function should return `[4, 5, 1, 2, 3]`.
'''

Solution:
```python
def rotate_list(nums, k):
    """
    Rotates a list to the right by k steps.
    """
    n = len(nums)
    k = k % n  # In case k is larger than the list size
    if k == 0:
        return nums
    
    # Rotate the list in-place
    nums[:] = nums[-k:] + nums[:-k]
    return nums

# Check function to verify the correctness of the solution
def check():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate_list([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
    assert rotate_list([1, 2], 3) == [2, 1]  # 3 rotations is equivalent to 1 rotation
    print("All tests passed.")

check()
```

This code snippet defines a function `rotate_list` that takes a list of integers and a non-negative integer `k` as input, rotates the list to the right by `k` steps, and then returns the modified list. The `check` function is used to verify the correctness of the solution with given test cases.