# DSA Problem 252

'''
Problem Statement:
You are given an array of integers, `nums`, and an integer `k`. Your task is to find the maximum possible sum of a contiguous subarray in `nums` that is divisible by `k`. If no such subarray exists, return 0.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= k <= 10^4
- -10^4 <= nums[i] <= 10^4

Example:
Input: nums = [5, 9, 9, 4], k = 6
Output: 18
Explanation: The subarray [9, 9] has the sum 18, which is divisible by 6.
'''

Solution:
```python
def max_sum_divisible_by_k(nums, k):
    # Initialize prefix sum and result
    prefix_sum = 0
    max_sum = 0
    # Dictionary to store the first occurrence of each remainder
    remainders = {0: 0}
    
    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k
        
        if remainder not in remainders:
            # Store the earliest occurrence of this remainder
            remainders[remainder] = prefix_sum
        else:
            # If the same remainder has been seen before,
            # calculate the potential max sum
            current_sum = prefix_sum - remainders[remainder]
            max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test the function
print(max_sum_divisible_by_k([5, 9, 9, 4], 6))  # Output: 18
```

Explanation of the solution:
The solution uses a prefix sum and a dictionary to keep track of the first occurrence of each remainder when the prefix sum is divided by `k`. If the same remainder is encountered again, it means that the subarray sum between these two occurrences is divisible by `k`. The maximum such subarray sum is tracked and returned as the result.