# Python Question: Longest Palindromic Substring
'''
Given a string `s`, find the longest palindromic substring in `s`.

A palindromic substring is a substring that reads the same forwards and backward.

Example:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring within a given string.

    The approach uses dynamic programming to efficiently determine if a substring is a palindrome.
    A 2D boolean array `dp` is used where dp[i][j] is True if the substring s[i:j+1] is a palindrome,
    and False otherwise.

    The algorithm iterates through substrings of increasing length, starting with length 1.
    For each substring, it checks if the characters at the start and end are equal.
    If they are equal and the substring between them is also a palindrome (or the substring has length 1 or 2),
    then the substring is a palindrome.

    The longest palindromic substring found so far is tracked and updated whenever a longer palindrome is found.
    """
    n = len(s)
    if n < 2:
        return s  # Single character string is a palindrome

    dp = [[False] * n for _ in range(n)]  # dp[i][j] is True if s[i:j+1] is a palindrome
    start = 0  # Start index of the longest palindrome
    max_len = 1  # Length of the longest palindrome

    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for palindromes of length 3 or greater
    for k in range(3, n + 1):  # k is the length of the substring
        for i in range(n - k + 1):  # i is the starting index
            j = i + k - 1  # j is the ending index
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if k > max_len:
                    start = i
                    max_len = k

    return s[start:start + max_len]

# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("") == ""
    assert longest_palindrome("aaaaa") == "aaaaa"
    assert longest_palindrome("ababa") == "ababa"
    print("All test cases passed")

if __name__ == "__main__":
    test_longest_palindrome()