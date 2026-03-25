# DSA Problem 72

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum number of unique pairs of numbers (i, j) in `nums` such that `nums[i] + nums[j] = k`. Each number in `nums` can only be used once in a pair.

For example, given `nums = [1, 3, 2, 2, 4, 0]` and `k = 4`, the possible pairs are (1, 3) and (0, 4), making the total number of unique pairs 2.

Constraints:
- 1 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= k <= 10^9
'''

Solution:
```python
def max_unique_pairs(nums, k):
    from collections import Counter
    
    count = Counter(nums)
    unique_pairs = 0
    
    for num in count:
        if k - num in count:
            if num == k - num:
                unique_pairs += count[num] // 2
            else:
                unique_pairs += min(count[num], count[k - num])
                count[k - num] = 0  # To avoid counting the pair twice
            count[num] = 0  # Mark this number as used
    
    return unique_pairs // 2  # Each pair is counted twice

# Example check
nums = [1, 3, 2, 2, 4, 0]
k = 4
print(max_unique_pairs(nums, k))  # Output should be 2
```

This Python solution uses a `Counter` to efficiently count the occurrences of each number in the `nums` list. It then iterates through each number, checking if its complement (the number that, when added to it, equals `k`) exists in the `Counter`. Special care is taken to handle the case where the number and its complement are the same, ensuring pairs are not double-counted.