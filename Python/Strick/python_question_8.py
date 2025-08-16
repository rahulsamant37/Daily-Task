# Python Question: Find the largest number that can be divided by any number from 1 to 10 without any remainder

# Problem Statement
'''
Write a function that takes an integer n as input and returns the largest number that can be divided by any number from 1 to n without any remainder.

For example,

Input: n = 5
Output: 100 (The largest number that can be divided by 1, 2, 3, 4, or 5 without any remainder is 100.)

Input: n = 10
Output: 400 (The largest number that can be divided by 1, 2, 3, ..., or 10 without any remainder is 400.)
'''

# Solution
def findLargestDivisibleNumber(n):
    result = 1
    for num in range(1, n + 1):
        while result % num == 0:
            result //= num
    return result

# Test Cases
def test_solution():
    assert findLargestDivisibleNumber(5) == 100
    assert findLargestDivisibleNumber(10) == 400

if __name__ == "__main__":
    test_solution()