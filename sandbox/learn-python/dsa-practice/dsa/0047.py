# DSA Problem 47

'''
Problem Statement:
A palindrome is a number that reads the same backward as forward. Given a positive integer `n`, find the smallest palindrome greater than `n`. For example, if `n` is 2030, the next palindrome is 2112. Write a function `next_palindrome` that takes an integer `n` and returns the smallest palindrome greater than `n`.

Note:
- Assume that the input `n` is always a positive integer.
- The function should handle large numbers efficiently.
'''

Solution:
def next_palindrome(n):
    """
    Finds the smallest palindrome greater than n.
    """
    n += 1  # Start checking from the next number
    while str(n) != str(n)[::-1]:  # Check if n is a palindrome
        n += 1
    return n

# Test cases to verify the correctness of the function
assert next_palindrome(808) == 818, "Test case 1 failed"
assert next_palindrome(2030) == 2112, "Test case 2 failed"
assert next_palindrome(1987) == 1991, "Test case 3 failed"
assert next_palindrome(999) == 1001, "Test case 4 failed"
assert next_palindrome(123456) == 1234321, "Test case 5 failed"

# Print statements for manual verification
print(next_palindrome(808))  # Expected output: 818
print(next_palindrome(2030))  # Expected output: 2112
print(next_palindrome(1987))  # Expected output: 1991
print(next_palindrome(999))  # Expected output: 1001
print(next_palindrome(123456))  # Expected output: 1234321

print("All test cases passed!")