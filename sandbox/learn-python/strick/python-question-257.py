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
    def longest_palindromic_subsequence(s):
        """
        Calculates the length of the longest palindromic subsequence in the given string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """

        n = len(s)

        # Create a table to store lengths of LPS for subproblems
        # dp[i][j] stores the length of LPS of substring s[i..j]
        dp = [[0] * n for _ in range(n)]

        # Strings of length 1 are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Consider substrings of length 2, 3, ... up to n
        for cl in range(2, n + 1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2  # If first and last characters match, add 2 to the length of LPS of substring s[i+1..j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j]) # If first and last characters do not match, take the maximum of LPS of s[i..j-1] and s[i+1..j]

        return dp[0][n-1] # The length of LPS of the entire string is stored in dp[0][n-1]
    return longest_palindromic_subsequence

# Test cases
def test_solution():
    longest_palindromic_subsequence = solution()

    # Test case 1
    s1 = "bbbab"
    expected1 = 4
    assert longest_palindromic_subsequence(s1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {longest_palindromic_subsequence(s1)}"

    # Test case 2
    s2 = "cbbd"
    expected2 = 2
    assert longest_palindromic_subsequence(s2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {longest_palindromic_subsequence(s2)}"

    # Test case 3
    s3 = "a"
    expected3 = 1
    assert longest_palindromic_subsequence(s3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {longest_palindromic_subsequence(s3)}"

    # Test case 4
    s4 = "aa"
    expected4 = 2
    assert longest_palindromic_subsequence(s4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {longest_palindromic_subsequence(s4)}"

    # Test case 5
    s5 = "aba"
    expected5 = 3
    assert longest_palindromic_subsequence(s5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {longest_palindromic_subsequence(s5)}"

    # Test case 6
    s6 = "character"
    expected6 = 5
    assert longest_palindromic_subsequence(s6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {longest_palindromic_subsequence(s6)}"

    # Test case 7
    s7 = "abcdefgh"
    expected7 = 1
    assert longest_palindromic_subsequence(s7) == expected7, f"Test Case 7 Failed: Expected {expected7}, got {longest_palindromic_subsequence(s7)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()