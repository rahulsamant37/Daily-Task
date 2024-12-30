# DSA Problem for 2024-12-31

Here is a novel DSA problem with a Python solution for 2024-12-31:

**Problem Statement:**

"Calendar Chaos"

You are a calendar designer tasked with creating a custom calendar for a futuristic society. The society has a unique way of celebrating special events, which are denoted by a sequence of integers representing the days of the month when the event occurs. However, due to a miscommunication, the event sequences have been mixed up, and you need to restore the original order.

Given a list of event sequences, write a function to restore the original order by finding the longest contiguous subsequence that appears in all sequences. If multiple such subsequences exist, return the one that appears first in the original sequence.

**Example:**

Input: `[[3, 1, 4, 2, 5], [1, 4, 2, 3], [4, 2, 1, 3, 5]]`

Output: `[1, 4, 2]`

**Optimal Solution:**
```python
def restore_calendar(events):
    n = len(events)
    max_len = 0
    result = []

    for i in range(n):
        for j in range(i + 1, n):
            len_ij = len_LONGEST_CONTIGUOUS_SUBSEQ(events[i], events[j])
            if len_ij > max_len:
                max_len = len_ij
                result = LONGEST_CONTIGUOUS_SUBSEQ(events[i], events[j])

    return result

def LONGEST_CONTIGUOUS_SUBSEQ(seq1, seq2):
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    longest = []

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > len(longest):
                    longest = seq1[i - dp[i][j]:i]
            else:
                dp[i][j] = 0

    return longest

def len_LONGEST_CONTIGUOUS_SUBSEQ(seq1, seq2):
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0

    return max(max(row) for row in dp)
```
**Time/Space Complexity Analysis:**

* The `restore_calendar` function has a time complexity of O(n^2 \* m^2), where n is the number of event sequences and m is the maximum length of an event sequence. This is because it iterates over all pairs of sequences and finds the longest contiguous subsequence using dynamic programming.
* The `LONGEST_CONTIGUOUS_SUBSEQ` function has a time complexity of O(m^2), where m is the maximum length of an event sequence. This is because it uses dynamic programming to find the longest contiguous subsequence.
* The `len_LONGEST_CONTIGUOUS_SUBSEQ` function has a time complexity of O(m^2), where m is the maximum length of an event sequence. This is because it uses dynamic programming to find the length of the longest contiguous subsequence.
* The space complexity is O(m^2) for the dynamic programming tables.

Note that the time complexity can be improved by using a more efficient algorithm, such as the suffix tree algorithm, to find the longest contiguous subsequence. However, the provided solution is a straightforward implementation using dynamic programming.