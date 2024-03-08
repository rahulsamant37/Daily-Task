# Python Question: Find the largest number that can be divided by each number from 2 to 10 without any remainder
'''
Write a Python program to find the largest number that can be divided by each number from 2 to 10 without any remainder.

Example:
Input: List of numbers [2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: 60 (30 divided by all numbers from 2 to 10 without any remainder)
'''

def largest_divisible_number(numbers):
    # Initialize the largest number as 1
    largest_number = 1
    
    # Iterate through the numbers from 2 to 10
    for i in range(2, 11):
        # Check if the current number divides the largest number without any remainder
        if numbers[0] % i == 0:
            # If it does, update the largest number to the sum of the previous largest number and the current number
            largest_number = largest_number + numbers[0]
    
    return largest_number

# Example input and output
numbers = [30]
print(largest_divisible_number(numbers))  # Output: 30

numbers = [24, 18, 15]
print(largest_divisible_number(numbers))  # Output: 24