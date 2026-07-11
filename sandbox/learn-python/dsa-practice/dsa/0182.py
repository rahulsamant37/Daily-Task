# DSA Problem 182

'''
Problem Statement:
A sequence of positive integers is given, and you are allowed to perform the following operation on this sequence any number of times: choose two adjacent elements, say x and y, and replace them with a single element equal to their greatest common divisor (GCD). Determine the minimum possible value that can be obtained as the final single element after performing the operation any number of times on the sequence.

For example, if the sequence is [12, 16, 24], you can first replace 12 and 16 with their GCD, which is 4, turning the sequence into [4, 24], and then replace 4 and 24 with their GCD, which is 4. Thus, the minimum value you can end up with is 4.

Write a function that takes a list of positive integers as input and returns the minimum possible value that can be obtained by performing the specified operation on the sequence.

Constraints:
- 1 <= len(sequence) <= 1000
- 1 <= sequence[i] <= 10^6
'''

Solution:
```python
from math import gcd
from functools import reduce

def min_possible_value(sequence):
    """
    Finds the minimum possible value that can be obtained by repeatedly
    replacing two adjacent elements with their GCD in the given sequence.
    """
    return reduce(gcd, sequence)

# Example check function
def check_solution():
    assert min_possible_value([12, 16, 24]) == 4
    assert min_possible_value([2, 4, 8, 16]) == 2
    assert min_possible_value([7, 35, 70]) == 7
    assert min_possible_value([100, 200, 50]) == 50
    print("All tests passed.")

check_solution()
```

This problem requires understanding of the GCD operation and how it can be applied iteratively across a sequence of numbers to find the minimum possible value that can be obtained. The solution elegantly makes use of Python's `reduce` function from the `functools` module to apply the GCD function across the entire list.