# Python Question: Longest Palindromic Subsequence
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
def longest_palindromic_subsequence(s):
    """
    Calculates the length of the longest palindromic subsequence of a string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """

    n = len(s)

    # Create a DP table to store the lengths of longest palindromic subsequences
    # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate through the string with increasing lengths of substrings
    for cl in range(2, n + 1):  # cl: current length of the substring
        for i in range(n - cl + 1):  # i: starting index of the substring
            j = i + cl - 1  # j: ending index of the substring

            # If the first and last characters of the substring are the same
            if s[i] == s[j]:
                # The length of the longest palindromic subsequence is 2 + the length of the longest palindromic subsequence of the substring without the first and last characters
                dp[i][j] = 2 + dp[i + 1][j - 1] if i + 1 <= j - 1 else 2
            else:
                # Otherwise, the length of the longest palindromic subsequence is the maximum of the lengths of the longest palindromic subsequences of the substrings without the first character and without the last character
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The length of the longest palindromic subsequence of the entire string is stored in dp[0][n-1]
    return dp[0][n - 1]

# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("aa") == 2
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("leetcode") == 3
    assert longest_palindromic_subsequence("") == 0
    assert longest_palindromic_subsequence("abcdefg") == 1
    assert longest_palindromic_subsequence("abcdcba") == 7

if __name__ == "__main__":
    test_longest_palindromic_subsequence()