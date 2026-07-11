# Python Question: Sum of Numbers from k to n (Recursion)
'''
Problem statement:
Given two integers, k and n, find the sum of all numbers from k to n.

Example:
Input: k = 3, n = 8
Output: 21 (3 + 4 + 5 + 6 + 7 + 8 = 21)
'''

# Solution
def sumRangeRecursion(k, n):
    if k > n:
        return 0
    return k + sumRangeRecursion(k+1, n)

# Test cases
def test_sumRangeRecursion():
    assert sumRangeRecursion(1, 4) == 10, "Expected 10, Got {}".format(sumRangeRecursion(1, 4))
    assert sumRangeRecursion(5, 10) == 55, "Expected 55, Got {}".format(sumRangeRecursion(5, 10))
    assert sumRangeRecursion(3, 8) == 21, "Expected 21, Got {}".format(sumRangeRecursion(3, 8))
    assert sumRangeRecursion(0, 0) == 0, "Expected 0, Got {}".format(sumRangeRecursion(0, 0))
    assert sumRangeRecursion(1, 5) == 15, "Expected 15, Got {}".format(sumRangeRecursion(1, 5))

test_sumRangeRecursion()