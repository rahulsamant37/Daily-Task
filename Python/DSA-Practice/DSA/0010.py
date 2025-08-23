# DSA Problem 10

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. You need to find the maximum number of unique integers you can pick from `nums` such that the sum of the picked integers is less than or equal to `k`. 

For example, if `nums = [1, 2, 3, 2]` and `k = 4`, you can pick [1, 2] or [1, 3], but not [1, 2, 2] because it exceeds `k` and [2, 2] has duplicate values. Your task is to return the maximum number of unique integers you can pick.

Constraints:
- 1 <= len(nums) <= 100
- 1 <= nums[i] <= 100
- 1 <= k <= 1000
'''

Solution:
```python
def max_unique_integers(nums, k):
    # Sort the array to pick the smallest unique numbers first
    nums = sorted(set(nums))
    count = 0
    total = 0
    for num in nums:
        if total + num <= k:
            total += num
            count += 1
        else:
            break
    return count

# Example usage
nums = [1, 2, 3, 2]
k = 4
print(max_unique_integers(nums, k))  # Output: 2
```

Explanation:
The solution first converts the list `nums` into a set to eliminate duplicates and then sorts it to ensure the smallest unique numbers are considered first. The algorithm iterates through the sorted unique numbers, adding them to `total` until adding another number would exceed `k`. The count of numbers added before exceeding `k` is returned as the result.