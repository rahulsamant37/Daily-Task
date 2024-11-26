# DSA Problem for 2024-11-27

Here is a novel DSA problem with a Python solution for 2024-11-27:

**Problem Statement:**

**Maximum Profit from Stock Transactions with Limited Transactions**

You are a stock trader who wants to maximize your profit from buying and selling stocks. You are given an array of integers `prices` representing the price of a stock on each day. You can perform at most `k` transactions (buy and sell operations). Find the maximum profit you can achieve.

**Example:**

`prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`
`k = 2`

**Output:** `150`

**Explanation:** You can perform two transactions: Buy on day 1 (price 10), sell on day 5 (price 50), and buy on day 7 (price 70), sell on day 10 (price 100). The total profit is 50 - 10 + 100 - 70 = 150.

**Optimal Solution:**
```python
def max_profit(prices, k):
    n = len(prices)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            max_profit_so_far = max(dp[i - 1][j - 1] - prices[i - 2] + prices[i - 1] if i > 1 else 0, dp[i - 1][j])
            dp[i][j] = max=max_profit_so_far, dp[i - 1][j] + prices[i - 1] - prices[i - 2] if i > 1 else 0)

    return dp[n][k]
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n \* k), where n is the length of the `prices` array and k is the number of transactions allowed. The reason is that we have a nested loop structure with two iterations: the outer loop iterates over the days (n times), and the inner loop iterates over the number of transactions (k times).

**Space Complexity Analysis:**

The space complexity of this solution is O(n \* k), where n is the length of the `prices` array and k is the number of transactions allowed. We use a 2D array `dp` of size (n + 1) x (k + 1) to store the maximum profit for each day and each possible number of transactions.

**Note:** This problem is a variation of the classic "Best Time to Buy and Sell Stock" problem, with an added twist of limiting the number of transactions. The solution uses dynamic programming to optimize the profit by considering all possible transactions and selecting the maximum profit achievable.