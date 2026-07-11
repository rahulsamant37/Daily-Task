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

        # Create a DP table to store the lengths of longest palindromic subsequences.
        # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1].
        dp = [[0] * n for _ in range(n)]

        # Initialize the diagonal elements to 1, as a single character is a palindrome of length 1.
        for i in range(n):
            dp[i][i] = 1

        # Iterate over the substrings of increasing length.
        for cl in range(2, n + 1):  # cl: current length
            for i in range(n - cl + 1):
                j = i + cl - 1
                if s[i] == s[j]:
                    # If the characters at the ends of the substring are equal,
                    # then the length of the longest palindromic subsequence is 2 plus
                    # the length of the longest palindromic subsequence of the substring
                    # without these two characters.
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # If the characters at the ends of the substring are not equal,
                    # then the length of the longest palindromic subsequence is the maximum of
                    # the lengths of the longest palindromic subsequences of the substrings
                    # obtained by removing either the first or the last character.
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        # The length of the longest palindromic subsequence of the entire string is stored in dp[0][n-1].
        return dp[0][n - 1]

    return longestPalindromeSubseq


# Test cases
def test_solution():
    func = solution()

    # Test case 1
    s1 = "bbbab"
    expected1 = 4
    assert func(s1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {func(s1)}"

    # Test case 2
    s2 = "cbbd"
    expected2 = 2
    assert func(s2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {func(s2)}"

    # Test case 3
    s3 = "a"
    expected3 = 1
    assert func(s3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {func(s3)}"

    # Test case 4
    s4 = "ac"
    expected4 = 1
    assert func(s4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {func(s4)}"

    # Test case 5
    s5 = "character"
    expected5 = 5
    assert func(s5) == 5, f"Test Case 5 Failed: Expected {expected5}, Got {func(s5)}"

    # Test case 6
    s6 = "abcdefghijklmnopqrstuvwxyz"
    expected6 = 1
    assert func(s6) == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {func(s6)}"

    # Test case 7
    s7 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    expected7 = 300
    assert func(s7) == expected7, f"Test Case 7 Failed: Expected {expected7}, Got {func(s7)}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()