# DSA Problem 7

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, return the length of the longest subarray with a sum that is divisible by `k`. If no such subarray exists, return 0. 

Example 1:
Input: nums = [4, 5, 0, -2, -3, 1], k = 5
Output: 3
Explanation: The subarray [5, 0, -2] has a sum of 3, which is divisible by 5.

Example 2:
Input: nums = [5], k = 9
Output: 0
Explanation: There is no subarray whose sum is divisible by 9.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= 10^4
'''

Solution:
```python
def longest_divisible_subarray(nums, k):
    # Dictionary to store the first occurrence of a remainder
    remainder_map = {0: -1}
    max_length = 0
    current_sum = 0
    
    for i, num in enumerate(nums):
        current_sum += num
        remainder = current_sum % k
        
        if remainder < 0:
            remainder += k
        
        if remainder in remainder_map:
            # If the same remainder was seen before, calculate the length of the subarray
            subarray_length = i - remainder_map[remainder]
            max_length = max(max_length, subarray_length)
        else:
            # Store the first occurrence of this remainder
            remainder_map[remainder] = i
            
    return max_length

# Example check function
def check_solution():
    assert longest_divisible_subarray([4, 5, 0, -2, -3, 1], 5) == 3
    assert longest_divisible_subarray([5], 9) == 0
    print("All tests passed!")

check_solution()
```

This solution takes advantage of the property that if two prefix sums have the same remainder when divided by `k`, the subarray between these two prefix sums is divisible by `k`. A hashmap (`remainder_map`) is used to keep track of the first occurrence of each remainder to find the longest subarray efficiently.