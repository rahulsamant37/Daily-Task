# Python Question: Find the Kth Largest Element in an Array
'''
Given an unsorted array of integers `nums` and an integer `k`, find the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

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
    Finds the kth largest element in an array using the QuickSelect algorithm.

    Args:
        nums: A list of integers.
        k: The kth largest element to find.

    Returns:
        The kth largest element in the array.
    """

    def partition(left, right, pivot_index):
        """
        Partitions the array around a pivot element.

        Args:
            left: The left index of the subarray.
            right: The right index of the subarray.
            pivot_index: The index of the pivot element.

        Returns:
            The new index of the pivot element after partitioning.
        """
        pivot = nums[pivot_index]
        # 1. move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        # 2. move all smaller elements to the left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # 3. move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]

        return store_index

    def quickselect(left, right, k_smallest):
        """
        Recursively finds the kth smallest element using QuickSelect.

        Args:
            left: The left index of the subarray.
            right: The right index of the subarray.
            k_smallest: The kth smallest element to find.

        Returns:
            The kth smallest element in the subarray.
        """
        if left == right:
            return nums[left]

        # select a random pivot_index
        pivot_index = random.randint(left, right)

        # find the pivot position in a sorted array
        pivot_index = partition(left, right, pivot_index)

        # the pivot is in its final sorted position
        if k_smallest == pivot_index:
            return nums[k_smallest]
        # go left
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        # go right
        else:
            return quickselect(pivot_index + 1, right, k_smallest)

    # kth largest is (n - k)th smallest
    return quickselect(0, len(nums) - 1, len(nums) - k)


# Test cases
def test_solution():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert findKthLargest([1], 1) == 1
    assert findKthLargest([2,1], 2) == 1
    assert findKthLargest([7,6,5,4,3,2,1], 5) == 3
    assert findKthLargest([3, 1, 2, 4], 2) == 3
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()