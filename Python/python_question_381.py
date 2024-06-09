# Python Question: Find the Largest Palindromic Subsequence Length
'''
Given a string `s`, find the length of the longest palindromic subsequence.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.  A palindrome is a sequence that reads the same backward as forward.

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
    def longestPalindromeSubseq(s):
        """
        Finds the length of the longest palindromic subsequence of a string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """
        n = len(s)

        # Create a DP table to store lengths of palindromic subsequences.
        # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1].
        dp = [[0] * n for _ in range(n)]

        # Base case: Single characters are palindromes of length 1.
        for i in range(n):
            dp[i][i] = 1

        # Fill the DP table diagonally.
        for cl in range(2, n + 1):  # cl: current length of the subsequence
            for i in range(n - cl + 1):
                j = i + cl - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        # The length of the longest palindromic subsequence of the entire string is stored in dp[0][n-1].
        return dp[0][n - 1]

    return longestPalindromeSubseq

# Test cases
def test_solution():
    longestPalindromeSubseq = solution()
    assert longestPalindromeSubseq("bbbab") == 4, "Test Case 1 Failed"
    assert longestPalindromeSubseq("cbbd") == 2, "Test Case 2 Failed"
    assert longestPalindromeSubseq("a") == 1, "Test Case 3 Failed"
    assert longestPalindromeSubseq("ac") == 1, "Test Case 4 Failed"
    assert longestPalindromeSubseq("aba") == 3, "Test Case 5 Failed"
    assert longestPalindromeSubseq("abcabcabcabc") == 4, "Test Case 6 Failed"
    assert longestPalindromeSubseq("character") == 5, "Test Case 7 Failed"
    assert longestPalindromeSubseq("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 300, "Test Case 8 Failed"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()