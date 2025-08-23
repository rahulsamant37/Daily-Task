# DSA Problem 347

'''
Problem Statement:
A palindrome is a string that reads the same backward as forward, such as "madam" or "racecar". Given a string s, you are allowed to perform at most k modifications (insert, remove, or replace a character) to convert s into a palindrome. Write a function that calculates the minimum number of modifications needed to make the string a palindrome. If it's possible to make it a palindrome with at most k modifications, return the number of modifications needed, otherwise return -1.

Examples:
- For s = "abccba" and k = 2, the function should return 0 since the string is already a palindrome.
- For s = "abcba" and k = 3, the function should return 0 as well, as the string is already a palindrome.
- For s = "abcde" and k = 1, the function should return -1, since we cannot turn this string into a palindrome with just one modification.
'''

Solution:
def min_modifications_to_palindrome(s: str, k: int) -> int:
    def dfs(i, j, k):
        if i >= j:  # Base case: if the indices have crossed, no modifications are needed
            return 0
        if (i, j, k) in memo:  # Return cached result if it exists
            return memo[(i, j, k)]
        if s[i] == s[j]:  # If the characters at both ends match, move inward
            memo[(i, j, k)] = dfs(i + 1, j - 1, k)
        else:
            # If they don't match, we can either modify one of them to match the other
            # or leave both as they are and count this as a modification
            memo[(i, j, k)] = min(1 + dfs(i + 1, j, k), 1 + dfs(i, j - 1, k), 2 + dfs(i + 1, j - 1, k))
        if memo[(i, j, k)] > k:  # If the calculated changes exceed k, this path is invalid
            memo[(i, j, k)] = float('inf')
        return memo[(i, j, k)]
    
    memo = {}
    res = dfs(0, len(s) - 1, k)
    return res if res != float('inf') else -1

# Test cases
print(min_modifications_to_palindrome("abccba", 2))  # Expected output: 0
print(min_modifications_to_palindrome("abcba", 3))  # Expected output: 0
print(min_modifications_to_palindrome("abcde", 1))  # Expected output: -1
print(min_modifications_to_palindrome("abcd", 2))   # Expected output: 2
print(min_modifications_to_palindrome("abcda", 2)) # Expected output: 1
print(min_modifications_to_palindrome("abcd", 1))   # Expected output: -1
'''

This problem involves dynamic programming with memoization to efficiently find the minimum number of modifications required to make a string a palindrome, within the constraint of a maximum number of allowed modifications.