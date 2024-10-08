# DSA Problem generated on 2024-10-09

Here is a unique DSA problem in Python with solution:

**Problem Statement:**

You are given a string `s` containing only lowercase alphabets and a integer `k`. You need to find the longest substring of `s` that contains at most `k` distinct characters. If there are multiple such substrings, return any one of them.

**Example:**

Input: `s = "abcba", k = 2`
Output: `"bcb"`

Input: `s = "abcde", k = 3`
Output: `"abc"`

**Solution Code:**
```
def longest_substring_with_k_distinct(s, k):
    if k == 0 or not s:
        return ""

    char_count = {}
    left = 0
    max_len = 0
    max_substring = ""

    for right, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_substring = s[left:right+1]

    return max_substring
```
**Time Complexity Analysis:**

The time complexity of the above solution is O(n), where n is the length of the input string `s`. Here's a breakdown of the time complexity:

* The outer loop iterates over the input string `s` once, so it takes O(n) time.
* The inner while loop is executed at most n times, since we are incrementing the `left` pointer at most n times.
* The operations inside the inner while loop (updating `char_count` and incrementing `left`) take O(1) time.
* The rest of the operations (checking if `right - left + 1 > max_len` and updating `max_len` and `max_substring`) take O(1) time.

Since the outer loop is the dominant one, the overall time complexity is O(n).

**Space Complexity Analysis:**

The space complexity of the above solution is O(min(n, k)), where n is the length of the input string `s` and k is the integer input. Here's a breakdown of the space complexity:

* The `char_count` dictionary stores at most k distinct characters, so it takes O(k) space.
* The `max_substring` variable stores a substring of length at most n, so it takes O(n) space.
* The rest of the variables ( `left`, `right`, `max_len`) take O(1) space.

Since k is typically much smaller than n, the overall space complexity is O(min(n, k)).