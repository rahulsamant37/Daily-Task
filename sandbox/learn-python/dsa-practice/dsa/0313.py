# DSA Problem 313

'''
Problem Statement:
Given a list of integers, find the maximum number of non-overlapping sublists such that the sum of elements in each sublist is equal to 0. Return the maximum number of such sublists.

For example, given the list [3, 2, -2, 5, -3, 1, -1], the sublists [2, -2] and [5, -3, 1, -1] both sum to 0, and they are non-overlapping. Thus, the function should return 2.
'''

Solution:
```python
def max_non_overlapping_zeros(arr):
    sum_to_index = {0: -1}
    current_sum = 0
    prev_end = -1
    count = 0
    
    for i, num in enumerate(arr):
        current_sum += num
        if current_sum in sum_to_index and sum_to_index[current_sum] >= prev_end:
            count += 1
            prev_end = i
        sum_to_index[current_sum] = i
    
    return count

# Test the function
print(max_non_overlapping_zeros([3, 2, -2, 5, -3, 1, -1]))  # Expected output: 2
```

Explanation:
- The function `max_non_overlapping_zeros` uses a dictionary `sum_to_index` to keep track of the cumulative sums and their first occurrence index.
- It iterates through the array, updating the current sum and checking if this sum has been seen before (indicating a zero sum sublist).
- The variable `prev_end` is used to ensure that the sublists do not overlap.
- The function returns the count of non-overlapping sublists with a sum of zero.