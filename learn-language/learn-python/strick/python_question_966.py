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
def longest_palindromic_subsequence(s):
    """
    Finds the length of the longest palindromic subsequence in a string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """
    n = len(s)

    # dp[i][j] stores the length of the longest palindromic subsequence of s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Base case: A single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Iterate over lengths of substrings
    for length in range(2, n + 1):
        # Iterate over starting indices of substrings
        for i in range(n - length + 1):
            j = i + length - 1
            # If the characters at the ends of the substring match
            if s[i] == s[j]:
                # Then the longest palindromic subsequence includes these characters
                # plus the longest palindromic subsequence of the substring in between
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                # Otherwise, the longest palindromic subsequence is the maximum of
                # the longest palindromic subsequence of the substring excluding the first character
                # and the longest palindromic subsequence of the substring excluding the last character
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]

# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("abcabcabcabc") == 7
    assert longest_palindromic_subsequence("character") == 5
    assert longest_palindromic_subsequence("leetcode") == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindromic_subsequence()