# Python Question: Find the Longest Palindromic Substring
'''
Given a string `s`, find the longest palindromic substring in `s`.

A palindromic substring is a substring that reads the same forwards and backward.

Example:
Input: s = "babad"
Output: "bab" or "aba" (Both are valid longest palindromic substrings)

Input: s = "cbbd"
Output: "bb"

Input: s = "a"
Output: "a"

Input: s = "ac"
Output: "a"

Constraints:
1 <= len(s) <= 1000
s consists only of digits and English letters (lower-case and/or upper-case)
'''

# Solution
def longest_palindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    Approach:
    This solution uses the "Expand Around Center" approach. It iterates through each character
    in the string and considers it as the center of a potential palindrome.  It expands outward
    from the center (both single character and between two characters) to find the longest
    palindrome centered at that position.

    Time Complexity: O(n^2), where n is the length of the string.
    Space Complexity: O(1)
    """

    if not s:
        return ""

    start = 0
    end = 0

    def expand_around_center(left, right):
        """
        Expands around the center (left, right) to find the longest palindrome.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1  # Return the correct start and end indices

    for i in range(len(s)):
        # Odd length palindrome
        left1, right1 = expand_around_center(i, i)

        # Even length palindrome
        left2, right2 = expand_around_center(i, i + 1)

        # Update the longest palindrome if necessary
        if (right1 - left1 + 1) > (end - start + 1):
            start = left1
            end = right1

        if (right2 - left2 + 1) > (end - start + 1):
            start = left2
            end = right2

    return s[start:end + 1]


# Test cases
def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
    assert longest_palindrome("banana") == "anana"
    assert longest_palindrome("") == ""
    assert longest_palindrome("ccc") == "ccc"
    assert longest_palindrome("abbcccddd") in ("ccc", "ddd")
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_palindrome()