# Python Question: Calculate the factorial of a number using a recursive function
'''
Problem Statement: Given a positive integer n, write a recursive function to calculate its factorial, which is the product of all positive integers less than or equal to n. For example, factorial(5) = 5 * 4 * 3 * 2 * 1.

Example:
Input: n = 5
Output: 120 (5 * 4 * 3 * 2 * 1)
'''

def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

def main():
    test_values = [1, 2, 3, 4, 5]
    for value in test_values:
        print(f"Factorial of {value} is: {recursive_factorial(value)}")

if __name__ == '__main__':
    main()