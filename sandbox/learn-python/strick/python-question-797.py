# Python Question: Find the Kth Largest Element in an Array
'''
Given an integer array `nums` and an integer `k`, return the k-th largest element in the array.

Note that it is the k-th largest element in the sorted order, not the k-th distinct element.

You must solve it in O(n) time complexity.

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
    Finds the k-th largest element in an array using a min-heap.

    Args:
        nums: The input array of integers.
        k: The rank of the largest element to find (e.g., k=1 for the largest).

    Returns:
        The k-th largest element in the array.
    """
    # Use a min-heap to keep track of the k largest elements seen so far.
    # The heap will always contain the k largest elements, with the smallest
    # of these k elements at the root.

    min_heap = []  # Initialize an empty min-heap

    for num in nums:
        # If the heap has fewer than k elements, add the current number.
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            # If the current number is larger than the smallest element in the heap
            # (i.e., the root), replace the root with the current number and
            # heapify to maintain the min-heap property.
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)

    # After processing all numbers, the root of the min-heap will be the
    # k-th largest element.
    return min_heap[0]

# Test cases
def test_solution():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert findKthLargest([7,6,5,4,3,2,1], 5) == 3
    assert findKthLargest([1], 1) == 1
    assert findKthLargest([1,2], 1) == 2
    assert findKthLargest([1,2], 2) == 1
    assert findKthLargest([2,1], 2) == 1
    assert findKthLargest([2,1,5,4,3], 3) == 3
    assert findKthLargest([2,1,5,4,3], 1) == 5
    assert findKthLargest([2,1,5,4,3], 5) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()