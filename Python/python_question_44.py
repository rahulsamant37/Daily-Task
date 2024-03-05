# Python Question: Fibonacci Series using Recursion
'''
Given a positive integer n, write a recursive function to calculate the n-th number in the Fibonacci series.

Example:
Input: n = 5
Output: 8

Explanation:
The first 5 numbers in the Fibonacci series are 0, 1, 1, 2, 3.
'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def test_fibonacci():
    assert fibonacci(0) == 0, "Recursive Fibonacci function should return 0 for n = 0"
    assert fibonacci(1) == 1, "Recursive Fibonacci function should return 1 for n = 1"
    assert fibonacci(5) == 8, "Recursive Fibonacci function for n = 5 should return 8"
    assert fibonacci(10) == 55, "Recursive Fibonacci function for n = 10 should return 55"

if __name__ == "__main__":
    test_fibonacci()