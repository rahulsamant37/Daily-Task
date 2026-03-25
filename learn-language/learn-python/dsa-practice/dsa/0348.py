# DSA Problem 348

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the number of unique pairs of elements in the list that sum up to `k`. A pair is considered unique if there are no other pairs with the same values in different positions. For instance, if the list is `[1, 3, 2, 2]`, and `k` is `4`, the function should return `2` because there are two unique pairs that sum up to `4`: (1, 3) and (2, 2).

Write a function `count_unique_pairs(nums, k)` that takes in a list of integers and an integer `k` and returns the number of unique pairs that sum up to `k`. You can assume that the list `nums` has at least two elements and that `k` is an integer.

Example:
For `nums = [1, 3, 2, 2]` and `k = 4`, the output should be `2`.
For `nums = [1, 5, 3, 4]` and `k = 9`, the output should be `1`.
'''

Solution:
```python
def count_unique_pairs(nums, k):
    from collections import defaultdict

    # Dictionary to store the frequency of each number
    num_counts = defaultdict(int)
    # Set to store the unique pairs that sum up to k
    unique_pairs = set()

    for num in nums:
        # Calculate the complement that we are looking for
        complement = k - num
        if complement in num_counts:
            # Add the pair to the set in a sorted order to avoid duplicates
            unique_pairs.add(tuple(sorted((num, complement))))
        # Update the count of the current number
        num_counts[num] += 1

    return len(unique_pairs)

# Test cases
print(count_unique_pairs([1, 3, 2, 2], 4))  # Output: 2
print(count_unique_pairs([1, 5, 3, 4], 9))  # Output: 1
```

This Python code snippet defines the function `count_unique_pairs` which uses a dictionary to track the frequency of numbers and a set to ensure that only unique pairs are counted. It iterates through the list of numbers, calculates the necessary complement for each number to sum up to `k`, and checks if this complement has already been seen (i.e., exists in the dictionary). If so, it adds the sorted pair to the set of unique pairs, ensuring that duplicates are not counted. Finally, it returns the size of this set, which represents the number of unique pairs that sum up to `k`.