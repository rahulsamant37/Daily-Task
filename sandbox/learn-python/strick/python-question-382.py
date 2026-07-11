# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length in `s`.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. A palindrome is a string that reads the same forward and backward.

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
        s (str): The input string.

    Returns:
        int: The length of the longest palindromic subsequence.
    """

    n = len(s)

    # Create a table to store lengths of LPS for subproblems.
    # dp[i][j] stores the length of the LPS of s[i...j]
    dp = [[0] * n for _ in range(n)]

    # Strings of length 1 are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Build the dp table in bottom-up manner.
    # Note that the diagonal values are already initialized to 1.
    for cl in range(2, n + 1):  # cl is the length of substring
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])

    # The value dp[0][n-1] contains the length of LPS for the entire string
    return dp[0][n-1]

# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("abcabcabcabc") == 4
    assert longest_palindromic_subsequence("abcdefg") == 1
    assert longest_palindromic_subsequence("aaaaaaaaaa") == 10
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindromic_subsequence()