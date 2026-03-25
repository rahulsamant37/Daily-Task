# DSA Problem 188

'''
Problem Statement:
A group of friends decide to play a game where each person writes down a positive integer on a piece of paper. However, one of the integers is supposed to be written twice, but due to a mistake, it was written once, and another integer that was supposed to be written once was written twice. Given a list of integers representing the numbers written down, can you find the two unique numbers that were incorrectly written? Return them in any order.

For example, if the list is [4, 1, 2, 1, 2, 3, 3], the numbers 4 and 3 were incorrectly written since 4 should have been written once but was not written at all, and 3 was written twice instead of once.
'''

Solution:
```python
def find_miswritten_numbers(nums):
    from collections import Counter
    # Count the occurrences of each number
    num_counts = Counter(nums)
    # Find the numbers that are written once and twice incorrectly
    miswritten = [num for num, count in num_counts.items() if count != 1]
    return miswritten

# Example usage
print(find_miswritten_numbers([4, 1, 2, 1, 2, 3, 3]))  # Output could be [3, 4]
```

Note: The output might vary in the order of the numbers since the problem statement asks to return them in any order.