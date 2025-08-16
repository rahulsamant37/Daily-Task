# Python Question: Find the Longest Palindromic Substring
'''
Given a string `s`, find the longest palindromic substring in `s`.

A palindromic substring is a substring that reads the same forwards and backward.

Example:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"

Input: s = "a"
Output: "a"

Input: s = "ac"
Output: "a"
'''

# Solution
def solution():
    def longestPalindrome(s: str) -> str:
        """
        Finds the longest palindromic substring in the given string.

        Args:
            s: The input string.

        Returns:
            The longest palindromic substring.
        """
        n = len(s)
        if n < 2:
            return s  # Single character or empty string is a palindrome

        start = 0  # Start index of the longest palindrome found so far
        max_len = 1  # Length of the longest palindrome found so far

        # Create a DP table to store palindrome information
        dp = [[False] * n for _ in range(n)]

        # All single characters are palindromes
        for i in range(n):
            dp[i][i] = True

        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # Check for palindromes of length 3 or more
        for k in range(3, n + 1):  # k is the length of the substring
            for i in range(n - k + 1):  # i is the starting index of the substring
                j = i + k - 1  # j is the ending index of the substring

                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True

                    if k > max_len:
                        start = i
                        max_len = k

        return s[start:start + max_len]

    return longestPalindrome
    

# Test cases
def test_solution():
    longestPalindrome = solution()

    assert longestPalindrome("babad") in ("bab", "aba")
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("a") == "a"
    assert longestPalindrome("ac") == "a"
    assert longestPalindrome("racecar") == "racecar"
    assert longestPalindrome("bananas") == "anana"
    assert longestPalindrome("") == ""
    assert longestPalindrome("abcda") == "a"
    assert longestPalindrome("aaaaa") == "aaaaa"
    assert longestPalindrome("ababa") == "ababa"
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()