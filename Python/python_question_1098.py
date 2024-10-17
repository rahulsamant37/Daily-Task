# Python Question: Find the Longest Palindromic Substring with k Mismatches
'''
Given a string `s` and an integer `k`, find the longest palindromic substring of `s` that has at most `k` mismatches with its reversed counterpart.

A palindrome is a string that reads the same forwards and backward.  A substring is a contiguous sequence of characters within a string.  A mismatch is when two characters at the same position in two strings are different.

Example:
Input: s = "abaxyzzyxf", k = 2
Output: "xyzzyx"

Input: s = "abaxyzzyxf", k = 0
Output: "zyz"

Input: s = "racecar", k = 0
Output: "racecar"

Input: s = "racecar", k = 1
Output: "racecar"
'''

# Solution
def longest_palindrome_with_k_mismatches(s, k):
    """
    Finds the longest palindromic substring of s with at most k mismatches.

    Args:
        s: The input string.
        k: The maximum number of allowed mismatches.

    Returns:
        The longest palindromic substring.
    """
    n = len(s)
    longest_palindrome = ""

    # Iterate through all possible center positions (single characters or between characters)
    for i in range(n):
        # Odd length palindromes (center is a single character)
        l, r = i, i
        mismatches = 0
        while l >= 0 and r < n:
            if s[l] != s[r]:
                mismatches += 1
            if mismatches > k:
                break
            if (r - l + 1) > len(longest_palindrome):
                longest_palindrome = s[l:r + 1]
            l -= 1
            r += 1

        # Even length palindromes (center is between two characters)
        l, r = i, i + 1
        mismatches = 0
        while l >= 0 and r < n:
            if s[l] != s[r]:
                mismatches += 1
            if mismatches > k:
                break
            if (r - l + 1) > len(longest_palindrome):
                longest_palindrome = s[l:r + 1]
            l -= 1
            r += 1

    return longest_palindrome


# Test cases
def test_solution():
    assert longest_palindrome_with_k_mismatches("abaxyzzyxf", 2) == "xyzzyx"
    assert longest_palindrome_with_k_mismatches("abaxyzzyxf", 0) == "zyz"
    assert longest_palindrome_with_k_mismatches("racecar", 0) == "racecar"
    assert longest_palindrome_with_k_mismatches("racecar", 1) == "racecar"
    assert longest_palindrome_with_k_mismatches("abcba", 0) == "abcba"
    assert longest_palindrome_with_k_mismatches("abcba", 1) == "abcba"
    assert longest_palindrome_with_k_mismatches("abc", 0) == "a" or longest_palindrome_with_k_mismatches("abc", 0) == "b" or longest_palindrome_with_k_mismatches("abc", 0) == "c"
    assert longest_palindrome_with_k_mismatches("abc", 1) == "aba" or longest_palindrome_with_k_mismatches("abc", 1) == "bcb"
    assert longest_palindrome_with_k_mismatches("aaaaa", 2) == "aaaaa"
    assert longest_palindrome_with_k_mismatches("aaaaa", 0) == "aaaaa"
    assert longest_palindrome_with_k_mismatches("abaab", 1) == "aba" or longest_palindrome_with_k_mismatches("abaab", 1) == "baab"
    assert longest_palindrome_with_k_mismatches("abaab", 0) == "aba" or longest_palindrome_with_k_mismatches("abaab", 0) == "baa"
    assert longest_palindrome_with_k_mismatches("abcde", 2) == "ada" or longest_palindrome_with_k_mismatches("abcde", 2) == "bdb" or longest_palindrome_with_k_mismatches("abcde", 2) == "cec" or longest_palindrome_with_k_mismatches("abcde", 2) == "ded" or longest_palindrome_with_k_mismatches("abcde", 2) == "eae"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()