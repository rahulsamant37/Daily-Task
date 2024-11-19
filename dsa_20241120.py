# DSA Problem for 2024-11-20

Here is a novel DSA problem with a Python solution for 2024-11-20:

**Problem Statement:**

Given a string `s` and an integer `k`, find the longest substring of `s` that contains at most `k` unique characters. If there are multiple substrings with the same maximum length, return the one with the lexicographically smallest characters.

**Example:**

Input: `s = "abcba", k = 2`
Output: `"bcb"`

Explanation: The longest substring with at most 2 unique characters is "bcb", which has a length of 3.

**Optimal Solution:**
```
def longest_substring_with_k_unique_chars(s, k):
    if k == 0 or not s:
        return ""

    char_count = {}
    max_length = 0
    max_substring = ""
    window_start = 0

    for window_end in range(len(s)):
        right_char = s[window_end]
        char_count[right_char] = char_count.get(right_char, 0) + 1

        while len(char_count) > k:
            left_char = s[window_start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            window_start += 1

        if window_end - window_start + 1 > max_length:
            max_length = window_end - window_start + 1
            max_substring = s[window_start:window_end + 1]

    return max_substring
```
**Time Complexity Analysis:**

The time complexity of the above solution is O(n), where n is the length of the input string `s`. This is because we are traversing the string once from left to right.

The inner while loop runs in O(k) time, where k is the number of unique characters in the sliding window. However, since k is a constant, the overall time complexity remains O(n).

**Space Complexity Analysis:**

The space complexity of the above solution is O(k), where k is the number of unique characters in the sliding window. This is because we are storing the character counts in a dictionary `char_count`, which has a maximum size of k.

Note that the space complexity is independent of the input size n, since we are only storing a fixed number of characters in the dictionary.