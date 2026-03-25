# DSA Problem 317

'''
Problem Statement:
You are given a list of integers representing the daily prices of a stock over a period. Your task is to find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times), but you must sell the stock before you buy again. Additionally, you are allowed to perform at most one transaction where you can buy and sell on the same day (a "same-day" transaction). This transaction, if chosen, must be the last transaction you make. How can you maximize your profit under these conditions?

For example, given the stock prices [1, 3, 2, 8, 4, 10], the maximum profit can be achieved by buying on day 1, selling on day 4, then performing a same-day transaction on day 6, resulting in a profit of (8-1) + (10-10) = 7.
'''

Solution:
```python
def max_profit_with_same_day_transaction(prices):
    # Initialize variables to store profits
    total_profit = 0
    max_profit_same_day = 0
    
    # Calculate profits from regular transactions
    for i in range(1, len(prices) - 1):
        if prices[i] > prices[i-1]:
            total_profit += prices[i] - prices[i-1]
    
    # Find the maximum same-day transaction profit
    for i in range(len(prices) - 1, 0, -1):
        if prices[i] > prices[i-1]:
            max_profit_same_day = max(max_profit_same_day, prices[i] - prices[i-1])
    
    # Add the max same-day profit to the total
    total_profit += max_profit_same_day
    
    return total_profit

# Example check
prices = [1, 3, 2, 8, 4, 10]
print(f"Maximum profit: {max_profit_with_same_day_transaction(prices)}")
```

Note: The provided solution assumes that no transaction fees or other costs are associated with the transactions. The solution calculates the maximum profit achievable under the given constraints, focusing on maximizing gains from regular transactions and identifying the most profitable same-day transaction to add to the total profit.