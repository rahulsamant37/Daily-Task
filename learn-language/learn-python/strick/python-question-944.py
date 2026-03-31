# Python Question: Longest Palindromic Substring
'''
Given a string s, find the longest palindromic substring in s.

A palindromic substring is a substring that reads the same forwards and backward.

Example:
Input: s = "babad"
Output: "bab" or "aba" (either is acceptable)

Input: s = "cbbd"
Output: "bb"
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring in the given string s.

    The approach is to iterate through each character in the string and consider it as the center of a potential palindrome.
    We expand outwards from the center, checking for palindromes of both odd and even lengths.
    We keep track of the longest palindrome found so far and update it whenever we find a longer one.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring in s.
    """
    if not s:
        return ""

    longest = ""
    for i in range(len(s)):
        # Odd length palindromes
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(longest):
                longest = s[l:r + 1]
            l -= 1
            r += 1

        # Even length palindromes
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(longest):
                longest = s[l:r + 1]
            l -= 1
            r += 1

    return longest

# Test cases
def test_longest_palindrome():
    """
    Tests the longest_palindrome function with several test cases.
    """
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("bb") == "bb"
    assert longest_palindrome("bananas") == "anana"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("") == ""
    assert longest_palindrome("abcda") in ("a", "b", "c", "d")
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome()