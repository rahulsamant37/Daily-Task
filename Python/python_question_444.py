# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

A palindrome is a string that reads the same backward as forward.

Example:
Input: "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Input: "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
'''

# Solution
def longest_palindromic_subsequence(s):
    """
    Calculates the length of the longest palindromic subsequence in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the longest palindromic subsequence.
    """

    n = len(s)

    # Create a DP table to store lengths of LPS for subproblems.
    # dp[i][j] stores the length of the LPS of s[i...j]
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are palindromes of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table diagonally.
    # cl is the length of the substring being considered.
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j]:
                # If the first and last characters are the same,
                # the LPS length is 2 + LPS of the substring without these characters.
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                # If the first and last characters are different,
                # the LPS length is the maximum of LPS of the substring without the first character
                # and the LPS of the substring without the last character.
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The result is stored in dp[0][n-1], which represents the LPS of the entire string.
    return dp[0][n - 1]

# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("abcdefg") == 1
    assert longest_palindromic_subsequence("abccba") == 6
    assert longest_palindromic_subsequence("character") == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindromic_subsequence()