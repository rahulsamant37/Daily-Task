# DSA Problem 29

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the number of unique pairs of numbers (nums[i], nums[j]) in the given list such that their absolute difference is exactly `k`. Note that (nums[i], nums[j]) and (nums[j], nums[i]) are considered the same pair, and i != j.

For example, given nums = [1, 5, 3, 4, 2] and k = 2, the unique pairs with an absolute difference of 2 are (1, 3), (3, 5), and (2, 4), so the answer would be 3.
'''

Solution:
```python
def count_k_difference(nums, k):
    num_counts = {}
    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    count = 0
    for num in num_counts:
        if (num + k) in num_counts:
            count += num_counts[num] * num_counts[num + k]
    return count

# Example usage
nums = [1, 5, 3, 4, 2]
k = 2
print(count_k_difference(nums, k))  # Output: 3
```

This function `count_k_difference` takes in a list of integers `nums` and an integer `k`, and returns the number of unique pairs in the list that have an absolute difference of `k`. It uses a dictionary `num_counts` to keep track of the frequency of each number in `nums` and then iterates through the dictionary to find and count pairs whose absolute difference is `k`.