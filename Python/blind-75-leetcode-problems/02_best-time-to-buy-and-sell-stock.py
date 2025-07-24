## Optimal Approach with Time Complexity: O(n) and Space Complexity: O(1)
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
                    
        return max_profit

prices = [7,1,5,3,6,4]
solution = Solution()
solution.maxProfit(prices)