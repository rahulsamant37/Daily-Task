# DSA Problem 175

'''
Problem Statement:
Given a list of non-negative integers `nums` and a positive integer `k`, you are asked to find the maximum value of the expression `(nums[i] & nums[j]) ^ k` where `&` is the bitwise AND operator and `^` is the bitwise XOR operator. It's guaranteed that `0 <= i, j < len(nums)` and `i ≠ j`.

Constraints:
- 2 <= len(nums) <= 10^5
- 0 <= nums[i] <= 10^6
- 0 <= k <= 10^6

Example:
Input: nums = [1, 2, 3, 4], k = 5
Output: 7
Explanation: The maximum value is obtained from (3 & 4) ^ 5 = 7.
'''

Solution:
```python
def find_max_expression_value(nums, k):
    max_val = 0
    # Iterate through each pair (i, j) with i < j
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # Calculate the value of the expression for the current pair
            val = (nums[i] & nums[j]) ^ k
            # Update max_val if the current value is greater
            max_val = max(max_val, val)
    return max_val

# Example check
nums = [1, 2, 3, 4]
k = 5
print(find_max_expression_value(nums, k))  # Output: 7
```
Note: The given solution is a brute force approach which may not be optimal for large lists due to its O(n^2) complexity. Considering the constraints provided in the problem, an optimized solution might be necessary for efficient computation.