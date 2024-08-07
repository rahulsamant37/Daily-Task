# Python Question: Find the Longest Palindromic Subsequence
'''
Given a string s, find the length of the longest palindromic subsequence's length.

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
    def longestPalindromeSubseq(s):
        """
        Finds the length of the longest palindromic subsequence of a string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """
        n = len(s)

        # dp[i][j] stores the length of the longest palindromic subsequence
        # of the substring s[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate over increasing lengths of substrings
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # If the characters at the ends of the substring match,
                # the length of the longest palindromic subsequence is
                # 2 + the length of the longest palindromic subsequence
                # of the substring without these characters
                if s[i] == s[j]:
                    dp[i][j] = 2 + (dp[i+1][j-1] if i+1 <= j-1 else 0)
                # Otherwise, the length of the longest palindromic subsequence
                # is the maximum of the lengths of the longest palindromic
                # subsequences of the substrings without the first or last character
                else:
                    dp[i][j] = max(dp[i+1][j] if i+1 <= j else 0, dp[i][j-1] if i <= j-1 else 0)

        # The length of the longest palindromic subsequence of the entire string
        # is stored in dp[0][n-1]
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
    assert longestPalindromeSubseq("character") == 5
    assert longestPalindromeSubseq("abcabcabcabc") == 4
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()