# Python Question: Fibonacci Series till a given number
'''
Problem statement: Given a positive number n, print the Fibonacci series till n.

Example:
Input: n = 10
Output: 144
1 1 2 3 5 8 13 21 34 55
'''

# Solution
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b


def main():
    n = int(input("Enter the number: "))
    fibonacci(n)


if __name__ == "__main__":
    main()