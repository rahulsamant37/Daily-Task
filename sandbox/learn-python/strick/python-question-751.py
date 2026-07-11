# Python Question: Minimum Window Substring
'''
Given two strings s and t, find the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note:

If there is such window, you are guaranteed that there will always be only one unique minimum window in s.

Example:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
'''

# Solution
def minWindow(s, t):
    """
    Finds the minimum window substring in s that contains all characters in t.

    Args:
        s: The string to search in.
        t: The string containing the characters to find.

    Returns:
        The minimum window substring in s that contains all characters in t.
        Returns an empty string "" if no such window exists.
    """

    if not s or not t:
        return ""

    # Create a dictionary to store the frequency of characters in t
    t_freq = {}
    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1

    # Create variables to track the window boundaries and the number of characters matched
    window_start = 0
    window_end = 0
    matched = 0

    # Create a dictionary to store the frequency of characters in the current window
    window_freq = {}

    # Create variables to store the minimum window substring and its length
    min_len = float('inf')
    min_start = 0

    # Iterate through the string s
    while window_end < len(s):
        right_char = s[window_end]

        # Add the right character to the window frequency
        window_freq[right_char] = window_freq.get(right_char, 0) + 1

        # If the right character is in t and its frequency in the window is less than or equal to its frequency in t, increment the matched count
        if right_char in t_freq and window_freq[right_char] <= t_freq[right_char]:
            matched += 1

        # While all characters in t are matched, shrink the window from the left
        while matched == len(t):
            # If the current window is smaller than the minimum window, update the minimum window
            if window_end - window_start + 1 < min_len:
                min_len = window_end - window_start + 1
                min_start = window_start

            # Remove the leftmost character from the window
            left_char = s[window_start]
            window_freq[left_char] -= 1

            # If the leftmost character is in t and its frequency in the window is less than its frequency in t, decrement the matched count
            if left_char in t_freq and window_freq[left_char] < t_freq[left_char]:
                matched -= 1

            # Move the window start to the right
            window_start += 1

        # Move the window end to the right
        window_end += 1

    # If no window was found, return an empty string
    if min_len == float('inf'):
        return ""

    # Return the minimum window substring
    return s[min_start:min_start + min_len]

# Test cases
def test_solution():
    assert minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert minWindow("a", "a") == "a"
    assert minWindow("a", "aa") == ""
    assert minWindow("abc", "ac") == "abc"
    assert minWindow("ab", "a") == "a"
    assert minWindow("cabwefgewcwaefgcf", "cae") == "cwae"
    assert minWindow("aa", "aa") == "aa"
    assert minWindow("ADOBECODEBANC", "ABCC") == "CODEBANC"
    assert minWindow("", "ABC") == ""
    assert minWindow("ABC", "") == ""
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()