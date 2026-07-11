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

def solution():
    def findKthLargest(nums, k):
        """
        Finds the kth largest element in an array using a min-heap.

        Args:
            nums: A list of integers.
            k: An integer representing the kth largest element to find.

        Returns:
            The kth largest element in the array.

        Approach:
        1. Use a min-heap (priority queue) to store the k largest elements seen so far.
        2. Iterate through the input array 'nums'.
        3. For each element, push it onto the min-heap.
        4. If the size of the heap becomes larger than 'k', pop the smallest element
           from the heap (the root of the min-heap). This ensures that the heap always
           contains the k largest elements.
        5. After iterating through all elements, the root of the min-heap (heap[0])
           will be the kth largest element.

        Time Complexity: O(N log k), where N is the length of nums.  We iterate through N elements and perform heap operations (push/pop) which take O(log k) time.
        Space Complexity: O(k), for storing the k largest elements in the min-heap.
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

    return findKthLargest

# Test cases
def test_solution():
    findKthLargest = solution()
    # Test case 1
    nums1 = [3,2,1,5,6,4]
    k1 = 2
    expected1 = 5
    assert findKthLargest(nums1, k1) == expected1, f"Test Case 1 Failed: Expected {expected1}, got {findKthLargest(nums1, k1)}"

    # Test case 2
    nums2 = [3,2,3,1,2,4,5,5,6]
    k2 = 4
    expected2 = 4
    assert findKthLargest(nums2, k2) == expected2, f"Test Case 2 Failed: Expected {expected2}, got {findKthLargest(nums2, k2)}"

    # Test case 3
    nums3 = [7,6,5,4,3,2,1]
    k3 = 5
    expected3 = 3
    assert findKthLargest(nums3, k3) == expected3, f"Test Case 3 Failed: Expected {expected3}, got {findKthLargest(nums3, k3)}"

    # Test case 4
    nums4 = [1]
    k4 = 1
    expected4 = 1
    assert findKthLargest(nums4, k4) == expected4, f"Test Case 4 Failed: Expected {expected4}, got {findKthLargest(nums4, k4)}"

    # Test case 5
    nums5 = [2,1]
    k5 = 2
    expected5 = 1
    assert findKthLargest(nums5, k5) == expected5, f"Test Case 5 Failed: Expected {expected5}, got {findKthLargest(nums5, k5)}"

    # Test case 6 (Large input)
    import random
    nums6 = [random.randint(1, 1000) for _ in range(1000)]
    k6 = 500
    sorted_nums6 = sorted(nums6, reverse=True)
    expected6 = sorted_nums6[k6 - 1]
    assert findKthLargest(nums6, k6) == expected6, f"Test Case 6 Failed: Expected {expected6}, got {findKthLargest(nums6, k6)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()