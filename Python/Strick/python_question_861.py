# Python Question: Find the Largest Palindromic Subsequence Length
'''
Given a string `s`, find the length of the longest palindromic subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. A palindrome is a sequence that reads the same forwards and backward.

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

        # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate over increasing lengths of subsequences
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # If the characters at the ends are equal, then the longest palindromic subsequence
                # is 2 plus the longest palindromic subsequence of the substring without the ends
                if s[i] == s[j]:
                    dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
                else:
                    # Otherwise, the longest palindromic subsequence is the maximum of the longest
                    # palindromic subsequences of the substrings without the first or last character
                    dp[i][j] = max(dp[i + 1][j] if i + 1 <= j else 0, dp[i][j - 1] if i <= j - 1 else 0)

        return dp[0][n - 1]

    return longest_palindromic_subsequence

# Test cases
def test_solution():
    longest_palindromic_subsequence = solution()

    # Test case 1
    s1 = "bbbab"
    expected1 = 4
    actual1 = longest_palindromic_subsequence(s1)
    assert actual1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {actual1}"

    # Test case 2
    s2 = "cbbd"
    expected2 = 2
    actual2 = longest_palindromic_subsequence(s2)
    assert actual2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {actual2}"

    # Test case 3
    s3 = "a"
    expected3 = 1
    actual3 = longest_palindromic_subsequence(s3)
    assert actual3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {actual3}"

    # Test case 4
    s4 = "ac"
    expected4 = 1
    actual4 = longest_palindromic_subsequence(s4)
    assert actual4 == expected4, f"Test Case 4 Failed: Expected {expected4}, got {actual4}"

    # Test case 5
    s5 = "aba"
    expected5 = 3
    actual5 = longest_palindromic_subsequence(s5)
    assert actual5 == expected5, f"Test Case 5 Failed: Expected {expected5}, got {actual5}"
    
    # Test case 6
    s6 = "character"
    expected6 = 5
    actual6 = longest_palindromic_subsequence(s6)
    assert actual6 == expected6, f"Test Case 6 Failed: Expected {expected6}, got {actual6}"
    
    # Test case 7
    s7 = "agbdba"
    expected7 = 5
    actual7 = longest_palindromic_subsequence(s7)
    assert actual7 == expected7, f"Test Case 7 Failed: Expected {expected7}, got {actual7}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()