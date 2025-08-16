# Python Question: Calculating Fibonacci Series till a given number
'''
Given a positive number 'n', write a function that calculates the Fibonacci series up to 'n'. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually the first two: 0, 1, 1, 2, 3, 5, 8, 13, ...

Example:

Input: n = 10
Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''

def fibonacci_series(n):
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

def print_fibonacci_series(n):
    result = fibonacci_series(n)
    for x in result:
        print(x, end=' ')

if __name__ == "__main__":
    n = int(input("Enter a positive number: "))
    print_fibonacci_series(n)