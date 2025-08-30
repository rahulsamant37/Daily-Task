"""
Dynamic Programming Optimizations
================================

Optimized dynamic programming patterns and techniques for competitive programming.
"""

import sys
from functools import lru_cache

def memoization_vs_tabulation():
    """
    Compare recursive (memoization) vs iterative (tabulation) DP
    """
    
    # Memoization (Top-down) - use for complex state transitions
    @lru_cache(maxsize=None)
    def fibonacci_memo(n):
        if n <= 1:
            return n
        return fibonacci_memo(n-1) + fibonacci_memo(n-2)
    
    # Tabulation (Bottom-up) - usually faster and more memory efficient
    def fibonacci_tab(n):
        if n <= 1:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
    
    # Space-optimized tabulation
    def fibonacci_optimized(n):
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b
    
    return fibonacci_memo, fibonacci_tab, fibonacci_optimized

def knapsack_optimizations():
    """
    Different approaches to knapsack problems
    """
    
    # 0/1 Knapsack - 2D DP
    def knapsack_2d(weights, values, capacity):
        n = len(weights)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for w in range(capacity + 1):
                # Don't take item i-1
                dp[i][w] = dp[i-1][w]
                
                # Take item i-1 if possible
                if weights[i-1] <= w:
                    dp[i][w] = max(dp[i][w], 
                                 dp[i-1][w - weights[i-1]] + values[i-1])
        
        return dp[n][capacity]
    
    # Space-optimized 0/1 Knapsack - 1D DP
    def knapsack_1d(weights, values, capacity):
        dp = [0] * (capacity + 1)
        
        for i in range(len(weights)):
            # Traverse backwards to avoid using updated values
            for w in range(capacity, weights[i] - 1, -1):
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
        
        return dp[capacity]
    
    # Unbounded Knapsack
    def unbounded_knapsack(weights, values, capacity):
        dp = [0] * (capacity + 1)
        
        for w in range(1, capacity + 1):
            for i in range(len(weights)):
                if weights[i] <= w:
                    dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
        
        return dp[capacity]
    
    return knapsack_2d, knapsack_1d, unbounded_knapsack

def longest_common_subsequence_optimizations():
    """
    LCS with space optimization
    """
    
    # Standard LCS - O(mn) space
    def lcs_2d(s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
    
    # Space-optimized LCS - O(min(m,n)) space
    def lcs_1d(s1, s2):
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        
        m, n = len(s1), len(s2)
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(prev[j], curr[j-1])
            
            prev, curr = curr, prev
        
        return prev[n]
    
    return lcs_2d, lcs_1d

def edit_distance_dp():
    """
    Edit distance with different optimizations
    """
    
    # Standard edit distance
    def edit_distance_2d(s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize base cases
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j],    # deletion
                                      dp[i][j-1],     # insertion
                                      dp[i-1][j-1])   # substitution
        
        return dp[m][n]
    
    # Space-optimized edit distance
    def edit_distance_1d(s1, s2):
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        
        m, n = len(s1), len(s2)
        prev = list(range(n + 1))
        curr = [0] * (n + 1)
        
        for i in range(1, m + 1):
            curr[0] = i
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(prev[j], curr[j-1], prev[j-1])
            
            prev, curr = curr, prev
        
        return prev[n]
    
    return edit_distance_2d, edit_distance_1d

def matrix_chain_multiplication():
    """
    Matrix chain multiplication DP
    """
    
    def matrix_chain_order(dimensions):
        n = len(dimensions) - 1  # number of matrices
        dp = [[0] * n for _ in range(n)]
        
        # l is chain length
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i][j] = float('inf')
                
                for k in range(i, j):
                    cost = (dp[i][k] + dp[k+1][j] + 
                           dimensions[i] * dimensions[k+1] * dimensions[j+1])
                    dp[i][j] = min(dp[i][j], cost)
        
        return dp[0][n-1]
    
    return matrix_chain_order

def coin_change_variations():
    """
    Different coin change problem variations
    """
    
    # Minimum coins needed
    def coin_change_min(coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
    
    # Number of ways to make change
    def coin_change_ways(coins, amount):
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]
    
    # Coin change with limited coins
    def coin_change_limited(coins, counts, amount):
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for i, coin in enumerate(coins):
            # Use multiple knapsack approach
            for _ in range(counts[i]):
                for j in range(amount, coin - 1, -1):
                    dp[j] += dp[j - coin]
        
        return dp[amount]
    
    return coin_change_min, coin_change_ways, coin_change_limited

