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
    Finds the length of the longest palindromic subsequence in the given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """
    n = len(s)

    # Create a DP table to store the lengths of palindromic subsequences.
    # dp[i][j] will store the length of the longest palindromic subsequence in s[i:j+1].
    dp = [[0] * n for _ in range(n)]

    # Base case: A single character is a palindrome of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Iterate through the string with increasing subsequence lengths.
    for cl in range(2, n + 1):  # cl: current length of the subsequence
        for i in range(n - cl + 1):  # i: starting index of the subsequence
            j = i + cl - 1  # j: ending index of the subsequence

            # If the characters at the ends of the subsequence match,
            # the length of the longest palindromic subsequence is 2 plus the
            # length of the longest palindromic subsequence of the substring
            # between the end characters.
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            # If the characters at the ends of the subsequence do not match,
            # the length of the longest palindromic subsequence is the maximum of
            # the lengths of the longest palindromic subsequences of the substrings
            # excluding either the first or the last character.
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The length of the longest palindromic subsequence of the entire string is
    # stored in dp[0][n-1].
    return dp[0][n - 1]


# Test cases
def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("ac") == 1
    assert longest_palindromic_subsequence("aba") == 3
    assert longest_palindromic_subsequence("abba") == 4
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("leetcode") == 3
    assert longest_palindromic_subsequence("") == 0
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindromic_subsequence()