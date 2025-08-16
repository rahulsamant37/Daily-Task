# Python Question: Calculate the factorial of a number
'''
Problem statement: Given a positive integer n, calculate its factorial using a function in Python. The factorial of a number is the product of all positive integers less than or equal to that number.

Example:
Input: n = 5
Output: 120 (5! = 5 × 4 × 3 × 2 × 1)
'''

# Solution:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def get_factorial_result(n):
    result = factorial(n)
    print(f'The factorial of {n} is {result}')

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    get_factorial_result(n)