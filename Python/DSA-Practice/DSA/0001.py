# DSA Problem 1

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, find the maximum number of unique pairs (i, j) in `nums` such that the sum of `nums[i]` and `nums[j]` equals `k`. Each element in `nums` can only be used once in a pair. Return the count of such unique pairs.

Example:
Input: nums = [1, 3, 4, 1, 5, 2], k = 6
Output: 2
Explanation: The pairs that sum up to 6 are (1, 5) and (4, 2). Each element is used only once.
'''

Solution:
```python
def max_unique_pairs(nums, k):
    from collections import Counter
    num_counts = Counter(nums)
    count = 0
    for num in num_counts:
        if num < k - num and num_counts[num] > 0 and num_counts[k - num] > 0:
            min_count = min(num_counts[num], num_counts[k - num])
            count += min_count
            num_counts[num] -= min_count
            num_counts[k - num] -= min_count
        elif 2 * num == k and num_counts[num] >= 2:
            count += num_counts[num] // 2
            num_counts[num] -= 2 * (num_counts[num] // 2)
    return count

# Example usage
nums = [1, 3, 4, 1, 5, 2]
k = 6
print(max_unique_pairs(nums, k))  # Output: 2
```

Explanation of the solution:
The solution uses a `Counter` from the `collections` module to count the occurrences of each number in the `nums` list. It then iterates through each unique number in the `nums` list and checks if it can form a pair with another number that sums up to `k`. The count of such pairs is incremented, and the counts of the numbers used in forming the pair are appropriately decreased. The function returns the total count of unique pairs found.