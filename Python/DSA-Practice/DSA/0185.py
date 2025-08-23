# DSA Problem 185

'''
Problem Statement:
Alice has a list of positive integers and wants to play a game with Bob. In this game, Alice will choose any two distinct numbers from the list, calculate their greatest common divisor (GCD), and add it to a score. The game continues until every possible pair of numbers has been used once. Your task is to help Bob calculate the total score Alice will achieve by the end of the game, given the list of positive integers.

For example, if the list is [2, 4, 6], Alice can choose pairs (2, 4) with GCD 2, (2, 6) with GCD 2, and (4, 6) with GCD 2, resulting in a total score of 6.

Constraints:
- The list will contain between 2 and 100 positive integers.
- Each integer in the list will be between 1 and 1000.
'''

Solution:
```python
from math import gcd
from itertools import combinations

def calculate_score(numbers):
    total_score = 0
    # Generate all possible pairs and calculate their GCD
    for pair in combinations(numbers, 2):
        total_score += gcd(pair[0], pair[1])
    return total_score

# Example check (This part is not part of the solution, just for verification)
print(calculate_score([2, 4, 6]))  # Expected output: 6
```

This solution takes advantage of Python's `math.gcd` function to calculate the greatest common divisor and `itertools.combinations` to generate all possible pairs from the input list. It iterates over each pair, calculates their GCD, and sums it up to get the total score.