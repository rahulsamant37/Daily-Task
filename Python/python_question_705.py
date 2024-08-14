# Python Question: Find the Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length in `s`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

A palindrome is a string that reads the same backward as forward.

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
    Finds the length of the longest palindromic subsequence in a string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """

    n = len(s)

    # Create a DP table to store the lengths of LPS for subproblems.
    # dp[i][j] stores the length of LPS in s[i...j]
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are palindromes of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table in a bottom-up manner.
    # l is the length of the substring.
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1  # End index of the substring s[i...j]

            if s[i] == s[j]:
                # If the first and last characters are the same,
                # the LPS length is 2 + LPS length of the inner substring.
                dp[i][j] = 2 + dp[i + 1][j - 1] if i + 1 <= j - 1 else 2  # handle single character substring
            else:
                # If the first and last characters are different,
                # the LPS length is the maximum of the LPS lengths of
                # the substrings without the first and last characters.
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The length of the LPS of the entire string is stored in dp[0][n-1].
    return dp[0][n - 1]

# Test cases
def test_solution():
    assert longest_palindrome_subsequence("bbbab") == 4
    assert longest_palindrome_subsequence("cbbd") == 2
    assert longest_palindrome_subsequence("a") == 1
    assert longest_palindrome_subsequence("aa") == 2
    assert longest_palindrome_subsequence("aba") == 3
    assert longest_palindrome_subsequence("abcdefgh") == 1
    assert longest_palindrome_subsequence("racecar") == 7
    assert longest_palindrome_subsequence("abcba") == 5
    assert longest_palindrome_subsequence("agbdba") == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()