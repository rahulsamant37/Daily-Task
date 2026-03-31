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
    # Approach: Dynamic Programming
    # We can use dynamic programming to solve this problem.
    # Let dp[i][j] be the length of the longest palindromic subsequence of s[i:j+1].
    # If s[i] == s[j], then dp[i][j] = dp[i+1][j-1] + 2.
    # Otherwise, dp[i][j] = max(dp[i+1][j], dp[i][j-1]).
    # The base case is dp[i][i] = 1 for all i.

    def longestPalindromeSubseq(s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate over the length of the substring
        for length in range(2, n + 1):
            # Iterate over the starting index of the substring
            for i in range(n - length + 1):
                j = i + length - 1  # Calculate the ending index of the substring
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2 if length > 2 else 2 # if substring is of length 2, then it's 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]
    
    return longestPalindromeSubseq

# Test cases
def test_solution():
    s1 = "bbbab"
    expected1 = 4
    assert solution()(s1) == expected1, f"Test case 1 failed: Expected {expected1}, got {solution()(s1)}"

    s2 = "cbbd"
    expected2 = 2
    assert solution()(s2) == expected2, f"Test case 2 failed: Expected {expected2}, got {solution()(s2)}"

    s3 = "a"
    expected3 = 1
    assert solution()(s3) == expected3, f"Test case 3 failed: Expected {expected3}, got {solution()(s3)}"

    s4 = "ac"
    expected4 = 1
    assert solution()(s4) == expected4, f"Test case 4 failed: Expected {expected4}, got {solution()(s4)}"

    s5 = "aba"
    expected5 = 3
    assert solution()(s5) == expected5, f"Test case 5 failed: Expected {expected5}, got {solution()(s5)}"
    
    s6 = "abcabcabcabc"
    expected6 = 4
    assert solution()(s6) == 4, f"Test case 6 failed: Expected 4, got {solution()(s6)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()