# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.
A palindromic substring is a string that reads the same backward as forward.

Example:
Input: s = "babad"
Output: "bab" or "aba" (both are valid)

Input: s = "cbbd"
Output: "bb"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    The approach used is dynamic programming. A 2D boolean table `dp` is constructed
    where `dp[i][j]` is True if the substring `s[i:j+1]` is a palindrome, and False otherwise.

    The table is filled diagonally. The base cases are single characters (length 1) and
    two consecutive characters (length 2).

    For substrings of length 3 or more, `dp[i][j]` is True if `s[i] == s[j]` and `dp[i+1][j-1]` is True.

    The starting and ending indices of the longest palindrome are tracked during the table filling.
    """
    n = len(s)
    if n < 2:
        return s  # Single character string is a palindrome

    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for substrings of length 3 or more
    for k in range(3, n + 1):  # k is the length of the substring
        for i in range(n - k + 1):
            j = i + k - 1  # Ending index of the substring
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
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("level") == "level"
    assert longest_palindrome("rotor") == "rotor"
    assert longest_palindrome("") == ""
    assert longest_palindrome("aaaaaaaa") == "aaaaaaaa"
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindrome()