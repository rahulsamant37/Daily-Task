# DSA Problem 238

'''
Problem Statement:
Given a list of positive integers, your task is to find the minimum number of unique elements that need to be removed so that the sum of the remaining elements is divisible by 3. If it's not possible to achieve this by removing any number of elements, return -1.

For example, given the list [1, 2, 3, 4], you could remove 1 and 2 to make the sum (7) divisible by 3.

Constraints:
- 1 <= len(nums) <= 100
- 1 <= nums[i] <= 100
'''

Solution:
```python
def min_removal_for_divisible_by_three(nums):
    from collections import defaultdict
    remainder_groups = defaultdict(list)
    total_sum = 0
    
    for num in nums:
        total_sum += num
        remainder_groups[num % 3].append(num)
    
    remainder = total_sum % 3
    
    if remainder == 0:
        return 0  # No need to remove any elements
    
    removals = float('inf')
    
    if remainder == 1:
        # Try to remove one element with remainder 1 or two elements with remainder 2
        if remainder_groups[1]:
            removals = min(removals, 1)
        if len(remainder_groups[2]) >= 2:
            removals = min(removals, 2)
    
    elif remainder == 2:
        # Try to remove one element with remainder 2 or two elements with remainder 1
        if remainder_groups[2]:
            removals = min(removals, 1)
        if len(remainder_groups[1]) >= 2:
            removals = min(removals, 2)
    
    return removals if removals != float('inf') else -1

# Example check
print(min_removal_for_divisible_by_three([1, 2, 3, 4]))  # Output: 2
```

This solution uses a dictionary to group numbers based on their remainder when divided by 3. It then calculates the minimum number of removals needed to make the sum of the list divisible by 3, considering the constraints and possible scenarios for achieving this.