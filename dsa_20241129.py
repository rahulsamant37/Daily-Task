# DSA Problem for 2024-11-29

Here is a novel DSA problem with a Python solution for 2024-11-29:

**Problem Statement:**

**Minimum Contiguous Subarray Sum**

Given an array of integers `arr` and an integer `k`, find the minimum contiguous subarray that sums up to at least `k`. If no such subarray exists, return `-1`.

**Constraints:**

* `1 <= arr.length <= 10^5`
* `1 <= arr[i] <= 10^4`
* `1 <= k <= 10^8`

**Example:**

Input: `arr = [1, 2, 3, 4, 5], k = 9`
Output: `[2, 3, 4]` (sum = 9)

Input: `arr = [1, 2, 3, 4, 5], k = 15`
Output: `-1` (no contiguous subarray sums up to 15)

**Optimal Solution:**
```python
def min_contiguous_subarray_sum(arr, k):
    n = len(arr)
    min_sum = float('inf')
    min_left = min_right = 0
    curr_sum = 0
    left = 0

    for right in range(n):
        curr_sum += arr[right]

        while curr_sum >= k:
            if curr_sum < min_sum:
                min_sum = curr_sum
                min_left = left
                min_right = right
            curr_sum -= arr[left]
            left += 1

    if min_sum == float('inf'):
        return -1
    return arr[min_left:min_right+1]
```
**Time Complexity Analysis:**

The time complexity of the solution is O(n), where n is the length of the input array. The outer loop iterates over the array once, and the inner while loop iterates at most n times in the worst case.

**Space Complexity Analysis:**

The space complexity of the solution is O(1), since we only use a few extra variables to store the minimum sum, left, and right indices.

**Explanation:**

The solution uses a sliding window approach to find the minimum contiguous subarray that sums up to at least `k`. We maintain a window of elements that sum up to `curr_sum`, and slide the window to the right by adding elements and sliding it to the left by subtracting elements. When `curr_sum` reaches or exceeds `k`, we update the minimum sum and the corresponding left and right indices. If no such subarray is found, we return `-1`.