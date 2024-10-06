# DSA Problem generated on 2024-10-07

Here is a unique DSA problem in Python:

**Problem Statement:**

Given a string `s` and an integer `k`, find the longest substring of `s` that contains at most `k` distinct characters.

**Example:**

Input: `s = "abcba", k = 2`
Output: `"bcb"`

**Solution Code:**
```
def longest_substring_with_k_distinct_chars(s, k):
    if k == 0 or not s:
        return ""

    char_freq = {}
    max_len = 0
    max_substring = ""
    window_start = 0

    for window_end in range(len(s)):
        right_char = s[window_end]
        char_freq[right_char] = char_freq.get(right_char, 0) + 1

        while len(char_freq) > k:
            left_char = s[window_start]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            window_start += 1

        if window_end - window_start + 1 > max_len:
            max_len = window_end - window_start + 1
            max_substring = s[window_start:window_end + 1]

    return max_substring
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string `s`. Here's a breakdown of the time complexity:

* The outer loop iterates `n` times, where `n` is the length of the input string.
* The inner while loop iterates at most `k` times, where `k` is the number of distinct characters allowed in the substring.
* The `char_freq` dictionary operations (insertion, deletion, and lookup) take O(1) time on average.
* The `window_start` and `window_end` variables are updated in O(1) time.

Since the inner while loop iterates at most `k` times, and `k` is a constant, the overall time complexity is O(n).

This solution uses a sliding window approach to keep track of the longest substring with at most `k` distinct characters. The `char_freq` dictionary is used to keep track of the frequency of each character in the current window. When the number of distinct characters exceeds `k`, the window is slid to the right by incrementing `window_start` until the number of distinct characters is at most `k`. The maximum length and corresponding substring are updated accordingly.