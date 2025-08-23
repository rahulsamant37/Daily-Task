# DSA Problem 145

'''
Problem Statement:
A "happy number" is defined as a number which eventually reaches 1 when replaced by the sum of the square of its digits repeatedly. If a number is not a happy number, it will enter a cycle that does not include 1. For instance, 19 is a happy number because the process eventually leads to 1:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Write a function `is_happy_number` that takes an integer `n` as input and returns `True` if `n` is a happy number, otherwise `False`.

Example:
>>> is_happy_number(19)
True
'''

Solution:
def is_happy_number(n):
    def get_next(number):
        return sum(int(char) ** 2 for char in str(number))
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    
    return n == 1

# Test the function
print(is_happy_number(19))  # Output: True
print(is_happy_number(2))    # Output: False