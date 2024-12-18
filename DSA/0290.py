# DSA Problem 290

'''
Problem Statement:
Given a list of positive integers `nums`, find the number of unique pairs (i, j) where i < j and the product of nums[i] and nums[j] is a perfect square. A perfect square is an integer that is the square of an integer. For example, 1, 4, 9, 16 are perfect squares. 

Your task is to implement a function `countPerfectSquarePairs(nums)` that returns the number of such unique pairs.

Example:
Input: nums = [1, 2, 3, 4, 5, 6]
Output: 2
Explanation: The pairs are (1, 4) and (4, 1) since 1*4 = 4 which is a perfect square. Note that (4, 1) is considered because the function considers order for uniqueness.
'''

Solution:
```python
from math import isqrt
from collections import Counter

def is_perfect_square(x):
    """Check if a number is a perfect square."""
    s = isqrt(x)
    return s * s == x

def countPerfectSquarePairs(nums):
    """
    Counts the number of unique pairs (i, j) in nums such that i < j and nums[i]*nums[j] is a perfect square.
    """
    num_counts = Counter(nums)
    count = 0
    for num1 in num_counts:
        for num2 in num_counts:
            if num1 < num2 and is_perfect_square(num1 * num2):
                count += num_counts[num1] * num_counts[num2]
            elif num1 == num2 and is_perfect_square(num1 * num2) and num_counts[num1] > 1:
                count += num_counts[num1] * (num_counts[num1] - 1) // 2
    return count

# Check function to verify the solution with provided data points
def check():
    assert countPerfectSquarePairs([1, 2, 3, 4, 5, 6]) == 2
    assert countPerfectSquarePairs([2, 2, 2]) == 1
    assert countPerfectSquarePairs([1, 1, 2, 2, 2]) == 4
    print("All tests passed.")

check()
```

This Python code defines a function `countPerfectSquarePairs` that calculates the number of unique pairs in the given list `nums` whose product is a perfect square. It uses a helper function `is_perfect_square` to check if a number is a perfect square and leverages the `collections.Counter` to efficiently count occurrences of each number and potential pairs.