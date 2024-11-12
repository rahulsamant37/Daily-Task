# DSA Problem generated on 2024-11-13

Here is a unique DSA problem in Python:

**Problem Statement:**

Given a string `s` and an integer `k`, find the longest substring of `s` that contains at most `k` distinct characters.

**Example:**

Input: `s = "abcba", k = 2`
Output: `"bcb"` (longest substring with at most 2 distinct characters)

**Solution Code:**
```
def longest_substring(s: str, k: int) -> str:
    if k == 0:
        return ""

    char_count = {}
    max_len = 0
    max_substr = ""

    left = 0
    for right, c in enumerate(s):
        char_count[c] = char_count.get(c, 0) + 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_substr = s[left:right + 1]

    return max_substr
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string `s`. Here's why:

* We iterate over the string `s` once using a sliding window approach, which takes O(n) time.
* Inside the loop, we update the `char_count` dictionary, which takes constant time.
* We also check if the number of distinct characters exceeds `k` and update the `left` pointer accordingly, which takes constant time.
* Finally, we update the `max_len` and `max_substr` variables, which takes constant time.

Since we only iterate over the input string once, the overall time complexity is O(n).

Note that the space complexity is O(min(k, n)), since we store at most `k` characters in the `char_count` dictionary, and in the worst case, we store all characters in the dictionary.