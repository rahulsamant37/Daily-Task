# Python Question: Find the Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length.

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
        Finds the length of the longest palindromic subsequence of a string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """
        n = len(s)
        # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate over increasing lengths of substrings
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    # If the characters at the ends are equal, add 2 to the length of the palindromic subsequence of the substring without these characters
                    if length == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    # If the characters at the ends are not equal, take the maximum of the lengths of the palindromic subsequences of the substrings excluding either the first or the last character
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        # The result is stored in dp[0][n-1]
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
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()