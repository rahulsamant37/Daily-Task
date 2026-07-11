# Python Question: Find the largest number that can be divided by each number from 2 to 10 without any remainder

'''
Write a Python program to find the largest number that can be divided by each number from 2 to 10 without any remainder.

Example:
Input: Find the largest number that can be divided by each number from 2 to 10 without any remainder.
Output: 50 (as 50 is the largest number which can be divided by all numbers from 2 to 10 without any remainder)
'''

def largest_number(n):
    # Initialize the largest number
    largest_number = 1

    # Iterate from 2 to n
    for i in range(2, n+1):
        # If number is divisible by current iteration value, add it to largest number
        if i % largest_number == 0:
            largest_number += i
    
    return largest_number

def main():
    n = 10
    print(largest_number(n))

if __name__ == "__main__":
    main()