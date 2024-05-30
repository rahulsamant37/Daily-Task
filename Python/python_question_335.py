# Python Question: Find the Longest Palindromic Substring
'''
Given a string `s`, find the longest palindromic substring in `s`.

A palindromic substring is a substring that reads the same backward as forward.

Example:

Input: s = "babad"
Output: "bab" or "aba" (both are valid)

Input: s = "cbbd"
Output: "bb"

Input: s = "a"
Output: "a"

Input: s = "ac"
Output: "a"
'''

# Solution
def longest_palindrome(s: str) -> str:
    """
    Finds the longest palindromic substring within a given string.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring found in s.
    """

    if not s:
        return ""

    n = len(s)
    if n == 1:
        return s

    # Initialize a table to store palindrome information.
    # dp[i][j] will be True if s[i:j+1] is a palindrome, False otherwise.
    dp = [[False] * n for _ in range(n)]

    # All single characters are palindromes.
    for i in range(n):
        dp[i][i] = True

    # Check for palindromes of length 2.
    start = 0  # Start index of the longest palindrome found so far.
    max_len = 1  # Length of the longest palindrome found so far.

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for palindromes of length 3 or greater.
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1  # End index of the substring.

            # If the substring s[i+1:j] is a palindrome and the characters at the
            # ends of the substring s[i:j+1] are the same, then s[i:j+1] is also a palindrome.
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True

                if k > max_len:
                    start = i
                    max_len = k

    # Return the longest palindromic substring found.
    return s[start:start + max_len]


# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("banana") == "anana"
    assert longest_palindrome("level") == "level"
    assert longest_palindrome("") == ""
    assert longest_palindrome("ababa") == "ababa"
    assert longest_palindrome("forgeeksskeegfor") == "geeksskeeg"

if __name__ == "__main__":
    test_longest_palindrome()