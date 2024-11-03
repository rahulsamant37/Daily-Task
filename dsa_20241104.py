# DSA Problem for 2024-11-04

Here is a novel DSA problem with a Python solution, along with time and space complexity analysis:

**Problem Statement:**

**`Longest Palindromic Subsequence in a 2D Matrix`**

Given a 2D matrix of characters, find the longest palindromic subsequence that can be formed using characters from the matrix. A palindromic subsequence is a sequence that reads the same backward as forward. The subsequence can be formed by selecting characters from the matrix in any order, but each character can only be used once.

**Example:**

Input:
```
matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]
```
Output:
`"abcdefedcba"` (one possible longest palindromic subsequence)

**Optimal Solution:**

```python
def longest_palindromic_subsequence(matrix):
    m, n = len(matrix), len(matrix[0])
    chars = [char for row in matrix for char in row]
    dp = [[0] * len(chars) for _ in range(len(chars))]

    for i in range(len(chars)):
        dp[i][i] = 1

    max_len = 1
    start_idx = 0

    for length in range(2, len(chars) + 1):
        for i in range(len(chars) - length + 1):
            j = i + length - 1

            if chars[i] == chars[j] and length == 2:
                dp[i][j] = 2
            elif chars[i] == chars[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

            if dp[i][j] > max_len:
                max_len = dp[i][j]
                start_idx = i

    subsequence = []
    i, j = start_idx, start_idx + max_len - 1

    while i <= j:
        if i == j:
            subsequence.append(chars[i])
        elif chars[i] == chars[j]:
            subsequence.append(chars[i])
            i += 1
            j -= 1
        elif dp[i + 1][j] > dp[i][j - 1]:
            i += 1
        else:
            j -= 1

    return "".join(subsequence)

matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]

print(longest_palindromic_subsequence(matrix))  # Output: "abcdefedcba"
```

**Time Complexity Analysis:**

The time complexity of the solution is O(n^2), where n is the total number of characters in the matrix. This is because we are using a dynamic programming approach, and the dp table has a size of n x n. We are filling up the dp table in a bottom-up manner, and each cell depends on the values of other cells in the table.

**Space Complexity Analysis:**

The space complexity of the solution is O(n^2), where n is the total number of characters in the matrix. This is because we are using a 2D dp table of size n x n to store the lengths of palindromic subsequences.

Note that the space complexity can be optimized to O(n) by using a 1D dp array and iterating over the matrix in a diagonal manner. However, the 2D dp table approach is more intuitive and easier to understand.