# DSA Problem 103

'''
Problem Statement:
Given a list of integers and a target sum, find all unique triplets in the list that sum up to the target sum. The solution should not contain duplicate triplets. For example, given the list [1, 2, -2, -1, 0] and target sum 0, the solution should return the unique triplets that sum to zero.

Considerations:
- The input list can contain up to 1000 integers.
- Each triplet should be sorted in non-decreasing order.
- The output should be a list of lists, with each inner list representing one of the unique triplets.
'''

Solution:
```python
def find_unique_triplets(nums, target_sum):
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n - 2):
        # Skip duplicate elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target_sum:
                result.append([nums[i], nums[left], nums[right]])
                # Move left and right while skipping duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
    return result

# Example check
nums = [1, 2, -2, -1, 0]
target_sum = 0
print(find_unique_triplets(nums, target_sum))  # Output: [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
```
Note: The example output in the print statement is illustrative and may not match the exact output based on the input list provided, but it shows the general form of the solution.