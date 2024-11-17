# DSA Problem generated on 2024-11-18

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a string `s` and an integer `k`, find the longest substring that contains at most `k` distinct characters. Return the length of this substring.

**Example:**

Input: `s = "abcba", k = 2`
Output: `3` (The longest substring with at most 2 distinct characters is "bcb" or "cba")

**Solution Code:**
```python
def longest_substring_with_k_distinct_chars(s, k):
    char_count = {}
    max_length = 0
    window_start = 0

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in char_count:
            char_count[right_char] = 0
        char_count[right_char] += 1

        while len(char_count) > k:
            left_char = s[window_start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string `s`. Here's why:

* We iterate through the string once, using a sliding window approach. This takes O(n) time.
* Within the loop, we perform constant-time operations (hash table lookups and updates) to maintain the `char_count` dictionary.
* The `while` loop inside the main loop runs at most `k` times, since we remove one character from the window for each iteration. This adds an additional O(k) time complexity, but since `k` is a constant, this is still O(n) overall.

Therefore, the overall time complexity is O(n).

**Space Complexity Analysis:**

The space complexity of this solution is O(k), where `k` is the maximum number of distinct characters in the input string. We use a hash table `char_count` to store the count of each character in the current window, which takes O(k) space.