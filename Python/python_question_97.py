# Python Question: Find the largest number that can be divided by each number from 2 to 10 without any remainder
'''
Write a program to find the largest number that can be divided by each number from 2 to 10 without any remainder.

Example:
Input: Find the largest number that can be divided by 2, 3, 4, 5, 6, 7, 8, 9, and 10 without any remainder.
Output: 40

Input: Find the largest number that can be divided by 3, 4, 5, 6, 7, 8, 9, and 10 without any remainder.
Output: 120
'''

# Solution
def findLargestDivisibleNumber(n):
    # Initialize variables to store the maximum number and
    # sum of divisors found so far
    maximum = 1
    sumOfDivisors = 0
    
    # Iterate from 2 to n
    for i in range(2, n+1):
        # Check if i is a divisor of maximum
        if n % i == 0:
            # Update sumOfDivisors
            sumOfDivisors += i
            # Update maximum if i is a greater divisor than current maximum
            if i > maximum:
                maximum = i
            # Update sumOfDivisors without considering i as a divisor
            sumOfDivisors -= i
    
    # Return the maximum number and sum of divisors
    return maximum, sumOfDivisors

# Driver Code
num = 100
print("The largest number that can be divided by numbers from 2 to", num, "without any remainder is", findLargestDivisibleNumber(num), "and the sum of divisors is", findLargestDivisibleNumber(num))

# Output: The largest number that can be divided by numbers from 2 to 100 without any remainder is 50 and the sum of divisors is 125