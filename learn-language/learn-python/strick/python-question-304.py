# Python Question: Find the Largest Palindromic Subsequence Length
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
    def longest_palindromic_subsequence(s):
        """
        Finds the length of the longest palindromic subsequence of a string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """
        n = len(s)
        # Create a DP table to store the lengths of palindromic subsequences
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate through substrings of increasing length
        for cl in range(2, n + 1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if s[i] == s[j]:
                    # If the end characters are equal, add 2 to the length of the
                    # palindromic subsequence of the substring without the end characters
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # If the end characters are not equal, take the maximum of the lengths
                    # of the palindromic subsequences of the substrings without either of the
                    # end characters
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        # The length of the longest palindromic subsequence is stored in dp[0][n-1]
        return dp[0][n - 1]

    return longest_palindromic_subsequence

# Test cases
def test_solution():
    longest_palindromic_subsequence = solution()

    # Test case 1
    s1 = "bbbab"
    expected1 = 4
    result1 = longest_palindromic_subsequence(s1)
    assert result1 == expected1, f"Test case 1 failed: Expected {expected1}, got {result1}"

    # Test case 2
    s2 = "cbbd"
    expected2 = 2
    result2 = longest_palindromic_subsequence(s2)
    assert result2 == expected2, f"Test case 2 failed: Expected {expected2}, got {result2}"

    # Test case 3
    s3 = "a"
    expected3 = 1
    result3 = longest_palindromic_subsequence(s3)
    assert result3 == expected3, f"Test case 3 failed: Expected {expected3}, got {result3}"

    # Test case 4
    s4 = "ac"
    expected4 = 1
    result4 = longest_palindromic_subsequence(s4)
    assert result4 == expected4, f"Test case 4 failed: Expected {expected4}, got {result4}"

    # Test case 5
    s5 = "racecar"
    expected5 = 7
    result5 = longest_palindromic_subsequence(s5)
    assert result5 == expected5, f"Test case 5 failed: Expected {expected5}, got {result5}"

    # Test case 6
    s6 = "bananas"
    expected6 = 5
    result6 = longest_palindromic_subsequence(s6)
    assert result6 == expected6, f"Test case 6 failed: Expected {expected6}, got {result6}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()