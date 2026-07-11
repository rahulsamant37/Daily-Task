# DSA Problem 223

'''
Problem Statement:
You are given a list of integers `nums`. Your task is to find all unique triplets in the list which gives the sum of zero. Note that the solution set must not contain duplicate triplets. The order of the triplets and the order of elements within each triplet are not important.

For example, given `nums = [-1, 0, 1, 2, -1, -4]`, the function should return `[[0, 1, -1], [2, -1, -1]]`. Note that [1, 0, -1] and [-1, 1, 0] would be considered the same triplet, and only one of them should be included in the output.
'''

Solution:
```python
def find_zero_sum_triplets(nums):
    nums.sort()  # Sort the list to avoid duplicate triplets
    triplets = []
    n = len(nums)
    
    for i in range(n-2):
        # Skip duplicate values
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                # Skip duplicate values
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
                
    return triplets

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print(find_zero_sum_triplets(nums))
```

This Python function `find_zero_sum_triplets` takes a list of integers as input and returns a list of unique triplets whose sum is zero. It first sorts the list to simplify finding and skipping duplicates. Then, for each element, it uses a two-pointer approach to find pairs that, together with the current element, sum up to zero. It carefully skips over duplicate values to ensure the uniqueness of the triplets.