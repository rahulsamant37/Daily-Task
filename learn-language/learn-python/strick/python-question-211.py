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
import random

def findKthLargest(nums, k):
    """
    Finds the kth largest element in the array using the QuickSelect algorithm.

    Args:
        nums: A list of integers.
        k: An integer representing the kth largest element to find.

    Returns:
        The kth largest element in the array.
    """

    def partition(left, right, pivot_index):
        """
        Partitions the array around the pivot element.

        Args:
            left: The left index of the subarray.
            right: The right index of the subarray.
            pivot_index: The index of the pivot element.

        Returns:
            The index of the pivot element after partitioning.
        """
        pivot = nums[pivot_index]
        # Move pivot to the end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        # Elements less than pivot will be moved to the left
        store_index = left

        # Iterate through all elements except the pivot
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # Move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]

        return store_index

    def quickselect(left, right, k_smallest):
        """
        Performs the QuickSelect algorithm to find the kth smallest element.

        Args:
            left: The left index of the subarray.
            right: The right index of the subarray.
            k_smallest: The index of the kth smallest element to find.

        Returns:
            The kth smallest element in the array.
        """
        if left == right:
            return nums[left]

        # Select a random pivot index
        pivot_index = random.randint(left, right)

        # Partition the array around the pivot
        pivot_index = partition(left, right, pivot_index)

        # If the pivot is the kth smallest element, return it
        if k_smallest == pivot_index:
            return nums[k_smallest]
        # If the kth smallest element is to the left of the pivot, recursively search the left subarray
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        # If the kth smallest element is to the right of the pivot, recursively search the right subarray
        else:
            return quickselect(pivot_index + 1, right, k_smallest)

    # Convert k to find the kth smallest element (index)
    k_smallest = len(nums) - k
    return quickselect(0, len(nums) - 1, k_smallest)

# Test cases
def test_solution():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert findKthLargest([1], 1) == 1
    assert findKthLargest([2,1], 1) == 2
    assert findKthLargest([2,1], 2) == 1
    assert findKthLargest([5,2,4,1,3,6,0], 4) == 3
    assert findKthLargest([7,6,5,4,3,2,1], 5) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()