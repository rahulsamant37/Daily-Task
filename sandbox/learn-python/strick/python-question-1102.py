# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. A palindrome is a sequence that reads the same backward as forward.

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
    Calculates the length of the longest palindromic subsequence of a given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """
    n = len(s)

    # Create a DP table to store lengths of LPS for subproblems.
    # dp[i][j] stores the length of the LPS of substring s[i:j+1].
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are palindromes of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table diagonally.
    # Iterate over the length of the substring.
    for cl in range(2, n + 1):
        # Iterate over the starting index of the substring.
        for i in range(n - cl + 1):
            j = i + cl - 1  # Calculate the ending index of the substring

            # If the first and last characters of the substring are equal,
            # then the LPS length is 2 plus the LPS length of the substring
            # without the first and last characters.
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            # Otherwise, the LPS length is the maximum of the LPS lengths of
            # the substrings without the first character and without the last character.
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The length of the LPS of the entire string is stored in dp[0][n-1].
    return dp[0][n - 1]

# Test cases
def test_solution():
    assert longest_palindrome_subsequence("bbbab") == 4
    assert longest_palindrome_subsequence("cbbd") == 2
    assert longest_palindrome_subsequence("a") == 1
    assert longest_palindrome_subsequence("aa") == 2
    assert longest_palindrome_subsequence("aba") == 3
    assert longest_palindrome_subsequence("racecar") == 7
    assert longest_palindrome_subsequence("leetcode") == 3
    assert longest_palindrome_subsequence("character") == 5
    assert longest_palindrome_subsequence("") == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()