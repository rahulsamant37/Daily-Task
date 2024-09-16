# DSA Problem 197

'''
Problem Statement:
You are given a list of integers, `nums`, and an integer `k`. Your task is to find the number of unique pairs of indices `(i, j)` such that `nums[i]` and `nums[j]` are both divisible by `k`, and `i < j`. 

For example, if `nums = [2, 4, 6, 8, 10]` and `k = 2`, there are 10 such pairs since every even number can pair with every other even number that comes after it in the list.
'''

Solution:
```python
from collections import defaultdict

def count_divisible_pairs(nums, k):
    """
    Counts the number of unique pairs (i, j) where nums[i] and nums[j] are divisible by k and i < j.
    """
    # Counter for the number of divisible numbers encountered so far
    count = 0
    # Dictionary to keep track of how many numbers divisible by k have been encountered
    divisible_count = defaultdict(int)
    
    for num in nums:
        if num % k == 0:
            # Increase the count of the current number modulo k
            divisible_count[num % k] += 1
            # Subtract one to exclude the current number itself, as we need i < j
            count += divisible_count[num % k] - 1
            
    return count

# Example check function to verify the solution
def check_solution():
    assert count_divisible_pairs([2, 4, 6, 8, 10], 2) == 10
    assert count_divisible_pairs([3, 6, 9, 12], 3) == 6
    assert count_divisible_pairs([5, 10, 15, 20], 5) == 6
    assert count_divisible_pairs([1, 2, 3, 4], 5) == 0
    print("All tests passed!")

check_solution()
```

This problem involves basic arithmetic operations and the use of a hash map (dictionary in Python) to efficiently keep track of divisible numbers and count the number of valid pairs.