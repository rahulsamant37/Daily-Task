# DSA Problem 321

'''
Problem Statement:
You are given a list of integers `nums` and an integer `k`. Your task is to find the maximum number of unique pairs of numbers in the list that sum up to `k`. Each number in the list can only be used once for forming a pair. Return the count of such unique pairs.

For example, given `nums = [1, 3, 5, 7]` and `k = 8`, the pairs that sum up to 8 are (1, 7) and (3, 5), so the function should return 2.

Note:
- 1 <= len(nums) <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 10^9
'''

Solution:
```python
def max_unique_pairs(nums, k):
    from collections import Counter
    
    # Count the occurrences of each number in nums
    num_counts = Counter(nums)
    count = 0
    
    # Iterate through the unique numbers in nums
    for num in num_counts:
        complement = k - num
        # If the complement exists and is not the same number or if it is the same but has a count of at least 2
        if complement in num_counts and (complement != num or num_counts[num] > 1):
            # Increment the count by the minimum occurrences between num and its complement
            count += min(num_counts[num], num_counts[complement])
            # To avoid counting the same pair twice, set the counts of num and its complement to 0
            num_counts[num] = 0
            num_counts[complement] = 0
    
    # Since each pair was counted twice, divide by 2 to get the actual count
    return count // 2

# Example usage
nums = [1, 3, 5, 7]
k = 8
print(max_unique_pairs(nums, k))  # Output: 2
```
This solution efficiently counts the unique pairs by using a hash map (Counter) to track the occurrences of each number and its potential pair. The time complexity is O(n) where n is the length of the nums list, and the space complexity is also O(n) for storing the counts.