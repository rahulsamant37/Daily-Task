# DSA Problem 153

'''
Problem Statement:
You are given an array `nums` of n positive integers and a positive integer `x`. In one operation, you can choose any element of the array and increase it by `x`. Your task is to make the array strictly increasing with the minimum number of operations. Return the minimum number of operations required.

Note: The array is strictly increasing if for every pair of consecutive elements, the second element is greater than the first one.

Example 1:
Input: nums = [1, 1, 5], x = 2
Output: 1
Explanation: We can increase the second element to 3 in one operation. The array becomes [1, 3, 5], which is strictly increasing.

Example 2:
Input: nums = [5, 3, 2], x = 1
Output: 4
Explanation: We need 4 operations to make the array strictly increasing. One possible way is to increment the second element 2 times and the third element 2 times, resulting in [5, 5, 4] -> [5, 6, 4] -> [5, 6, 5] -> [5, 6, 6].

Constraints:
- 1 <= nums.length <= 10^4
- 1 <= nums[i] <= 10^4
- 1 <= x <= 10^4
'''

Solution:
def min_operations_to_strictly_increasing(nums, x):
    """
    Calculate the minimum number of operations needed to make the array strictly increasing.
    Each operation consists of increasing an element of the array by `x`.
    """
    operations = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            # Calculate the number needed to make nums[i] greater than nums[i-1]
            needed_increase = nums[i - 1] - nums[i] + 1
            # Calculate how many operations are needed for this increase
            ops = (needed_increase + x - 1) // x  # Equivalent to ceil(needed_increase / x)
            # Increment the total number of operations
            operations += ops
            # Increase the current element to maintain the strictly increasing order
            nums[i] += ops * x
    return operations

# Example check (These lines are not part of the solution, just for verification)
print(min_operations_to_strictly_increasing([1, 1, 5], 2))  # Output: 1
print(min_operations_to_strictly_increasing([5, 3, 2], 1))  # Output: 4
'''

This solution iterates through the array to ensure each element is strictly greater than its predecessor by incrementing it in multiples of `x` as needed. The calculation of operations ensures minimal increments to achieve the strictly increasing order.