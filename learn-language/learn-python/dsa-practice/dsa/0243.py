# DSA Problem 243

'''
Problem Statement:
A palindrome is a string that reads the same forward and backward. Given a string `s` consisting of lowercase English letters, determine the minimum number of characters that need to be changed to make `s` a palindrome. In one change, you can change any single character in the string to any other character. Note that you can also change characters to other characters that may not be present in the original string.

For example, "abccba" is a palindrome, and "abccda" can be turned into a palindrome by changing 'd' to 'b', requiring only 1 change.

Write a function `min_changes_to_palindrome(s: str) -> int` that takes in a string `s` and returns the minimum number of changes needed to make `s` a palindrome.

Constraints:
- The input string `s` will have a length between 1 and 1000, inclusive.
- The string `s` will only contain lowercase English letters.
'''

Solution:
```python
def min_changes_to_palindrome(s: str) -> int:
    """
    Calculates the minimum number of changes required to make the input string a palindrome.
    
    Args:
    s (str): The input string.
    
    Returns:
    int: The minimum number of changes required.
    """
    changes = 0
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            changes += 1
        left += 1
        right -= 1
    
    return changes

# Example usage
if __name__ == "__main__":
    test_cases = [
        ("abca", 1),
        ("abcba", 0),
        ("abcd", 2),
        ("aaa", 0),
        ("abcde", 2),
    ]
    
    for s, expected in test_cases:
        assert min_changes_to_palindrome(s) == expected, f"Failed for input: {s}"
    print("All test cases passed.")
```

This Python solution includes a function `min_changes_to_palindrome` that calculates the minimum number of changes needed to make a given string a palindrome. The solution iterates over the string from both ends towards the center, counting mismatches that need to be changed. The provided test cases at the end of the script serve to validate the correctness of the function.