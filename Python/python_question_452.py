# Python Question: Find the Kth Largest Element in an Array
'''
Given an unsorted array of integers `nums` and an integer `k`, find the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

# Solution
import random

def findKthLargest(nums, k):
    """
    Finds the kth largest element in an array using the QuickSelect algorithm.

    Args:
      nums: A list of integers.
      k: An integer representing the kth largest element to find.

    Returns:
      The kth largest element in the array.
    """

    def partition(nums, low, high):
        """
        Partitions the array around a pivot element.

        Args:
          nums: The list of integers to partition.
          low: The starting index of the partition.
          high: The ending index of the partition.

        Returns:
          The index of the pivot element after partitioning.
        """
        pivot = nums[high]  # Choose the last element as the pivot
        i = low - 1

        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def quickSelect(nums, low, high, k):
        """
        Recursively selects the kth largest element using the QuickSelect algorithm.

        Args:
          nums: The list of integers to search in.
          low: The starting index of the search range.
          high: The ending index of the search range.
          k: The kth largest element to find.

        Returns:
          The kth largest element in the array.
        """
        if low == high:
            return nums[low]

        pi = partition(nums, low, high)

        if k == pi + 1:
            return nums[pi]
        elif k < pi + 1:
            return quickSelect(nums, low, pi - 1, k)
        else:
            return quickSelect(nums, pi + 1, high, k)

    n = len(nums)
    return quickSelect(nums, 0, n - 1, n - k + 1)  # kth largest is (n - k + 1)th smallest


# Test cases
def test_solution():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert findKthLargest([1], 1) == 1
    assert findKthLargest([5,2,4,1,3,6,0], 4) == 3
    assert findKthLargest([7,6,5,4,3,2,1], 5) == 3
    assert findKthLargest([3,2,1,5,6,4], 1) == 6
    assert findKthLargest([3,2,1,5,6,4], 6) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()