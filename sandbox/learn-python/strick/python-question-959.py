# Python Question: Longest Palindromic Subsequence Length
'''
Given a string `s`, find the length of the longest palindromic subsequence's length.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
A palindrome is a sequence that reads the same backward as forward.

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
    def longest_palindromic_subsequence_length(s):
        """
        Calculates the length of the longest palindromic subsequence of a given string.

        Args:
            s: The input string.

        Returns:
            The length of the longest palindromic subsequence.
        """

        n = len(s)

        # Create a DP table to store the lengths of longest palindromic subsequences.
        # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1].
        dp = [[0] * n for _ in range(n)]

        # Base case: Single characters are palindromes of length 1.
        for i in range(n):
            dp[i][i] = 1

        # Iterate over increasing lengths of substrings.
        for length in range(2, n + 1):
            # Iterate over starting indices of substrings of the given length.
            for i in range(n - length + 1):
                j = i + length - 1

                # If the characters at the start and end of the substring are the same,
                # then the longest palindromic subsequence length is 2 plus the length of the
                # longest palindromic subsequence of the substring without those characters.
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                # Otherwise, the longest palindromic subsequence length is the maximum of the
                # lengths of the longest palindromic subsequences of the substrings without either
                # the start or end character.
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The result is stored in dp[0][n-1], which represents the longest palindromic
        # subsequence of the entire string.
        return dp[0][n - 1]

    return longest_palindromic_subsequence_length


# Test cases
def test_solution():
    longest_palindromic_subsequence_length = solution()

    # Test case 1
    s1 = "bbbab"
    expected1 = 4
    assert longest_palindromic_subsequence_length(s1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {longest_palindromic_subsequence_length(s1)}"

    # Test case 2
    s2 = "cbbd"
    expected2 = 2
    assert longest_palindromic_subsequence_length(s2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {longest_palindromic_subsequence_length(s2)}"

    # Test case 3
    s3 = "a"
    expected3 = 1
    assert longest_palindromic_subsequence_length(s3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {longest_palindromic_subsequence_length(s3)}"

    # Test case 4
    s4 = "ac"
    expected4 = 1
    assert longest_palindromic_subsequence_length(s4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {longest_palindromic_subsequence_length(s4)}"

    # Test case 5
    s5 = "bananas"
    expected5 = 5
    assert longest_palindromic_subsequence_length(s5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {longest_palindromic_subsequence_length(s5)}"

    # Test case 6
    s6 = "character"
    expected6 = 5
    assert longest_palindromic_subsequence_length(s6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {longest_palindromic_subsequence_length(s6)}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()