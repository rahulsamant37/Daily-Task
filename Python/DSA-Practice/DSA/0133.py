# DSA Problem 133

'''
Problem Statement:
You are given an array `nums` of positive integers and an integer `k`. You can perform the following operation any number of times: choose any element from `nums` and increase it by `k`. Your task is to find the minimum number of operations required to make all the elements in the array equal. If it is impossible to make all elements equal, return -1.

For example, if `nums = [1, 2, 3]` and `k = 1`, you can make all elements equal in 3 operations: increase the first element twice and the second element once to get `[3, 3, 3]`.
'''

Solution:
```python
def min_operations_to_equalize(nums, k):
    """
    Calculate the minimum number of operations required to make all elements of nums equal
    by increasing elements by k. Returns -1 if it's impossible.
    """
    if k == 0:
        if len(set(nums)) == 1:
            return 0
        else:
            return -1

    max_num = max(nums)
    operations = 0
    for num in nums:
        diff = max_num - num
        if diff % k != 0:
            return -1
        operations += diff // k
    return operations

# Check function with provided data points
def check_solution():
    assert min_operations_to_equalize([4, 1, 6, 0], 2) == 5, "Test case 1 failed"
    assert min_operations_to_equalize([2, 5, 3, 2], 1) == 5, "Test case 2 failed"
    assert min_operations_to_equalize([1, 3, 2], 2) == -1, "Test case 3 failed"
    assert min_operations_to_equalize([5, 5, 5], 0) == 0, "Test case 4 failed"
    assert min_operations_to_equalize([10, 10], 5) == 0, "Test case 5 failed"
    print("All test cases passed!")

check_solution()
```

This code snippet provides a solution to the problem described in the problem statement. It checks if it's possible to make all elements in the array equal by increasing any of the elements by a given integer `k`. If possible, it calculates and returns the minimum number of operations needed; otherwise, it returns -1.