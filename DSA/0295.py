# DSA Problem 295

'''
Problem Statement:
A palindrome is a string that reads the same forward and backward. For example, "madam" and "racecar" are palindromes. Given a string `s`, you can perform the following operation any number of times: choose any character in `s` and change it to any other character. What is the minimum number of operations required to make `s` a palindrome?

Constraints:
- 1 <= len(s) <= 1000
- `s` consists of lowercase English letters.
'''

Solution:
def min_operations_to_palindrome(s: str) -> int:
    operations = 0
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            operations += 1
        left += 1
        right -= 1
    
    return operations

# Example check (Uncomment to test)
# print(min_operations_to_palindrome("abcca"))  # Output: 1
# print(min_operations_to_palindrome("abcba"))  # Output: 0
# print(min_operations_to_palindrome("abcde"))  # Output: 2

This solution calculates the minimum number of character changes needed to make a given string a palindrome. It compares characters from the start and end of the string, moving towards the center, counting mismatches which represent necessary operations.