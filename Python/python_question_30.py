# Python Question: Fibonacci Series using Recursion
'''
Given a positive number n, generate a series of numbers where each number is the sum of the previous two numbers in the series. For example,

Input: n = 5
Output: [0, 1, 1, 2, 3, 5]
'''

# Solution
def fibonacci(n, a=0, b=1):
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return a
    elif n == 2:
        return b
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test cases
def test_fibonacci():
    assert fibonacci(0) == 0, "Fibonacci(0) is not returning 0"
    assert fibonacci(1) == 1, "Fibonacci(1) is not returning 1"
    assert fibonacci(2) == 1, "Fibonacci(2) is not returning 1"
    assert fibonacci(5) == 5, "Fibonacci(5) is not returning 5"
    assert fibonacci(10) == 55, "Fibonacci(10) is not returning 55"
    assert fibonacci(15) == 89, "Fibonacci(15) is not returning 89"

# Main program
if __name__ == "__main__":
    test_fibonacci()