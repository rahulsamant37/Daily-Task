# Python Question: Find the Longest Palindromic Substring with K Deletions
'''
Given a string `s` and an integer `k`, find the length of the longest palindromic substring that can be obtained from `s` by deleting at most `k` characters.

Example:
Input: s = "abcdeca", k = 1
Output: 5
Explanation: The longest palindromic substring we can obtain is "abeca" by deleting 'd'.

Input: s = "ababa", k = 0
Output: 5
Explanation: The longest palindromic substring is "ababa" itself.

Input: s = "abca", k = 2
Output: 4
Explanation: The longest palindromic substring is "abca" itself (or "aba", "aca", etc.).

Input: s = "abc", k = 1
Output: 2
Explanation: Longest palindromic substring is "aa", "bb", or "cc".

Input: s = "axbyczda", k = 2
Output: 4
Explanation: "azda" is the longest palindromic substring.
'''

# Solution
def solution():
    def longest_palindrome_with_k_deletions(s, k):
        """
        Finds the length of the longest palindromic substring obtainable from s with at most k deletions.

        Args:
            s: The input string.
            k: The maximum number of allowed deletions.

        Returns:
            The length of the longest palindromic substring.
        """
        n = len(s)

        # dp[i][j][l] stores the length of the longest palindromic subsequence of s[i:j+1]
        # with at most l deletions allowed.
        dp = [[[0 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]

        # Base case: single characters are palindromes of length 1.
        for i in range(n):
            for l in range(k + 1):
                dp[i][i][l] = 1

        # Iterate over substring lengths from 2 to n.
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Iterate over the allowed number of deletions.
                for l in range(k + 1):
                    # If the characters at the ends of the substring match,
                    # the length of the LPS is 2 + the length of the LPS of the substring without these characters.
                    if s[i] == s[j]:
                        dp[i][j][l] = 2 + dp[i + 1][j - 1][l]
                    else:
                        # If the characters at the ends do not match, we have two options:
                        # 1. Delete the character at the beginning of the substring.
                        # 2. Delete the character at the end of the substring.
                        # We choose the option that gives us the longer LPS.
                        if l > 0:
                            dp[i][j][l] = max(dp[i + 1][j][l - 1], dp[i][j - 1][l - 1])
                        else:
                            dp[i][j][l] = 0  # No deletions left, so can't form a palindrome

                        dp[i][j][l] = max(dp[i][j][l], dp[i+1][j][l], dp[i][j-1][l])
        return dp[0][n - 1][k]

    return longest_palindrome_with_k_deletions
    

# Test cases
def test_solution():
    longest_palindrome_with_k_deletions = solution()
    assert longest_palindrome_with_k_deletions("abcdeca", 1) == 5
    assert longest_palindrome_with_k_deletions("ababa", 0) == 5
    assert longest_palindrome_with_k_deletions("abca", 2) == 4
    assert longest_palindrome_with_k_deletions("abc", 1) == 2
    assert longest_palindrome_with_k_deletions("axbyczda", 2) == 4
    assert longest_palindrome_with_k_deletions("abcdba", 0) == 6
    assert longest_palindrome_with_k_deletions("abcdba", 1) == 6
    assert longest_palindrome_with_k_deletions("abcdba", 2) == 6
    assert longest_palindrome_with_k_deletions("abc", 0) == 1
    assert longest_palindrome_with_k_deletions("abc", 2) == 3
    assert longest_palindrome_with_k_deletions("racecar", 0) == 7
    assert longest_palindrome_with_k_deletions("racecar", 1) == 7
    assert longest_palindrome_with_k_deletions("abcbda", 1) == 5
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()