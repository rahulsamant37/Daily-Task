# Python Question: Calculate the sum of squares of the first n natural numbers

'''
Problem Statement:
Given a positive integer n, calculate the sum of squares of the first n natural numbers.

Example:
Input: n = 5
Output: 55 (1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55)
'''

# Solution
def sum_of_squares(n):
    result = 0
    for i in range(1, n+1):
        result += i**2
    return result

# Test Cases
def test_sum_of_squares():
    assert sum_of_squares(1) == 1, 'For n=1, the expected result is 1, but got {}'.format(sum_of_squares(1))
    assert sum_of_squares(2) == 9, 'For n=2, the expected result is 9, but got {}'.format(sum_of_squares(2))
    assert sum_of_squares(5) == 55, 'For n=5, the expected result is 55, but got {}'.format(sum_of_squares(5))
    assert sum_of_squares(10) == 385, 'For n=10, the expected result is 385, but got {}'.format(sum_of_squares(10))

# Main Program
if __name__ == "__main__":
    test_sum_of_squares()