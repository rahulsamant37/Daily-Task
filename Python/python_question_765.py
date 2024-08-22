# Python Question: Find the Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

A palindromic substring is a substring that reads the same forwards and backward.

Example:
Input: "babad"
Output: "bab" or "aba" (either is a valid answer)

Input: "cbbd"
Output: "bb"

Input: "a"
Output: "a"

Input: "ac"
Output: "a"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring.
    """

    if not s:
        return ""

    n = len(s)
    if n == 1:
        return s

    longest_substring = ""

    # Helper function to expand around center
    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    for i in range(n):
        # Odd length palindromes
        substring1 = expand_around_center(i, i)
        if len(substring1) > len(longest_substring):
            longest_substring = substring1

        # Even length palindromes
        substring2 = expand_around_center(i, i + 1)
        if len(substring2) > len(longest_substring):
            longest_substring = substring2

    return longest_substring

# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("level") == "level"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("") == ""
    assert longest_palindrome("abcda") in ("a", "b", "c", "d")
    assert longest_palindrome("aaaaa") == "aaaaa"
    assert longest_palindrome("ababa") == "ababa"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()