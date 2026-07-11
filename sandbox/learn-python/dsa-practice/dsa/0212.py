# DSA Problem 212

'''
Problem Statement:
You are given a list of positive integers and a target integer. Your task is to find the number of unique pairs of integers in the list that, when summed, equal the target integer. Note that the order of the numbers in the pair does not matter, meaning (a, b) is considered the same as (b, a).

For example, if the list is [1, 3, 2, 2, 3, 4] and the target integer is 5, the unique pairs that sum up to 5 are (1, 4) and (2, 3). Even though there are multiple occurrences of 2 and 3, they are counted as only one unique pair.

Write a function `count_unique_pairs(nums, target)` that returns the number of such unique pairs. Assume that the list `nums` will have at least two elements and will not exceed 1000 elements, and `target` will be a positive integer.
'''

Solution:
```python
def count_unique_pairs(nums, target):
    seen = set()
    nums_set = set(nums)  # Convert to set to remove duplicates and allow O(1) lookups
    count = 0

    for num in nums_set:
        complement = target - num
        if complement in nums_set and (complement, num) not in seen and (num, complement) not in seen:
            seen.add((num, complement))
            count += 1

    return count

# Example check
print(count_unique_pairs([1, 3, 2, 2, 3, 4], 5))  # Expected output: 2
```

This solution ensures that each pair is counted only once regardless of the number of occurrences of each number in the list. It uses a set to store seen pairs to avoid counting duplicates.