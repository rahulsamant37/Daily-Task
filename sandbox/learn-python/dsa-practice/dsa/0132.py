# DSA Problem 132

'''
Problem Statement:
You are given a list of integers `nums` and an integer `target`. You need to find all unique pairs of numbers in the list that sum up to the target. Each pair should be sorted in non-decreasing order, and the list of pairs should also be sorted based on the first element of each pair. Note that each number in `nums` can only be used once in a pair.

For example, if `nums = [1, 3, 2, 2, 4]` and `target = 5`, the output should be `[[1, 4], [2, 3]]` because 1+4=5 and 2+3=5, and these pairs are unique and sorted. The pair [2, 3] is not repeated even though 2 appears twice in the input list.
'''

Solution:
```python
def find_pairs(nums, target):
    nums.sort()  # Sort the input list to ensure the pairs are in non-decreasing order
    seen = set()  # To store unique pairs
    pairs = []  # To store the result

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append([min(num, complement), max(num, complement)])
            seen.remove(complement)  # Remove the used number to ensure each number is used only once
        seen.add(num)

    # Remove duplicate pairs
    unique_pairs = list(set(tuple(sorted(sub)) for sub in pairs))
    # Sort the pairs based on the first element of each pair
    unique_pairs.sort(key=lambda x: x[0])
    return unique_pairs

# Example usage
nums = [1, 3, 2, 2, 4]
target = 5
print(find_pairs(nums, target))  # Output: [[1, 4], [2, 3]]
```

This Python solution addresses the problem by first sorting the input list to ensure that potential pairs are considered in order. It then uses a set to track seen numbers and another set to ensure uniqueness of pairs, leveraging tuple conversion and set operations to eliminate duplicates. Finally, it sorts the resulting pairs list based on the first element of each pair to meet the problem's requirements.