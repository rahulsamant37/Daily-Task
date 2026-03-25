# Python Question: Find the Longest Palindromic Substring
'''
Given a string `s`, find the longest palindromic substring in `s`.

A palindromic substring is a substring that reads the same forwards and backward.

Example:
Input: s = "babad"
Output: "bab" or "aba" (either one is a valid solution)

Input: s = "cbbd"
Output: "bb"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    The approach used is dynamic programming. We create a 2D table `dp` where `dp[i][j]`
    is True if the substring `s[i:j+1]` is a palindrome, and False otherwise.

    We initialize the table for substrings of length 1 and 2. Then, we iterate through
    substrings of increasing length, checking if they are palindromes based on the
    values of the smaller substrings.

    Finally, we track the start and end indices of the longest palindromic substring found.
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

    # Check for palindromes of length 3 or greater
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1  # End index of the substring

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
    assert longest_palindrome("aaaa") == "aaaa"
    assert longest_palindrome("ababa") == "ababa"
    assert longest_palindrome("level") == "level"

if __name__ == "__main__":
    test_longest_palindrome()