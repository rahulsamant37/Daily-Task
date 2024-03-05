# Python Question: Find the largest number that can be formed using the digits of a given number (1 to 9) without any repetition

'''
For example, consider the number 234. The largest number that can be formed using its digits without any repetition is 243.

Input: A positive integer n (1 to 9)
Output: The largest number that can be formed using its digits without any repetition
'''

# Solution
def largest_digit_number(n):
    # Sort the digits in descending order
    digits_list = sorted([int(digit) for digit in str(n)], reverse=True)
  
    # Construct the largest number using the sorted digits
    result = ''.join([str(digit) for digit in digits_list])
    return int(result)

# Test cases
print(largest_digit_number(125))  # Output: 521 (The largest number can be formed using digits 1, 2, and 5 without repetition)
print(largest_digit_number(356))  # Output: 653 (The largest number can be formed using digits 3, 5, and 6 without repetition)
print(largest_digit_number(8472))  # Output: 2748 (The largest number can be formed using digits 2, 4, 7, and 8 without repetition)