# Python Question: Find the Longest Palindromic Subsequence
'''
Given a string `s`, find the length of the longest palindromic subsequence's length.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. A palindrome is a sequence that reads the same backward as forward.

Example:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
'''

# Solution
def solution(s):
    """
    Finds the length of the longest palindromic subsequence in a given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.
    """

    n = len(s)

    # Create a DP table to store the lengths of longest palindromic subsequences.
    # dp[i][j] stores the length of the longest palindromic subsequence in s[i:j+1].
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are palindromes of length 1.
    for i in range(n):
        dp[i][i] = 1

    # Iterate through substrings of increasing length.
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # If the characters at the ends of the substring match,
            # then the longest palindromic subsequence is 2 plus the length of the
            # longest palindromic subsequence of the substring without the end characters.
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            # Otherwise, the longest palindromic subsequence is the maximum of the
            # longest palindromic subsequences of the substrings without the left or right end character.
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The length of the longest palindromic subsequence of the entire string is stored in dp[0][n-1].
    return dp[0][n - 1]

# Test cases
def test_solution():
    assert solution("bbbab") == 4
    assert solution("cbbd") == 2
    assert solution("a") == 1
    assert solution("ac") == 1
    assert solution("aba") == 3
    assert solution("racecar") == 7
    assert solution("abcdefg") == 1
    assert solution("bananas") == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()