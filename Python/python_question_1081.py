# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length in `s`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

A palindrome is a string that reads the same forward and backward.

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

    # Create a DP table to store lengths of longest palindromic subsequences
    # dp[i][j] stores the length of LPS in substring s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate through different substring lengths (length = 2, 3, ...)
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1  # End index of the current substring

            # If the characters at the ends are equal, we can extend the LPS
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                # Otherwise, take the maximum LPS length from the two subproblems
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    # The result is stored in dp[0][n-1], which represents the LPS of the whole string
    return dp[0][n-1]

# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("abca") == 3
    assert longest_palindromic_subsequence("bananas") == 5
    assert longest_palindromic_subsequence("character") == 5
    assert longest_palindromic_subsequence("") == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindromic_subsequence()