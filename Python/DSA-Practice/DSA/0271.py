# DSA Problem 271

'''
Problem Statement:
Given a list of integers, find the length of the longest subsequence such that elements in the subsequence are consecutive integers, the order doesn't matter, and every element in the subsequence is unique. For example, in the list [1, 9, 3, 10, 4, 20, 2], the longest such subsequence is [1, 2, 3, 4], so the function should return 4.

Constraints:
- The list can contain up to 10^5 elements.
- Elements in the list can range from -10^9 to 10^9.
'''

Solution:
```python
def longest_consecutive_subsequence(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    longest_streak = 0
    
    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak

# Example check (this is not part of the solution, just for verification)
print(longest_consecutive_subsequence([100, 4, 200, 1, 3, 2]))  # Output: 4
```

Explanation:
The solution leverages a set to first eliminate duplicates and then checks for each number if it's the beginning of a sequence (i.e., the number right before it is not in the set). If so, it calculates the length of the consecutive sequence by incrementing from that number as long as the next consecutive number is found in the set. The length of the longest such sequence found is returned.