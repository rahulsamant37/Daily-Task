# Python Question: Longest Palindromic Subsequence
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
def longest_palindromic_subsequence(s):
    """
    Calculates the length of the longest palindromic subsequence in a given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """
    n = len(s)

    # Create a DP table to store lengths of LPS for subproblems.
    # dp[i][j] stores the length of the LPS in substring s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: A single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table diagonally.  `cl` is the length of the substring.
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1  # End index of the substring
            if s[i] == s[j]:
                # If the first and last characters are the same,
                # then the LPS length is 2 + LPS length of the substring without those characters
                dp[i][j] = 2 + dp[i + 1][j - 1] if cl > 2 else 2
            else:
                # If the first and last characters are different,
                # then the LPS length is the maximum of the LPS lengths of the two substrings
                # obtained by excluding either the first or the last character
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The top-right corner of the DP table contains the length of the LPS for the entire string
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
    assert longest_palindromic_subsequence("character") == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindromic_subsequence()