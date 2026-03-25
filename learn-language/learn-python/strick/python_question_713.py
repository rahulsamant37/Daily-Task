# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length.

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
    Finds the length of the longest palindromic subsequence of a string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """

    n = len(s)

    # Create a table to store lengths of palindromic subsequences.
    # dp[i][j] stores the length of the LPS of s[i...j]
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are palindromes of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Iterate through lengths of subsequences.
    for length in range(2, n + 1):
        # Iterate through starting positions of subsequences.
        for i in range(n - length + 1):
            j = i + length - 1  # Ending position of the subsequence.

            # If the characters at the ends are equal,
            # the LPS length is 2 + LPS of the inner substring.
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1] if length > 2 else 2
            # Otherwise, take the maximum of LPS of the two substrings
            # obtained by excluding either the first or the last character.
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The length of the LPS of the entire string is stored in dp[0][n-1].
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
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindromic_subsequence()