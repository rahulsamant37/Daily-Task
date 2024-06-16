# Python Question: Longest Palindromic Subsequence Length
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
        Calculates the length of the longest palindromic subsequence of a string.

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

                # If the characters at the ends of the substring match,
                # the longest palindromic subsequence is 2 plus the length of the
                # longest palindromic subsequence of the substring without the ends.
                if s[i] == s[j]:
                    dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)  # Handle edge case where i+1 > j-1
                # Otherwise, the longest palindromic subsequence is the maximum of the
                # longest palindromic subsequences of the substrings without the left or right end.
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]

    return longestPalindromeSubseq

# Test cases
def test_solution():
    longestPalindromeSubseq = solution()

    # Test case 1
    s1 = "bbbab"
    expected1 = 4
    assert longestPalindromeSubseq(s1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {longestPalindromeSubseq(s1)}"

    # Test case 2
    s2 = "cbbd"
    expected2 = 2
    assert longestPalindromeSubseq(s2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {longestPalindromeSubseq(s2)}"

    # Test case 3
    s3 = "a"
    expected3 = 1
    assert longestPalindromeSubseq(s3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {longestPalindromeSubseq(s3)}"

    # Test case 4
    s4 = "ac"
    expected4 = 1
    assert longestPalindromeSubseq(s4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {longestPalindromeSubseq(s4)}"

    # Test case 5
    s5 = "bananas"
    expected5 = 5
    assert longestPalindromeSubseq(s5) == 5, f"Test Case 5 Failed: Expected {expected5}, Got {longestPalindromeSubseq(s5)}"

    # Test case 6: Empty string
    s6 = ""
    expected6 = 0
    assert longestPalindromeSubseq(s6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {longestPalindromeSubseq(s6)}"

    # Test case 7
    s7 = "character"
    expected7 = 5
    assert longestPalindromeSubseq(s7) == 5, f"Test Case 7 Failed: Expected {expected7}, Got {longestPalindromeSubseq(s7)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()