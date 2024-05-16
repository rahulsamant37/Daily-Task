# DSA Problem 74

'''
Problem Statement:
You are given a list of positive integers `nums` and an integer `k`. Your task is to find the sum of the smallest k integers in the list. However, there's a twist: you are also given a list of operations `ops`, where each operation is represented as a tuple `(index, value)`. For each operation, you increment the integer at the given index by the given value. The operations must be applied in order before calculating the sum of the smallest k integers. 

Write a function `smallest_k_sum(nums: List[int], k: int, ops: List[Tuple[int, int]]) -> int` that returns the sum of the smallest k integers after all operations have been applied.

Example:
nums = [1, 4, 3, 2]
k = 2
ops = [(0, 5), (2, 2)]
After applying the operations, nums becomes [6, 4, 5, 2]. The sum of the smallest 2 integers is 2 + 4 = 6.
'''

Solution:
from typing import List, Tuple

def smallest_k_sum(nums: List[int], k: int, ops: List[Tuple[int, int]]) -> int:
    # Apply operations
    for index, value in ops:
        nums[index] += value
    
    # Sort the list and sum the smallest k integers
    nums.sort()
    return sum(nums[:k])

# Test the function
nums = [1, 4, 3, 2]
k = 2
ops = [(0, 5), (2, 2)]
print(smallest_k_sum(nums, k, ops))  # Output should be 6

# This solution first applies all the operations on the given indices of `nums`.
# It then sorts the list and sums up the first k elements to find the sum of the smallest k integers.
# This approach ensures that we correctly calculate the result after each operation is applied.
# The time complexity of this solution is O((n + m) log n), where n is the length of `nums` and m is the number of operations.
# The space complexity is O(1), not counting the input and output, as we are sorting the array in place.