# DSA Problem 82

'''
Problem Statement:
A sequence of positive integers, `nums`, and a positive integer `k` are given. You need to find the number of contiguous subarrays of `nums` where the largest number in the subarray is exactly `k`. For example, if `nums = [2, 1, 5, 2, 4]` and `k = 5`, the answer would be 4 because the subarrays are [5], [2, 1, 5], [1, 5], and [5].

Write a function that takes an array of positive integers and a positive integer `k`, and returns the number of contiguous subarrays where the largest number is exactly `k`.
'''

Solution:
```python
def count_subarrays_with_max_k(nums, k):
    def count_subarrays_le_k(arr, x):
        count = 0
        subarray_count = 0
        for num in arr:
            if num > x:
                subarray_count = 0
            else:
                subarray_count += 1
                count += subarray_count
        return count

    return count_subarrays_le_k(nums, k) - count_subarrays_le_k(nums, k-1)

# Example check function
def check_solution():
    assert count_subarrays_with_max_k([2, 1, 5, 2, 4], 5) == 4
    assert count_subarrays_with_max_k([10, 9, 8, 7], 8) == 3
    print("All test cases passed.")

check_solution()
```

This solution defines a function `count_subarrays_with_max_k` that calculates the number of subarrays where the maximum is exactly `k` by leveraging the helper function `count_subarrays_le_k` which counts the number of subarrays where all elements are less than or equal to a given value `x`. The difference between the number of subarrays with a maximum less than or equal to `k` and those less than or equal to `k-1` gives the desired count.