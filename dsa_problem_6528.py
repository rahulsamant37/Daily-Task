# DSA Problem generated on 2024-11-12

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a string `s` containing only lowercase English letters, design an algorithm to find the longest substring that contains at most `k` distinct characters. Return the length of the longest substring.

**Example:**

Input: `s = "abcba", k = 2`
Output: `3`
Explanation: The longest substring with at most 2 distinct characters is "bcb" or "cba" with a length of 3.

**Solution Code:**
```python
def longest_substring_with_k_distinct(s: str, k: int) -> int:
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

The time complexity of this solution is O(n), where n is the length of the input string `s`. Here's a breakdown of the complexity:

* The outer loop iterates over the entire string, which takes O(n) time.
* The inner while loop, which is responsible for maintaining the sliding window, takes O(k) time in the worst case, where k is the number of distinct characters.
* Since k is a constant, the overall time complexity is O(n).

The space complexity is O(k) because we use a dictionary to store the frequency of each character, which can store at most k distinct characters.

Note that this problem is a variation of the classic sliding window problem, and the solution uses a similar approach to the "Longest Substring with At Most K Repeating Characters" problem. However, this problem has a twist, as we need to find the longest substring with at most k distinct characters, rather than k repeating characters.