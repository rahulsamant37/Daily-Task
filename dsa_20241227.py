# DSA Problem for 2024-12-27

Here's a novel DSA problem for 2024-12-27:

**Problem Statement:**

You are given a string `s` consisting of lowercase English letters and a positive integer `k`. You need to find the longest substring of `s` that contains at most `k` distinct characters.

**Example:**

Input: `s = "abcba", k = 2`
Output: `"bcb"` (The longest substring with at most 2 distinct characters is "bcb")

Input: `s = "aaaa", k = 1`
Output: `"aaaa"` (The longest substring with at most 1 distinct character is "aaaa")

**Optimal Solution:**
```python
def longest_substring_with_k_distinct_chars(s: str, k: int) -> str:
    if k == 0 or not s:
        return ""

    char_freq = {}
    max_len = 0
    max_substr = ""
    window_start = 0

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1

        while len(char_freq) > k:
            left_char = s[window_start]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            window_start += 1

        if window_end - window_start + 1 > max_len:
            max_len = window_end - window_start + 1
            max_substr = s[window_start:window_end + 1]

    return max_substr
```
**Time/Space Complexity Analysis:**

* Time complexity: O(n), where n is the length of the input string `s`. We iterate through the string once, and the inner while loop runs at most n times in the worst case.
* Space complexity: O(min(n, k)), where k is the maximum number of distinct characters allowed. We store the frequency of each character in the `char_freq` dictionary, which has at most k entries in the worst case. If k is smaller than n, the space complexity is O(k).

**Explanation:**

The solution uses a sliding window approach to find the longest substring with at most k distinct characters. We maintain a dictionary `char_freq` to store the frequency of each character in the current window. We iterate through the string, and for each character, we update the frequency dictionary and slide the window to the right.

When the number of distinct characters in the window exceeds k, we slide the window to the left by decrementing the frequency of the leftmost character and removing it from the dictionary if its frequency becomes zero. This process continues until we find the longest substring with at most k distinct characters.

Note that the solution has a linear time complexity because we iterate through the string only once, and the inner while loop runs at most n times in the worst case. The space complexity is bounded by the number of distinct characters in the string, which is at most k.