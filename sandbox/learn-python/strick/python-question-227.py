# Python Question: Longest Palindromic Subsequence
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
def solution():
    # The problem can be solved using dynamic programming.
    # dp[i][j] represents the length of the longest palindromic subsequence of the substring s[i:j+1].

    # Base case: If i == j, then the length of the longest palindromic subsequence is 1.
    # If s[i] == s[j], then dp[i][j] = dp[i+1][j-1] + 2.
    # Otherwise, dp[i][j] = max(dp[i+1][j], dp[i][j-1]).

    def longestPalindromeSubseq(s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # Initialize the base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate through substrings of increasing length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]

    return longestPalindromeSubseq

# Test cases
def test_solution():
    longestPalindromeSubseq = solution()

    assert longestPalindromeSubseq("bbbab") == 4
    assert longestPalindromeSubseq("cbbd") == 2
    assert longestPalindromeSubseq("a") == 1
    assert longestPalindromeSubseq("aa") == 2
    assert longestPalindromeSubseq("aba") == 3
    assert longestPalindromeSubseq("racecar") == 7
    assert longestPalindromeSubseq("leetcode") == 3
    assert longestPalindromeSubseq("") == 0
    assert longestPalindromeSubseq("abcabcabcabc") == 4

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()