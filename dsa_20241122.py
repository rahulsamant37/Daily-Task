# DSA Problem for 2024-11-22

Here is a novel DSA problem with a Python solution for 2024-11-22:

**Problem Statement:**

"Maximum Product of K Pairs": Given an integer array `nums` and an integer `k`, find the maximum product of `k` pairs of numbers in the array. Each number can only be used once in the product.

**Example:**

Input: `nums = [1, 2, 3, 4, 5, 6], k = 2`
Output: `60` (maximum product of 2 pairs is 4*6 and 5*3)

**Optimal Solution:**
```python
import heapq

def max_product_k_pairs(nums, k):
    # Create a min-heap to store the k largest numbers
    max_heap = []
    for num in nums:
        if len(max_heap) < k:
            heapq.heappush(max_heap, num)
        else:
            heapq.heappushpop(max_heap, num)

    # Create a min-heap to store the k smallest numbers
    min_heap = []
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, -num)
        else:
            heapq.heappushpop(min_heap, -num)

    # Calculate the maximum product of k pairs
    product = 1
    for i in range(k):
        product *= max_heap[i] * min_heap[i]

    return product
```
**Time Complexity Analysis:**

* The time complexity of creating the max-heap is O(n log k), where n is the length of the input array and k is the number of pairs.
* The time complexity of creating the min-heap is also O(n log k).
* The time complexity of calculating the maximum product of k pairs is O(k).
* Therefore, the overall time complexity is O(n log k).

**Space Complexity Analysis:**

* The space complexity is O(k) for storing the max-heap and min-heap.

**Note:**

* The problem can be solved using a single heap by storing the indices of the numbers instead of the numbers themselves. This approach would have a time complexity of O(n log n) and a space complexity of O(n).
* The optimal solution provided has a better time complexity of O(n log k) but requires more space to store the two heaps.