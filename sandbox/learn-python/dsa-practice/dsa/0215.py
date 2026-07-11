# DSA Problem 215

'''
Problem Statement:
Alice and Bob are playing a game with a list of integers. The game starts with Alice picking any number from the list and removing it. After that, Bob can choose either of the two numbers at the ends of the list and remove it. They alternate turns like this until the list is empty. The goal is to maximize the sum of the numbers they remove. Assuming both play optimally, what is the maximum sum Alice can achieve?

Constraints:
- 1 <= len(numbers) <= 100
- 1 <= numbers[i] <= 100
- The list "numbers" will not be empty.

Example:
Input: [3, 9, 1, 2]
Output: 12
Explanation: Alice picks 3, Bob picks 2, Alice picks 9, Bob picks 1. The sum Alice achieves is 3 + 9 = 12.
'''

Solution:
```python
def max_sum(numbers):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def optimal_sum(start, end, turn):
        if start > end:
            return 0
        if turn == 0:  # Alice's turn
            return max(numbers[start] + optimal_sum(start + 1, end, 1), numbers[end] + optimal_sum(start, end - 1, 1))
        else:  # Bob's turn, minimizing for Bob
            return min(optimal_sum(start + 1, end, 0), optimal_sum(start, end - 1, 0))

    return optimal_sum(0, len(numbers) - 1, 0)

# Example check
print(max_sum([3, 9, 1, 2]))  # Expected output: 12
```

Note: This solution uses dynamic programming with memoization to efficiently solve the problem. The `lru_cache` decorator is used to cache the results of the recursive calls, which prevents the function from recalculating the same subproblems multiple times, thus significantly improving the performance for larger lists.