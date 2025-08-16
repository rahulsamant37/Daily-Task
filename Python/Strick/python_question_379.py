# Python Question: Find the Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

A palindrome is a string that reads the same backward as forward.

Example:
Input: "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Input: "cbbd"
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
        # Create a DP table to store the lengths of the longest palindromic subsequences
        # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate over the lengths of the substrings
        for length in range(2, n + 1):
            # Iterate over the starting indices of the substrings
            for i in range(n - length + 1):
                # Calculate the ending index of the substring
                j = i + length - 1

                # If the characters at the start and end of the substring match
                if s[i] == s[j]:
                    # The length of the longest palindromic subsequence is 2 plus the length of the longest palindromic subsequence of the substring without the start and end characters
                    dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0) # Handle edge case when i+1 > j-1
                else:
                    # Otherwise, the length of the longest palindromic subsequence is the maximum of the lengths of the longest palindromic subsequences of the substrings without the start or end character
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The length of the longest palindromic subsequence of the entire string is stored in dp[0][n-1]
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
    assert longestPalindromeSubseq("abba") == 4
    assert longestPalindromeSubseq("abcdefg") == 1
    assert longestPalindromeSubseq("racecar") == 7
    assert longestPalindromeSubseq("leetcode") == 3
    assert longestPalindromeSubseq("") == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()