def digit_dp_example():
    """
    Digit DP - count numbers with certain properties
    """
    
    def count_numbers_with_digit_sum(n, target_sum):
        """
        Count numbers from 0 to n with digit sum equal to target_sum
        """
        s = str(n)
        memo = {}
        
        def dp(pos, current_sum, tight, started):
            if pos == len(s):
                return 1 if current_sum == target_sum and started else 0
            
            if (pos, current_sum, tight, started) in memo:
                return memo[(pos, current_sum, tight, started)]
            
            result = 0
            limit = int(s[pos]) if tight else 9
            
            for digit in range(0, limit + 1):
                new_tight = tight and (digit == limit)
                new_started = started or (digit > 0)
                new_sum = current_sum + digit if new_started else 0
                
                if new_sum <= target_sum:  # Pruning
                    result += dp(pos + 1, new_sum, new_tight, new_started)
            
            memo[(pos, current_sum, tight, started)] = result
            return result
        
        return dp(0, 0, True, False)
    
    return count_numbers_with_digit_sum

def dp_optimization_techniques():
    """
    Various DP optimization techniques
    """
    
    # Technique 1: State compression using bitmasks
    def traveling_salesman_dp(dist):
        n = len(dist)
        dp = {}
        
        def tsp(mask, pos):
            if mask == (1 << n) - 1:
                return dist[pos][0]  # Return to start
            
            if (mask, pos) in dp:
                return dp[(mask, pos)]
            
            result = float('inf')
            for city in range(n):
                if mask & (1 << city) == 0:  # City not visited
                    new_mask = mask | (1 << city)
                    result = min(result, dist[pos][city] + tsp(new_mask, city))
            
            dp[(mask, pos)] = result
            return result
        
        return tsp(1, 0)  # Start from city 0
    
    # Technique 2: Convex Hull Optimization (for certain recurrences)
    def convex_hull_optimization_example():
        """
        Example: dp[i] = min(dp[j] + cost(j, i)) for j < i
        where cost function satisfies certain properties
        """
        # This is a template - specific implementation depends on the problem
        from collections import deque
        
        def solve_with_convex_hull(arr):
            n = len(arr)
            dp = [float('inf')] * n
            dp[0] = 0
            
            # Convex hull optimization would go here
            # This is problem-specific
            
            return dp[n-1]
        
        return solve_with_convex_hull
    
    return traveling_salesman_dp

def dp_optimization_tips():
    """
    Key DP optimization strategies
    """
    tips = [
        "1. Use tabulation instead of memoization when possible",
        "2. Optimize space by using only necessary previous states",
        "3. Use rolling arrays for problems needing only few previous rows",
        "4. Consider state compression with bitmasks for small sets",
        "5. Use bottom-up approach to avoid recursion overhead",
        "6. Precompute transitions when possible",
        "7. Use early termination/pruning in recursive solutions",
        "8. Consider digit DP for number-based problems",
        "9. Use convex hull optimization for certain cost functions",
        "10. Profile memory usage and optimize accordingly",
        "11. Use lru_cache for simple memoization in contests",
        "12. Consider matrix exponentiation for linear recurrences"
    ]
    return tips

def dp_examples_runner():
    """
    Test all DP implementations
    """
    
    # Test Fibonacci
    _, fib_tab, fib_opt = memoization_vs_tabulation()
    fib_result = fib_opt(10)
    
    # Test Knapsack
    knapsack_2d, knapsack_1d, _ = knapsack_optimizations()
    weights = [2, 1, 3, 2]
    values = [12, 10, 20, 15]
    capacity = 5
    knapsack_result = knapsack_1d(weights, values, capacity)
    
    # Test LCS
    lcs_2d, lcs_1d = longest_common_subsequence_optimizations()
    lcs_result = lcs_1d("ABCDGH", "AEDFHR")
    
    # Test Edit Distance
    edit_2d, edit_1d = edit_distance_dp()
    edit_result = edit_1d("kitten", "sitting")
    
    # Test Coin Change
    coin_min, coin_ways, _ = coin_change_variations()
    coins = [1, 2, 5]
    amount = 11
    min_coins = coin_min(coins, amount)
    ways = coin_ways(coins, amount)
    
    return {
        'fibonacci_10': fib_result,
        'knapsack_result': knapsack_result,
        'lcs_result': lcs_result,
        'edit_distance': edit_result,
        'min_coins': min_coins,
        'coin_ways': ways
    }

if __name__ == "__main__":
    print("Dynamic Programming Optimizations")
    
    # Test all implementations
    results = dp_examples_runner()
    
    print("Results:")
    for key, value in results.items():
        print(f"{key}: {value}")
    
    # Test matrix chain multiplication
    matrix_chain = matrix_chain_multiplication()
    dimensions = [1, 2, 3, 4, 5]
    matrix_result = matrix_chain(dimensions)
    print(f"Matrix chain multiplication: {matrix_result}")
    
    # Test digit DP
    digit_dp = digit_dp_example()
    count = digit_dp(100, 10)
    print(f"Numbers <= 100 with digit sum 10: {count}")
    
    # Show optimization tips
    tips = dp_optimization_tips()
    print("\nDP Optimization Tips:")
    for tip in tips:
        print(tip)
    
    print("\nDP optimizations demonstrated successfully!")
