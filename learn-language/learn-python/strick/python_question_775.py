# Python Question: Find the Longest Palindromic Substring with k Mismatches
'''
Given a string `s` and an integer `k`, find the longest palindromic substring of `s` that can be formed by changing at most `k` characters.

Example:
Input: s = "abaxyzzyxf", k = 2
Output: "xyzzyx"

Input: s = "abcde", k = 1
Output: "bcb" or "cdc" or "ded"

Input: s = "abcba", k = 0
Output: "abcba"
'''

# Solution
def longest_palindrome_with_k_mismatches(s, k):
    """
    Finds the longest palindromic substring of s with at most k mismatches.

    Args:
        s: The input string.
        k: The maximum number of allowed mismatches.

    Returns:
        The longest palindromic substring with at most k mismatches.
    """
    n = len(s)
    longest_palindrome = ""

    for i in range(n):
        # Odd length palindromes
        l, r = i, i
        mismatches = 0
        while l >= 0 and r < n:
            if s[l] != s[r]:
                mismatches += 1
            if mismatches > k:
                break
            if (r - l + 1) > len(longest_palindrome):
                longest_palindrome = s[l:r+1]
            l -= 1
            r += 1

        # Even length palindromes
        l, r = i, i + 1
        mismatches = 0
        while l >= 0 and r < n:
            if s[l] != s[r]:
                mismatches += 1
            if mismatches > k:
                break
            if (r - l + 1) > len(longest_palindrome):
                longest_palindrome = s[l:r+1]
            l -= 1
            r += 1

    return longest_palindrome

# Test cases
def test_longest_palindrome_with_k_mismatches():
    assert longest_palindrome_with_k_mismatches("abaxyzzyxf", 2) == "xyzzyx"
    assert longest_palindrome_with_k_mismatches("abcde", 1) in ("bcb", "cdc", "ded")
    assert longest_palindrome_with_k_mismatches("abcba", 0) == "abcba"
    assert longest_palindrome_with_k_mismatches("abaxyzzyxf", 0) == "zyz"
    assert longest_palindrome_with_k_mismatches("aaaaa", 1) == "aaaaa"
    assert longest_palindrome_with_k_mismatches("a", 0) == "a"
    assert longest_palindrome_with_k_mismatches("a", 1) == "a"
    assert longest_palindrome_with_k_mismatches("", 0) == ""
    assert longest_palindrome_with_k_mismatches("racecar", 0) == "racecar"
    assert longest_palindrome_with_k_mismatches("racecar", 1) == "racecar"
    assert longest_palindrome_with_k_mismatches("abcdeba", 1) == "abcdeba"
    assert longest_palindrome_with_k_mismatches("abcdeba", 2) == "abcdeba"
    assert longest_palindrome_with_k_mismatches("abcdeba", 3) == "abcdeba"
    assert longest_palindrome_with_k_mismatches("aabbcc", 2) in ("aabb", "bbcc", "acca", "bcca")
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome_with_k_mismatches()