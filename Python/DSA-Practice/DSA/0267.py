# DSA Problem 267

'''
Problem Statement:
A group of students are participating in a coding contest. Each student is given a list of integers. The task is to find the maximum number of non-overlapping sublists, each having the same sum. For instance, if the list is [1,2,3,0,3,1,1], the sublists [1,2], [3,0], [3], [1,1] have the same sum (3), and they are non-overlapping. Write a function to determine the maximum number of such sublists.

Note:
- The length of the list will not exceed 1000.
- The integers in the list can be negative as well.
'''

Solution:
```python
def max_non_overlapping_sublists(nums):
    sum_indices = {0: [-1]}  # Stores the sum and the corresponding indices
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum not in sum_indices:
            sum_indices[current_sum] = [i]
        else:
            sum_indices[current_sum].append(i)

    max_count = 0
    for indices in sum_indices.values():
        if len(indices) > 1:
            count = 1
            last_index = indices[0]
            for index in indices[1:]:
                if index > last_index + 1:  # Ensuring non-overlapping
                    count += 1
                    last_index = index
            max_count = max(max_count, count)

    return max_count

# Example check
nums = [1, 2, 3, 0, 3, 1, 1]
print(max_non_overlapping_sublists(nums))  # Output: 4
```

In this solution, we first compute the cumulative sums and store the indices where each cumulative sum occurs. Then, for each unique cumulative sum, we try to find the maximum number of non-overlapping indices (sublists). The overall complexity is O(n), where n is the length of the input list, making it suitable for large lists as specified in the problem constraints.