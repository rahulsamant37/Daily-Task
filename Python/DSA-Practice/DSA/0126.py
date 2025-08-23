# DSA Problem 126

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum sum of a subarray with a length of exactly `k`. A subarray is a contiguous part of an array.

For example, given `nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]` and `k = 4`, the subarray with the maximum sum is `[10, 23, 3, 1]`, which has a sum of 37.

Write a function `max_sum_subarray(nums, k)` that returns the maximum sum of any subarray of length `k`.
'''

Solution:
```python
def max_sum_subarray(nums, k):
    """
    Finds the maximum sum of any subarray of length k.

    :param nums: List[int] -- List of integers representing the array.
    :param k: int -- Length of the subarray.
    :return: int -- Maximum sum of any subarray of length k.
    """
    if not nums or k <= 0:
        return 0
    
    max_sum = 0
    window_sum = 0
    
    # Calculate the sum of the first window
    for i in range(k):
        window_sum += nums[i]
    
    max_sum = window_sum
    
    # Slide the window across the list
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Check function to verify the correctness of the solution
def check_function():
    assert max_sum_subarray([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 37, "Test case 1 failed"
    assert max_sum_subarray([1, 4, -2, -1, 5, 3], 3) == 7, "Test case 2 failed"
    assert max_sum_subarray([], 3) == 0, "Test case 3 failed"
    assert max_sum_subarray([2, 3], 3) == 0, "Test case 4 failed"

    print("All test cases passed!")

check_function()
```

This Python function `max_sum_subarray` efficiently computes the maximum sum of any subarray of length `k` using a sliding window technique, achieving an optimal solution with a time complexity of O(n).