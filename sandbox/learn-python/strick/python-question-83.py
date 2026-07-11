# Python Question: Calculate the largest number that can be formed using the digits of n

# Problem Statement:
# Given a positive integer n, calculate the largest number that can be formed using the digits of n. If multiple combinations can form the largest number, return the one with the smallest units digit.
# For example:
# Input: n = 123
# Output: 321 (largest number using digits of 123)
#
# Input: n = 741
# Output: 147 (largest number using digits of 741, ignoring the tens digit)

def largestNumber(n):
    # Sort the digits in descending order
    digits = sorted([int(digit) for digit in str(n)], reverse=True)

    # Join the sorted digits to form the largest number
    largest_number = ''.join(str(digit) for digit in digits)

    # Convert the string back to an integer
    return int(largest_number)

# Test Cases
n1 = 123
print("Largest number using digits of", n1, "is", largestNumber(n1))  # Output: 321

n2 = 741
print("Largest number using digits of", n2, "is", largestNumber(n2))  # Output: 147