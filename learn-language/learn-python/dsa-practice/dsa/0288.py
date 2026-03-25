# DSA Problem 288

'''
Problem Statement:
Arun has a collection of N unique books arranged on a shelf. He decides to play a game where he picks a book at random, notes its position, and then places it back in its original position. He does this K times. After each of these K operations, Arun is interested in knowing the expected sum of the positions of the chosen books.

For example, if Arun has 3 books and he picks books 2 times, the expected sum can be calculated considering all possible combinations. 

Write a function `expectedPositionSum(N, K)` that returns the expected sum of the positions of the chosen books, given the total number of unique books N and the number of times this operation is performed K. The result should be rounded to 6 decimal places.

Constraints:
1 <= N <= 100
1 <= K <= 50
'''

Solution:
```python
def expectedPositionSum(N, K):
    """
    Calculates the expected sum of the positions of the chosen books.
    """
    # The sum of positions from 1 to N
    sum_of_positions = sum(range(1, N + 1))
    # Since each book is equally likely to be picked, the expected value for one pick is the average of all positions.
    expected_value_per_pick = sum_of_positions / N
    # The expected sum is simply the expected value per pick multiplied by the number of picks (K).
    expected_sum = expected_value_per_pick * K
    return round(expected_sum, 6)

# Example check function
def check_solution():
    print(expectedPositionSum(3, 2))  # Example input
    print(expectedPositionSum(5, 3))  # Example input

# Running the check function to verify correctness
check_solution()
```

This solution leverages the principle of linearity of expectation to compute the expected sum of positions efficiently. It assumes that each book is equally likely to be picked during each operation, which simplifies the calculation to a straightforward mathematical formula.