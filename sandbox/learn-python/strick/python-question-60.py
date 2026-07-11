# Python Question: Calculate the sum of natural numbers from n to 1
'''
Problem statement: Given a positive integer n, calculate the sum of natural numbers from n to 1.

Example:
Input: n = 5
Output: 15 (Sum of numbers from 5 to 1)
'''

# Solution
def sum_numbers(n):
    '''
    Calculate the sum of natural numbers from n to 1 using a loop.
    '''
    result = 0
    for i in range(1, n+1):
        result += i
    return result

# Test cases
def test_sum_numbers():
    assert sum_numbers(5) == 15, 'Sum of numbers from 5 to 1 should be 15'
    assert sum_numbers(10) == 55, 'Sum of numbers from 10 to 1 should be 55'
    assert sum_numbers(0) == 0, 'Sum of numbers from 0 to 1 should be 0'
    assert sum_numbers(-3) == 0, 'Sum of negative numbers from -3 to 1 should be 0'