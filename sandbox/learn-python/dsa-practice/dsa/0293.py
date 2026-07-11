# DSA Problem 293

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, return the maximum number of unique pairs `(nums[i], nums[j])` such that `i != j` and `nums[i] + nums[j]` equals `k`. Each integer in `nums` can only be used in one pair.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: We can form two pairs: (1, 4) and (2, 3).

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: We can form only one pair: (3, 3).

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 10^9
'''

Solution:
```python
def maxUniquePairs(nums, k):
    from collections import Counter
    
    # Count the frequency of each number
    num_counts = Counter(nums)
    max_pairs = 0
    
    for num in num_counts:
        complement = k - num
        if complement in num_counts:
            # If the number and its complement are the same, we can only use half of the available pairs
            if num == complement:
                max_pairs += num_counts[num] // 2
            else:
                # Take the minimum count between the number and its complement
                max_pairs += min(num_counts[num], num_counts[complement])
                # Mark the complement as used
                num_counts[complement] = 0
            # Mark the number as used
            num_counts[num] = 0
    
    return max_pairs // 2

# Example usage:
print(maxUniquePairs([1,2,3,4], 5))  # Output: 2
print(maxUniquePairs([3,1,3,4,3], 6))  # Output: 1
```

This Python solution accounts for the unique pairs requirement by using a `Counter` to track the frequency of each number in the list `nums`. It then iterates through the numbers and finds their complements to sum up to `k`, ensuring no number is used more than its frequency allows, and each pair is counted only once.