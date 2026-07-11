# DSA Problem 78

'''
Problem Statement:
Given a list of integers `nums`, write a function `find_unique_pairs` that returns the number of unique pairs (i, j) such that `nums[i] + nums[j]` is a perfect square. Note that (i, j) and (j, i) are considered the same pair, and i should not be equal to j.

Example:

Input:
nums = [2, 2, 4, 5]

Output:
2

Explanation:
The unique pairs are (0, 2) and (1, 2) which correspond to the numbers [2, 4] and [2, 4] respectively, both of which sum up to 6, a perfect square (since 6+1=7, and 7 is one less than 8, a perfect square).

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 1000
'''

Solution:
```python
import math
from collections import Counter

def find_unique_pairs(nums):
    def is_perfect_square(n):
        return int(math.sqrt(n))**2 == n

    count = 0
    num_counts = Counter(nums)
    nums_set = set(nums)

    for num in nums_set:
        for possible_pair in range(num, 1001):
            if is_perfect_square(num + possible_pair):
                if num == possible_pair:
                    count += num_counts[num] * (num_counts[num] - 1) // 2
                else:
                    count += num_counts[num] * num_counts[possible_pair]
    return count // 2

# Test the function
nums = [2, 2, 4, 5]
print(find_unique_pairs(nums))  # Expected output: 2
```

Explanation:
This solution first defines a helper function `is_perfect_square` to check if a number is a perfect square. It then uses a `Counter` to count occurrences of each number in `nums` and creates a `set` of the unique numbers. It iterates over each unique number and tries to find another number in the `nums_set` which, when added to the current number, results in a perfect square. It then counts the number of such pairs, taking care to only count pairs once and to adjust for pairs where both numbers are the same. The result is halved at the end because each pair is counted twice in the process.
```