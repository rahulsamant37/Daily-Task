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
def longest_palindrome_subsequence(s: str) -> int:
    """
    Finds the length of the longest palindromic subsequence in a string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """
    n = len(s)

    # Create a DP table to store the lengths of longest palindromic subsequences.
    # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1].
    dp = [[0] * n for _ in range(n)]

    # Initialize the diagonal elements of the DP table.
    # A single character is a palindrome of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Iterate through the DP table in a bottom-up manner.
    # The outer loop iterates through the length of the subsequence.
    for length in range(2, n + 1):
        # The inner loop iterates through the starting indices of the subsequence.
        for i in range(n - length + 1):
            j = i + length - 1  # Calculate the ending index of the subsequence.

            # If the characters at the start and end of the subsequence are equal,
            # then the length of the longest palindromic subsequence is 2 + the length of the
            # longest palindromic subsequence of the substring without the start and end characters.
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            # Otherwise, the length of the longest palindromic subsequence is the maximum of the
            # lengths of the longest palindromic subsequences of the substrings without the start
            # and end characters.
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The length of the longest palindromic subsequence of the entire string is stored in dp[0][n-1].
    return dp[0][n - 1]


# Test cases
def test_longest_palindrome_subsequence():
    assert longest_palindrome_subsequence("bbbab") == 4
    assert longest_palindrome_subsequence("cbbd") == 2
    assert longest_palindrome_subsequence("a") == 1
    assert longest_palindrome_subsequence("aa") == 2
    assert longest_palindrome_subsequence("aba") == 3
    assert longest_palindrome_subsequence("abcdefg") == 1
    assert longest_palindrome_subsequence("racecar") == 7
    assert longest_palindrome_subsequence("") == 0
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindrome_subsequence()