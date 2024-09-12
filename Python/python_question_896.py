# Python Question: Find the Longest Palindromic Substring with k Mismatches
'''
Given a string `s` and an integer `k`, find the longest palindromic substring of `s` that can be formed by changing at most `k` characters.

Example:
Input: s = "abaxyzzyxf", k = 2
Output: "xyzzyx"

Input: s = "abaxyzzyxf", k = 0
Output: "zyzz"

Input: s = "abcda", k = 1
Output: "bcda" or "acbd" or "abcda" (any of these is acceptable)
'''

# Solution
def solution():
    def longest_palindrome_with_k_mismatches(s: str, k: int) -> str:
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
            for j in range(i, n):
                # Extract the substring
                substring = s[i:j+1]
                
                # Check if it can be made a palindrome with at most k changes
                mismatches = 0
                left = 0
                right = len(substring) - 1

                while left < right:
                    if substring[left] != substring[right]:
                        mismatches += 1
                    left += 1
                    right -= 1
                
                if mismatches <= k and len(substring) > len(longest_palindrome):
                    longest_palindrome = substring

        return longest_palindrome

    return longest_palindrome_with_k_mismatches

# Test cases
def test_solution():
    longest_palindrome_with_k_mismatches = solution()

    assert longest_palindrome_with_k_mismatches("abaxyzzyxf", 2) == "xyzzyx"
    assert longest_palindrome_with_k_mismatches("abaxyzzyxf", 0) == "zyzz"
    assert longest_palindrome_with_k_mismatches("abcda", 1) in ("abcba", "acbca", "abcdcba") # Allow for variations.
    assert longest_palindrome_with_k_mismatches("racecar", 0) == "racecar"
    assert longest_palindrome_with_k_mismatches("racecar", 1) == "racecar"
    assert longest_palindrome_with_k_mismatches("a", 0) == "a"
    assert longest_palindrome_with_k_mismatches("aa", 0) == "aa"
    assert longest_palindrome_with_k_mismatches("ab", 1) == "a" or longest_palindrome_with_k_mismatches("ab", 1) == "b" # Allow for variations.
    assert longest_palindrome_with_k_mismatches("abc", 2) in ("a", "b", "c") # Allow for variations.
    assert longest_palindrome_with_k_mismatches("abc", 3) == "a" or longest_palindrome_with_k_mismatches("abc", 3) == "b" or longest_palindrome_with_k_mismatches("abc", 3) == "c" #Allow for variations.
    assert longest_palindrome_with_k_mismatches("bananas", 1) == "anana"
    assert longest_palindrome_with_k_mismatches("bananas", 2) == "anana"
    assert longest_palindrome_with_k_mismatches("bananas", 3) == "anana"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()