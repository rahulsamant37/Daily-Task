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

    Approach:
    We use a min-heap of size k to store the k largest elements seen so far.
    We iterate through the input array.  For each element:
        1. If the heap has fewer than k elements, we add the element to the heap.
        2. If the heap has k elements and the current element is larger than the smallest element in the heap (heap[0]),
           we replace the smallest element with the current element.

    After iterating through the array, the smallest element in the heap (heap[0]) will be the kth largest element.
    This is because the heap contains the k largest elements, and the smallest among them is the kth largest.

    This approach has a time complexity of O(N log K), where N is the length of the input array and K is the value of k.
    The space complexity is O(K) for the heap.
    """
    min_heap = []
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heapreplace(min_heap, num)  # More efficient than pop and push
    return min_heap[0]

# Test cases
def test_solution():
    nums1 = [3,2,1,5,6,4]
    k1 = 2
    assert findKthLargest(nums1, k1) == 5, "Test Case 1 Failed"

    nums2 = [3,2,3,1,2,4,5,5,6]
    k2 = 4
    assert findKthLargest(nums2, k2) == 4, "Test Case 2 Failed"

    nums3 = [1]
    k3 = 1
    assert findKthLargest(nums3, k3) == 1, "Test Case 3 Failed"

    nums4 = [2,1]
    k4 = 1
    assert findKthLargest(nums4, k4) == 2, "Test Case 4 Failed"

    nums5 = [2,1]
    k5 = 2
    assert findKthLargest(nums5, k5) == 1, "Test Case 5 Failed"

    nums6 = [7,6,5,4,3,2,1]
    k6 = 5
    assert findKthLargest(nums6, k6) == 3, "Test Case 6 Failed"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()