# Python Question: Find the Kth Largest Element in an Array
'''
Given an unsorted array of integers, find the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

# Solution
import heapq

def findKthLargest(nums, k):
    """
    Finds the kth largest element in the given array.

    Args:
      nums: A list of integers.
      k: An integer representing the kth largest element to find.

    Returns:
      The kth largest element in the array.

    Approach:
    We can use a min-heap of size k to keep track of the k largest elements seen so far.
    Iterate through the array. For each element:
      1. If the heap size is less than k, add the element to the heap.
      2. Otherwise, if the element is larger than the smallest element in the heap (heap[0]),
         replace the smallest element with the current element and heapify.

    After iterating through the array, the smallest element in the heap (heap[0]) will be the kth largest element.
    """
    min_heap = []

    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heapreplace(min_heap, num)

    return min_heap[0]

# Test cases
def test_solution():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert findKthLargest([7,6,5,4,3,2,1], 5) == 3
    assert findKthLargest([1], 1) == 1
    assert findKthLargest([2,1], 2) == 1
    assert findKthLargest([2,1], 1) == 2
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()