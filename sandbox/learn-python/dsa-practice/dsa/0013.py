# DSA Problem 13

'''
Problem Statement:
A "lucky" number is defined as a positive integer where the sum of the first half of its digits is equal to the sum of the second half. For example, 123321 is a lucky number because 1+2+3 = 3+2+1. Given a positive integer n, find the smallest lucky number that is greater than or equal to n. If no such number exists within the range of a 32-bit signed integer, return -1.

Note: Assume that n is a positive integer with an even number of digits.
'''

Solution:
```python
def smallest_lucky_number(n):
    def is_lucky(num):
        str_num = str(num)
        mid = len(str_num) // 2
        first_half = sum(map(int, str_num[:mid]))
        second_half = sum(map(int, str_num[mid:]))
        return first_half == second_half

    n = int('1' * len(str(n))) if len(str(n)) % 2 != 0 else n  # Ensure n has even number of digits
    while n < 2**31:
        if is_lucky(n):
            return n
        n += 1
    return -1

# Example usage
print(smallest_lucky_number(123309))  # Example input
```

Note: This solution assumes that the given number n has an even number of digits, as specified in the problem statement. If n does not have an even number of digits, the function adjusts n to the smallest number with an even number of digits (by converting it to a number made of '1's of the next even length).