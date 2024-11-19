# Python Question: Fibonacci Series up to a Given Number
'''
Problem Statement:
Consider a series of numbers where each number is the sum of the two preceding ones. This series is known as the Fibonacci series. Write a function that takes an integer n as input and returns the Fibonacci series up to that number.

Example:
Input: n = 5
Output: [0, 1, 1, 2, 3, 5]
'''

# Solution
def fibonacci_series(n):
    a, b, temp = 0, 1, 0
    result = [temp]
    while a < n:
        temp = a
        a, b = b, a + b
        result.append(b)
    return result

# Test Cases
def test_fibonacci_series():
    assert fibonacci_series(0) == []
    assert fibonacci_series(1) == [1]
    assert fibonacci_series(5) == [0, 1, 1, 2, 3, 5]
    print(fibonacci_series(10)) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Main Program
if __name__ == "__main__":
    test_fibonacci_series()