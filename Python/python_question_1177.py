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
def longest_palindrome_subsequence(s):
    """
    Calculates the length of the longest palindromic subsequence in a given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """
    n = len(s)

    # Create a DP table to store the lengths of longest palindromic subsequences.
    # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1].
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters are palindromes of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Iterate over increasing lengths of substrings.
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # If the characters at the ends of the substring are equal,
            # then the length of the longest palindromic subsequence is
            # 2 plus the length of the longest palindromic subsequence of the
            # substring without the end characters.
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            # Otherwise, the length of the longest palindromic subsequence is
            # the maximum of the lengths of the longest palindromic subsequences
            # of the substrings without the first or last character.
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The result is the length of the longest palindromic subsequence of the entire string.
    return dp[0][n - 1]

# Test cases
def test_longest_palindrome_subsequence():
    assert longest_palindrome_subsequence("bbbab") == 4
    assert longest_palindrome_subsequence("cbbd") == 2
    assert longest_palindrome_subsequence("a") == 1
    assert longest_palindrome_subsequence("ac") == 1
    assert longest_palindrome_subsequence("aba") == 3
    assert longest_palindrome_subsequence("racecar") == 7
    assert longest_palindrome_subsequence("leetcode") == 3
    assert longest_palindrome_subsequence("") == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome_subsequence()