# DSA Problem 307

'''
Problem Statement:
You are given a list of integers `nums`. Your task is to find the maximum length of a contiguous subarray with an equal number of odd and even integers. If no such subarray exists, return 0.

For example, given `nums = [1, 2, 3, 4, 5, 6]`, the subarray `[1, 2, 3, 4]` has an equal number of odd and even integers (2 each), and there's no longer subarray with this property, so the function should return 4.
'''

Solution:
```python
def max_even_odd_subarray_length(nums):
    max_length = 0
    count_diff = 0
    diff_index_map = {0: -1}
    
    for i, num in enumerate(nums):
        if num % 2 == 0:
            count_diff += 1
        else:
            count_diff -= 1
        
        if count_diff in diff_index_map:
            max_length = max(max_length, i - diff_index_map[count_diff])
        else:
            diff_index_map[count_diff] = i
    
    return max_length

# Test the function
nums = [1, 2, 3, 4, 5, 6]
print(max_even_odd_subarray_length(nums))  # Expected output: 4
```

Explanation:
The solution uses a hashmap to store the first occurrence of each difference between the count of even and odd numbers encountered in the array. As we iterate over the array, we maintain a count of the difference between the number of even and odd numbers. If the difference has been seen before, it means that the subarray between the two occurrences of this difference has an equal number of even and odd numbers. The length of this subarray is calculated and the maximum length is tracked.