# DSA Problem 218

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, find the number of unique pairs of elements in `nums` such that the absolute difference between the two elements is exactly `k`. 

For example, if `nums = [1, 5, 3, 4, 2]` and `k = 2`, the pairs that satisfy the condition are (1, 3), (3, 5), and (2, 4), so the answer is 3.
'''

Solution:
```python
def count_pairs_with_diff(nums, k):
    num_set = set(nums)
    count = 0
    for num in num_set:
        if num + k in num_set:
            count += 1
    return count

# Example usage
nums = [1, 5, 3, 4, 2]
k = 2
print(count_pairs_with_diff(nums, k))  # Output: 3
```

This solution works as follows:
1. Convert the list `nums` into a set `num_set` to remove any duplicate values and enable O(1) average time complexity for lookups.
2. Initialize a counter `count` to zero.
3. Iterate through each unique number `num` in `num_set`.
4. Check if `num + k` is also present in `num_set`. If so, it means there exists a pair `(num, num + k)` in the original list `nums` that satisfies the condition.
5. If such a pair is found, increment the `count`.
6. Return the final count after all unique numbers have been checked.