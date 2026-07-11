# DSA Problem 345

'''
Problem Statement:
A palindrome is a string that reads the same forward and backward, e.g., "madam" or "racecar". Given a string `s` consisting of lowercase English letters, you can perform the following operation any number of times:

- Choose any character in `s` and change it to any other lowercase English letter.

Your task is to find the minimum number of operations required to make `s` a palindrome.

For example, the string "abca" can be turned into a palindrome "abba" with one operation (changing the last character from 'a' to 'b').

Constraints:
- 1 <= len(s) <= 1000
- `s` consists of lowercase English letters only.

Example:
Input: s = "abca"
Output: 1
Explanation: One possible solution is to change the last character to 'b' to make the string "abba", which is a palindrome.
'''

Solution:
```python
def min_operations_to_palindrome(s: str) -> int:
    """
    Calculates the minimum number of operations required to make the given string a palindrome.
    """
    operations = 0
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            operations += 1
        left += 1
        right -= 1
    
    return operations

# Check function to verify the correctness of the solution
def check_solution():
    assert min_operations_to_palindrome("abca") == 1, "Test case 1 failed"
    assert min_operations_to_palindrome("abc") == 1, "Test case 2 failed"
    assert min_operations_to_palindrome("a") == 0, "Test case 3 failed"
    assert min_operations_to_palindrome("abcdcba") == 0, "Test case 4 failed"
    assert min_operations_to_palindrome("abcde") == 2, "Test case 5 failed"
    print("All test cases passed!")

check_solution()
```

This code snippet defines a function `min_operations_to_palindrome` that calculates the minimum number of character changes required to turn the given string into a palindrome. It uses a two-pointer approach to compare characters from both ends, incrementing the operation count when characters do not match. The `check_solution` function is provided to verify the solution against several test cases.