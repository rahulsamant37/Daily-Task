# Python Question: Find the Kth Largest Element in an Array
'''
Given an integer array `nums` and an integer `k`, return the k-th largest element in the array.

Note that it is the k-th largest element in the sorted order, not the k-th distinct element.

You must solve it in O(n) average time complexity.

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
    Finds the k-th largest element in the array using the QuickSelect algorithm.

    Args:
        nums: The input array of integers.
        k: The k-th largest element to find.

    Returns:
        The k-th largest element in the array.
    """

    def partition(left, right, pivot_index):
        """
        Partitions the array around the pivot element.

        Args:
            left: The left index of the subarray to partition.
            right: The right index of the subarray to partition.
            pivot_index: The index of the pivot element.

        Returns:
            The index of the pivot element after partitioning.
        """
        pivot_value = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  # Move pivot to the end
        store_index = left

        for i in range(left, right):
            if nums[i] > pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        nums[right], nums[store_index] = nums[store_index], nums[right]  # Move pivot to its final place
        return store_index

    def quickselect(left, right, k_smallest):
        """
        Recursively finds the k-th smallest element using QuickSelect.

        Args:
            left: The left index of the subarray.
            right: The right index of the subarray.
            k_smallest: The k-th smallest element to find.

        Returns:
            The k-th smallest element in the subarray.
        """
        if left == right:
            return nums[left]

        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)

        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        else:
            return quickselect(pivot_index + 1, right, k_smallest)

    # Convert k to find the k-th smallest element (k-th largest is n - k + 1 smallest)
    return quickselect(0, len(nums) - 1, len(nums) - k)


# Test cases
def test_solution():
    assert findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert findKthLargest([1], 1) == 1
    assert findKthLargest([7,6,5,4,3,2,1], 5) == 3
    assert findKthLargest([3,3,3,3,4,3,3,3,3], 2) == 4
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()