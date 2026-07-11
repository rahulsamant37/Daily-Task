# DSA Problem 165

'''
Problem Statement:
Given a list of positive integers `nums` and a positive integer `k`, return the number of (contiguous, non-empty) subarrays such that the product of all the elements in the subarray is strictly less than `k`.

For example, given the list [10, 5, 2, 6] and k = 100, the subarrays [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [10, 5, 2] have products less than 100.

Note:
- `1 <= nums.length <= 30000`.
- `1 <= nums[i] <= 1000`.
- `1 <= k <= 10000`.
'''

Solution:
```python
def num_subarrays_product_less_than_k(nums, k):
    if k <= 1:
        return 0
    
    count = 0
    left = 0
    product = 1
    
    for right in range(len(nums)):
        product *= nums[right]
        while product >= k:
            product /= nums[left]
            left += 1
        count += right - left + 1
    
    return count

# Example check (This is not part of the solution, just for verification)
print(num_subarrays_product_less_than_k([10, 5, 2, 6], 100))  # Output should be 8
```

This Python function implements a sliding window approach to efficiently find the number of subarrays with a product less than the given threshold `k`. The `left` and `right` pointers define the current window of the array which is being considered, and the `product` variable keeps track of the product of elements within the current window. As soon as the product is greater than or equal to `k`, the left pointer is moved to the right to shrink the window until the product meets the condition again. The count of valid subarrays is incremented by the size of the current valid window for each position of the right pointer.