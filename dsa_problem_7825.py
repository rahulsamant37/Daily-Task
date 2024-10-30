# DSA Problem generated on 2024-10-31

Here is a unique DSA problem in Python:

**Problem Statement:**

Given a string `s` and an integer `k`, find the maximum number of substrings that can be formed from `s` such that each substring has a length of `k` and contains at least one unique character that is not present in any other substring.

**Example:**

Input: `s = "abcdeabcde", k = 3`
Output: `4`

Explanation: The maximum number of substrings that can be formed are `["abc", "de", "abc", "de"]`.

**Solution Code:**
```python
def max_unique_substrings(s, k):
    substring_set = set()
    max_substrings = 0
    char_count = {}
    window_start = 0

    for window_end in range(len(s)):
        right_char = s[window_end]
        char_count[right_char] = char_count.get(right_char, 0) + 1

        if window_end >= k - 1:
            left_char = s[window_start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]

            substring = s[window_start:window_end + 1]
            if all(c not in substring_set for c in set(substring)):
                substring_set.add(substring)
                max_substrings += 1

            window_start += 1

    return max_substrings
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string `s`. Here's a breakdown of the time complexity:

* The outer loop iterates over the input string `s` once, which takes O(n) time.
* The inner loop iterates over a window of size `k` at most, which takes O(k) time.
* The `set` operations (add, remove, and check membership) take O(1) time on average.
* The `char_count` dictionary operations (increment, decrement, and check existence) take O(1) time on average.

Since `k` is a constant, the overall time complexity is O(n). The space complexity is O(n) as well, as we store at most `n` substrings in the `substring_set` set and at most `n` characters in the `char_count` dictionary.