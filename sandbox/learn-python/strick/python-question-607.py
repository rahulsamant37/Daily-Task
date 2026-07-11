# Python Question: Find the Minimum Window Substring
'''
Given two strings `s` and `t`, find the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string "".

If there are multiple such substrings satisfying the minimum length requirement, return the one with the leftmost starting position.

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Input: s = "a", t = "a"
Output: "a"

Input: s = "a", t = "aa"
Output: ""
'''

# Solution
def solution():
    def min_window(s: str, t: str) -> str:
        """
        Finds the minimum window substring of s such that every character in t is included in the window.
        """
        if not t or not s:
            return ""

        # Dictionary to store the frequency of characters in t
        dict_t = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        # Number of unique characters in t that we need to find in s
        required = len(dict_t)

        # Left and right pointers for the sliding window
        left, right = 0, 0

        # Number of unique characters in t that are present in the current window
        formed = 0

        # Dictionary to store the frequency of characters in the current window
        window_counts = {}

        # Result window coordinates and length
        ans = float('inf'), None, None  # (window length, left, right)

        while right < len(s):
            # Add one character from the right to the window
            character = s[right]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character in the window is equal to its frequency in t,
            # then increment the formed counter
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'
            while left <= right and formed == required:
                character = s[left]

                # Save the smallest window until now.
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # The character at the left pointer is going to be removed from the window, so decrement its count
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                left += 1

            # Keep expanding the window once we are done contracting.
            right += 1

        return "" if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]
    
    return min_window

# Test cases
def test_solution():
    min_window = solution()
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("abcabcbb", "abc") == "abc"
    assert min_window("abcabcbb", "abd") == ""
    assert min_window("aa", "aa") == "aa"
    assert min_window("babb", "baba") == ""
    assert min_window("cabwefgewcwaefgcf", "cae") == "cwae"
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()