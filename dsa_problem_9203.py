# DSA Problem generated on 2024-10-01

Here is a unique DSA problem in Python with solution:

**Problem Statement:**

Given a string `s` and an integer `k`, find the longest substring of `s` that contains at most `k` distinct characters. If there are multiple such substrings, return the one with the smallest starting index.

**Example:**

Input: `s = "abcbaabc", k = 2`
Output: `"bca"`

**Solution Code:**
```python
def longest_substring_with_k_distinct(s, k):
    if k == 0 or not s:
        return ""

    char_freq = {}
    start = 0
    max_len = 0
    max_substring = ""

    for end, char in enumerate(s):
        char_freq[char] = char_freq.get(char, 0) + 1

        while len(char_freq) > k:
            char_freq[s[start]] -= 1
            if char_freq[s[start]] == 0:
                del char_freq[s[start]]
            start += 1

        if end - start + 1 > max_len:
            max_len = end - start + 1
            max_substring = s[start:end+1]

    return max_substring
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string `s`. Here's why:

* We iterate through the input string `s` once using the `enumerate` function, which takes O(n) time.
* Inside the loop, we perform the following operations:
	+ We update the `char_freq` dictionary, which takes O(1) time.
	+ We check if the number of distinct characters exceeds `k`, and if so, we remove characters from the start of the window until the number of distinct characters is less than or equal to `k`. This takes O(min(k, n)) time, since we only need to remove at most `k` characters from the window.
* We keep track of the maximum length substring and its starting index, which takes O(1) time.

Since the loop iterates `n` times, and each iteration takes O(min(k, n)) time, the overall time complexity is O(n).

Note that the space complexity is O(k), since we store at most `k` distinct characters in the `char_freq` dictionary.