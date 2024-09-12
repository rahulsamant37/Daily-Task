# Python Question: Find the Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. A palindrome is a sequence that reads the same backward as forward.

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
        Calculates the length of the longest palindromic subsequence of a given string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """

        n = len(s)

        # Create a DP table to store lengths of LPS for subproblems.
        # dp[i][j] will store the length of the LPS of s[i...j].
        dp = [[0] * n for _ in range(n)]

        # Strings of length 1 are palindromes of length 1.
        for i in range(n):
            dp[i][i] = 1

        # Fill the DP table in bottom-up manner.
        # cl is the length of the substring.
        for cl in range(2, n + 1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if s[i] == s[j]:
                    # If the first and last characters are the same,
                    # then the LPS length is 2 plus the LPS length of the
                    # substring without these characters.
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # If the first and last characters are different,
                    # then the LPS length is the maximum of the LPS lengths
                    # of the substrings without the first and last characters.
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        # The length of the LPS of the entire string is stored in dp[0][n-1].
        return dp[0][n - 1]

    return longest_palindromic_subsequence

# Test cases
def test_solution():
    longest_palindromic_subsequence = solution()

    # Test case 1
    s1 = "bbbab"
    expected1 = 4
    assert longest_palindromic_subsequence(s1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {longest_palindromic_subsequence(s1)}"

    # Test case 2
    s2 = "cbbd"
    expected2 = 2
    assert longest_palindromic_subsequence(s2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {longest_palindromic_subsequence(s2)}"

    # Test case 3
    s3 = "a"
    expected3 = 1
    assert longest_palindromic_subsequence(s3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {longest_palindromic_subsequence(s3)}"

    # Test case 4
    s4 = "ac"
    expected4 = 1
    assert longest_palindromic_subsequence(s4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {longest_palindromic_subsequence(s4)}"

    # Test case 5
    s5 = "aba"
    expected5 = 3
    assert longest_palindromic_subsequence(s5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {longest_palindromic_subsequence(s5)}"

    # Test case 6
    s6 = "bananas"
    expected6 = 5
    assert longest_palindromic_subsequence(s6) == 5, f"Test Case 6 Failed: Expected {5}, Got {longest_palindromic_subsequence(s6)}"


    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()