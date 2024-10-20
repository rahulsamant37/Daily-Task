# DSA Problem for 2024-10-21

Here is a novel DSA problem with a Python solution for 2024-10-21:

**Problem Statement:**

**Largest Subarray with Equal Sum**

Given an array of integers, find the largest subarray (contiguous subset) where the sum of elements is equal to the sum of elements in the remaining part of the array.

**Example:**

Input: `arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
Output: `[3, 4, 5, 6, 7]` (sum of subarray is 25, and sum of remaining part is also 25)

**Optimal Solution:**
```python
def largest_subarray_with_equal_sum(arr):
    n = len(arr)
    total_sum = sum(arr)
    left_sum = 0
    max_len = 0
    max_subarray = []
    for i in range(n):
        left_sum += arr[i]
        right_sum = total_sum - left_sum
        if left_sum == right_sum:
            if i + 1 > max_len:
                max_len = i + 1
                max_subarray = arr[:i+1]
    return max_subarray
```
**Time Complexity Analysis:**

The time complexity of this solution is O(n), where n is the length of the input array. This is because we only need to traverse the array once to calculate the sum of the subarray and the remaining part.

**Space Complexity Analysis:**

The space complexity of this solution is O(1), as we only use a few extra variables to store the sum of the subarray and the remaining part, and the maximum length and subarray found so far.

**Explanation:**

The idea behind this solution is to iterate through the array and keep track of the sum of the subarray and the remaining part. We check if the sum of the subarray is equal to the sum of the remaining part at each step. If it is, we update the maximum length and subarray found so far. At the end of the iteration, we return the maximum subarray found.

Note: This problem is similar to the "Partition Equal Subset Sum" problem, but with a twist. Instead of finding two subsets with equal sum, we need to find a contiguous subarray with sum equal to the sum of the remaining part.