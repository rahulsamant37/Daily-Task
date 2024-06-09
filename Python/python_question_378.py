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
    def longest_palindromic_subsequence_length(s):
        """
        Calculates the length of the longest palindromic subsequence in a given string.

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

        # Iterate over increasing subsequence lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    # If the characters at the ends of the subsequence match,
                    # the length of the longest palindromic subsequence is 2 plus the
                    # length of the longest palindromic subsequence of the substring
                    # without those end characters.
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # If the characters at the ends of the subsequence do not match,
                    # the length of the longest palindromic subsequence is the maximum of
                    # the lengths of the longest palindromic subsequences of the substrings
                    # excluding either the first or the last character.
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
    
    return longest_palindromic_subsequence_length

# Test cases
def test_solution():
    longest_palindromic_subsequence_length = solution()

    # Test case 1
    s1 = "bbbab"
    expected1 = 4
    result1 = longest_palindromic_subsequence_length(s1)
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Test Case 1 Passed")

    # Test case 2
    s2 = "cbbd"
    expected2 = 2
    result2 = longest_palindromic_subsequence_length(s2)
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Test Case 2 Passed")

    # Test case 3
    s3 = "a"
    expected3 = 1
    result3 = longest_palindromic_subsequence_length(s3)
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Test Case 3 Passed")

    # Test case 4
    s4 = "ac"
    expected4 = 1
    result4 = longest_palindromic_subsequence_length(s4)
    assert result4 == expected4, f"Test Case 4 Failed: Expected {expected4}, got {result4}"
    print("Test Case 4 Passed")

    # Test case 5
    s5 = "aba"
    expected5 = 3
    result5 = longest_palindromic_subsequence_length(s5)
    assert result5 == expected5, f"Test Case 5 Failed: Expected {expected5}, got {result5}"
    print("Test Case 5 Passed")
    
    # Test case 6
    s6 = "character"
    expected6 = 5
    result6 = longest_palindromic_subsequence_length(s6)
    assert result6 == expected6, f"Test Case 6 Failed: Expected {expected6}, got {result6}"
    print("Test Case 6 Passed")

if __name__ == "__main__":
    test_solution()