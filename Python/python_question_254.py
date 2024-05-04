# Python Question: Longest Palindromic Substring
'''
Given a string `s`, find the longest palindromic substring in `s`.

A palindromic substring is a substring that reads the same backward as forward.

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

    The approach used is dynamic programming.  A 2D boolean array `dp` is created,
    where dp[i][j] is True if the substring s[i:j+1] is a palindrome, and False otherwise.

    The `dp` array is filled in diagonally.

    1.  Base case: All substrings of length 1 are palindromes (dp[i][i] = True).
    2.  Substrings of length 2: dp[i][i+1] = (s[i] == s[i+1]).
    3.  Substrings of length 3 or more: dp[i][j] = (s[i] == s[j] and dp[i+1][j-1]).

    While filling the `dp` array, the starting and ending indices of the longest
    palindromic substring encountered so far are tracked.  Finally, the substring
    corresponding to these indices is returned.
    """

    n = len(s)
    if n < 2:
        return s  # Empty string or single character string is a palindrome

    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1

    # Base case: single character palindromes
    for i in range(n):
        dp[i][i] = True

    # Base case: two character palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for palindromes of length 3 or more
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
    assert longest_palindrome("babad") in ["bab", "aba"]
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("") == ""
    assert longest_palindrome("bananas") in ["anana", "nanan"]
    assert longest_palindrome("abacab") in ["bacab", "abaca"]
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()