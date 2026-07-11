# DSA Problem 226

'''
Problem Statement:
You are given a list of positive integers representing the weights of different items. Your task is to find the minimum possible difference between the sum of the weights of items placed in two different bags. Each item must be placed in exactly one of the two bags. Write a function `min_weight_difference` that takes a list of integers and returns the minimum possible difference between the sums of the two bags.

Example:
- For the input `[1, 2, 3, 4, 5]`, one possible way to divide the items is to put `[1, 2, 4]` in one bag and `[3, 5]` in the other, resulting in a difference of `1`.
- For the input `[10, 10]`, the difference is `0` since both items can be placed in separate bags, making the sums equal.
'''

Solution:
```python
def min_weight_difference(weights):
    total_weight = sum(weights)
    n = len(weights)
    dp = [[False] * (total_weight + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(total_weight + 1):
            if dp[i - 1][j]:
                dp[i][j] = True
            elif j >= weights[i - 1]:
                dp[i][j] = dp[i - 1][j - weights[i - 1]]
    
    for diff in range(total_weight // 2 + 1):
        if dp[n][total_weight // 2 - diff]:
            return (total_weight // 2 - (total_weight // 2 - diff)) - (total_weight - (total_weight // 2 - diff))
    return total_weight

# Test the function
print(min_weight_difference([1, 2, 3, 4, 5]))  # Expected output: 1
print(min_weight_difference([10, 10]))        # Expected output: 0
```

Explanation:
- The solution uses dynamic programming to find the subset of items that can get the closest to half the total weight. This way, the difference between the sums of the two groups of items can be minimized.
- The `dp` array is used to track the possible sums up to half the total weight with the items considered so far.
- Finally, the function calculates and returns the minimum difference possible between the two bags.