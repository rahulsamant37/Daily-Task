# Python Question: Fibonacci Series till a given number
'''
You are given a number n, your task is to find the Fibonacci series till that number. A Fibonacci series is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

Example:
Input: n = 10
Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''

def fibonacci(n):
    # Initialize first two numbers of the series
    a, b = 0, 1

    # Generate the series till the given number
    fib_series = [a]
    while b < n:
        fib_series.append(b)
        a, b = b, a + b
    return fib_series

def main():
    n = int(input("Enter the number for which you want to generate Fibonacci series: "))
    print(fibonacci(n))

if __name__ == "__main__":
    main()