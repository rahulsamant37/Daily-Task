# Python Question: Find the Minimum Window Substring
'''
Given two strings s and t, find the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

The characters in t can appear multiple times, and the window in s must contain all these characters with their respective frequencies.

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
    def min_window(s, t):
        """
        Finds the minimum window substring in s that contains all characters in t.

        Args:
            s: The string to search in.
            t: The string containing the characters to find.

        Returns:
            The minimum window substring, or an empty string if no such window exists.
        """

        if not s or not t:
            return ""

        # Create a dictionary to store the frequency of characters in t
        t_freq = {}
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        # Initialize window pointers and required character count
        window_start = 0
        window_end = 0
        required_chars = len(t_freq)
        formed_chars = 0
        window_freq = {}

        # Initialize variables to track the minimum window
        min_window_length = float('inf')
        min_window_start = 0

        while window_end < len(s):
            char = s[window_end]
            window_freq[char] = window_freq.get(char, 0) + 1

            # Check if the current character is in t and its frequency matches
            if char in t_freq and window_freq[char] == t_freq[char]:
                formed_chars += 1

            # Shrink the window while all required characters are present
            while formed_chars == required_chars:
                # Update the minimum window if necessary
                window_length = window_end - window_start + 1
                if window_length < min_window_length:
                    min_window_length = window_length
                    min_window_start = window_start

                # Remove the leftmost character from the window
                left_char = s[window_start]
                window_freq[left_char] -= 1

                # Check if the removed character was a required character
                if left_char in t_freq and window_freq[left_char] < t_freq[left_char]:
                    formed_chars -= 1

                window_start += 1

            window_end += 1

        # Return the minimum window or an empty string if not found
        if min_window_length == float('inf'):
            return ""
        else:
            return s[min_window_start:min_window_start + min_window_length]

    return min_window

# Test cases
def test_solution():
    min_window = solution()

    # Test case 1
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    expected1 = "BANC"
    assert min_window(s1, t1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {min_window(s1, t1)}"

    # Test case 2
    s2 = "a"
    t2 = "a"
    expected2 = "a"
    assert min_window(s2, t2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {min_window(s2, t2)}"

    # Test case 3
    s3 = "a"
    t3 = "aa"
    expected3 = ""
    assert min_window(s3, t3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {min_window(s3, t3)}"

    # Test case 4
    s4 = "aa"
    t4 = "aa"
    expected4 = "aa"
    assert min_window(s4, t4) == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {min_window(s4, t4)}"

    # Test case 5
    s5 = "cabwefgewcwaefgcf"
    t5 = "cae"
    expected5 = "cwae"
    assert min_window(s5, t5) == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {min_window(s5, t5)}"

    # Test case 6
    s6 = "abcabcbb"
    t6 = "abc"
    expected6 = "abc"
    assert min_window(s6, t6) == "abc", f"Test Case 6 Failed: Expected abc, Got {min_window(s6,t6)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()