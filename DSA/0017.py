# DSA Problem 17

'''
Problem Statement:
Given a list of integers, write a function `find_unique_pairs` that returns the number of unique pairs (i, j) such that:
- `i < j`
- `nums[j] - nums[i] = k`, where `k` is a given integer.

For example, given the list `[1, 5, 3, 4, 2]` and `k = 2`, the unique pairs are `(1, 3)` and `(2, 4)` because `3-1 = 2` and `4-2 = 2`. Thus, the function should return `2`.

Constraints:
1. The list `nums` will have at least 2 and at most 10^4 elements.
2. Each element in `nums` will be in the range [-10^9, 10^9].
3. `k` is an integer in the range [-10^9, 10^9].
'''

Solution:
```python
from collections import defaultdict

def find_unique_pairs(nums, k):
    """
    Finds the number of unique pairs (i, j) in the list `nums` such that nums[j] - nums[i] = k.
    
    :param nums: List[int] -- a list of integers
    :param k: int -- the difference value
    :return: int -- the number of unique pairs
    """
    if k < 0:
        # If k is negative, swap the roles of nums[i] and nums[j] to make k positive
        nums = [-num for num in nums]
        k = -k
    
    count = 0
    num_counts = defaultdict(int)
    
    for num in nums:
        if num - k in num_counts:
            count += num_counts[num - k]
        num_counts[num] += 1
    
    return count

# Check function to verify the correctness of the solution
def check():
    assert find_unique_pairs([1, 5, 3, 4, 2], 2) == 2
    assert find_unique_pairs([1, 2, 3, 4, 5], 1) == 4
    assert find_unique_pairs([1, 1, 1, 1], 0) == 6
    assert find_unique_pairs([-1, -5, -3, -4, -2], 2) == 2
    assert find_unique_pairs([1, 2, 3, 4, 5], -1) == 4
    print("All test cases passed successfully.")

check()
```

This Python solution employs a dictionary to keep track of the occurrences of each number in the list and iterates through the list to count the number of valid pairs based on the given difference `k`.