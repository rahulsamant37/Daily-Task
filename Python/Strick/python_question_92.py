# Python Question: Fibonacci Series
'''
Problem statement: Given a positive number 'n', find the nth number in the Fibonacci series.

Example:
Input: n = 5
Output: 8
'''

# Solution
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Test cases
def test_fibonacci():
    assert fibonacci(0) == 0, "Zero is not part of Fibonacci series"
    assert fibonacci(1) == 1, "First number in Fibonacci series is 1"
    assert fibonacci(5) == 8, "(0, 1, 1, 2, 3) -> (0, 1, 1, 2, 3)"
    assert fibonacci(10) == 55, "(1, 1, 2, 3, 5, 8, 13, 21, 34, 55) -> (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)

if __name__ == "__main__":
    test_fibonacci()