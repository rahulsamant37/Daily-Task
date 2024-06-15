# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length.

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
def longest_palindromic_subsequence(s):
    """
    Finds the length of the longest palindromic subsequence of a string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """
    n = len(s)

    # Create a DP table to store lengths of LPS for subproblems.
    # dp[i][j] stores the length of LPS of s[i...j]
    dp = [[0] * n for _ in range(n)]

    # Base case: All single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table diagonally, considering increasing lengths of substrings
    for cl in range(2, n + 1):  # cl: current length of substring
        for i in range(n - cl + 1):  # i: starting index of substring
            j = i + cl - 1  # j: ending index of substring

            if s[i] == s[j]:
                # If the first and last characters are the same,
                # the LPS length is 2 + LPS length of the substring without those characters
                dp[i][j] = 2 + dp[i + 1][j - 1] if (i+1 <= j-1) else 2
            else:
                # If the first and last characters are different,
                # the LPS length is the maximum of the LPS lengths of two subproblems:
                # 1. Excluding the first character: s[i+1...j]
                # 2. Excluding the last character: s[i...j-1]
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The length of the LPS of the entire string is stored in dp[0][n-1]
    return dp[0][n - 1]

# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("aa") == 2
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("agbdba") == 5
    assert longest_palindromic_subsequence("character") == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindromic_subsequence()