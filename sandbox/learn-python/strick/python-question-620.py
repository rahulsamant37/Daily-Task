# Python Question: Find the Kth Largest Element in an Array
'''
Given an integer array `nums` and an integer `k`, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

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
    Finds the kth largest element in an array.

    Args:
        nums: A list of integers.
        k: An integer representing the kth largest element to find.

    Returns:
        The kth largest element in the array.
    """

    # Use a min-heap of size k to store the k largest elements seen so far.
    # The root of the min-heap will always be the smallest among the k largest elements.
    # This ensures that when we encounter a number larger than the root, we can replace the root
    # with the larger number, maintaining the invariant that the heap contains the k largest elements.

    min_heap = []

    # Iterate through the array
    for num in nums:
        # If the heap has fewer than k elements, add the current number to the heap.
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        # If the current number is larger than the smallest element in the heap (the root),
        # replace the root with the current number.
        elif num > min_heap[0]:
            heapq.heapreplace(min_heap, num)

    # After iterating through the entire array, the root of the heap will be the kth largest element.
    return min_heap[0]


# Test cases
def test_findKthLargest():
    assert findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert findKthLargest([1], 1) == 1
    assert findKthLargest([2, 1], 1) == 2
    assert findKthLargest([2, 1], 2) == 1
    assert findKthLargest([7,6,5,4,3,2,1], 5) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_findKthLargest()