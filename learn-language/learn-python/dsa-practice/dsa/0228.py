# DSA Problem 228

'''
Problem Statement:
You are given a list of integers `nums` and a positive integer `k`. Your task is to find the maximum number of unique elements you can have in any subsequence of `nums` whose sum does not exceed `k`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, given `nums = [1, 2, 3, 4]` and `k = 5`, you can have subsequences like `[1, 4]` or `[2, 3]` which have sums not exceeding `5` and contain the maximum number of unique elements (2 in this case).

Return the maximum number of unique elements that can be included in such a subsequence.

Constraints:
- 1 <= len(nums) <= 100
- 1 <= nums[i] <= 100
- 1 <= k <= 1000
'''

Solution:
```python
def max_unique_elements(nums, k):
    nums.sort()
    unique_elements = 0
    total_sum = 0
    for num in nums:
        if total_sum + num <= k:
            total_sum += num
            unique_elements += 1
        else:
            break
    return unique_elements

# Example check (You can remove or comment this part before submitting your solution)
print(max_unique_elements([1, 2, 3, 4], 5))  # Output: 2
print(max_unique_elements([1, 2, 3, 4], 10))  # Output: 4
```

This code sorts the list of numbers to ensure that we can include as many unique elements as possible without exceeding `k`. It iterates through the sorted list, adding elements to the sum until adding the next element would exceed `k`. The function then returns the count of unique elements that were added to the sum.