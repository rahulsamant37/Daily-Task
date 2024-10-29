# DSA Problem generated on 2024-10-30

Here's a unique DSA problem in Python:

**Problem Statement:**

Given a string `s` and an integer `k`, find the maximum number of unique substrings of `s` that can be formed by removing at most `k` characters from `s`. A unique substring is a substring that has not been seen before.

**Example:**

Input: `s = "abcabc", k = 2`
Output: `5`

Explanation: The maximum number of unique substrings that can be formed by removing at most 2 characters from `s` is 5. The unique substrings are: "a", "ab", "abc", "b", "bc".

**Solution Code:**
```python
def max_unique_substrings(s, k):
    n = len(s)
    dp = [[set() for _ in range(k + 1)] for _ in range(n + 1)]
    dp[0][0] = set()

    for i in range(1, n + 1):
        for j in range(min(i, k + 1)):
            for substr_len in range(1, i + 1):
                substr = s[i - substr_len:i]
                if j >= substr_len:
                    dp[i][j] |= dp[i - substr_len][j - substr_len]
                dp[i][j].add(substr)

    return len(dp[n][k])
```
**Time Complexity Analysis:**

The time complexity of the solution is O(n^2 \* k), where n is the length of the input string `s`.

Here's a breakdown of the time complexity:

* The outer loop iterates `n` times.
* The middle loop iterates at most `k` times.
* The inner loop iterates at most `n` times (for each `substr_len`).
* The set operations (union and addition) take O(1) time.

Therefore, the overall time complexity is O(n^2 \* k).

Note: The space complexity is O(n \* k) due to the DP table, but it's not a concern in this case since we're more concerned about the time complexity.