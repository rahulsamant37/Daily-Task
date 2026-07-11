# DSA Problem 70

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the number of unique pairs of elements in `nums` that have a difference of exactly `k`. A pair of elements (nums[i], nums[j]) is considered unique if it satisfies the following conditions:
1. The absolute difference between nums[i] and nums[j] is exactly `k`.
2. The pair (nums[i], nums[j]) is counted only once, regardless of the order of elements, i.e., (nums[i], nums[j]) is considered the same as (nums[j], nums[i]).

For example, if nums = [1, 5, 3, 4, 2] and k = 2, there are 3 pairs with a difference of 2: (1, 3), (2, 4), and (3, 5).

Write a function `count_pairs_with_difference` that takes a list of integers and an integer `k` as its arguments and returns the count of such pairs.

Constraints:
- 1 <= len(nums) <= 10^4
- -10^7 <= nums[i] <= 10^7
- 0 <= k <= 2 * 10^7
'''

Solution:
```python
def count_pairs_with_difference(nums, k):
    # Sort the list to ensure the pairs are counted in order
    nums.sort()
    count = 0
    seen = set()
    for i in range(len(nums)):
        # Calculate the target value that, when subtracted by nums[i], gives k
        target = nums[i] + k
        if target in nums and (nums[i], target) not in seen:
            count += 1
            seen.add((nums[i], target))
    return count

# Example check
nums = [1, 5, 3, 4, 2]
k = 2
print(count_pairs_with_difference(nums, k))  # Expected output: 3
```

Note: This solution assumes that the list of numbers does not contain duplicates. If duplicates are allowed, additional logic would be needed to correctly handle them within the `seen` set mechanism.