# Python Question: Fibonacci Series
'''
Problem statement: Given an integer n, generate the nth number in the Fibonacci series.
For example, for n = 0, the output should be 0, for n = 1, the output should be 1, for n = 2, the output should be 1, and for n = 3, the output should be 2.
'''

# Solution
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test cases
def test_fibonacci():
    assert fibonacci(0) == 0, "For n = 0, the expected output is 0"
    assert fibonacci(1) == 1, "For n = 1, the expected output is 1"
    assert fibonacci(2) == 1, "For n = 2, the expected output is 1"
    assert fibonacci(3) == 2, "For n = 3, the expected output is 2"
    assert fibonacci(10) == 55, "For n = 10, the expected output is 55"
    assert fibonacci(15) == 89, "For n = 15, the expected output is 89"

# Main program
if __name__ == "__main__":
    test_fibonacci()