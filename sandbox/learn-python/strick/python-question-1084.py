# Python Question: Find the Longest Palindromic Substring with k Mismatches
'''
Given a string `s` and an integer `k`, find the longest palindromic substring of `s` that allows at most `k` mismatches with its reversed counterpart.

A substring `s[i:j+1]` is considered a palindrome with at most `k` mismatches if the number of positions where `s[x]` != `s[j-x+i]` for `i <= x <= j` is less than or equal to `k`.

Input: s = "abaxyzzyxf", k = 2
Output: "xyzzyx"

Input: s = "racecar", k = 0
Output: "racecar"

Input: s = "racecar", k = 1
Output: "racecar"

Input: s = "banana", k = 1
Output: "anana"
'''

# Solution
def longest_palindrome_with_k_mismatches(s, k):
    """
    Finds the longest palindromic substring of s with at most k mismatches.

    Args:
        s: The input string.
        k: The maximum number of allowed mismatches.

    Returns:
        The longest palindromic substring of s with at most k mismatches.
    """
    n = len(s)
    longest_palindrome = ""

    # Iterate through all possible center positions in the string
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
def test_solution():
    assert longest_palindrome_with_k_mismatches("abaxyzzyxf", 2) == "xyzzyx"
    assert longest_palindrome_with_k_mismatches("racecar", 0) == "racecar"
    assert longest_palindrome_with_k_mismatches("racecar", 1) == "racecar"
    assert longest_palindrome_with_k_mismatches("banana", 1) == "anana"
    assert longest_palindrome_with_k_mismatches("abc", 0) == "a"
    assert longest_palindrome_with_k_mismatches("abc", 1) == "a"
    assert longest_palindrome_with_k_mismatches("abcdba", 1) == "bcdb"
    assert longest_palindrome_with_k_mismatches("abcdba", 2) == "abcdba"
    assert longest_palindrome_with_k_mismatches("aaaaaaaaa", 0) == "aaaaaaaaa"
    assert longest_palindrome_with_k_mismatches("aaaaaaaaa", 1) == "aaaaaaaaa"
    assert longest_palindrome_with_k_mismatches("abcdeffedcba", 0) == "abcdeffedcba"
    assert longest_palindrome_with_k_mismatches("abcdeffedcba", 1) == "abcdeffedcba"
    assert longest_palindrome_with_k_mismatches("abcdeffedcbaa", 1) == "abcdeffedcba"
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()