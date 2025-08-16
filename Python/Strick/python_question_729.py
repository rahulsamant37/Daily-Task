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
    # Create a 2D array dp where dp[i][j] stores the length of the longest palindromic subsequence
    # in the substring s[i:j+1].
    #
    # Base case: dp[i][i] = 1 for all i (a single character is a palindrome of length 1).
    #
    # For i < j:
    # - If s[i] == s[j], then dp[i][j] = dp[i+1][j-1] + 2 (we can extend the palindrome by including s[i] and s[j]).
    # - If s[i] != s[j], then dp[i][j] = max(dp[i+1][j], dp[i][j-1]) (we either exclude s[i] or s[j] and take the max).
    #
    # The result is dp[0][n-1], where n is the length of the string.

    s = input()
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters
    for i in range(n):
        dp[i][i] = 1

    # Iterate over increasing lengths of substrings
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    print(dp[0][n - 1])

# Test cases
def test_solution():
    # Test case 1
    print("Test Case 1:")
    s1 = "bbbab"
    input_mock = lambda: s1
    original_input = __builtins__.input
    __builtins__.input = input_mock
    solution()
    __builtins__.input = original_input
    # Expected output: 4

    # Test case 2
    print("\nTest Case 2:")
    s2 = "cbbd"
    input_mock = lambda: s2
    original_input = __builtins__.input
    __builtins__.input = input_mock
    solution()
    __builtins__.input = original_input
    # Expected output: 2

    # Test case 3
    print("\nTest Case 3:")
    s3 = "a"
    input_mock = lambda: s3
    original_input = __builtins__.input
    __builtins__.input = input_mock
    solution()
    __builtins__.input = original_input
    # Expected output: 1

    # Test case 4
    print("\nTest Case 4:")
    s4 = "ac"
    input_mock = lambda: s4
    original_input = __builtins__.input
    __builtins__.input = input_mock
    solution()
    __builtins__.input = original_input
    # Expected output: 1

    # Test case 5
    print("\nTest Case 5:")
    s5 = "aba"
    input_mock = lambda: s5
    original_input = __builtins__.input
    __builtins__.input = input_mock
    solution()
    __builtins__.input = original_input

if __name__ == "__main__":
    test_solution()