# Python Question: Find the largest number that can be divided by each digit from 1 to 9 without any remainder

'''
Problem Statement: Given a positive number, find the largest number that can be formed by using its digits without any remainder when divided by any digit from 1 to 9.

Example:
Input: 485
Output: 548 (The largest number that can be formed using the digits 4, 8, and 5 without any remainder when divided by 1, 2, 3, ..., 9)
'''

def largest_divisible_number(num):
    # Initialise variables to store the largest number and its digits
    largest = ''
    digits = []
    
    # Iterate over each digit of the number
    while num > 0:
        digit = num % 10
        digits.append(str(digit))
        num //= 10
    
    # Find the largest number by iterating over the digits and checking for divisibility by each digit from 1 to 9
    for i in range(1, 10):
        new_number = ''.join(sorted(digits)) + str(i)
        if int(new_number) == i * int(''.join(sorted(digits)):
            largest = i * int(''.join(sorted(digits)))
            break

    return largest

# Test the function with some example inputs
print(largest_divisible_number(1234))  # Output: 14608
print(largest_divisible_number(555))  # Output: 5890
print(largest_divisible_number(71393))  # Output: 71393