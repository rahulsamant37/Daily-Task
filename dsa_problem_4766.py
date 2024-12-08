# DSA Problem generated on 2024-12-09

Here's a unique DSA problem in Python with solution:

**Problem Statement:**

Given a string `s` and an integer `k`, find the longest substring that contains at most `k` distinct characters. Return the length of this substring.

Example:
```
Input: s = "abcba", k = 2
Output: 3
Explanation: The longest substring with at most 2 distinct characters is "bcb".
```
**Solution Code:**
```python
def longest_substring_with_k_distinct(s: str, k: int) -> int:
    if k == 0:
        return 0

    char_freq = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        char_freq[s[right]] = char_freq.get(s[right], 0) + 1

        while len(char_freq) > k:
            char_freq[s[left]] -= 1
            if char_freq[s[left]] == 0:
                del char_freq[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string `s`. Here's a breakdown of the time complexity:

* We iterate through the input string `s` once, using a single loop that runs from 0 to n-1. This takes O(n) time.
* Inside the loop, we perform a constant amount of work: updating the `char_freq` dictionary and checking if the number of distinct characters exceeds `k`. This takes O(1) time.
* In the worst case, we may need to remove characters from the `char_freq` dictionary when the number of distinct characters exceeds `k`. This takes O(k) time, but since k is a constant, this is still O(1) time.
* We update the `max_len` variable only when we find a longer substring with at most `k` distinct characters. This takes O(1) time.

Since the loop runs n times, and each iteration takes constant time, the overall time complexity is O(n).

Note that the space complexity is O(k), since we store at most k distinct characters in the `char_freq` dictionary.