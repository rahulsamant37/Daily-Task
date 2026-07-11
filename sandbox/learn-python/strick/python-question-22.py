# Python Question: Find the largest number that can be divided by each number from 2 to n without any remainder

'''
Problem Statement: Given an integer n, find the largest number that can be divided by each number from 2 to n without any remainder.

Example:

Input: n = 5
Output: 120 (Largest number that can be divided by 2, 3, 4, 5 without any remainder)
'''

# Solution
def largest_divisible_by_numbers(n):
    # Initialize the result with 1
    result = 1
    for i in range(2, n + 1):
        # Calculate the product of numbers from 2 to i
        result = result * (i // result)
    return result

# Test Cases
def test_largest_divisible_by_numbers():
    assert largest_divisible_by_numbers(5) == 120, "For n = 5, the expected result is 120"
    assert largest_divisible_by_numbers(10) == 456, "For n = 10, the expected result is 456"

if __name__ == "__main__":
    test_largest_divisible_by_numbers()