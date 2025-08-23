# DSA Problem 265

'''
Problem Statement:
You are given a list of integers and a target integer. Your task is to find all unique pairs in the list which sum up to the target. Each pair should be sorted in ascending order, and the resulting list of pairs should also be sorted. You must ensure that no pair is repeated.

For example, if the list is [1, 2, 3, 4, 5] and the target is 6, the pairs would be (1, 5) and (2, 4). Note that (3, 3) cannot be a pair as we need two distinct numbers.

Note:
- The list will contain at most 1000 integers.
- All integers in the list are in the range [-1000, 1000].
- The target is in the range [-2000, 2000].
'''

Solution:
```python
def find_unique_pairs(nums, target):
    """
    Finds all unique pairs in nums that sum up to target.
    Each pair in the output list is sorted, and the list of pairs is also sorted.
    """
    nums.sort()  # Sort the list to ensure the pairs will be in ascending order
    pairs = set()  # Use a set to avoid duplicate pairs
    seen = set()  # Track seen numbers to form pairs

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)

    return sorted(list(pairs))  # Convert the set to a sorted list

# Example check function
def check_solution():
    print(find_unique_pairs([1, 2, 3, 4, 5], 6))  # Expected: [(1, 5), (2, 4)]
    print(find_unique_pairs([0, -1, 2, -3, 1], -2))  # Expected: [(-3, 1)]
    print(find_unique_pairs([1, -1, 1, -1], 0))  # Expected: [(-1, 1)]

check_solution()
```

This solution defines a function `find_unique_pairs` that takes a list of integers `nums` and a target integer and returns all unique pairs that sum up to the target. The pairs are sorted within themselves and the list of pairs is sorted as well. Duplicates are removed using a set, and the function is tested with a check function that provides a few test cases.