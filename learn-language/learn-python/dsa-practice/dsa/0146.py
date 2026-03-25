# DSA Problem 146

'''
Problem Statement:
Given a list of positive integers, find the number of unique pairs (i, j) such that the sum of the elements at indices i and j is a power of 2. Note that (i, j) and (j, i) are considered the same pair, and i should not be equal to j.

For example, consider the list [1, 2, 2, 3]. The unique pairs with a sum that is a power of 2 are (0, 1) and (0, 2) because 1+2=3 is not a power of 2, but 1+3=4 is. The function should return 1.

Constraints:
- 2 <= len(list) <= 10^4
- 1 <= list[i] <= 10^9
'''

Solution:
```python
from collections import Counter

def is_power_of_two(n):
    return (n != 0) and (n & (n - 1) == 0)

def count_power_of_two_pairs(nums):
    num_counts = Counter(nums)
    count = 0
    for num in num_counts:
        for i in range(2):
            target = 2 ** i
            while target - num > 0:
                if target - num in num_counts:
                    if num == target - num:
                        count += num_counts[num] * (num_counts[num] - 1) // 2
                    else:
                        count += num_counts[num] * num_counts[target - num]
                target *= 2
    return count // 2

# Example usage
nums = [1, 2, 2, 3]
print(count_power_of_two_pairs(nums))  # Output: 1
```

Note: This solution includes a function to check if a number is a power of two and a main function to count the pairs. The example usage demonstrates how to call the function with a sample list.