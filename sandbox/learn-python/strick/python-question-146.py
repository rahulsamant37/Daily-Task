# Python Question: Longest Palindromic Subsequence
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
        Finds the length of the longest palindromic subsequence of a given string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """
        n = len(s)
        # Create a DP table to store the lengths of longest palindromic subsequences.
        # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1].
        dp = [[0] * n for _ in range(n)]

        # Base case: A single character is a palindrome of length 1.
        for i in range(n):
            dp[i][i] = 1

        # Iterate over different lengths of subsequences.
        for length in range(2, n + 1):
            # Iterate over the starting indices of subsequences.
            for i in range(n - length + 1):
                j = i + length - 1
                # If the characters at the start and end of the subsequence match,
                # then the length of the longest palindromic subsequence is 2 plus
                # the length of the longest palindromic subsequence of the substring
                # excluding the start and end characters.
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                # Otherwise, the length of the longest palindromic subsequence is the
                # maximum of the lengths of the longest palindromic subsequences of the
                # substrings excluding either the start or the end character.
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The length of the longest palindromic subsequence of the entire string is
        # stored in dp[0][n-1].
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
    assert longestPalindromeSubseq("aaaaaaaaaaaa") == 12
    assert longestPalindromeSubseq("") == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()