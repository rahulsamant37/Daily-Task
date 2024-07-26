# Python Question: Longest Palindromic Subsequence
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
    def longest_palindromic_subsequence(s):
        """
        Finds the length of the longest palindromic subsequence of a string.

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

        # Iterate through subsequences of increasing length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    # If the characters at the ends are the same,
                    # the LPS includes these characters and the LPS of the substring in between
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # If the characters at the ends are different,
                    # the LPS is the maximum of the LPS of the substring excluding the first character
                    # and the LPS of the substring excluding the last character
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]

    return longest_palindromic_subsequence


# Test cases
def test_solution():
    longest_palindromic_subsequence = solution()

    # Test case 1
    s1 = "bbbab"
    expected1 = 4
    actual1 = longest_palindromic_subsequence(s1)
    assert actual1 == expected1, f"Test Case 1 Failed: Input={s1}, Expected={expected1}, Actual={actual1}"

    # Test case 2
    s2 = "cbbd"
    expected2 = 2
    actual2 = longest_palindromic_subsequence(s2)
    assert actual2 == expected2, f"Test Case 2 Failed: Input={s2}, Expected={expected2}, Actual={actual2}"

    # Test case 3
    s3 = "a"
    expected3 = 1
    actual3 = longest_palindromic_subsequence(s3)
    assert actual3 == expected3, f"Test Case 3 Failed: Input={s3}, Expected={expected3}, Actual={actual3}"

    # Test case 4
    s4 = "ac"
    expected4 = 1
    actual4 = longest_palindromic_subsequence(s4)
    assert actual4 == expected4, f"Test Case 4 Failed: Input={s4}, Expected={expected4}, Actual={actual4}"

    # Test case 5
    s5 = "character"
    expected5 = 5
    actual5 = longest_palindromic_subsequence(s5)
    assert actual5 == expected5, f"Test Case 5 Failed: Input={s5}, Expected={expected5}, Actual={actual5}"

    # Test case 6
    s6 = "racecar"
    expected6 = 7
    actual6 = longest_palindromic_subsequence(s6)
    assert actual6 == expected6, f"Test Case 6 Failed: Input={s6}, Expected={expected6}, Actual={actual6}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()