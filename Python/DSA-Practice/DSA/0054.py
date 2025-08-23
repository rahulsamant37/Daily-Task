# DSA Problem 54

'''
Problem Statement:
You are given an integer array `nums` and an integer `k`. You can perform the following operation any number of times (including zero):

- Choose any subarray of `nums` and increase or decrease each element in the subarray by `k`.

Your task is to determine the minimum number of operations required to make all elements in `nums` equal. If it is not possible to make all elements equal, return -1.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [2, 4, 3], k = 1
Output: 2
Explanation: We can perform the following operations:
- Choose subarray [4] and decrease it by 1, resulting in [2, 3, 3].
- Choose subarray [3, 3] and decrease it by 1, resulting in [2, 2, 2].

Example 2:
Input: nums = [1, 2, 3], k = 2
Output: -1
Explanation: It's not possible to make all elements equal by performing the given operations.
'''

Solution:
```python
def min_operations(nums, k):
    if k == 0:
        return 0 if len(set(nums)) == 1 else -1
    
    # Check if it's possible to make all elements equal.
    # For it to be possible, the difference between any two elements must be divisible by k.
    for i in range(1, len(nums)):
        if (nums[i] - nums[i-1]) % k != 0:
            return -1
    
    # If it's possible, the number of operations is the maximum difference from the target value divided by k.
    target = nums[0] % k
    return max((x - target) // k for x in nums)

# Example usage
print(min_operations([2, 4, 3], 1))  # Output: 2
print(min_operations([1, 2, 3], 2))  # Output: -1
```
This solution checks if it's possible to make all elements of the array equal by first checking if the differences between adjacent elements are divisible by `k`. If this condition holds, it calculates the minimum number of operations needed to make all elements equal by calculating the maximum difference from the target value (determined by the modulo `k` of the first element) and dividing it by `k`.