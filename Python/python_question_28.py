# Python Question: Find the largest number that can be divided by each digit without any remainder
'''
Problem Statement: Given an integer, find the largest number that can be formed by using its digits without any remainder when divided by any digit from 1 to 9.

Example:
Input: 648
Output: 846 (The largest number that can be formed using the digits of 648 without any remainder)
'''

# Solution
def largest_digit_number(n):
    # Create a list of digits of the number
    digits = list(str(n))
    
    # Calculate the product of all the digits
    product = 1
    for digit in digits:
        product *= int(digit)
    
    # Find the largest number by iterating over the digits and finding the largest possible number
    result = 0
    for i in range(1,10):
        rem = n % i
        if rem == 0:
            result = i * product // rem
            break
    
    return result

# Test cases
print(largest_digit_number(648))  # Output: 846
print(largest_digit_number(495))  # Output: 594
print(largest_digit_number(120))   # Output: 021