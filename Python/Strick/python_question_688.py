# Python Question: Longest Palindromic Subsequence Length
'''
Given a string `s`, find the length of the longest palindromic subsequence's length in `s`.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
A palindrome is a sequence that reads the same backward as forward.

Example:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
'''

# Solution
def longest_palindrome_subsequence(s):
    """
    Calculates the length of the longest palindromic subsequence of a given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """
    n = len(s)

    # Create a table to store lengths of longest palindromic subsequences of substrings.
    # dp[i][j] will store the length of the LPS of substring s[i:j+1].
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are palindromes of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Build the dp table from bottom up.
    # l is the length of the substring.
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1  # End index of the substring

            # If the end characters of the substring match, then the length of the LPS
            # is 2 plus the length of the LPS of the substring without those end characters.
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            # If the end characters do not match, then the length of the LPS is the maximum
            # of the lengths of the LPS of the substring without the first character
            # and the substring without the last character.
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The length of the LPS of the entire string is stored in dp[0][n-1].
    return dp[0][n - 1]

# Test cases
def test_longest_palindrome_subsequence():
    assert longest_palindrome_subsequence("bbbab") == 4
    assert longest_palindrome_subsequence("cbbd") == 2
    assert longest_palindrome_subsequence("a") == 1
    assert longest_palindrome_subsequence("ac") == 1
    assert longest_palindrome_subsequence("aba") == 3
    assert longest_palindrome_subsequence("abcabcabcabc") == 4
    assert longest_palindrome_subsequence("") == 0
    assert longest_palindrome_subsequence("abcdefghijklmnopqrstuvwxyz") == 1
    assert longest_palindrome_subsequence("racecar") == 7

if __name__ == "__main__":
    test_longest_palindrome_subsequence()