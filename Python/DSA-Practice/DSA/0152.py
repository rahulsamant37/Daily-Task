# DSA Problem 152

'''
Problem Statement:
Alice and Bob are playing a game with a list of positive integers. Alice starts by choosing any number from the list and then the game alternates between them. In each turn, a player can choose a number from the list that is either 1 less or 1 more than the number last chosen by the other player. The game ends when no more numbers can be chosen according to the rules. The player who cannot make a move loses. Given a list of integers, determine if Alice can win assuming both play optimally. Return True if Alice wins, otherwise False.

Example:
For nums = [1, 2, 3, 4, 5], the function should return True because Alice can always win by choosing 3 and then following Bob's moves accordingly.
'''

Solution:
```python
def can_alice_win(nums):
    """
    Determine if Alice can win the game given the list of numbers.
    """
    dp = [False] * 101  # Assuming the max number in nums is 100 for simplicity
    for num in sorted(set(nums)):
        dp[num] = not dp[num - 1] or not dp[num + 1]
    return dp[max(nums)]

# Example check
nums = [1, 2, 3, 4, 5]
print(can_alice_win(nums))  # Expected output: True
```

Note: This solution assumes a simplified upper bound for the numbers in the list for the dynamic programming array `dp`. The approach calculates for each number if it's a winning position under the assumption that all numbers are unique and sorted for the calculation.