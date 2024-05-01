# Python Question: Find the Kth Largest Element in an Unsorted Array
'''
Given an unsorted array of integers, find the kth largest element in the array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

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
    Finds the kth largest element in an unsorted array.

    Args:
        nums: A list of integers.
        k: An integer representing the kth largest element to find.

    Returns:
        The kth largest element in the array.

    Approach:
    We can use a min-heap of size k to keep track of the k largest elements seen so far.
    Iterate through the array:
    - If the current element is larger than the smallest element in the heap (heap[0]),
      remove the smallest element from the heap and add the current element.
    After iterating through the entire array, the smallest element in the heap (heap[0])
    will be the kth largest element in the array.
    """
    heap = []  # Initialize an empty min-heap
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)  # Add the first k elements to the heap
        elif num > heap[0]:
            heapq.heapreplace(heap, num)  # Replace the smallest element with the current element if it's larger

    return heap[0]  # The smallest element in the heap is the kth largest element

# Test cases
def test_solution():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert findKthLargest([7,6,5,4,3,2,1], 5) == 3
    assert findKthLargest([1], 1) == 1
    assert findKthLargest([2,1], 2) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()