# Python Question: Find the Longest Palindromic Subsequence
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
    def longest_palindromic_subsequence(s):
        """
        Finds the length of the longest palindromic subsequence in a given string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """
        n = len(s)
        # Create a DP table to store the lengths of longest palindromic subsequences
        # dp[i][j] represents the length of the longest palindromic subsequence of s[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate through subsequences of increasing length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    # If the characters at the ends of the subsequence are equal,
                    # the length of the longest palindromic subsequence is 2 plus the
                    # length of the longest palindromic subsequence of the substring
                    # without these characters.
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # If the characters at the ends of the subsequence are not equal,
                    # the length of the longest palindromic subsequence is the maximum
                    # of the lengths of the longest palindromic subsequences of the
                    # substrings obtained by removing either the first or the last
                    # character.
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The length of the longest palindromic subsequence of the entire string is
        # stored in dp[0][n-1].
        return dp[0][n - 1]

    return longest_palindromic_subsequence

# Test cases
def test_solution():
    longest_palindromic_subsequence = solution() # Get the function

    # Test case 1
    s1 = "bbbab"
    expected1 = 4
    assert longest_palindromic_subsequence(s1) == expected1, f"Test Case 1 Failed: Input = {s1}, Expected = {expected1}, Got = {longest_palindromic_subsequence(s1)}"

    # Test case 2
    s2 = "cbbd"
    expected2 = 2
    assert longest_palindromic_subsequence(s2) == expected2, f"Test Case 2 Failed: Input = {s2}, Expected = {expected2}, Got = {longest_palindromic_subsequence(s2)}"

    # Test case 3
    s3 = "a"
    expected3 = 1
    assert longest_palindromic_subsequence(s3) == expected3, f"Test Case 3 Failed: Input = {s3}, Expected = {expected3}, Got = {longest_palindromic_subsequence(s3)}"

    # Test case 4
    s4 = "ac"
    expected4 = 1
    assert longest_palindromic_subsequence(s4) == expected4, f"Test Case 4 Failed: Input = {s4}, Expected = {expected4}, Got = {longest_palindromic_subsequence(s4)}"

    # Test case 5
    s5 = "aba"
    expected5 = 3
    assert longest_palindromic_subsequence(s5) == expected5, f"Test Case 5 Failed: Input = {s5}, Expected = {expected5}, Got = {longest_palindromic_subsequence(s5)}"

    # Test case 6
    s6 = "character"
    expected6 = 5
    assert longest_palindromic_subsequence(s6) == 5, f"Test Case 6 Failed: Input = {s6}, Expected = {5}, Got = {longest_palindromic_subsequence(s6)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()