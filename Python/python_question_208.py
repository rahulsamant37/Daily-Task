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

        # Create a DP table to store the lengths of longest palindromic subsequences.
        # dp[i][j] stores the length of the LPS in s[i:j+1].
        dp = [[0] * n for _ in range(n)]

        # Base case: Single characters are palindromes of length 1.
        for i in range(n):
            dp[i][i] = 1

        # Iterate over increasing lengths of substrings.
        for cl in range(2, n + 1):  # cl: current length
            for i in range(n - cl + 1):
                j = i + cl - 1

                # If the characters at the ends of the substring match,
                # then the LPS length is 2 plus the LPS length of the substring
                # without those characters.
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # Otherwise, the LPS length is the maximum of the LPS lengths
                    # of the substrings obtained by excluding either the first or
                    # the last character.
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
    result1 = longest_palindromic_subsequence(s1)
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {result1}"

    # Test case 2
    s2 = "cbbd"
    expected2 = 2
    result2 = longest_palindromic_subsequence(s2)
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {result2}"

    # Test case 3
    s3 = "a"
    expected3 = 1
    result3 = longest_palindromic_subsequence(s3)
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {result3}"

    # Test case 4
    s4 = "ac"
    expected4 = 1
    result4 = longest_palindromic_subsequence(s4)
    assert result4 == expected4, f"Test Case 4 Failed: Expected {expected4}, got {result4}"

    # Test case 5
    s5 = "character"
    expected5 = 5
    result5 = longest_palindromic_subsequence(s5)
    assert result5 == 5, f"Test Case 5 Failed: Expected {5}, got {result5}"

    # Test case 6
    s6 = "bananas"
    expected6 = 5
    result6 = longest_palindromic_subsequence(s6)
    assert result6 == 5, f"Test Case 6 Failed: Expected {5}, got {result6}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()