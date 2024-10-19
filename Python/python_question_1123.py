# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

A palindrome is a string that reads the same backward as forward.

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

    The approach used is dynamic programming.  We create a 2D table `dp`
    where `dp[i][j]` is True if the substring s[i:j+1] is a palindrome, and False otherwise.

    The base cases are:
    - dp[i][i] = True for all i (single characters are palindromes)
    - dp[i][i+1] = True if s[i] == s[i+1] (two-character substrings)

    For substrings of length 3 or more, dp[i][j] is True if s[i] == s[j] and dp[i+1][j-1] is True.

    We iterate through the string, building up the dp table and keeping track of the start index
    and maximum length of the longest palindrome found so far.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring in s.
    """
    n = len(s)
    if n < 2:
        return s

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
    assert longest_palindrome("aaaaaaaa") == "aaaaaaaa"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()