# DSA Problem 62

'''
Problem Statement:
Imagine a game where you start with a sequence of `n` ones, represented as a list `nums`. In each move, you can choose any two adjacent elements `nums[i]` and `nums[i+1]`, replace them with a single element whose value is `nums[i] + nums[i+1]`, and earn points equal to the new element's value. The game ends when there is only one element left in the list.

Your task is to find the maximum number of points you can earn by playing optimally.

For example, if `nums = [1, 1, 1, 1]`, one possible sequence of moves to maximize the score could be:
- Combine the first two 1s: [2, 1, 1], score += 2
- Combine the last two 1s: [2, 2], score += 2
- Combine the two 2s: [4], score += 4
The total score is 8, which is the maximum possible score for this sequence.

Constraints:
- 1 <= n <= 100
'''

Solution:
```python
def max_score(nums):
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for gap in range(1, n):
        for left in range(n - gap):
            right = left + gap
            dp[left][right] = float('inf')
            for mid in range(left, right):
                points = dp[left][mid] + dp[mid + 1][right] + sum(nums[left:right + 1])
                dp[left][right] = max(dp[left][right], points)
    return dp[0][n - 1]

# Example check
nums = [1, 1, 1, 1]
print(max_score(nums))  # Expected output: 8
```

Note: The provided solution optimizes the process of calculating the maximum score using dynamic programming. The `dp` array is used to store the maximum score achievable for every subsequence, reducing the need for recalculating the same subproblems multiple times.