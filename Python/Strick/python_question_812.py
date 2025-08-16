# Python Question: Find the Largest Palindromic Substring
'''
Given a string `s`, find the longest palindromic substring in `s`.
A palindromic substring is a substring that reads the same forwards and backward.

Example:
Input: s = "babad"
Output: "bab" or "aba" (both are valid)

Input: s = "cbbd"
Output: "bb"

Input: s = "a"
Output: "a"

Input: s = "ac"
Output: "a"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring in the given string.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring.
    """
    n = len(s)
    if n < 2:
        return s

    # dp[i][j] will be true if the substring s[i:j+1] is a palindrome, otherwise false.
    dp = [[False] * n for _ in range(n)]

    # All substrings of length 1 are palindromes.
    for i in range(n):
        dp[i][i] = True

    # longest_palindrome_substring will store the longest palindromic substring found so far.
    longest_palindrome_substring = s[0]

    # Check for palindromes of length 2.
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            longest_palindrome_substring = s[i:i + 2]

    # Check for palindromes of length 3 or greater.
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if k > len(longest_palindrome_substring):
                    longest_palindrome_substring = s[i:j + 1]

    return longest_palindrome_substring


# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ["bab", "aba"]
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("forgeeksskeegfor") == "geeksskeeg"
    assert longest_palindrome("") == ""
    assert longest_palindrome("abcda") == "a"
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindrome()