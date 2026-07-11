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
        Calculates the length of the longest palindromic subsequence in a given string.

        The approach uses dynamic programming.  dp[i][j] stores the length of the longest
        palindromic subsequence in the substring s[i:j+1].

        If s[i] == s[j], then dp[i][j] = dp[i+1][j-1] + 2.
        If s[i] != s[j], then dp[i][j] = max(dp[i+1][j], dp[i][j-1]).

        Base case: dp[i][i] = 1 for all i.
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # Initialize base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Fill the dp table in bottom-up manner (from shorter substrings to longer ones)
        for cl in range(2, n + 1):  # cl: current length of the substring
            for i in range(n - cl + 1):
                j = i + cl - 1
                if s[i] == s[j]:
                    if cl == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]

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
    s4 = "ac"
    expected4 = 1
    assert longest_palindromic_subsequence(s4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {longest_palindromic_subsequence(s4)}"

    # Test case 5
    s5 = "aba"
    expected5 = 3
    assert longest_palindromic_subsequence(s5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {longest_palindromic_subsequence(s5)}"

    # Test case 6
    s6 = "character"
    expected6 = 5
    assert longest_palindromic_subsequence(s6) == 5, f"Test Case 6 Failed: Expected {5}, got {longest_palindromic_subsequence(s6)}"
    
    # Test case 7
    s7 = "abcdefg"
    expected7 = 1
    assert longest_palindromic_subsequence(s7) == expected7, f"Test Case 7 Failed: Expected {expected7}, got {longest_palindromic_subsequence(s7)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()