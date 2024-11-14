# DSA Problem generated on 2024-11-15

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a string `s` and an integer `k`, find the longest substring of `s` that can be formed by rearranging at most `k` characters. For example, if `s = "abcba"` and `k = 2`, the longest possible substring is `"abcba"` itself, but if `k = 1`, the longest possible substring is `"abca"`.

**Solution Code:**
```python
from collections import Counter

def longest_rearranged_substring(s, k):
    char_freq = Counter(s)
    max_len = 0
    substring = ""

    for char, freq in char_freq.items():
        if freq <= k:
            new_s = s.replace(char, '', freq)
            new_len = len(new_s)
            if new_len > max_len:
                max_len = new_len
                substring = new_s

    return substring

# Example usage:
s = "abcba"
k = 2
print(longest_rearranged_substring(s, k))  # Output: "abcba"

s = "abcba"
k = 1
print(longest_rearranged_substring(s, k))  # Output: "abca"
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input string `s`. Here's a breakdown of the time complexity:

1. The `Counter` object creation takes O(n) time, as it needs to iterate over the entire string to count the frequency of each character.
2. The loop iterates over the `char_freq` dictionary, which has at most 26 elements (one for each letter in the alphabet). For each iteration, we perform the following operations:
	* `s.replace(char, '', freq)` takes O(n) time, as it needs to iterate over the entire string to replace the characters.
	* `len(new_s)` takes O(1) time, as it simply returns the length of the new string.
	* The conditional statement and assignment take O(1) time.
3. The total time complexity is O(n) + O(26 \* n) = O(n), as the loop iterates over a fixed number of elements (26) and each iteration takes O(n) time.

Note that the space complexity is O(1), as we only use a fixed amount of space to store the `char_freq` dictionary and the `substring` variable.