# DSA Problem generated on 2024-12-13

Here's a unique DSA problem with a solution in Python:

**Problem Statement:**

Given a string `s` containing only alphabets, find the maximum length of a substring that contains at most `k` distinct characters. If there are multiple such substrings, return the maximum length.

Example:
```
s = "abcba", k = 2
Output: 3 ( longest substring "bca" has 2 distinct characters)

s = "abcabcabc", k = 3
Output: 6 ( longest substring "abcabc" has 3 distinct characters)
```
**Solution Code:**
```python
def max_length_substring(s, k):
    char_freq = {}  # dictionary to store character frequencies
    max_len = 0  # maximum length of substring
    left = 0  # left pointer of the sliding window
    distinct_chars = 0  # number of distinct characters in the window

    for right in range(len(s)):
        char_freq[s[right]] = char_freq.get(s[right], 0) + 1
        if char_freq[s[right]] == 1:
            distinct_chars += 1

        while distinct_chars > k:
            char_freq[s[left]] -= 1
            if char_freq[s[left]] == 0:
                distinct_chars -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string `s`. Here's the breakdown:

* The outer loop iterates over each character in the string, which takes O(n) time.
* Inside the loop, we maintain a dictionary `char_freq` to store character frequencies. The dictionary operations (insertion, lookup, and deletion) take O(1) time on average.
* The inner while loop runs at most `k` times, since we remove characters from the window until we have at most `k` distinct characters. The time complexity of this loop is O(k).
* Since k is a constant, the overall time complexity is O(n).

**Space Complexity Analysis:**

The space complexity of this solution is O(min(n, k)), where n is the length of the input string `s`. Here's the breakdown:

* We use a dictionary `char_freq` to store character frequencies, which takes O(min(n, k)) space, since there are at most `k` distinct characters in the window.
* We use a few extra variables to store the maximum length and the left pointer of the window, which takes O(1) space.

Overall, the solution has a time complexity of O(n) and a space complexity of O(min(n, k)).