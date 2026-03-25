# DSA Problem 246

'''
Problem Statement:
You are given a list of integers representing the daily prices of a stock over a period. You are also given a list of queries, where each query is a pair of indices [i, j] (0-indexed) indicating a subsequence of the stock prices from day i to day j, inclusive. For each query, calculate the maximum profit that can be achieved by buying and selling the stock once within the given subsequence. If no profit can be made, return 0 for that query.

Constraints:
- 1 <= len(prices) <= 10^5
- 1 <= len(queries) <= 10^5
- 0 <= prices[i] <= 10^9
- 0 <= queries[i][0] <= queries[i][1] < len(prices)

Example:
Input:
prices = [7,1,5,3,6,4]
queries = [[0,3],[2,5],[0,5]]
Output:
[4,3,5]
Explanation:
For the first query [0,3], the maximum profit is 4 (buy on day 1 and sell on day 2).
For the second query [2,5], the maximum profit is 3 (buy on day 3 and sell on day 4).
For the third query [0,5], the maximum profit is 5 (buy on day 1 and sell on day 4).
'''

Solution:
```python
def maxProfitQueries(prices, queries):
    """
    Calculates the maximum profit for each query in O(n + q) time complexity,
    where n is the length of the prices list and q is the number of queries.
    """
    n = len(prices)
    minSoFar = [0] * n  # Minimum price so far from the start
    maxSoFar = [0] * n  # Maximum price so far from the end

    minSoFar[0] = prices[0]
    for i in range(1, n):
        minSoFar[i] = min(minSoFar[i-1], prices[i])

    maxSoFar[-1] = prices[-1]
    for i in range(n-2, -1, -1):
        maxSoFar[i] = max(maxSoFar[i+1], prices[i])

    results = []
    for start, end in queries:
        # If the minimum price before or on 'start' day is less than the maximum price on or after 'end' day,
        # then the profit is the difference; otherwise, no profit can be made.
        if minSoFar[end] < maxSoFar[start]:
            results.append(maxSoFar[start] - minSoFar[end])
        else:
            results.append(0)
    return results

# Example usage
prices = [7,1,5,3,6,4]
queries = [[0,3],[2,5],[0,5]]
print(maxProfitQueries(prices, queries))
```

Note: This solution assumes each query is processed after reading all query inputs, which is optimal for handling large inputs efficiently. The solution calculates the maximum profit for each query in linear time relative to the number of days and queries.