# DSA Problem 159

'''
Problem Statement:
You are given a list of positive integers `nums`. You need to find the number of unique pairs (i, j) where i < j and the bitwise AND of `nums[i]` and `nums[j]` is a perfect square. For example, if `nums = [2, 3, 4, 5]`, the only valid pair is (2, 4) because 2 & 4 = 0, and 0 is a perfect square (0^2 = 0). Return the count of such pairs.

Note: A number is a perfect square if it can be expressed as the square of an integer. For example, 1, 4, 9, 16, etc., are perfect squares.
'''

Solution:
```python
from math import isqrt
from itertools import combinations

def is_perfect_square(n):
    return isqrt(n) ** 2 == n

def count_pairs_with_square_and(nums):
    count = 0
    for a, b in combinations(nums, 2):
        if is_perfect_square(a & b):
            count += 1
    return count

# Example check function
def check_solution():
    assert count_pairs_with_square_and([2, 3, 4, 5]) == 1, "Test case 1 failed"
    assert count_pairs_with_square_and([1, 2, 4, 8]) == 0, "Test case 2 failed"
    assert count_pairs_with_square_and([1, 8, 4, 2]) == 2, "Test case 3 failed"
    print("All test cases passed")

check_solution()
```

This solution defines a function `count_pairs_with_square_and` that calculates the number of unique pairs in the list `nums` whose bitwise AND operation results in a perfect square. It uses the `is_perfect_square` function to check if a number is a perfect square and the `combinations` function from the itertools module to generate all unique pairs of indices in the list. The solution also includes a check function with provided data points to verify the correctness of the implemented function.