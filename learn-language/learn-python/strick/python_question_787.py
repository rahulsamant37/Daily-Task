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

def solution():
    def findKthLargest(nums, k):
        """
        Finds the kth largest element in an unsorted array.

        Args:
            nums: A list of integers.
            k: An integer representing the kth largest element to find.

        Returns:
            The kth largest element in the array.

        Approach:
        1. Use a min-heap of size k to store the k largest elements seen so far.
        2. Iterate through the array.
        3. For each element, if the heap size is less than k, add the element to the heap.
        4. If the heap size is equal to k and the current element is larger than the smallest element in the heap (heap[0]),
           replace the smallest element with the current element and heapify the heap.
        5. After iterating through the array, the smallest element in the heap (heap[0]) will be the kth largest element.
        """
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            elif num > min_heap[0]:
                heapq.heapreplace(min_heap, num)
        return min_heap[0]

    return findKthLargest

# Test cases
def test_solution():
    findKthLargest = solution()  # get the function from the solution

    # Test case 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    expected1 = 5
    assert findKthLargest(nums1, k1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {findKthLargest(nums1, k1)}"

    # Test case 2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    expected2 = 4
    assert findKthLargest(nums2, k2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {findKthLargest(nums2, k2)}"

    # Test case 3
    nums3 = [7, 6, 5, 4, 3, 2, 1]
    k3 = 5
    expected3 = 3
    assert findKthLargest(nums3, k3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {findKthLargest(nums3, k3)}"

    # Test case 4 (k = 1, find the largest)
    nums4 = [1, 2, 3, 4, 5]
    k4 = 1
    expected4 = 5
    assert findKthLargest(nums4, k4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {findKthLargest(nums4, k4)}"

    # Test case 5 (k = len(nums), find the smallest)
    nums5 = [5, 4, 3, 2, 1]
    k5 = 5
    expected5 = 1
    assert findKthLargest(nums5, k5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {findKthLargest(nums5, k5)}"

    # Test case 6 (negative numbers)
    nums6 = [-1, -2, -3, -4, -5]
    k6 = 2
    expected6 = -2
    assert findKthLargest(nums6, k6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {findKthLargest(nums6, k6)}"

    # Test case 7 (duplicate and negative numbers)
    nums7 = [-1, 2, 0, -2, 2, 3, 4, 1]
    k7 = 3
    expected7 = 2
    assert findKthLargest(nums7, k7) == expected7, f"Test Case 7 Failed: Expected {expected7}, got {findKthLargest(nums7, k7)}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()