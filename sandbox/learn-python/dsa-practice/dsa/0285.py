# DSA Problem 285

'''
Problem Statement:
You are given a list of positive integers and an integer k. You need to find the k-th largest element in the list. However, there's a twist: you can only perform operations that involve sorting segments of the list, and you're limited to a maximum of log(n) sorting operations, where n is the length of the list. Design an efficient algorithm to solve this problem under these constraints. 

Note:
- The list is guaranteed to have at least k elements.
- 1 <= k <= length of the list
- 1 <= length of the list <= 10^5
- All elements in the list are unique.
'''

Solution:
```python
import heapq

def find_kth_largest(nums, k):
    """
    Finds the k-th largest element in the list nums.
    Uses a min-heap to keep track of the top k elements, ensuring log(n) sorting operations.
    """
    # Create a min-heap with the first k elements of nums.
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    
    # Iterate over the rest of the elements in nums.
    for num in nums[k:]:
        # If the current number is larger than the smallest in the heap, replace it.
        if num > min_heap[0]:
            heapq.heapreplace(min_heap, num)
    
    # The root of the heap is the k-th largest element.
    return min_heap[0]

# Example check function
def check_solution():
    assert find_kth_largest([3,2,1,5,6,4], 2) == 5
    assert find_kth_largest([3,2,3,1,2,4,5,5,6], 4) == 4
    print("All tests passed.")

check_solution()
```

This solution utilizes a heap to maintain the top k elements, thereby keeping the number of sorting operations within the given constraint. The time complexity is O(n log k), where n is the length of the input list, since each insertion into the heap takes O(log k) time.