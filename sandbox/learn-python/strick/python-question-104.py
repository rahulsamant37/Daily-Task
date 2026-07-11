# Python Question: Calculate the factorial of a number using recursion
'''
Given a positive integer, n, calculate its factorial using recursion. The factorial of a number n, denoted as n!, is the product of all positive integers less than or equal to n. For example, factorial of 5 (5!)=5*4*3*2*1 = 120
'''

# Solution
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test cases
def test_factorial():
    assert factorial(0) == 1, "For n = 0, factorial should be 1"
    assert factorial(1) == 1, "For n = 1, factorial should be 1"
    assert factorial(5) == 120, "For n = 5, factorial should be 120"
    assert factorial(10) == 3628800, "For n = 10, factorial should be 3628800"

if __name__ == "__main__":
    test_factorial()

# Output