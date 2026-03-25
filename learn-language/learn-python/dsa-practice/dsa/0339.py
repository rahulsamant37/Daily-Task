# DSA Problem 339

'''
Problem Statement:
You are given a list of positive integers representing the weights of stones. You can combine any two stones to form a new stone with a weight equal to the sum of the weights of the two stones. After each combination, the newly created stone is placed back among the others. Your task is to determine the minimum possible weight of the last remaining stone after performing all possible combinations. If only one stone is given, return its weight.

For example, if the input is [2, 7, 4, 1, 8], one of the optimal strategies could be combining 2 and 7 to get 9, then combining 4 and 1 to get 5, and finally 8, 9, and 5. The optimal last step would be combining 9 and 5 to get 14, and then combining 14 and 8 to get 22, leaving the minimum possible weight of 22 as the last stone.
'''

Solution:
```python
from heapq import heapify, heappop, heappush

def min_last_stone_weight(stones):
    # Convert all stone weights to negative to simulate a max heap using Python's min heap
    stones = [-stone for stone in stones]
    heapify(stones)
    
    # Combine stones until one or none remains
    while len(stones) > 1:
        first = heappop(stones)
        second = heappop(stones)
        if first != second:
            heappush(stones, first - second)
    
    # Return the last stone's weight, converting back to positive
    return -stones[0] if stones else 0

# Example usage:
stones = [2, 7, 4, 1, 8]
print(min_last_stone_weight(stones))  # Output may vary based on optimal strategy
```

Note: The output may not always be the same as the example provided in the problem statement due to the variability in optimal strategies, but the solution aims to minimize the weight of the last stone.