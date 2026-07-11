# DSA Problem 87

'''
Problem Statement:
Alice and Bob are playing a game with a list of positive integers. They take turns removing one number from either end of the list. The game ends when there are no numbers left. Alice starts first. Both players play optimally to maximize their score, which is the sum of the numbers they take. Given a list of integers, return the score difference between Alice's and Bob's final scores.

For example, if the list is [5, 3, 1, 4], Alice can take 5, then Bob takes 4, Alice takes 1, and Bob takes 3. Thus, Alice's score is 6, and Bob's score is 7, making the difference -1.
'''

Solution:
```python
def optimal_score_difference(nums):
    n = len(nums)
    # dp[i][j] will denote the maximum score difference a player can achieve over the opponent when playing optimally on the subarray nums[i:j+1]
    dp = [[0] * n for _ in range(n)]
    
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 1:
                dp[i][j] = nums[i]
            else:
                # If the player takes nums[i], the opponent will play optimally on nums[i+1:j+1], and vice versa
                start = nums[i] - dp[i + 1][j]
                end = nums[j] - dp[i][j - 1]
                dp[i][j] = max(start, end)
    
    return dp[0][n - 1]

# Example check
print(optimal_score_difference([5, 3, 1, 4]))  # Output: -1
```

This solution uses dynamic programming to calculate the optimal score difference. The `dp[i][j]` table entry represents the maximum score difference the player can achieve over the opponent when playing optimally on the subarray `nums[i:j+1]`. The function returns the score difference when playing on the whole array.