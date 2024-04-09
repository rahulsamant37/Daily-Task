# Python Question: Longest Palindromic Subsequence Length
'''
Given a string `s`, find the length of the longest palindromic subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. A palindrome is a sequence that reads the same backward as forward.

Example:
Input: "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Input: "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
'''

# Solution
def longest_palindromic_subsequence_length(s):
    """
    Calculates the length of the longest palindromic subsequence of a given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """

    n = len(s)

    # Create a table to store lengths of LPS for subproblems
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill the dp table in bottom-up manner
    # l is the length of substring
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The result is the length of LPS of the entire string
    return dp[0][n - 1]

# Test cases
def test_longest_palindromic_subsequence_length():
    assert longest_palindromic_subsequence_length("bbbab") == 4
    assert longest_palindromic_subsequence_length("cbbd") == 2
    assert longest_palindromic_subsequence_length("a") == 1
    assert longest_palindromic_subsequence_length("ab") == 1
    assert longest_palindromic_subsequence_length("aba") == 3
    assert longest_palindromic_subsequence_length("racecar") == 7
    assert longest_palindromic_subsequence_length("agbdba") == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindromic_subsequence_length()