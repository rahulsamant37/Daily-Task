# DSA Problem for 2024-12-19

Here is a novel DSA problem with a Python solution for 2024-12-19:

**Problem Statement:**

**"Maximizing Ski Resort Profit"**

A popular ski resort has `n` ski trails, each with a unique difficulty level and a corresponding ticket price. The resort wants to maximize its profit by assigning a subset of trails to a special "VIP" package, which attracts high-paying customers. The VIP package can only include trails with difficulty levels that are within a certain range (inclusive) of each other.

Given an array `trails` of length `n`, where `trails[i] = [difficulty_level_i, ticket_price_i]`, and an integer `range`, find the maximum profit the ski resort can generate by assigning trails to the VIP package.

**Example:**

`trails = [[3, 10], [1, 5], [4, 15], [2, 8], [5, 20]]`
`range = 2`

**Output:** `45` (Assign trails with difficulty levels 3, 4, and 5 to the VIP package, which generates a total profit of 10 + 15 + 20 = 45)

**Optimal Solution:**
```python
def max_ski_resort_profit(trails, range):
    trails.sort(key=lambda x: x[0])  # Sort trails by difficulty level

    n = len(trails)
    dp = [0] * (n + 1)  # Dynamic programming array to store maximum profit

    for i in range(1, n + 1):
        max_profit = 0
        for j in range(i):
            if trails[i - 1][0] - trails[j][0] <= range:
                max_profit = max(max_profit, dp[j] + trails[i - 1][1])
        dp[i] = max_profit

    return dp[-1]
```
**Time Complexity Analysis:**

The time complexity of the solution is O(n^2), where n is the number of trails. The outer loop iterates n times, and the inner loop iterates up to n times in the worst case. The sorting step takes O(n log n) time, but this is dominated by the quadratic time complexity of the dynamic programming step.

**Space Complexity Analysis:**

The space complexity of the solution is O(n), where n is the number of trails. We need to store the dynamic programming array `dp` of size n + 1.

This problem involves dynamic programming, sorting, and iteration, making it a challenging and interesting DSA problem for 2024-12-19.