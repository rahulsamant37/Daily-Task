# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.

Example:
Input: s = "babad"
Output: "bab" or "aba"

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
    Finds the longest palindromic substring in a given string.

    The approach uses dynamic programming to build a table indicating whether a substring
    from i to j is a palindrome.  The table is built bottom-up, starting with single-character
    palindromes and expanding to longer substrings.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring found in s.
    """
    n = len(s)
    if n < 2:
        return s  # Single character or empty string is a palindrome

    # dp[i][j] will be True if the substring s[i:j+1] is a palindrome, False otherwise.
    dp = [[False] * n for _ in range(n)]

    # All substrings of length 1 are palindromes.
    for i in range(n):
        dp[i][i] = True

    # Start with the longest palindrome being the first character.
    start = 0
    max_length = 1

    # Check for palindromes of length 2.
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    # Check for palindromes of length 3 or more.  k is the length of the substring.
    for k in range(3, n + 1):
        # Iterate through all possible starting positions for substrings of length k.
        for i in range(n - k + 1):
            # j is the ending index of the substring.
            j = i + k - 1

            # If the substring s[i+1:j] is a palindrome and s[i] == s[j], then s[i:j+1] is a palindrome.
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True

                # If this palindrome is longer than the current longest palindrome, update the start and max_length.
                if k > max_length:
                    start = i
                    max_length = k

    # Return the longest palindromic substring.
    return s[start:start + max_length]

# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("abcda") == "a"
    assert longest_palindrome("") == ""
    assert longest_palindrome("ccc") == "ccc"
    assert longest_palindrome("aaaa") == "aaaa"

if __name__ == "__main__":
    test_longest_palindrome()