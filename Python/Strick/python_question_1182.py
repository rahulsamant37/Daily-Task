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
    Finds the kth largest element in an array.

    Args:
        nums: A list of integers.
        k: An integer representing the kth largest element to find.

    Returns:
        The kth largest element in the array.
    """

    # Use a min-heap to store the k largest elements seen so far.
    # Initialize the heap with the first k elements of the array.
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    # Iterate over the remaining elements in the array.
    for i in range(k, len(nums)):
        # If the current element is larger than the smallest element in the heap,
        # replace the smallest element with the current element and heapify.
        if nums[i] > min_heap[0]:
            heapq.heapreplace(min_heap, nums[i])

    # The smallest element in the heap is the kth largest element in the array.
    return min_heap[0]

# Test cases
def test_solution():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert findKthLargest([1], 1) == 1
    assert findKthLargest([2,1], 2) == 1
    assert findKthLargest([2,1], 1) == 2
    assert findKthLargest([7,6,5,4,3,2,1], 5) == 3
    assert findKthLargest([1,2,3,4,5,6,7], 5) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()