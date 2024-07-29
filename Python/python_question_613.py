# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence (LPS).
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
A palindrome is a sequence that reads the same backward as forward.

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
    Calculates the length of the longest palindromic subsequence of a given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """

    n = len(s)

    # Create a DP table to store the lengths of LPS for different subproblems.
    # dp[i][j] stores the length of the LPS of s[i:j+1].
    dp = [[0] * n for _ in range(n)]

    # Initialize the diagonal elements.  A single character is a palindrome of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table in a bottom-up manner.
    # l is the length of the substring being considered.
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1  # End index of the substring

            # If the first and last characters of the substring are equal,
            # the LPS length is 2 + LPS length of the substring without those characters.
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)  # handle edge case of single char
            # Otherwise, the LPS length is the maximum of the LPS lengths of the two substrings
            # obtained by removing either the first or the last character.
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The length of the LPS of the entire string is stored in dp[0][n-1].
    return dp[0][n - 1]


# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("agbdba") == 5
    assert longest_palindromic_subsequence("") == 0
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindromic_subsequence()