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
        Finds the length of the longest palindromic subsequence in a given string.

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

        # Iterate through the string with increasing lengths of substrings
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # If the characters at the ends of the substring are equal,
                # then the length of the longest palindromic subsequence is
                # 2 (for the two characters) plus the length of the longest
                # palindromic subsequence of the substring without those characters.
                if s[i] == s[j]:
                    dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
                # Otherwise, the length of the longest palindromic subsequence is
                # the maximum of the lengths of the longest palindromic subsequences
                # of the substrings obtained by removing one of the end characters.
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The result is the length of the longest palindromic subsequence of the entire string.
        return dp[0][n - 1]

    return longestPalindromeSubseq

# Test cases
def test_solution():
    longestPalindromeSubseq = solution()

    # Test case 1
    s1 = "bbbab"
    expected1 = 4
    assert longestPalindromeSubseq(s1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {longestPalindromeSubseq(s1)}"

    # Test case 2
    s2 = "cbbd"
    expected2 = 2
    assert longestPalindromeSubseq(s2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {longestPalindromeSubseq(s2)}"

    # Test case 3
    s3 = "a"
    expected3 = 1
    assert longestPalindromeSubseq(s3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {longestPalindromeSubseq(s3)}"

    # Test case 4
    s4 = "ac"
    expected4 = 1
    assert longestPalindromeSubseq(s4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {longestPalindromeSubseq(s4)}"

    # Test case 5
    s5 = "bananas"
    expected5 = 5
    assert longestPalindromeSubseq(s5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {longestPalindromeSubseq(s5)}"

    # Test case 6
    s6 = "character"
    expected6 = 5
    assert longestPalindromeSubseq(s6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {longestPalindromeSubseq(s6)}"

    # Test case 7 (empty string)
    s7 = ""
    expected7 = 0
    assert longestPalindromeSubseq(s7) == expected7, f"Test Case 7 Failed: Expected {expected7}, got {longestPalindromeSubseq(s7)}"


    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()