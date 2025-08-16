# Python Question: Maximum Profit with Cooldown
'''
You are given an array of integers `prices` representing the price of a stock on each day.

You have the following restrictions:

*   You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
*   However, you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
*   After you sell your stock, you cannot buy stock on the next day (i.e., there is a cooldown period of 1 day).

Find the maximum profit you can make.

Example:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''

# Solution
def solution():
    def maxProfit(prices):
        """
        Calculates the maximum profit achievable with the given constraints.

        Args:
            prices: A list of integers representing the stock prices on each day.

        Returns:
            The maximum profit achievable.
        """
        if not prices:
            return 0

        n = len(prices)
        # buy[i]: Maximum profit ending at day i with a buy action.
        # sell[i]: Maximum profit ending at day i with a sell action.
        # cooldown[i]: Maximum profit ending at day i with a cooldown action.

        buy = [0] * n
        sell = [0] * n
        cooldown = [0] * n

        # Initialization for the first day:
        buy[0] = -prices[0]  # Buy on the first day
        sell[0] = 0          # No profit if we sell on the first day
        cooldown[0] = 0      # No profit/loss if we cooldown on the first day

        for i in range(1, n):
            # Buy[i]:
            # Either we bought today (after cooldown yesterday),
            # or we held the buy from yesterday.
            buy[i] = max(cooldown[i-1] - prices[i], buy[i-1])

            # Sell[i]:
            # Either we sold today,
            # or we held the sell from yesterday.
            sell[i] = max(buy[i-1] + prices[i], sell[i-1])

            # Cooldown[i]:
            # Either we cooled down today (after selling yesterday),
            # or we held the cooldown from yesterday.
            cooldown[i] = max(sell[i-1], cooldown[i-1])

        # The maximum profit will be either from selling on the last day or from cooldown on the last day.
        return max(sell[n-1], cooldown[n-1])

    return maxProfit

# Test cases
def test_solution():
    maxProfit = solution()
    # Test case 1
    prices1 = [1,2,3,0,2]
    expected1 = 3
    assert maxProfit(prices1) == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {maxProfit(prices1)}"

    # Test case 2
    prices2 = [1]
    expected2 = 0
    assert maxProfit(prices2) == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {maxProfit(prices2)}"

    # Test case 3
    prices3 = [1,2]
    expected3 = 1
    assert maxProfit(prices3) == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {maxProfit(prices3)}"

    # Test case 4
    prices4 = [1,2,4,2,5,7,2,4,9,0]
    expected4 = 10
    assert maxProfit(prices4) == 10, f"Test Case 4 Failed: Expected 10, Got {maxProfit(prices4)}"

    # Test case 5
    prices5 = []
    expected5 = 0
    assert maxProfit(prices5) == 0, f"Test Case 5 Failed: Expected {expected5}, Got {maxProfit(prices5)}"

    # Test case 6
    prices6 = [2,1]
    expected6 = 0
    assert maxProfit(prices6) == 0, f"Test Case 6 Failed: Expected {expected6}, Got {maxProfit(prices6)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()