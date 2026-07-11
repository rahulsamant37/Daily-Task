# DSA Problem 300

'''
Problem Statement:
Given a list of integers, find the maximum number of non-overlapping sublists whose sum is exactly equal to a given target value `k`. Each integer from the list can only be part of one sublist. Return the maximum number of such sublists that can be formed.

For example, if the list is [1, 2, 3, 4, 5] and k = 3, one possible way is to have the sublists [1, 2] and [3], which both sum up to 3. Note that [1, 2] and [4 - 1] (using 3 from the next segment) are not allowed as they overlap.

Constraints:
- The length of the list will be at most 1000.
- The values in the list and `k` will be integers in the range [-1000, 1000].
'''

Solution:
```python
def max_non_overlapping_sublists(nums, k):
    from collections import defaultdict

    prefix_sum_to_index = defaultdict(list)
    prefix_sum_to_index[0].append(-1)  # Base case
    current_sum = 0
    count = 0
    last_end = -1  # To keep track of the end of the last valid sublist

    for i, num in enumerate(nums):
        current_sum += num
        if (current_sum - k) in prefix_sum_to_index:
            for start_index in prefix_sum_to_index[current_sum - k]:
                if start_index >= last_end:  # Ensuring non-overlapping
                    count += 1
                    last_end = i  # Update the last end index
                    break  # Only one valid start per current_sum - k is needed

        prefix_sum_to_index[current_sum].append(i)

    return count

# Example usage
nums = [1, 2, 3, 4, 5]
k = 3
print(max_non_overlapping_sublists(nums, k))  # Output: 2
```

This solution uses a dictionary to track the indices at which each prefix sum occurs. For each number in the list, it calculates the current prefix sum and checks if there exists a prefix sum that would create a sublist summing to `k` (i.e., current_sum - k). If such a prefix sum exists and the starting index of this valid sublist does not overlap with the last valid sublist found, it increments the count of valid sublists.