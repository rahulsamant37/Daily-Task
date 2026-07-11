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
        Finds the length of the longest palindromic subsequence in a string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """
        n = len(s)
        # Create a DP table to store the lengths of palindromic subsequences.
        # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1].
        dp = [[0] * n for _ in range(n)]

        # Initialize the diagonal elements of the DP table.
        # A single character is always a palindrome of length 1.
        for i in range(n):
            dp[i][i] = 1

        # Iterate over the lengths of the subsequences.
        for length in range(2, n + 1):
            # Iterate over the starting indices of the subsequences.
            for i in range(n - length + 1):
                # Calculate the ending index of the subsequence.
                j = i + length - 1

                # If the characters at the start and end of the subsequence are the same,
                # then the length of the longest palindromic subsequence is 2 plus the
                # length of the longest palindromic subsequence of the substring between
                # the start and end characters.
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                # Otherwise, the length of the longest palindromic subsequence is the maximum
                # of the lengths of the longest palindromic subsequences of the substrings
                # without the start character and without the end character.
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The length of the longest palindromic subsequence of the entire string is stored
        # in the top-right corner of the DP table.
        return dp[0][n - 1]

    return longestPalindromeSubseq

# Test cases
def test_solution():
    sol = solution()
    longestPalindromeSubseq = sol()
    assert longestPalindromeSubseq("bbbab") == 4
    assert longestPalindromeSubseq("cbbd") == 2
    assert longestPalindromeSubseq("a") == 1
    assert longestPalindromeSubseq("aa") == 2
    assert longestPalindromeSubseq("aba") == 3
    assert longestPalindromeSubseq("racecar") == 7
    assert longestPalindromeSubseq("leetcode") == 3
    assert longestPalindromeSubseq("") == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()