# DSA Problem 136

'''
Problem Statement:
A company has decided to reward its employees based on their performance ratings. The performance ratings are given as an array `ratings` where `ratings[i]` represents the performance rating of the i-th employee. The company has decided to give each employee at least one reward and ensure that any employee with a higher performance rating gets more rewards than their neighbors. Find the minimum number of rewards the company must give out.

For example, if the ratings are [4, 2, 3, 6, 1], the rewards could be [2, 1, 2, 3, 1], so the total rewards given out are 9.

Write a function `minRewards` that takes in an array of integers representing the ratings of each employee and returns the minimum number of rewards needed.
'''

Solution:
def minRewards(ratings):
    if not ratings:
        return 0
    
    n = len(ratings)
    rewards = [1] * n
    
    # Forward pass
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            rewards[i] = rewards[i - 1] + 1
    
    # Backward pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    
    return sum(rewards)

# Example usage
ratings = [4, 2, 3, 6, 1]
print(minRewards(ratings))  # Output: 9

'''
This solution works by first ensuring that every employee gets at least one reward, and then it does a forward pass to make sure that any employee with a higher rating than the previous one gets more rewards. It then does a backward pass to make sure the same condition holds when looking at the next employee. This ensures that the minimum possible rewards are given while satisfying the conditions.
'''