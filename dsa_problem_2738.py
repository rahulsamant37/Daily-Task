# DSA Problem generated on 2024-12-18

Here is a unique DSA problem in Python:

**Problem Statement:**

Given a string `s` and an integer `k`, find the longest substring that contains at most `k` distinct characters. Return the length of the longest such substring.

**Example:**

```
Input: s = "abcba", k = 2
Output: 3
Explanation: The longest substring with at most 2 distinct characters is "bcb".
```

**Solution Code:**
```python
def longest_substring_with_k_distinct(s, k):
    if k == 0 or not s:
        return 0

    char_count = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string `s`. Here's a breakdown of the analysis:

* The outer loop iterates over each character in the string, which takes O(n) time.
* The inner while loop iterates at most k times, since we only need to remove characters from the window until we have at most k distinct characters. This takes O(k) time.
* The dictionary lookups and insertions take O(1) time on average, since we use a hash table to store the character counts.
* The space complexity is O(k), since we store at most k characters in the dictionary.

Overall, the time complexity is O(n) because the outer loop dominates the inner loop, and the space complexity is O(k) because we only store a small number of characters in the dictionary.

I hope this problem and solution are helpful! Let me know if you have any questions.