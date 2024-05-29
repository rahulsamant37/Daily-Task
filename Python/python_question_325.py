# Python Question: Find the Longest Substring with K Distinct Characters
'''
Given a string `s` and an integer `k`, find the length of the longest substring of `s` that contains at most `k` distinct characters.

Example:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" which its length is 3.

Input: s = "aaabccbbbc", k = 3
Output: 7
Explanation: The substring is "aaabccb" which its length is 7.
'''

# Solution
def longest_substring_with_k_distinct_characters(s, k):
    """
    Finds the length of the longest substring of s with at most k distinct characters.

    Args:
        s: The input string.
        k: The maximum number of distinct characters allowed in the substring.

    Returns:
        The length of the longest substring with at most k distinct characters.
    """

    if not s or k == 0:
        return 0

    # Use a sliding window approach with a frequency map.
    window_start = 0
    max_length = 0
    char_frequency = {}  # Stores the frequency of each character in the current window.

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # Shrink the window until the number of distinct characters is at most k.
        while len(char_frequency) > k:
            left_char = s[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1

        # Update the maximum length.
        max_length = max(max_length, window_end - window_start + 1)

    return max_length

# Test cases
def test_solution():
    assert longest_substring_with_k_distinct_characters("eceba", 2) == 3
    assert longest_substring_with_k_distinct_characters("aaabccbbbc", 3) == 7
    assert longest_substring_with_k_distinct_characters("abaccc", 2) == 4
    assert longest_substring_with_k_distinct_characters("a", 1) == 1
    assert longest_substring_with_k_distinct_characters("a", 2) == 1
    assert longest_substring_with_k_distinct_characters("", 2) == 0
    assert longest_substring_with_k_distinct_characters("aabbcc", 1) == 2
    assert longest_substring_with_k_distinct_characters("aabbcc", 2) == 6
    assert longest_substring_with_k_distinct_characters("aabbcc", 3) == 6
    assert longest_substring_with_k_distinct_characters("aabbcc", 4) == 6
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()