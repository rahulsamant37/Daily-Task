# DSA Problem 19

'''
Problem Statement:
A palindrome is a string that reads the same forward and backward. Given a string s, you are allowed to delete at most one character from s. Determine if it is possible to make the string a palindrome under this constraint. For instance, the string "aba" is a palindrome, and "abca" can be turned into a palindrome by removing the character 'c'.

Write a function `is_almost_palindrome` that takes a string `s` and returns `True` if the string can be turned into a palindrome by deleting at most one character, and `False` otherwise.

Examples:
- is_almost_palindrome("aba") should return True as "aba" is already a palindrome.
- is_almost_palindrome("abca") should return True, as removing 'c' makes "aba", which is a palindrome.
- is_almost_palindrome("abc") should return False, as no single character removal can make it a palindrome.
'''

Solution:
```python
def is_almost_palindrome(s: str) -> bool:
    def is_palindrome_range(start, end):
        return all(s[i] == s[end - i + start] for i in range(start, (end + start) // 2 + 1))
    
    for i in range(len(s) // 2):
        if s[i] != s[~i]:
            return is_palindrome_range(i + 1, len(s) - i - 1) or is_palindrome_range(i, len(s) - i - 2)
    return True

# Check function to test the solution
def check_solution():
    test_cases = [("aba", True), ("abca", True), ("abc", False), ("deeee", True), ("", True), ("abcdc", False)]
    for s, expected in test_cases:
        assert is_almost_palindrome(s) == expected, f"Failed for {s}"
    print("All test cases passed!")

check_solution()
```

This solution defines a helper function `is_palindrome_range` to check if a substring within given start and end indices is a palindrome. The main function `is_almost_palindrome` iterates through the string, comparing characters from the start and the end. If a mismatch is found, it checks if skipping the character at the start or the end would make the rest of the string a palindrome.