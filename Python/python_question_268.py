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
    def longestPalindromeSubseq(s: str) -> int:
        """
        Calculates the length of the longest palindromic subsequence in a given string.

        The approach uses dynamic programming.  `dp[i][j]` stores the length of the longest
        palindromic subsequence in the substring `s[i:j+1]`.

        If `s[i] == s[j]`, then `dp[i][j] = dp[i+1][j-1] + 2`. This is because we can extend the
        longest palindromic subsequence of `s[i+1:j]` by adding `s[i]` and `s[j]` to both ends.

        If `s[i] != s[j]`, then `dp[i][j] = max(dp[i+1][j], dp[i][j-1])`.  This is because the
        longest palindromic subsequence must either exclude `s[i]` or `s[j]`.

        The base case is when `i == j`, in which case `dp[i][j] = 1`.
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # Initialize the diagonal (single characters are palindromes of length 1)
        for i in range(n):
            dp[i][i] = 1

        # Iterate through substrings of increasing length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1  # Calculate the end index of the substring

                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]

    return longestPalindromeSubseq

# Test cases
def test_solution():
    longestPalindromeSubseq = solution()
    assert longestPalindromeSubseq("bbbab") == 4
    assert longestPalindromeSubseq("cbbd") == 2
    assert longestPalindromeSubseq("a") == 1
    assert longestPalindromeSubseq("ac") == 1
    assert longestPalindromeSubseq("aba") == 3
    assert longestPalindromeSubseq("abcabcabcabc") == 7
    assert longestPalindromeSubseq("character") == 5
    assert longestPalindromeSubseq("abcdefg") == 1
    assert longestPalindromeSubseq("racecar") == 7
    assert longestPalindromeSubseq("") == 0

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()