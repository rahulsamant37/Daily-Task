# Python Question: Fibonacci Series till a given number
'''
Given a positive number n, write a function to print the Fibonacci series till the number n.

Example:
Input: n = 10
Output: 144
'''

# Solution
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        result = a
        a, b = b, a + b
        print(result)

# Test cases
def test_fibonacci():
    fibonacci(10)
    fibonacci(15)

# Run the test cases
test_fibonacci()