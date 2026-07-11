# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example:
Input: "babad"
Output: "bab" or "aba"

Input: "cbbd"
Output: "bb"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    The approach uses dynamic programming. A 2D table dp is created where dp[i][j]
    is True if the substring s[i:j+1] is a palindrome, and False otherwise.

    The table is filled diagonally.
    - Single characters are palindromes.
    - Two consecutive characters are palindromes if they are equal.
    - For longer substrings, dp[i][j] is True if s[i] == s[j] and dp[i+1][j-1] is True.

    The longest palindrome is tracked by storing its start index and length.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring.
    """
    n = len(s)
    if n < 2:
        return s  # Single character or empty string is a palindrome

    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1

    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for palindromes of length 3 or more
    for k in range(3, n + 1):
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
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("") == ""
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("forgeeksskeegfor") == "geeksskeeg"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()