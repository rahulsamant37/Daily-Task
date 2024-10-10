# Python Question: Find the Minimum Window Substring
'''
Given two strings s and t, find the minimum window in s which will contain all the characters in t in complexity O(n). If there is no such window in s that covers all characters in t, return the empty string "".

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Explanation:
Minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
'''

# Solution
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

    # 1. Create a dictionary to store the frequency of characters in t.
    dict_t = {}
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1

    # 2. Initialize variables for the sliding window.
    required = len(dict_t)  # Number of unique characters in t
    formed = 0  # Number of unique characters in t that are present in the current window with the required frequency
    window_counts = {}  # Dictionary to store the frequency of characters in the current window
    left = 0
    right = 0
    min_length = float('inf')
    min_start = 0

    # 3. Iterate through the string s using the right pointer.
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        # If the character is in t and its frequency in the window matches its frequency in t,
        # increment the formed counter.
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1

        # 4. While the window contains all characters in t, try to shrink the window from the left.
        while left <= right and formed == required:
            char = s[left]

            # Update the minimum window length and start index if the current window is smaller.
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_start = left

            # Decrement the frequency of the character at the left pointer in the window counts.
            window_counts[char] -= 1

            # If the character is in t and its frequency in the window is now less than its frequency in t,
            # decrement the formed counter.
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1

            # Move the left pointer to shrink the window.
            left += 1

        # Move the right pointer to expand the window.
        right += 1

    # 5. Return the minimum window substring, or an empty string if no such window exists.
    if min_length == float('inf'):
        return ""
    else:
        return s[min_start:min_start + min_length]


# Test cases
def test_min_window():
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("ADOBECODEBANC", "X") == ""
    assert min_window("ABC", "CBA") == "ABC"
    assert min_window("AAAA", "AA") == "AA"
    assert min_window("cabwefgewcwaefgcf", "cae") == "cwae"
    assert min_window("bdab", "ab") == "ab"
    assert min_window("abcabcbb", "abc") == "abc"
    assert min_window("ab", "ba") == "ab"


if __name__ == "__main__":
    test_min_window()