# Python Question: Find the Kth Largest Element in an Array using Quickselect
'''
Given an unsorted array of integers, find the kth largest element in the array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

# Solution
def findKthLargest(nums, k):
    """
    Finds the kth largest element in an unsorted array using the Quickselect algorithm.

    Args:
        nums: A list of integers.
        k: An integer representing the kth largest element to find.

    Returns:
        The kth largest element in the array.
    """

    def partition(left, right, pivot_index):
        """
        Partitions the array around a pivot element.

        Args:
            left: The starting index of the subarray.
            right: The ending index of the subarray.
            pivot_index: The index of the pivot element.

        Returns:
            The index of the pivot element after partitioning.
        """
        pivot = nums[pivot_index]
        # Move pivot to the end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        # Move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]

        return store_index

    def quickselect(left, right, k_smallest):
        """
        Recursively finds the kth smallest element using Quickselect.

        Args:
            left: The starting index of the subarray.
            right: The ending index of the subarray.
            k_smallest: The kth smallest element to find.

        Returns:
            The kth smallest element in the subarray.
        """
        if left == right:
            return nums[left]

        # Select a random pivot index
        import random
        pivot_index = random.randint(left, right)

        # Partition the array around the pivot
        pivot_index = partition(left, right, pivot_index)

        # If the pivot is the kth smallest element, return it
        if k_smallest == pivot_index:
            return nums[pivot_index]
        # If the kth smallest element is to the left of the pivot, search in the left subarray
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        # If the kth smallest element is to the right of the pivot, search in the right subarray
        else:
            return quickselect(pivot_index + 1, right, k_smallest)

    # Find the (n - k + 1)th smallest element
    return quickselect(0, len(nums) - 1, len(nums) - k)


# Test cases
def test_solution():
    assert findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert findKthLargest([1], 1) == 1
    assert findKthLargest([1, 2], 1) == 2
    assert findKthLargest([1, 2, 3, 4, 5], 3) == 3
    assert findKthLargest([5, 4, 3, 2, 1], 3) == 3
    assert findKthLargest([7,6,5,4,3,2,1], 5) == 3
    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()