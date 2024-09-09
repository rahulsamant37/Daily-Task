# Python Question: Longest Palindromic Subsequence Length
'''
Given a string s, find the length of the longest palindromic subsequence's length.
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
    Calculates the length of the longest palindromic subsequence of a given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """

    n = len(s)

    # Create a DP table to store lengths of LPS for substrings
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table diagonally, starting from subsequences of length 2
    for cl in range(2, n + 1):  # cl is current length of subsequence
        for i in range(n - cl + 1):
            j = i + cl - 1  # j is the ending index of the subsequence
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2  # If endpoints match, add 2 to the length of LPS of the inner substring
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])  # If endpoints don't match, take the max of the LPS of the substrings excluding either endpoint

    return dp[0][n - 1]  # The length of the LPS of the entire string is at dp[0][n-1]


# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("") == 0
    assert longest_palindromic_subsequence("agbdba") == 5
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindromic_subsequence()