# DSA Problem 94

'''
Problem Statement:
You are given a list of positive integers `nums` and an integer `k`. Your task is to find the number of unique pairs (i, j) in `nums` where `nums[i]` is divisible by `nums[j]` and `nums[i] / nums[j]` equals `k`. Note that (i, j) and (j, i) are considered the same pair and should not be counted twice.

For example, given `nums = [1, 2, 3, 6]` and `k = 2`, there are 2 such unique pairs: (1, 2) and (3, 6).
'''

Solution:
```python
from collections import defaultdict

def find_divisible_pairs(nums, k):
    """
    Finds the number of unique pairs (i, j) in nums where nums[i] is divisible by nums[j]
    and nums[i] / nums[j] equals k.
    """
    count = 0
    num_counts = defaultdict(int)
    for num in nums:
        num_counts[num] += 1
    
    for num in num_counts:
        if num * k in num_counts:
            if num == num * k:
                count += num_counts[num] * (num_counts[num] - 1) // 2
            else:
                count += num_counts[num] * num_counts[num * k]
                
    return count

# Check function to verify the solution with provided data points
def check_solution():
    assert find_divisible_pairs([1, 2, 3, 6], 2) == 2, "Test case 1 failed"
    assert find_divisible_pairs([1, 1, 1], 1) == 3, "Test case 2 failed"
    assert find_divisible_pairs([2, 4, 8], 2) == 2, "Test case 3 failed"
    assert find_divisible_pairs([10, 5, 2], 2) == 1, "Test case 4 failed"
    print("All test cases passed!")

check_solution()
```

This Python code snippet defines a function `find_divisible_pairs` that calculates the number of unique pairs (i, j) in the list `nums` where one number is divisible by the other and the division result is equal to `k`. It uses a dictionary to count occurrences of each number and then iterates through the dictionary to find and count valid pairs. The `check_solution` function is used to verify the correctness of the solution with provided data points.