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
        Finds the length of the longest palindromic subsequence in a string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """

        n = len(s)

        # Create a DP table to store the lengths of LPS for subproblems.
        # dp[i][j] stores the length of the LPS of s[i...j].
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters are palindromes of length 1.
        for i in range(n):
            dp[i][i] = 1

        # Iterate through subproblems of increasing length.
        for cl in range(2, n + 1):  # cl: current length of substring
            for i in range(n - cl + 1):  # i: starting index
                j = i + cl - 1  # j: ending index

                # If the characters at the start and end are the same,
                # then the LPS includes these characters, and we add 2 to
                # the LPS of the substring without these characters.
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                # Otherwise, the LPS is the maximum of the LPS of the
                # substrings excluding either the start or end character.
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        # The length of the LPS of the entire string is stored in dp[0][n-1].
        return dp[0][n - 1]

    return longest_palindromic_subsequence

# Test cases
def test_solution():
    lps = solution()

    # Test case 1
    s1 = "bbbab"
    expected1 = 4
    actual1 = lps(s1)
    assert actual1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {actual1}"

    # Test case 2
    s2 = "cbbd"
    expected2 = 2
    actual2 = lps(s2)
    assert actual2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {actual2}"

    # Test case 3
    s3 = "a"
    expected3 = 1
    actual3 = lps(s3)
    assert actual3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {actual3}"

    # Test case 4
    s4 = "ac"
    expected4 = 1
    actual4 = lps(s4)
    assert actual4 == expected4, f"Test Case 4 Failed: Expected {expected4}, got {actual4}"

    # Test case 5
    s5 = "character"
    expected5 = 5
    actual5 = lps(s5)
    assert actual5 == 5, f"Test Case 5 Failed: Expected {expected5}, got {actual5}"

    # Test case 6
    s6 = "bananas"
    expected6 = 5
    actual6 = lps(s6)
    assert actual6 == expected6, f"Test Case 6 Failed: Expected {expected6}, got {actual6}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()