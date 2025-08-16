# Python Question: Fibonacci Series till a given number
'''
A series of numbers in which each number is the sum of the two preceding ones is called the Fibonacci sequence. Write a program to generate the Fibonacci series till a given number.

Example:
Input: n = 10
Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
'''

def fibonacci(n):
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

def main():
    n = int(input("Enter the value of n: "))
    print("Fibonacci Series till", n, "is:", fibonacci(n))

if __name__ == "__main__":
    main()