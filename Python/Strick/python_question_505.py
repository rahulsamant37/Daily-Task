# Python Question: Longest Palindromic Subsequence
'''
Given a string s, find the length of the longest palindromic subsequence's length in s.
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
def solution():
    def longestPalindromeSubseq(s):
        """
        Finds the length of the longest palindromic subsequence in a string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """
        n = len(s)

        # Create a DP table to store lengths of LPS for substrings
        dp = [[0] * n for _ in range(n)]

        # Base case: Single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate through substrings of increasing length
        for cl in range(2, n + 1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if s[i] == s[j]:
                    # If the characters at the start and end are the same,
                    # extend the LPS by 2 (including these characters)
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    # If the characters are different, take the maximum LPS length
                    # from either excluding the start or the end character
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        # The length of the LPS for the entire string is at dp[0][n-1]
        return dp[0][n-1]
    
    return longestPalindromeSubseq

# Test cases
def test_solution():
    longestPalindromeSubseq = solution()
    assert longestPalindromeSubseq("bbbab") == 4
    assert longestPalindromeSubseq("cbbd") == 2
    assert longestPalindromeSubseq("a") == 1
    assert longestPalindromeSubseq("ac") == 1
    assert longestPalindromeSubseq("aba") == 3
    assert longestPalindromeSubseq("bananas") == 5
    assert longestPalindromeSubseq("character") == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()