# Python Question: Find the largest number that can be divided by each digit from 1 to 9

'''
Problem Statement: Given a positive integer, find the largest number that can be formed by using its digits from 1 to 9. If a digit is used more than once, it is allowed.

Example:
Input: 123
Output: 999 (largest number using digits of 123)
'''

# Solution
def largest_digit_number(num):
    # Get the digits of the number
    digits = str(num)
    
    # Sort the digits in descending order
    sorted_digits = sorted(digits, reverse=True)
    
    # Reconstruct the number by joining the sorted digits
    output_num = ''.join(sorted_digits)
    
    return int(output_num)

# Test Cases
numbers = [123, 456, 789]

for num in numbers:
    output = largest_digit_number(num)
    print(f"Input: {num}, Output: {output}")