# Python Question: Find the Longest Palindromic Subsequence
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
def longest_palindrome_subsequence(s):
    """
    Finds the length of the longest palindromic subsequence in a string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """

    n = len(s)

    # Create a DP table to store lengths of longest palindromic subsequences
    # dp[i][j] stores the length of the LPS of s[i...j]
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate over increasing lengths of subsequences
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j]:
                # If the first and last characters are equal, then the LPS
                # length is 2 + LPS length of the substring without these characters
                dp[i][j] = 2 + dp[i + 1][j - 1] if i + 1 <= j - 1 else 2 #Handle the case where i+1 and j-1 cross
            else:
                # If the first and last characters are not equal, then the LPS
                # length is the maximum of the LPS lengths of the substrings
                # without the first or last character
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The result is stored in dp[0][n-1] which represents the LPS length of the entire string
    return dp[0][n - 1]


# Test cases
def test_solution():
    assert longest_palindrome_subsequence("bbbab") == 4
    assert longest_palindrome_subsequence("cbbd") == 2
    assert longest_palindrome_subsequence("a") == 1
    assert longest_palindrome_subsequence("aa") == 2
    assert longest_palindrome_subsequence("aba") == 3
    assert longest_palindrome_subsequence("abcabcabcabc") == 7
    assert longest_palindrome_subsequence("character") == 5
    assert longest_palindrome_subsequence("leetcode") == 3
    assert longest_palindrome_subsequence("racecar") == 7
    assert longest_palindrome_subsequence("") == 0

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()