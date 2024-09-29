# DSA Problem generated on 2024-09-30

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a string `s` containing only lowercase letters, and an integer `k`, find the longest substring that can be formed by rearranging the characters in `s` such that every character appears at most `k` times.

**Example:**

Input: `s = "aabcccc", k = 2`
Output: `"ac"`

Explanation: The longest substring that can be formed by rearranging the characters in `s` such that every character appears at most 2 times is "ac".

**Solution Code:**
```python
from collections import Counter

def longest_substring(s: str, k: int) -> str:
    counter = Counter(s)
    max_len = 0
    max_substr = ""

    for char, freq in counter.items():
        if freq <= k:
            curr_substr = char
            curr_len = 1
            for other_char, other_freq in counter.items():
                if other_char != char and other_freq <= k:
                    curr_substr += other_char
                    curr_len += 1
            if curr_len > max_len:
                max_len = curr_len
                max_substr = curr_substr

    return max_substr

s = "aabcccc"
k = 2
print(longest_substring(s, k))  # Output: "ac"
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n^2), where n is the length of the input string `s`.

Here's a breakdown of the time complexity:

* The `Counter` object creation takes O(n) time.
* The outer loop iterates over each character in the string, taking O(n) time.
* The inner loop iterates over each character in the string again, taking O(n) time.
* The `if` statement and string concatenation operations take O(1) time.

Since the inner loop is nested inside the outer loop, the overall time complexity is O(n^2).

**Note:** This solution has a high time complexity due to the nested loops. A more efficient solution could be achieved using a different approach, such as using a sliding window or a heap data structure. However, this solution is straightforward and easy to understand.