# Python Question: Longest Palindromic Substring
'''
Given a string `s`, find the longest palindromic substring in `s`. You may assume that the maximum length of `s` is 1000.

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

    The approach uses dynamic programming. A 2D boolean table `dp` is created where `dp[i][j]` is true if the substring `s[i:j+1]` is a palindrome, and false otherwise.
    The table is filled diagonally, starting with substrings of length 1 and increasing the length.

    Time Complexity: O(n^2), where n is the length of the string.
    Space Complexity: O(n^2) for the dp table.
    """
    n = len(s)
    if n < 2:
        return s

    # dp[i][j] will be true if the substring s[i..j] is a palindrome, else false
    dp = [[False] * n for _ in range(n)]

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # start and maxlen will store the starting index and length of the longest
    # palindromic substring found so far
    start = 0
    max_length = 1

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for lengths greater than 2. k is the length of the substring
    for k in range(3, n + 1):
        # Fix the starting index
        for i in range(n - k + 1):
            # Get the ending index for substring s[i..j]
            j = i + k - 1

            # checking for sub-string from ith index to jth index if s[i+1] to s[j-1]
            # is a palindrome
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True

                if k > max_length:
                    start = i
                    max_length = k

    return s[start:start + max_length]

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

if __name__ == "__main__":
    test_longest_palindrome()