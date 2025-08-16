# Python Question: Find the maximum number of coins that can be made using any combination of coins from a given set

'''
Problem Statement:
You are given a set of coins (denoted as 'coin[i]') with given denominations (denoted as 'denom[i]'). The goal is to find the maximum number of coins that can be made using any combination of coins from the given set.

For example, consider the following set of coins:

coin = ['1', '2', '3', '4', '5']
denom = [10, 20, 50, 100]

The maximum number of coins that can be made from this set of coins are:

1. Using only coins ['1', '2', '3'] = 3 coins (denom[3] = 100)
2. Using only coins ['4', '5'] = 2 coins (denom[4] = 100)
3. Using coins ['1', '2', '4'] = 3 coins (denom[3] = 100)
4. Using coins ['1', '2', '5'] = 3 coins (denom[1] + denom[2] + denom[5] = 30 + 20 + 5 = 55)
5. Using coins ['3', '4', '5'] = 3 coins (denom[3] + denom[4] + denom[5] = 30 + 10 + 5 = 45)

So, the maximum number of coins that can be made are 45 coins.
'''

def findMaxCoins(coin, denom):
    n = len(coin)
    dp = [[0 for _ in range(len(denom))] for _ in range(n + 1)]
    
    for coin_index in range(n + 1):
        for denom_index in range(len(denom)):
            if coin_index == 0 or denom_index == 0:
                dp[coin_index][denom_index] = 0
            elif coin[coin_index - 1] == denom[denom_index - 1]:
                dp[coin_index][denom_index] = 1 + dp[coin_index - 1][denom_index - 1]
            else:
                min_denom = min(denom)
                dp[coin_index][denom_index] = dp[coin_index][min_denom] + dp[coin_index][denom[min_denom]]

    return dp[n][len(denom)-1]

coin = ['1', '2', '3', '4', '5']
denom = [10, 20, 50, 100]

result = findMaxCoins(coin, denom)
print(result)