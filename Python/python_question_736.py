# Python Question: Longest Palindromic Substring
'''
Given a string `s`, find the longest palindromic substring in `s`.

A palindromic substring is a substring that reads the same forwards and backward.

Example:
Input: s = "babad"
Output: "bab" or "aba" (either is acceptable)

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
    Finds the longest palindromic substring in the given string s.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring in s.
    """

    n = len(s)
    if n < 2:
        return s  # Single character or empty string is a palindrome

    # dp[i][j] will be True if the substring s[i:j+1] is a palindrome, False otherwise.
    dp = [[False] * n for _ in range(n)]

    # All substrings of length 1 are palindromes.
    for i in range(n):
        dp[i][i] = True

    # longest_palindrome_start and max_length will store the start index and length of the
    # longest palindromic substring found so far.
    longest_palindrome_start = 0
    max_length = 1

    # Check for palindromes of length 2.
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            longest_palindrome_start = i
            max_length = 2

    # Check for palindromes of length 3 or greater.  Iterate through possible lengths (k) and starting indices (i)
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1  # Ending index of the substring

            # If the substring s[i+1:j] is a palindrome and the characters at the start and end
            # are equal, then s[i:j+1] is also a palindrome.
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True

                # Update the longest palindrome if we found a longer one.
                if k > max_length:
                    longest_palindrome_start = i
                    max_length = k

    # Return the longest palindromic substring.
    return s[longest_palindrome_start:longest_palindrome_start + max_length]


# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("forgeeksskeegfor") == "geeksskeeg"
    assert longest_palindrome("") == ""
    assert longest_palindrome("abcda") == "a"
    assert longest_palindrome("aaaaaaaaa") == "aaaaaaaaa"

if __name__ == "__main__":
    test_longest_palindrome()