# DSA Problem 65

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. You need to find the total number of continuous subarrays whose sum equals to `k`.

For example, given the list `nums = [1, 1, 1]` and `k = 2`, the solution would be 2 because there are two subarrays that sum up to 2: `[1, 1]` at the start and `[1, 1]` at the end.

Your task is to implement the function `subarray_sum_count(nums, k)` that returns the total number of continuous subarrays whose sum equals to `k`.

Constraints:
- 1 <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4
- -2^31 <= k <= 2^31 - 1
'''

Solution:
```python
def subarray_sum_count(nums, k):
    count, current_sum = 0, 0
    sum_occurrences = {0: 1}  # Initialize with 0 sum having one occurrence.
    
    for num in nums:
        current_sum += num
        if current_sum - k in sum_occurrences:
            count += sum_occurrences[current_sum - k]
        sum_occurrences[current_sum] = sum_occurrences.get(current_sum, 0) + 1
    
    return count

# Example check (This part is not part of the solution, just for verification)
print(subarray_sum_count([1, 1, 1], 2))  # Output should be 2
```

Explanation:
This solution uses a hashmap (`sum_occurrences`) to store the cumulative sum frequencies up to the current point. If at any point, the current cumulative sum minus `k` exists in the hashmap, it means there is a subarray that sums up to `k`. The count of such occurrences is then added to the total count. This approach ensures that the solution is efficient, with a time complexity of O(n).