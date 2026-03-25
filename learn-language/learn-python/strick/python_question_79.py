# Python Question: Calculate the factorial of a number using recursion
'''
Given a positive integer, find its factorial using recursion. The factorial of a number n, denoted as n!, is the product of all positive integers less than or equal to n.

Example:
Input: n = 5
Output: 120 (5! = 5 × 4 × 3 × 2 × 1 = 120)
'''

def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)

def main():
    num = int(input("Enter a positive integer: "))
    if num < 0:
        print("Invalid input. Please enter a positive integer.")
    elif num == 0:
        print("Factorial of", num, "is", recursive_factorial(num))
    else:
        print("Factorial of", num, "is", recursive_factorial(num))

if __name__ == "__main__":
    main()

# Output:
# Enter a positive integer: 5
# Factorial of 5 is 120