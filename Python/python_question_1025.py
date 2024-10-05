# Python Question: Find the Longest Palindromic Substring with K Changes
'''
Given a string `s` and an integer `k`, find the length of the longest palindromic substring of `s` that can be formed by making at most `k` changes to the characters in the string.

Example:
Input: s = "abcba", k = 0
Output: 5

Input: s = "abcda", k = 1
Output: 5 (abcba)

Input: s = "abcade", k = 1
Output: 5 (abcba or edcde, etc.)

Input: s = "abcade", k = 2
Output: 6 (abcdea)

Input: s = "abcadef", k = 2
Output: 5 (abcdcba, edcfe, etc.)
'''

# Solution
def solution():
    def longest_palindrome_with_k_changes(s, k):
        """
        Finds the length of the longest palindromic substring of s with at most k changes.

        Args:
            s: The input string.
            k: The maximum number of changes allowed.

        Returns:
            The length of the longest palindromic substring.
        """

        n = len(s)
        max_len = 0

        # Iterate through all possible substring starting positions
        for i in range(n):
            # Iterate through all possible substring ending positions
            for j in range(i, n):
                # Extract the substring
                substring = s[i:j+1]
                
                # Calculate the number of changes needed to make the substring a palindrome
                changes_needed = 0
                for l in range(len(substring) // 2):
                    if substring[l] != substring[len(substring) - 1 - l]:
                        changes_needed += 1
                
                # If the number of changes needed is less than or equal to k,
                # update the maximum length
                if changes_needed <= k:
                    max_len = max(max_len, len(substring))

        return max_len

    return longest_palindrome_with_k_changes

# Test cases
def test_solution():
    longest_palindrome_with_k_changes = solution()

    # Test case 1
    s1 = "abcba"
    k1 = 0
    expected1 = 5
    actual1 = longest_palindrome_with_k_changes(s1, k1)
    assert actual1 == expected1, f"Test Case 1 Failed: Expected {expected1}, but got {actual1}"

    # Test case 2
    s2 = "abcda"
    k2 = 1
    expected2 = 5
    actual2 = longest_palindrome_with_k_changes(s2, k2)
    assert actual2 == expected2, f"Test Case 2 Failed: Expected {expected2}, but got {actual2}"

    # Test case 3
    s3 = "abcade"
    k3 = 1
    expected3 = 5
    actual3 = longest_palindrome_with_k_changes(s3, k3)
    assert actual3 == expected3, f"Test Case 3 Failed: Expected {expected3}, but got {actual3}"

    # Test case 4
    s4 = "abcade"
    k4 = 2
    expected4 = 6
    actual4 = longest_palindrome_with_k_changes(s4, k4)
    assert actual4 == expected4, f"Test Case 4 Failed: Expected {expected4}, but got {actual4}"
    
    # Test case 5
    s5 = "abcadef"
    k5 = 2
    expected5 = 5
    actual5 = longest_palindrome_with_k_changes(s5, k5)
    assert actual5 == expected5, f"Test Case 5 Failed: Expected {expected5}, but got {actual5}"

    # Test case 6
    s6 = "aaaaa"
    k6 = 2
    expected6 = 5
    actual6 = longest_palindrome_with_k_changes(s6, k6)
    assert actual6 == expected6, f"Test Case 6 Failed: Expected {expected6}, but got {actual6}"

    # Test case 7
    s7 = "abcdefg"
    k7 = 3
    expected7 = 4
    actual7 = longest_palindrome_with_k_changes(s7, k7)
    assert actual7 == expected7, f"Test Case 7 Failed: Expected {expected7}, but got {actual7}"

    # Test case 8
    s8 = "zzazz"
    k8 = 0
    expected8 = 5
    actual8 = longest_palindrome_with_k_changes(s8, k8)
    assert actual8 == expected8, f"Test Case 8 Failed: Expected {expected8}, but got {actual8}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()