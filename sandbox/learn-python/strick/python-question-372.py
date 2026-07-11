# Python Question: Find the Longest Palindromic Substring with k Mismatches
'''
Given a string `s` and an integer `k`, find the longest palindromic substring of `s` that contains at most `k` mismatches. A mismatch is defined as a position where characters at symmetric positions in the substring are different.

For example:
Input: s = "abaxyzzyxf", k = 1
Output: "xyzzyx"

Input: s = "banana", k = 0
Output: "anana"

Input: s = "abcde", k = 2
Output: "bcde" or "abcd" (any longest valid substring is acceptable)
'''

# Solution
def solution():
    def longest_palindrome_with_k_mismatches(s, k):
        """
        Finds the longest palindromic substring of s with at most k mismatches.

        Args:
            s: The input string.
            k: The maximum allowed mismatches.

        Returns:
            The longest palindromic substring with at most k mismatches.
        """
        n = len(s)
        longest_palindrome = ""

        # Iterate through all possible center positions of the palindrome
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

    return longest_palindrome_with_k_mismatches

# Test cases
def test_solution():
    func = solution()
    assert func("abaxyzzyxf", 1) == "xyzzyx"
    assert func("banana", 0) == "anana"
    assert func("abcde", 2) in ("bcde", "abcd")
    assert func("racecar", 0) == "racecar"
    assert func("a", 0) == "a"
    assert func("aa", 0) == "aa"
    assert func("ab", 1) in ("a", "b", "ab")
    assert func("abc", 1) in ("a", "b", "c", "ab", "bc")
    assert func("abcba", 1) == "abcba"
    assert func("abccba", 1) == "abccba"
    assert func("abccba", 0) == "bccb"
    assert func("aaabbbaaa", 1) == "aaabbbaaa"
    assert func("aaabbbaaa", 0) == "aaabbbaaa"
    assert func("aabbccaabbcc", 1) == "aabbcc"
    assert func("aabbccaabbcc", 2) == "aabbccaabbcc"
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()