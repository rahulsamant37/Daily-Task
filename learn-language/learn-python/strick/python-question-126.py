# Python Question: Find the Longest Palindromic Substring with k Mismatches
'''
Given a string `s` and an integer `k`, find the longest palindromic substring of `s` that can be formed by changing at most `k` characters.

Example:
Input: s = "abaxyzzyxf", k = 2
Output: "xyzzyx"

Input: s = "banana", k = 1
Output: "anana"

Constraints:
1 <= len(s) <= 250
0 <= k <= len(s)
'''

# Solution
def longest_palindrome_with_k_mismatches(s, k):
    """
    Finds the longest palindromic substring of s that can be formed by changing at most k characters.

    Args:
        s: The input string.
        k: The maximum number of characters that can be changed.

    Returns:
        The longest palindromic substring.
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
                longest_palindrome = s[l:r + 1]
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
                longest_palindrome = s[l:r + 1]
            l -= 1
            r += 1

    return longest_palindrome

# Test cases
def test_longest_palindrome_with_k_mismatches():
    assert longest_palindrome_with_k_mismatches("abaxyzzyxf", 2) == "xyzzyx"
    assert longest_palindrome_with_k_mismatches("banana", 1) == "anana"
    assert longest_palindrome_with_k_mismatches("abc", 0) == "a" or longest_palindrome_with_k_mismatches("abc", 0) == "b" or longest_palindrome_with_k_mismatches("abc", 0) == "c"
    assert longest_palindrome_with_k_mismatches("abcba", 0) == "abcba"
    assert longest_palindrome_with_k_mismatches("abcba", 1) == "abcba"
    assert longest_palindrome_with_k_mismatches("abcda", 1) == "abcba" or longest_palindrome_with_k_mismatches("abcda", 1) == "adcda"
    assert longest_palindrome_with_k_mismatches("racecar", 2) == "racecar"
    assert longest_palindrome_with_k_mismatches("racecar", 0) == "racecar"
    assert longest_palindrome_with_k_mismatches("aba", 0) == "aba"
    assert longest_palindrome_with_k_mismatches("a", 0) == "a"
    assert longest_palindrome_with_k_mismatches("", 0) == ""
    assert longest_palindrome_with_k_mismatches("aaaaa", 2) == "aaaaa"
    assert longest_palindrome_with_k_mismatches("abcdedca", 1) == "abcdedca"
    assert longest_palindrome_with_k_mismatches("abcdedca", 0) == "a" or longest_palindrome_with_k_mismatches("abcdedca", 0) == "b" or longest_palindrome_with_k_mismatches("abcdedca", 0) == "c" or longest_palindrome_with_k_mismatches("abcdedca", 0) == "d" or longest_palindrome_with_k_mismatches("abcdedca", 0) == "e"
    assert longest_palindrome_with_k_mismatches("abcde", 2) == "abcba" or longest_palindrome_with_k_mismatches("abcde", 2) == "bcdcb" or longest_palindrome_with_k_mismatches("cdec"
                                                                                                    ) == "cdec"
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_palindrome_with_k_mismatches()