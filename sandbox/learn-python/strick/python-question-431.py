# Python Question: Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length in `s`.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. A palindrome is a string that reads the same backward as forward.

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
    Finds the length of the longest palindromic subsequence in a string.

    Args:
      s: The input string.

    Returns:
      The length of the longest palindromic subsequence.
    """
    n = len(s)

    # Create a DP table to store the lengths of palindromic subsequences.
    # dp[i][j] stores the length of the longest palindromic subsequence in s[i:j+1].
    dp = [[0] * n for _ in range(n)]

    # Initialize the diagonal elements of the DP table.
    # A single character is a palindrome of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Iterate through the string, increasing the length of the subsequence.
    for cl in range(2, n + 1):  # cl is the length of substring we are considering
        for i in range(n - cl + 1): # i is the start index of the substring
            j = i + cl - 1 # j is the end index of the substring

            # If the characters at the start and end of the subsequence are equal,
            # then the length of the longest palindromic subsequence is 2 plus the
            # length of the longest palindromic subsequence of the substring without
            # the start and end characters.
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            # Otherwise, the length of the longest palindromic subsequence is the
            # maximum of the lengths of the longest palindromic subsequences of the
            # substrings without the start and end characters.
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The length of the longest palindromic subsequence of the entire string is
    # stored in dp[0][n-1].
    return dp[0][n - 1]


# Test cases
def test_solution():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("leetcode") == 3
    assert longest_palindromic_subsequence("") == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()