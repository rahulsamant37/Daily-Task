# DSA Problem 99

'''
Problem Statement:
Given a list of integers `nums` and an integer `k`, write a function `find_kth_largest` to return the kth largest element in the list. Assume that 1 ≤ k ≤ length of `nums`, and the list will have at least one element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Note:
- You can assume that k is always valid, 1 ≤ k ≤ length of the array.
- Try to solve it with time complexity better than O(n log n).
'''

Solution:
```python
import heapq

def find_kth_largest(nums, k):
    """
    Finds the kth largest element in the list using a min heap.
    
    :param nums: List[int], the list of numbers.
    :param k: int, the kth position to find the largest element for.
    :return: int, the kth largest element in the list.
    """
    # Use a min heap of size k to keep track of the top k elements
    min_heap = []
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            # If the current number is larger than the smallest in the heap, replace it
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
                
    # The root of the heap is the kth largest element
    return min_heap[0]

# Check function to verify the solution with provided data points
def check_solution():
    assert find_kth_largest([3,2,1,5,6,4], 2) == 5, "Test case 1 failed"
    assert find_kth_largest([3,2,3,1,2,4,5,5,6], 4) == 4, "Test case 2 failed"
    print("All test cases passed!")

check_solution()
```

This solution uses a heap data structure to efficiently find the kth largest element with a time complexity of O(n log k), which is better than O(n log n) for sorting the entire array.